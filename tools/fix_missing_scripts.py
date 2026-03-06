import os
import glob

# Collect all HTML files
files = glob.glob('*.html') + glob.glob('pages/*.html')

count = 0
for f_path in files:
    with open(f_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # Custom Script (js/script.js)
    # Determine what it SHOULD be
    correct_script = 'js/script.js' if not f_path.startswith('pages') else '../js/script.js'
    
    # Check if ANY form of script.js exists
    if 'script.js' not in content:
        script_tag = f'<script src="{correct_script}"></script>'
        if '</body>' in content:
            content = content.replace('</body>', '  ' + script_tag + '\n</body>')
            modified = True
            
    if modified:
        with open(f_path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Force-injected missing script.js into {count} files.")
