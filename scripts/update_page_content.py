import json
from pathlib import Path
from bs4 import BeautifulSoup

DATA_DIR = Path('data')

def update_html_text(slug):
    json_path = DATA_DIR / f"{slug}.json"
    html_path = Path(f"{slug}.html")
    
    if not json_path.exists() or not html_path.exists():
        return
        
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    # Update Overview
    overview_section = None
    for h2 in soup.find_all('h2'):
        if 'Overview' in h2.text or 'What is' in h2.text:
            overview_section = h2.parent
            break
            
    if overview_section:
        # Find paragraphs and update
        p_tags = overview_section.find_all('p')
        if p_tags:
            p_tags[0].string = data.get('overview', p_tags[0].text)
            
    # Add History and Architecture sections if they don't exist
    page_content = soup.find('div', class_='page-content')
    if page_content:
        # Check for History
        if not any('History' in h2.text for h2 in soup.find_all('h2')):
            new_sec = soup.new_tag("div", **{'class': 'content-section'})
            h2 = soup.new_tag("h2")
            h2.string = "📜 History"
            p = soup.new_tag("p")
            p.string = data.get('history', '')
            new_sec.append(h2)
            new_sec.append(p)
            page_content.append(new_sec)
            
        # Check for Architecture
        if not any('Architecture' in h2.text for h2 in soup.find_all('h2')):
            new_sec = soup.new_tag("div", **{'class': 'content-section'})
            h2 = soup.new_tag("h2")
            h2.string = "🏗️ Architecture"
            p = soup.new_tag("p")
            p.string = data.get('architecture', '')
            new_sec.append(h2)
            new_sec.append(p)
            page_content.append(new_sec)

    # Add Image Gallery if media images are many
    if 'media' in data and len(data['media']['images']) > 1:
        gallery_id = "image-gallery"
        if not soup.find(id=gallery_id):
            gallery_sec = soup.new_tag("div", **{'class': 'content-section', 'id': gallery_id})
            h2 = soup.new_tag("h2")
            h2.string = "🖼️ Visual Gallery"
            gallery_sec.append(h2)
            
            grid = soup.new_tag("div", **{'class': 'products-grid'})
            for img in data['media']['images']:
                fig = soup.new_tag("figure", **{'class': 'product-card', 'style': 'margin:0;'})
                i = soup.new_tag("img", src=img['local_path'], alt=img['alt_text'], style="max-width:100%; border-radius:8px;")
                cap = soup.new_tag("figcaption", style="margin-top:10px; font-size:0.85rem; color:var(--text-muted);")
                cap.string = img['caption']
                fig.append(i)
                fig.append(cap)
                grid.append(fig)
            gallery_sec.append(grid)
            
            # Insert at the end or before related
            related = soup.find(id="detail-pages-nav")
            if related:
                related.insert_before(gallery_sec)
            else:
                page_content.append(gallery_sec)

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))

def main():
    for json_file in DATA_DIR.glob('*.json'):
        slug = json_file.stem
        update_html_text(slug)
        print(f"Updated content for {slug}.html")

if __name__ == '__main__':
    main()
