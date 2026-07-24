import json

with open('advanced_audit.json', 'r') as f:
    data = json.load(f)

todo = """# Project Audit & TODO Checklist

## 1. High Priority (Critical Functionality)
"""

if data['missing_assets']:
    todo += "### Fix Missing Core Assets (CSS/JS)\n"
    for f, l in data['missing_assets']:
        todo += f"- [ ] In `{f}`, fix link to `{l}`\n"
else:
    todo += "- [x] No missing CSS/JS assets found.\n"

if data['broken_links']:
    todo += "\n### Fix Broken Links\n"
    # Group by file
    from collections import defaultdict
    broken_by_file = defaultdict(list)
    for f, l in data['broken_links']:
        broken_by_file[f].append(l)

    for f, links in broken_by_file.items():
        todo += f"- [ ] Fix {len(links)} broken links in `{f}`\n"
else:
    todo += "- [x] No broken links found.\n"

if data['broken_images']:
    todo += "\n### Fix Broken Images\n"
    broken_by_file = defaultdict(list)
    for f, l in data['broken_images']:
        broken_by_file[f].append(l)

    for f, images in broken_by_file.items():
        todo += f"- [ ] Fix {len(images)} broken images in `{f}`\n"
else:
    todo += "- [x] No broken images found.\n"

todo += """
## 2. Medium Priority (SEO, Accessibility, Cleanup)
"""

if data['missing_alt']:
    todo += "### Fix Missing Image Alt Attributes\n"
    todo += f"- [ ] Add missing alt tags to {len(data['missing_alt'])} images across the site\n"
else:
    todo += "- [x] No missing alt attributes found.\n"

if data['missing_title'] or data['missing_meta_desc'] or data['missing_viewport']:
    todo += "\n### Fix SEO & Mobile Responsiveness\n"
    if data['missing_title']:
        todo += f"- [ ] Add missing `<title>` to {len(data['missing_title'])} pages\n"
    if data['missing_meta_desc']:
        todo += f"- [ ] Add missing `<meta name=\"description\">` to {len(data['missing_meta_desc'])} pages\n"
    if data['missing_viewport']:
        todo += f"- [ ] Add missing viewport meta tag to {len(data['missing_viewport'])} pages\n"
else:
    todo += "- [x] Basic SEO and viewport tags are present on all pages.\n"

if data['duplicates']:
    todo += "\n### Remove Duplicate CSS Files\n"
    for d in data['duplicates']:
        todo += f"- [ ] `{d[0]}` is a duplicate of `{d[1]}` - remove it and update references\n"

todo += """
## 3. Low Priority (Performance & Maintenance)
"""

if data['large_files']:
    todo += "### Optimize Large Files (>500KB)\n"
    for f, size in data['large_files']:
        todo += f"- [ ] Compress `{f}` (Current size: {size:.1f} KB)\n"
else:
    todo += "- [x] No excessively large files found.\n"

if data['unused_files']:
    todo += "\n### Remove Unused Files\n"
    todo += f"- [ ] Clean up {len(data['unused_files'])} potentially unused assets/images\n"

with open('TODO.md', 'w') as f:
    f.write(todo)

print("TODO.md generated.")
