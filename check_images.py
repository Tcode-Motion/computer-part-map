import os, glob, re
from pathlib import Path

img_dir = set(os.listdir('images'))
missing = []

for html_file in glob.glob('*.html'):
    try:
        content = Path(html_file).read_text('utf-8')
        matches = re.findall(r'src="images/([^"]+)"', content)
        matches += re.findall(r"src='images/([^']+)'", content)
        for m in matches:
            if m not in img_dir:
                missing.append((html_file, m))
    except Exception as e:
        pass

for m in missing:
    print(f"Missing in {m[0]}: images/{m[1]}")
