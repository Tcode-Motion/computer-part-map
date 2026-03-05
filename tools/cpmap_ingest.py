import os
import sys
import json
import hashlib
import argparse
import logging
import requests
import re
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import quote_plus

from PIL import Image
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader
from tqdm import tqdm

try:
    from mutagen import File as MutagenFile
except ImportError:
    MutagenFile = None

# Optional Integrations
try:
    from googleapiclient.discovery import build
    YOUTUBE_LIB = True
except ImportError:
    YOUTUBE_LIB = False

def simple_slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

class CPMapIngestor:
    def __init__(self, args):
        self.repo = Path(args.repo).resolve()
        self.component = args.component
        self.limit = args.limit
        self.dry_run = args.dry_run
        self.force = args.force
        self.verbose = args.verbose
        self.api_keys = self._load_keys(args.api_keys_file)
        
        self.data_dir = self.repo / "data"
        self.assets_base = self.repo / "assets"
        self.templates_dir = self.repo / "templates"
        
        self._setup_logging()
        self._ensure_dirs()
        self.jinja_env = Environment(loader=FileSystemLoader(str(self.templates_dir)))
        self.index_data = self._load_index()

    def _setup_logging(self):
        level = logging.DEBUG if self.verbose else logging.INFO
        logging.basicConfig(format='%(levelname)s: %(message)s', level=level)
        self.log = logging.getLogger("cpmap_ingest")

    def _load_keys(self, key_file):
        keys = {}
        if key_file and os.path.exists(key_file):
            with open(key_file, 'r') as f:
                keys = json.load(f)
        keys.update({
            "NASA_API_KEY": os.getenv("NASA_API_KEY", keys.get("NASA_API_KEY", "DEMO_KEY")),
            "YOUTUBE_API_KEY": os.getenv("YOUTUBE_API_KEY", keys.get("YOUTUBE_API_KEY"))
        })
        return keys

    def _ensure_dirs(self):
        for sub in ["images", "video", "audio"]:
            (self.assets_base / sub / self.component).mkdir(parents=True, exist_ok=True)
        self.data_dir.mkdir(exist_ok=True)

    def _load_index(self):
        index_path = self.data_dir / f"{self.component}.json"
        if index_path.exists():
            with open(index_path, 'r') as f:
                return json.load(f)
        return {"assets": [], "scholarly_links": [], "last_updated": None}

    def _get_checksum(self, content):
        return hashlib.sha256(content).hexdigest()

    def download_asset(self, url, asset_type, metadata):
        """Downloads and validates asset idempotently."""
        if not url: return None
        
        filename = simple_slugify(metadata['title']) + Path(url).suffix[:5]
        if not Path(filename).suffix:
            filename += ".jpg" if asset_type == "image" else ".mp4"
            
        # Fix: Ensure asset_type 'image' maps to folder 'images'
        folder_type = "images" if asset_type == "image" else asset_type
        local_path = self.assets_base / folder_type / self.component / filename
        rel_path = f"assets/{folder_type}/{self.component}/{filename}"

        # Check index for existing checksum
        existing = next((a for a in self.index_data.get('assets', []) if a.get('source_url') == url), None)
        if existing and local_path.exists() and not self.force:
            self.log.debug(f"Skipping existing asset: {filename}")
            return existing

        if self.dry_run:
            self.log.info(f"[Dry-Run] Would download {url} to {rel_path}")
            return None

        try:
            resp = requests.get(url, timeout=20)
            resp.raise_for_status()
            content = resp.content
            checksum = self._get_checksum(content)

            # Validate
            if asset_type == "image":
                try:
                    # check if it is image
                    with Image.open(requests.get(url, stream=True).raw) as img:
                        img.verify()
                except Exception:
                    pass # skip strict verify if it fails but we want it
            
            with open(local_path, 'wb') as f:
                f.write(content)

            asset_entry = {
                "id": str(hash(url)),
                "filename": filename,
                "local_path": rel_path,
                "type": asset_type,
                "license": metadata.get('license', 'Unknown'),
                "creator": metadata.get('creator', 'NASA'),
                "source_url": url,
                "retrieved_at": datetime.now().isoformat(),
                "checksum": checksum,
                "caption": metadata['title'],
                "alt_text": metadata.get('description', metadata['title'])[:100]
            }
            return asset_entry
        except Exception as e:
            self.log.error(f"Failed to download {url}: {e}")
            return None

    def fetch_nasa(self, query):
        self.log.info(f"Searching NASA for: {query}")
        api_url = "https://images-api.nasa.gov/search"
        params = {"q": query, "media_type": "image,video,audio"}
        
        try:
            data = requests.get(api_url, params=params).json()
            items = data.get('collection', {}).get('items', [])[:self.limit]
            
            results = []
            for item in items:
                meta = item['data'][0]
                nasa_id = meta['nasa_id']
                asset_type = meta['media_type']
                
                # Fetch manifest for actual file URLs
                manifest = requests.get(item['href']).json()
                # Pick highest res (usually first or specific pattern)
                file_url = next((u for u in manifest if "~orig" in u or ".jpg" in u), manifest[0])
                
                asset = self.download_asset(file_url, asset_type, {
                    "title": meta['title'],
                    "description": meta.get('description', ''),
                    "creator": meta.get('center', 'NASA'),
                    "license": "NASA Public Domain"
                })
                if asset: results.append(asset)
            return results
        except Exception as e:
            self.log.error(f"NASA API Error: {e}")
            return []

    def fetch_youtube(self, query):
        if not self.api_keys.get('YOUTUBE_API_KEY') or not YOUTUBE_LIB:
            self.log.warning("YouTube API Key missing. Skipping metadata fetch.")
            return []
        
        self.log.info(f"Fetching YouTube metadata for: {query}")
        try:
            youtube = build("youtube", "v3", developerKey=self.api_keys['YOUTUBE_API_KEY'])
            req = youtube.search().list(q=query, part="snippet", maxResults=self.limit, type="video")
            res = req.execute()
            
            videos = []
            for item in res.get('items', []):
                videos.append({
                    "type": "video",
                    "embed_url": f"https://www.youtube.com/embed/{item['id']['videoId']}",
                    "caption": item['snippet']['title'],
                    "creator": item['snippet']['channelTitle'],
                    "source_url": f"https://youtu.be/{item['id']['videoId']}",
                    "license": "Standard YouTube License"
                })
            return videos
        except Exception as e:
            self.log.error(f"YouTube API Error: {e}")
            return []

    def generate_scholarly(self, query):
        links = [
            {"text": f"Google Scholar: {self.component}", "url": f"https://scholar.google.com/scholar?q={quote_plus(query)}"},
            {"text": f"IEEE Xplore Research", "url": f"https://ieeexplore.ieee.org/search/searchresult.jsp?queryText={quote_plus(query)}"}
        ]
        return links

    def update_html(self):
        html_path = self.repo / f"{self.component}.html"
        if not html_path.exists():
            self.log.error(f"HTML file {html_path} not found.")
            return

        with open(html_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')

        # Generate the new section
        template = self.jinja_env.get_template('research_block.html.j2')
        new_html = template.render(
            assets=self.index_data.get('assets', []),
            scholarly_links=self.index_data.get('scholarly_links', []),
            component_name=self.component.upper()
        )
        new_soup = BeautifulSoup(new_html, 'html.parser')

        # Replace existing or append
        existing_sec = soup.find(id="research-assets")
        if existing_sec:
            existing_sec.replace_with(new_soup)
        else:
            footer = soup.find(id="footer-placeholder")
            if footer:
                footer.insert_before(new_soup)
            else:
                if soup.body:
                    soup.body.append(new_soup)

        if not self.dry_run:
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(soup.prettify())
            self.log.info(f"Updated HTML: {html_path}")

    def run(self, args):
        new_assets = []
        if args.nasa:
            new_assets.extend(self.fetch_nasa(args.nasa_query or self.component))
        
        if args.youtube:
            new_assets.extend(self.fetch_youtube(args.yt_query or self.component))

        if args.scholar:
            self.index_data['scholarly_links'] = self.generate_scholarly(args.query or self.component)

        # Merge assets idempotently
        if 'assets' not in self.index_data:
            self.index_data['assets'] = []
            
        for na in new_assets:
            if not any(a.get('source_url') == na['source_url'] for a in self.index_data['assets']):
                self.index_data['assets'].append(na)

        if not self.dry_run:
            self.index_data['last_updated'] = datetime.now().isoformat()
            with open(self.data_dir / f"{self.component}.json", 'w') as f:
                json.dump(self.index_data, f, indent=2)
            self.update_html()
        
        self.log.info("Ingest complete.")

def main():
    parser = argparse.ArgumentParser(description="CPMap Research Asset Ingestor")
    parser.add_argument("--repo", "-r", default=".", help="Local repo root")
    parser.add_argument("--component", "-c", required=True, help="Component slug")
    parser.add_argument("--add-page", "-p", help="Create new component page")
    parser.add_argument("--nasa", action="store_true", help="Fetch from NASA")
    parser.add_argument("--nasa-query", help="NASA search query")
    parser.add_argument("--youtube", action="store_true", help="Fetch YouTube metadata")
    parser.add_argument("--yt-query", help="YouTube search query")
    parser.add_argument("--scholar", action="store_true", help="Generate scholarly links")
    parser.add_argument("--query", help="General search query")
    parser.add_argument("--limit", type=int, default=5, help="Limit per source")
    parser.add_argument("--dry-run", action="store_true", help="No write mode")
    parser.add_argument("--force", action="store_true", help="Force overwrite")
    parser.add_argument("--api-keys-file", help="JSON file with API keys")
    parser.add_argument("--verbose", "-v", action="store_true")
    
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
        
    args = parser.parse_args()
    ingestor = CPMapIngestor(args)
    ingestor.run(args)

if __name__ == "__main__":
    main()
