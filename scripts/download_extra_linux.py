import urllib.request
from pathlib import Path

def download(url, path):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(path, 'wb') as out_file:
            out_file.write(response.read())
        print(f"Downloaded {path}")
    except Exception as e:
        print(f"Failed {path}: {e}")

Path('assets/images/linux').mkdir(parents=True, exist_ok=True)

downloads = [
    ('https://upload.wikimedia.org/wikipedia/commons/2/22/Kali-linux-2023.1-desktop.png', 'assets/images/linux/linux-12-Kali.png'),
    ('https://upload.wikimedia.org/wikipedia/commons/a/ac/Ubuntu_24.04_LTS_Desktop.png', 'assets/images/linux/linux-13-Ubuntu.png'),
    ('https://upload.wikimedia.org/wikipedia/commons/e/e8/Arch_Linux_KDE_Plasma.png', 'assets/images/linux/linux-14-Arch.png')
]

for url, path in downloads:
    download(url, path)
