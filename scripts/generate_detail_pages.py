import os
import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from bs4 import BeautifulSoup

DATA_DIR = Path('data')
TEMPLATE_DIR = Path('templates')

env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)))

def update_main_page(slug, comp_data):
    main_html_path = Path(f"{slug}.html")
    if not main_html_path.exists():
        return

    with open(main_html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # Add navigation to detail pages
    subpages = comp_data.get('subpages', [])
    if subpages:
        nav_section = soup.find(id="detail-pages-nav")
        if not nav_section:
            new_nav = soup.new_tag("div", **{'class': 'content-section', 'id': 'detail-pages-nav'})
            h2 = soup.new_tag("h2")
            h2.string = "📚 Detailed Research Pages"
            new_nav.append(h2)
            
            grid = soup.new_tag("div", **{'class': 'related-grid'})
            for sub in subpages:
                a = soup.new_tag("a", href=sub['slug'], **{'class': 'related-link'})
                a.string = f"📄 {sub['title']}"
                grid.append(a)
            new_nav.append(grid)
            
            # Insert before the related components section or at the end of page-content
            page_content = soup.find('div', class_='page-content')
            if page_content:
                # Find the last content-section
                sections = page_content.find_all('div', class_='content-section')
                if sections:
                    sections[-1].insert_before(new_nav)
                else:
                    page_content.append(new_nav)

    # Add Video/Audio sections if present
    media = comp_data.get('media', {})
    if media.get('videos') or media.get('audio'):
        media_section = soup.find(id="media-section")
        if not media_section:
            m_sec = soup.new_tag("div", **{'class': 'content-section', 'id': 'media-section'})
            m_h2 = soup.new_tag("h2")
            m_h2.string = "🎥 Explanatory Media"
            m_sec.append(m_h2)
            
            if media.get('videos'):
                for vid in media['videos']:
                    vid_wrapper = soup.new_tag("div", style="position:relative; padding-bottom:56.25%; height:0; overflow:hidden; border-radius:8px; margin-bottom:15px;")
                    iframe = soup.new_tag("iframe", src=vid['embed_url'], style="position:absolute; top:0; left:0; width:100%; height:100%; border:none;", allowfullscreen="")
                    vid_wrapper.append(iframe)
                    m_sec.append(vid_wrapper)
            
            if media.get('audio'):
                for aud in media['audio']:
                    aud_tag = soup.new_tag("audio", controls="", src=aud['local_path'], style="width:100%; margin-top:10px;")
                    m_sec.append(aud_tag)
            
            page_content = soup.find('div', class_='page-content')
            if page_content:
                page_content.insert(0, m_sec)

    with open(main_html_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
def main():
    print("Generating detail pages...")
    template = env.get_template('detail_page.html.j2')
    
    generated_count = 0
    for json_file in DATA_DIR.glob('*.json'):
        slug = json_file.stem
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        subpages = data.get('subpages', [])
        for sub in subpages:
            html_content = template.render(
                subpage_title=sub['title'],
                component_name=data.get('name', slug),
                overview=data.get('overview', ''),
                architecture=data.get('architecture', ''),
                working_principle=data.get('working_principle', ''),
                media=data.get('media', {}),
                parent_slug=slug
            )
            
            out_path = Path(sub['slug'])
            with open(out_path, 'w', encoding='utf-8') as out_f:
                out_f.write(html_content)
            generated_count += 1
            print(f"Created: {out_path}")
            
        # Update main page
        update_main_page(slug, data)
        
    print(f"Generated {generated_count} detail pages.")

if __name__ == '__main__':
    main()
