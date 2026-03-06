import os
import json

ROOT_DIR = os.path.abspath(".")
PAGES_DIR = os.path.join(ROOT_DIR, "pages") # Using the new structure
DATA_DIR = os.path.join(ROOT_DIR, "data")
DOCS_DIR = os.path.join(ROOT_DIR, "docs")
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")

# Ensure base directories exist
for d in [PAGES_DIR, DATA_DIR, DOCS_DIR, ASSETS_DIR, 
          os.path.join(ASSETS_DIR, "audio"), os.path.join(ASSETS_DIR, "video")]:
    os.makedirs(d, exist_ok=True)

# File definitions
html_pages = {
    "Core Pages": [
        "index.html", "explore.html", "compare.html", "history.html", 
        "architecture.html", "learn.html", "search.html", "timeline.html", 
        "about.html", "contribute.html"
    ],
    "Hardware Detail Pages": [
        "cpu.html", "gpu.html", "ram.html", "motherboard.html", "storage.html", 
        "psu.html", "cooling.html", "case.html", "network.html", "input.html", 
        "output.html", "ports.html", "chips.html"
    ],
    "Sub-Component Pages": [
        "cpu-core.html", "cpu-cache.html", "cpu-threads.html", "cpu-architecture.html", 
        "cpu-instruction-set.html", "cpu-fabrication.html",
        "gpu-core.html", "gpu-memory.html", "gpu-cuda.html", "gpu-raytracing.html", "gpu-tensor.html"
    ],
    "Deep Hardware Knowledge": [
        "transistor.html", "semiconductor.html", "binary.html", "logic-gates.html", 
        "microarchitecture.html", "instruction-cycle.html", "bus-system.html", 
        "chip-fabrication.html", "nanometer-process.html"
    ],
    "Visual Learning Sections": [
        "pc-build.html", "hardware-map.html", "3d-pc.html", "component-flow.html", 
        "boot-process.html", "data-flow.html"
    ],
    "Historical Knowledge": [
        "history-cpu.html", "history-storage.html", "history-ram.html", 
        "history-gpu.html", "history-computers.html"
    ],
    "Comparison Pages": [
        "cpu-compare.html", "gpu-compare.html", "ram-types.html", "storage-types.html", 
        "interface-types.html"
    ],
    "Standards & Interfaces": [
        "pcie.html", "sata.html", "nvme.html", "usb.html", "thunderbolt.html", 
        "ethernet.html", "wifi.html", "bluetooth.html"
    ],
    "Computer Architecture": [
        "von-neumann.html", "harvard-architecture.html", "pipeline.html", 
        "parallel-computing.html", "quantum-computing.html", "neuromorphic.html"
    ],
    "Educational Pages": [
        "how-computer-works.html", "how-cpu-works.html", "how-gpu-works.html", 
        "how-ram-works.html", "how-ssd-works.html", "how-motherboard-works.html"
    ],
    "Future Tech Pages": [
        "quantum-computer.html", "optical-computing.html", "dna-computing.html", 
        "ai-chips.html", "neuromorphic-chips.html", "photonics.html"
    ],
    "Visualization Pages": [
        "component-network.html", "system-map.html", "hardware-tree.html"
    ]
}

data_files = {
    "parts.json": {"parts": []},
    "categories.json": {"categories": []},
    "timeline.json": {"events": []},
    "cpu-database.json": {"cpus": [{"name": "Intel 4004", "year": 1971, "transistors": 2300, "architecture": "4-bit", "importance": "First commercial microprocessor"}]},
    "gpu-database.json": {"gpus": []},
    "ram-database.json": {"rams": []},
    "storage-database.json": {"storages": []},
    "schema.json": {"$schema": "http://json-schema.org/draft-07/schema#"},
    "component-map.json": {"components": []},
    "relationships.json": {"relations": [{"source": "CPU", "relation": "uses", "target": "RAM"}, {"source": "GPU", "relation": "connects", "target": "PCIe"}]}
}

# HTML Template
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Computer Parts Map</title>
    <meta name="description" content="Detailed guide on {title}. Part of the 100-Year Hardware Archive.">
    <link rel="stylesheet" href="../css/styles.css">
</head>
<body class="dark-mode">
    <div id="navbar-placeholder"></div>
    
    <main class="page-content" style="padding: 100px 5%;">
        <div class="badge">{category}</div>
        <h1>{title}</h1>
        <p>This is a placeholder page for <strong>{title}</strong>. This section will contain detailed explanations, diagrams, and historical context.</p>
        
        <div class="content-section">
            <h2>Under Construction 🏗️</h2>
            <p>Data for this module is being curated for the 100-year knowledge base.</p>
        </div>
    </main>

    <div id="footer-placeholder"></div>
    <script src="../js/script.js"></script>
</body>
</html>
"""

# Generate HTML Files
for category, files in html_pages.items():
    for filename in files:
        filepath = os.path.join(PAGES_DIR, filename)
        if not os.path.exists(filepath):
            title = filename.replace('.html', '').replace('-', ' ').title()
            # Special case for index.html which goes to root
            if filename == "index.html":
                filepath = os.path.join(ROOT_DIR, filename)
                # Adjust CSS/JS paths for root
                content = html_template.format(title="Computer Hardware Wikipedia", category=category).replace("../css/styles.css", "css/styles.css").replace("../js/script.js", "js/script.js")
            else:
                content = html_template.format(title=title, category=category)
                
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

# Generate JSON Data Files
for filename, content in data_files.items():
    # If the file is schema, component-map, or relationships, they can go in root or data. Let's put in data.
    filepath = os.path.join(DATA_DIR, filename)
    if not os.path.exists(filepath):
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(content, f, indent=2)

print("Scaffolded all required 100-year architecture files successfully.")
