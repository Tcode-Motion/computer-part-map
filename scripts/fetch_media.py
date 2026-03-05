import os
import json
import urllib.request
from pathlib import Path
from bs4 import BeautifulSoup
import wikipedia
from gtts import gTTS

DATA_DIR = Path('data')
ASSETS_DIR = Path('assets')

def download_image(url, save_path):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(save_path, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False

def generate_audio(text, save_path):
    try:
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(str(save_path))
        return True
    except Exception as e:
        print(f"Failed to generate audio: {e}")
        return False

def get_wikimedia_image(query):
    try:
        # Get page and its images
        page = wikipedia.page(query)
        images = page.images
        
        # Filter for diagrams or main images (avoid icons, svg if possible or just take first jpg/png)
        valid_images = [img for img in images if img.lower().endswith(('.jpg', '.png'))]
        if valid_images:
            img_url = valid_images[0]
            filename = img_url.split('/')[-1]
            return {
                'url': img_url,
                'filename': filename,
                'caption': f"Technical diagram or image related to {query}",
                'alt_text': f"Image of {query}",
                'license': 'Public Domain / Creative Commons via Wikimedia',
                'source_link': img_url
            }
    except Exception as e:
        print(f"Wikimedia fetch failed for {query}: {e}")
    return None

def fetch_media_for_component(slug, comp_data):
    name = comp_data.get('name', slug)
    
    # Setup directories
    img_dir = ASSETS_DIR / 'images' / slug
    audio_dir = ASSETS_DIR / 'audio' / slug
    img_dir.mkdir(parents=True, exist_ok=True)
    audio_dir.mkdir(parents=True, exist_ok=True)
    
    if 'media' not in comp_data:
        comp_data['media'] = {'images': [], 'videos': [], 'audio': []}
        
    # 1. Fetch Image
    if not comp_data['media']['images']:
        print(f"Fetching image for {name}...")
        img_info = get_wikimedia_image(name)
        if img_info:
            save_path = img_dir / img_info['filename']
            if download_image(img_info['url'], save_path):
                comp_data['media']['images'].append({
                    'local_path': f"assets/images/{slug}/{img_info['filename']}",
                    'alt_text': img_info['alt_text'],
                    'caption': img_info['caption'],
                    'source_link': img_info['source_link'],
                    'license': img_info['license']
                })
                
    # 2. Generate Audio
    if not comp_data['media']['audio']:
        print(f"Generating audio for {name}...")
        audio_filename = f"{slug}-overview.mp3"
        audio_path = audio_dir / audio_filename
        text_to_speak = f"Welcome to the overview of {name}. {comp_data.get('overview', '')}"
        if generate_audio(text_to_speak, audio_path):
            comp_data['media']['audio'].append({
                'local_path': f"assets/audio/{slug}/{audio_filename}",
                'caption': f"Audio Overview of {name}",
                'type': 'audio/mpeg'
            })
            
    # 3. Add Video (Hardcoded educational links for demonstration)
    if not comp_data['media']['videos']:
        video_map = {
            'cpu': 'https://www.youtube.com/embed/cNN_tTXABUA',
            'gpu': 'https://www.youtube.com/embed/L1jkEht3Ezo',
            'ram': 'https://www.youtube.com/embed/p3q5zWCwTeM',
            'motherboard': 'https://www.youtube.com/embed/Q0F7Z5Y4AXY'
        }
        if slug in video_map:
            comp_data['media']['videos'].append({
                'embed_url': video_map[slug],
                'caption': f"How the {name} works",
                'source': 'YouTube'
            })

def main():
    print("Fetching media...")
    for json_file in DATA_DIR.glob('*.json'):
        slug = json_file.stem
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        fetch_media_for_component(slug, data)
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
            
    print("Media fetched and JSON updated.")

if __name__ == '__main__':
    main()
