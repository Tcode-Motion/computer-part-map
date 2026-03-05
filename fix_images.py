import os
from pathlib import Path

replacements = {
    'computer-types.html': ('images/computer-types.png', 'images/computer.jpg'),
    'cooling.html': ('images/cooling.jpg', 'images/frameless fan.jpg'),
    'linux.html': ('images/linux.png', 'images/windows operating system.jpg'),
    'macos.html': ('images/macos.png', 'images/computer.jpg'),
    'operating-systems.html': ('images/os.png', 'images/windows operating system.jpg'),
    'optical-drive.html': ('images/optical-drive.jpg', 'images/cd dvd rider.jpg'),
    'server-guide.html': ('images/server.png', 'images/LAN.jpg'),
    'software-types.html': ('images/software.png', 'images/windows operating system.jpg'),
    'ups.html': ('images/ups.jpg', 'images/battery.jpg'),
    'windows.html': ('images/windows.png', 'images/windows operating system.jpg')
}

for filename, (old, new) in replacements.items():
    p = Path(filename)
    if p.exists():
        content = p.read_text('utf-8')
        content = content.replace(old, new)
        p.write_text(content, 'utf-8')
        print(f"Fixed {filename}")
