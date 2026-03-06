import os

root_dir = r"c:\Users\tanmoy\Documents\jast work on this now\basic web"
pages_dir = os.path.join(root_dir, "pages")

symbols = [
    "—", "–", "’", "“", "”", "‘", "•", "é", "®", "©", "…",
    "⚙️", "🎥", "📖", "💡", "🆚", "📊", "🛒", "🔗", "💾", "🖥️",
    "🔌", "📚", "▶️", "📜", "🏗️", "🔬", "₹", "💻", "🛠️", "🧠",
    "🔮", "🌐", "📡", "📀", "🖱️", "🖨️", "🚀", "⚡", "🌟"
]

mapping = {}
for sym in symbols:
    utf8_bytes = sym.encode("utf-8")
    corrupted_str = utf8_bytes.decode("cp1252", errors="replace")
    mapping[corrupted_str] = sym

sorted_mapping = sorted(mapping.items(), key=lambda x: len(x[0]), reverse=True)

def fix_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        new_content = content
        for corrupted, fixed in sorted_mapping:
            if corrupted in new_content:
                new_content = new_content.replace(corrupted, fixed)

        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            return True
    except Exception as e:
        print("Error in", filepath, e)
    return False

count = 0
for file in os.listdir(root_dir):
    if file.endswith(".html"):
        if fix_file(os.path.join(root_dir, file)): count += 1

for subdir, _, files in os.walk(pages_dir):
    for file in files:
        if file.endswith(".html"):
            if fix_file(os.path.join(subdir, file)): count += 1

print("Total restored:", count)
