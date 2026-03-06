import os

root_dir = r"c:\Users\tanmoy\Documents\jast work on this now\basic web"
pages_dir = os.path.join(root_dir, "pages")

# Mappings based on literal corrupted strings left in the files
mapping = {
    "€”": "—",
    "€“": "–",
    "€™": "’",
    "€œ": "“",
    "€ ": "”",
    "€\x9d": "”", # \x9d control char
    "€˜": "‘",
    "€¢": "•",
    "š™ï¸ ": "⚙️",
    "š™": "⚙️",
    "ŸŽ¥": "🎥",
    "Ÿ“–": "📖",
    "Ÿ’¡": "💡",
    "Ÿ†š": "🆚",
    "Ÿ“Š": "📊",
    "Ÿ›’": "🛒",
    "Ÿ”—": "🔗",
    "Ÿ’¾": "💾",
    "Ÿ–¥ï¸ ": "🖥️",
    "Ÿ”Œ": "🔌",
    "Ÿ“š": "📚",
    "–¶ï¸ ": "▶️",
    "Ÿ“œ": "📜",
    "Ÿ —ï¸ ": "🏗️",
    "Ÿ”¬": "🔬",
    "‚¹": "₹",
    "Ÿ’»": "💻",
    "Ÿ› ï¸ ": "🛠️",
    "Ÿ§ ": "🧠",
    "Ÿ”®": "🔮",
    "ŸŒ": "🌐",
    "Ÿ“¡": "📡",
    "Ÿ“€": "📀",
    "Ÿ–±ï¸ ": "🖱️",
    "Ÿ–¨ï¸ ": "🖨️",
    "Ÿš€": "🚀",
    "¨": "⚡",
    "ŸŒŸ": "🌟"
}

def fix_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        new_content = content
        
        # Specific cleanup for GPU â€”€” issue where it might be structured 'GPU €”' replacing with 'GPU —'
        for corrupted, fixed in mapping.items():
            if corrupted in new_content:
                new_content = new_content.replace(corrupted, fixed)

        # Ensure no double dashes from "GPU —€”" -> "GPU ——"
        new_content = new_content.replace("——", "—")
        new_content = new_content.replace(" GPU —", " GPU —")

        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            return True
    except Exception as e:
        print("Error in", filepath, e)
    return False

count = 0
for subdir, _, files in os.walk(pages_dir):
    for file in files:
        if file.endswith(".html"):
            if fix_file(os.path.join(subdir, file)): count += 1

for file in os.listdir(root_dir):
    if file.endswith(".html"):
        if fix_file(os.path.join(root_dir, file)): count += 1

print("Total literal restored:", count)
