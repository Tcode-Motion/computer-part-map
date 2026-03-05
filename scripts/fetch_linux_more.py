import os
import json
import urllib.request
from pathlib import Path
import wikipedia

DATA_DIR = Path('data')
ASSETS_DIR = Path('assets')

def download_image(url, save_path):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(save_path, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        return True
    except Exception:
        return False

def fetch_specific_images(slug, queries, start_count=0):
    img_dir = ASSETS_DIR / 'images' / slug
    img_dir.mkdir(parents=True, exist_ok=True)
    
    json_path = DATA_DIR / f"{slug}.json"
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    count = start_count
    for query in queries:
        print(f"Deep search for {query}...")
        try:
            # Try to get the exact page
            try:
                page = wikipedia.page(query)
            except wikipedia.DisambiguationError as e:
                page = wikipedia.page(e.options[0])
            except wikipedia.PageError:
                continue
                
            images = [img for img in page.images if img.lower().endswith(('.jpg', '.png', '.jpeg'))]
            
            for img_url in images[:3]: # Take up to 3 per specific query
                filename = f"{slug}-extra-{count}-" + img_url.split('/')[-1]
                save_path = img_dir / filename
                
                if download_image(img_url, save_path):
                    data['media']['images'].append({
                        'local_path': f"assets/images/{slug}/{filename}",
                        'alt_text': f"Image from {query}",
                        'caption': f"{query} - Hardware/Software view",
                        'source_link': img_url,
                        'license': 'Public Domain / Creative Commons via Wikimedia'
                    })
                    count += 1
                    print(f"Downloaded {filename}")
        except Exception as e:
            print(f"Error for {query}: {e}")

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def main():
    linux_extras = ["Ubuntu (operating system)", "Kali Linux", "Arch Linux", "Debian", "Linux Mint", "Manjaro", "Deepin"]
    fetch_specific_images('linux', linux_extras, start_count=20)
    
    # Update HTML again after fetching
    import sys
    sys.path.append('scripts')
    from update_page_content import update_html_text
    update_html_text('linux')

if __name__ == '__main__':
    main()
