import os
import json
from pathlib import Path
from bs4 import BeautifulSoup

DATA_DIR = Path('data')
INDEX_FILE = Path('search_index.json')

def main():
    print("Building search index...")
    documents = []
    
    # Also index all HTML files
    for html_file in Path('.').glob('*.html'):
        if html_file.name in ['index.html', 'about.html']:
            continue
            
        with open(html_file, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
            
        title_tag = soup.find('title')
        title = title_tag.text.split('|')[0].strip() if title_tag else html_file.stem
        
        # Extract text from page content
        page_content = soup.find('div', class_='page-content')
        text_content = ""
        if page_content:
            text_content = " ".join([p.text for p in page_content.find_all(['p', 'li', 'td'])])
            
        # Add basic html doc
        documents.append({
            'id': html_file.name,
            'title': title,
            'body': text_content[:1000],  # truncate to keep index small
            'url': html_file.name
        })

    # Index JSON data deeper
    for json_file in DATA_DIR.glob('*.json'):
        slug = json_file.stem
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        text_fields = [
            data.get('overview', ''),
            data.get('architecture', ''),
            data.get('history', ''),
            data.get('working_principle', ''),
            " ".join(data.get('applications', [])),
            " ".join(data.get('benchmarks', []))
        ]
        
        for ref in data.get('references', []):
            text_fields.append(ref.get('text', ''))
            
        combined_text = " ".join(text_fields)
        
        # We can just update or add to the existing doc if needed, but simple append is fine.
        documents.append({
            'id': f"data-{slug}",
            'title': f"{data.get('name', slug)} Deep Data",
            'body': combined_text,
            'url': f"{slug}.html"
        })

    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        json.dump(documents, f, indent=2)
        
    print(f"Search index built with {len(documents)} documents.")

if __name__ == '__main__':
    main()
