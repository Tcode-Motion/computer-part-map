import os
import glob
from bs4 import BeautifulSoup
import json
import hashlib
import re

def get_files():
    html_files = glob.glob('**/*.html', recursive=True)
    return html_files

def check_link(file_path, link_url):
    if not link_url:
        return True
    if link_url.startswith(('http://', 'https://', 'mailto:', 'tel:', 'javascript:', '#')):
        return True

    link_url = link_url.split('?')[0].split('#')[0]
    if not link_url:
        return True

    if link_url.startswith('/'):
        target = os.path.join(os.getcwd(), link_url.lstrip('/'))
    else:
        target = os.path.normpath(os.path.join(os.path.dirname(file_path), link_url))

    return os.path.exists(target)

def audit():
    html_files = get_files()

    broken_links = []
    broken_images = []
    missing_assets = []
    missing_alt = []
    missing_meta_desc = []
    missing_title = []
    missing_viewport = []
    large_files = []

    file_hashes = {}
    duplicates = []

    # CSS and JS hashes for duplicate checking
    for asset_type, ext in [('CSS', '*.css'), ('JS', '*.js')]:
        for f in glob.glob(f'**/{ext}', recursive=True):
            if os.path.isfile(f):
                with open(f, 'rb') as file:
                    content = file.read()
                    f_hash = hashlib.md5(content).hexdigest()
                    if f_hash in file_hashes:
                        duplicates.append((f, file_hashes[f_hash]))
                    else:
                        file_hashes[f_hash] = f

                # Check for large files
                size_kb = os.path.getsize(f) / 1024
                if size_kb > 500: # 500KB threshold
                    large_files.append((f, size_kb))

    # Check images for size
    for f in glob.glob('**/*.jpg', recursive=True) + glob.glob('**/*.png', recursive=True):
        if os.path.isfile(f):
            size_kb = os.path.getsize(f) / 1024
            if size_kb > 500: # 500KB threshold for images
                large_files.append((f, size_kb))

    for f in html_files:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            soup = BeautifulSoup(content, 'html.parser')

            # Links
            for a in soup.find_all('a', href=True):
                if not check_link(f, a['href']):
                    broken_links.append((f, a['href']))

            # Images & A11y
            for img in soup.find_all('img', src=True):
                if not check_link(f, img['src']):
                    broken_images.append((f, img['src']))
                if not img.get('alt'):
                    missing_alt.append((f, img['src']))

            # Assets
            for link in soup.find_all('link', href=True):
                if link.get('rel') == ['stylesheet'] or link['href'].endswith('.css'):
                    if not check_link(f, link['href']):
                        missing_assets.append((f, link['href']))

            for script in soup.find_all('script', src=True):
                if not check_link(f, script['src']):
                    missing_assets.append((f, script['src']))

            # SEO & Mobile
            title = soup.find('title')
            if not title or not title.text.strip():
                missing_title.append(f)

            meta_desc = soup.find('meta', attrs={'name': 'description'})
            if not meta_desc or not meta_desc.get('content'):
                missing_meta_desc.append(f)

            viewport = soup.find('meta', attrs={'name': 'viewport'})
            if not viewport:
                missing_viewport.append(f)

    # Calculate unused files
    used_files = set()
    for f in html_files:
        used_files.add(os.path.abspath(f))
        with open(f, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            for tag in soup.find_all(['a', 'link', 'script', 'img']):
                url = tag.get('href') or tag.get('src')
                if url and not url.startswith(('http://', 'https://', 'mailto:', 'tel:', 'javascript:', '#')):
                    url = url.split('?')[0].split('#')[0]
                    if url:
                        if url.startswith('/'):
                            target = os.path.join(os.getcwd(), url.lstrip('/'))
                        else:
                            target = os.path.normpath(os.path.join(os.path.dirname(f), url))
                        used_files.add(os.path.abspath(target))

    all_files = set([os.path.abspath(f) for f in glob.glob('**/*', recursive=True) if os.path.isfile(f)])

    unused_files = all_files - used_files

    # Exclude standard things from unused files like .git, scripts, json, etc
    unused_files_filtered = []
    for f in unused_files:
        if '.git' in f or '/tools/' in f or '/scripts/' in f or '/ci/' in f or '/templates/' in f or f.endswith('.json') or f.endswith('.py') or f.endswith('README.md') or f.endswith('.txt'):
            continue
        rel_path = os.path.relpath(f, os.getcwd())
        unused_files_filtered.append(rel_path)

    result = {
        'broken_links': broken_links,
        'broken_images': broken_images,
        'missing_assets': missing_assets,
        'missing_alt': missing_alt,
        'missing_title': missing_title,
        'missing_meta_desc': missing_meta_desc,
        'missing_viewport': missing_viewport,
        'large_files': large_files,
        'duplicates': duplicates,
        'unused_files': unused_files_filtered
    }

    with open('advanced_audit.json', 'w') as f:
        json.dump(result, f, indent=2)

if __name__ == "__main__":
    audit()
