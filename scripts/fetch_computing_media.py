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

def fetch_multiple_images(slug, queries, limit=5):
    img_dir = ASSETS_DIR / 'images' / slug
    img_dir.mkdir(parents=True, exist_ok=True)
    
    json_path = DATA_DIR / f"{slug}.json"
    if not json_path.exists(): return
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if 'media' not in data:
        data['media'] = {'images': [], 'videos': [], 'audio': []}
    
    count = len(data['media']['images'])
    for query in queries:
        if count >= limit: break
        print(f"Searching for {query}...")
        try:
            search_results = wikipedia.search(query)
            if not search_results: continue
            
            page = wikipedia.page(search_results[0])
            images = [img for img in page.images if img.lower().endswith(('.jpg', '.png', '.jpeg'))]
            
            for img_url in images:
                if count >= limit: break
                filename = f"{slug}-comp-{count}-" + img_url.split('/')[-1]
                save_path = img_dir / filename
                
                if download_image(img_url, save_path):
                    data['media']['images'].append({
                        'local_path': f"assets/images/{slug}/{filename}",
                        'alt_text': f"Image from {query}",
                        'caption': f"{query} technical image",
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
    # Raspberry Pi
    fetch_multiple_images('raspberry-pi', ["Raspberry Pi 5", "Raspberry Pi 4", "Single-board computer", "GPIO pins"], limit=10)
    
    # NPU
    fetch_multiple_images('npu', ["Neural processing unit", "Tensor Processing Unit", "Apple Neural Engine", "AI accelerator"], limit=10)
    
    # Quantum
    fetch_multiple_images('quantum-computing', ["Quantum computer", "Superconducting quantum computing", "Quantum processor", "Qubit"], limit=10)
    
    # Networking
    fetch_multiple_images('router', ["Wireless router", "Network switch", "Router (computing)"], limit=8)
    fetch_multiple_images('nic', ["Network interface controller", "Ethernet card"], limit=8)
    fetch_multiple_images('wifi-adapter', ["WiFi adapter", "Wireless network interface controller"], limit=8)

if __name__ == '__main__':
    main()
