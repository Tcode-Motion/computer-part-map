import os
import glob

files = glob.glob('*.html') + glob.glob('pages/*.html')
bs_css = '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">'
bs_js = '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>'

count = 0
for f_path in files:
    with open(f_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    if 'bootstrap.min.css' not in content:
        if '<link' in content:
            content = content.replace('<link', bs_css + '\n  <link', 1)
            modified = True
        elif '</head>' in content:
            content = content.replace('</head>', '  ' + bs_css + '\n</head>')
            modified = True
            
    if 'bootstrap.bundle.min.js' not in content:
        if '</body>' in content:
            content = content.replace('</body>', '  ' + bs_js + '\n</body>')
            modified = True
            
    if modified:
        with open(f_path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Successfully added Bootstrap to {count} files.")
