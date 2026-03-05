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
    except Exception as e:
        # print(f"Failed to download {url}: {e}")
        return False

def fetch_multiple_images(slug, queries, limit=5):
    img_dir = ASSETS_DIR / 'images' / slug
    img_dir.mkdir(parents=True, exist_ok=True)
    
    json_path = DATA_DIR / f"{slug}.json"
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if 'media' not in data:
        data['media'] = {'images': [], 'videos': [], 'audio': []}
    
    count = 0
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
                filename = f"{slug}-{count}-" + img_url.split('/')[-1]
                save_path = img_dir / filename
                
                if download_image(img_url, save_path):
                    data['media']['images'].append({
                        'local_path': f"assets/images/{slug}/{filename}",
                        'alt_text': f"Image from {query}",
                        'caption': f"{query} screenshot or diagram",
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
    # Linux: 15+ images
    linux_queries = [
        "Kali Linux", "Parrot Security OS", "Ubuntu", "Arch Linux", "Fedora Linux",
        "Debian", "Linux Mint", "Manjaro Linux", "Elementary OS", "Pop!_OS",
        "CentOS", "Red Hat Enterprise Linux", "Gentoo Linux", "Slackware", "OpenSUSE"
    ]
    print("Fetching Linux images...")
    fetch_multiple_images('linux', linux_queries, limit=20)

    # Windows: 7, 10, 11
    windows_queries = ["Windows 7", "Windows 10", "Windows 11"]
    print("Fetching Windows images...")
    fetch_multiple_images('windows', windows_queries, limit=10)

    # macOS
    macos_queries = ["macOS", "MacBook Pro", "iMac", "macOS Sonoma", "macOS Ventura"]
    print("Fetching macOS images...")
    fetch_multiple_images('macos', macos_queries, limit=10)

    # Android
    android_queries = ["Android (operating system)", "Android 14", "Android 13", "Material You"]
    print("Fetching Android images...")
    fetch_multiple_images('android', android_queries, limit=10)

    # iOS
    ios_queries = ["iOS", "iPhone 15", "iOS 17", "App Store"]
    print("Fetching iOS images...")
    fetch_multiple_images('ios', ios_queries, limit=10)

if __name__ == '__main__':
    main()
