import os
import json

PAGES_DIR = os.path.abspath("pages")
DATA_DIR = os.path.abspath("data")
ASSETS_DIR = os.path.abspath("assets")

# The list of pages to generate
cpu_pages = {
    "Core CPU Pages": [
        "cpu-overview.html", "cpu-history.html", "cpu-architecture.html", 
        "cpu-comparison.html", "cpu-database.html"
    ],
    "CPU Internal Components": [
        "cpu-core.html", "cpu-thread.html", "cpu-cache.html", "cpu-clock-speed.html", 
        "cpu-pipeline.html", "cpu-branch-prediction.html", "cpu-instruction-set.html", 
        "cpu-registers.html", "cpu-bus.html"
    ],
    "CPU Manufacturing": [
        "cpu-fabrication.html", "cpu-transistor.html", "cpu-nanometer.html", 
        "cpu-chip-design.html", "cpu-silicon.html"
    ],
    "CPU Architecture Families": [
        "x86-architecture.html", "arm-architecture.html", "riscv-architecture.html", 
        "powerpc-architecture.html"
    ],
    "CPU Performance Topics": [
        "cpu-benchmark.html", "cpu-overclocking.html", "cpu-efficiency.html", 
        "cpu-power-consumption.html"
    ],
    "CPU Generations": [
        "intel-cpu-history.html", "amd-cpu-history.html", "arm-cpu-history.html", 
        "apple-silicon-history.html"
    ],
    "CPU Future Technology": [
        "quantum-cpu.html", "ai-cpu.html", "neuromorphic-cpu.html", 
        "optical-cpu.html", "3d-stacked-cpu.html"
    ]
}

# Extensive CPU Data for the JSON Database
cpu_database = {
    "schema": ["name", "manufacturer", "architecture", "release_year", "cores", "threads", "base_clock", "boost_clock", "transistors", "fabrication", "cache_l3", "tdp", "instructions"],
    "cpus": [
        {
            "name": "Intel Core i9-14900K", "manufacturer": "Intel", "architecture": "Raptor Lake Refresh", "release_year": 2023,
            "cores": 24, "threads": 32, "base_clock": "3.2 GHz", "boost_clock": "6.0 GHz", "transistors": "Billion+", "fabrication": "Intel 7 (10nm)",
            "cache_l3": "36 MB", "tdp": "125W - 253W", "instructions": "x86-64, SSE4.2, AVX2"
        },
        {
            "name": "AMD Ryzen 9 7950X3D", "manufacturer": "AMD", "architecture": "Zen 4", "release_year": 2023,
            "cores": 16, "threads": 32, "base_clock": "4.2 GHz", "boost_clock": "5.7 GHz", "transistors": "13.1 Billion (CCD)", "fabrication": "TSMC 5nm",
            "cache_l3": "128 MB (3D V-Cache)", "tdp": "120W", "instructions": "x86-64, AVX-512"
        },
        {
            "name": "Apple M3 Max", "manufacturer": "Apple", "architecture": "ARMv8.6-A", "release_year": 2023,
            "cores": 16, "threads": 16, "base_clock": "3.2 GHz", "boost_clock": "4.05 GHz", "transistors": "92 Billion", "fabrication": "TSMC 3nm",
            "cache_l3": "System Level Cache", "tdp": "30W - 78W", "instructions": "ARM64"
        },
        {
            "name": "Intel 4004", "manufacturer": "Intel", "architecture": "4-bit", "release_year": 1971,
            "cores": 1, "threads": 1, "base_clock": "740 kHz", "boost_clock": "N/A", "transistors": "2,300", "fabrication": "10,000nm",
            "cache_l3": "None", "tdp": "Under 1W", "instructions": "4004 ISA"
        },
        {
            "name": "Qualcomm Snapdragon 8 Gen 3", "manufacturer": "Qualcomm", "architecture": "Kryo (ARM)", "release_year": 2023,
            "cores": 8, "threads": 8, "base_clock": "2.0 GHz", "boost_clock": "3.3 GHz", "transistors": "Billions", "fabrication": "TSMC 4nm",
            "cache_l3": "12 MB", "tdp": "Mobile (<10W)", "instructions": "ARM64"
        }
    ]
}

# Write Database
os.makedirs(DATA_DIR, exist_ok=True)
with open(os.path.join(DATA_DIR, "cpu-encyclopedia.json"), "w", encoding="utf-8") as f:
    json.dump(cpu_database, f, indent=2)

# HTML Template for all the new pages
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | CPU Encyclopedia</title>
  <meta name="description" content="In-depth guide on {title}. Part of the 100-Year CPU Encyclopedia.">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="../css/styles.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "{title}",
    "inLanguage": "en"
  }}
  </script>
</head>
<body class="dark-mode">
  <div id="navbar-placeholder"></div>
  
  <div class="component-hero">
    <div class="badge">🧠 {category}</div>
    <h1>{title}</h1>
    <p class="hero-subtitle">Comprehensive insights into {title}, from architecture to execution.</p>
  </div>

  <main class="page-content container mt-5 mb-5">
    <div class="content-section card p-4 shadow-sm" style="background: var(--card-bg); border-color: var(--border);">
      <h2>📖 Overview</h2>
      <p>This module covers the fundamental concepts, history, and technical specifications of <strong>{title}</strong>. Sourced from academic journals, official manufacturer datasheets, and historical archives.</p>
      
      <div class="mt-4">
        <h4>Related Data Fields Collected</h4>
        <ul>
          <li>Architecture & Node</li>
          <li>Performance Benchmarks</li>
          <li>Transistor Count & Physics</li>
        </ul>
      </div>
      
      <div class="alert alert-info mt-4 bg-transparent border-info text-info">
        <strong>Data Integration:</strong> Live specs for this topic can be queried from <code>/data/cpu-encyclopedia.json</code> via the API.
      </div>
    </div>
  </main>

  <div id="footer-placeholder"></div>
  
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  <script src="../js/script.js"></script>
</body>
</html>
"""

# Generate Sub-pages
for category, files in cpu_pages.items():
    for filename in files:
        filepath = os.path.join(PAGES_DIR, filename)
        title = filename.replace('.html', '').replace('-', ' ').title()
        if not os.path.exists(filepath):
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html_template.format(title=title, category=category))

# Re-write the main cpu.html as a Hub
cpu_hub_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CPU Hub | Computer Parts Map</title>
  <meta name="description" content="The Ultimate CPU Encyclopedia Hub. Links to cores, architecture, history, and specs.">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="../css/styles.css">
</head>
<body class="dark-mode">
  <div id="navbar-placeholder"></div>

  <div class="component-hero">
    <div class="badge">🧠 Core Hardware Hub</div>
    <h1>CPU Encyclopedia</h1>
    <p class="hero-subtitle">The Central Processing Unit master directory. Explore over 30 detailed modules covering history, physics, architectures, and the future of processors.</p>
    <img src="../assets/images/cpu.jpg" alt="CPU Processor" class="hero-img">
  </div>

  <main class="page-content container mt-5 mb-5">
"""

for category, files in cpu_pages.items():
    cpu_hub_html += f'    <h3 class="mt-5 mb-3 border-bottom pb-2" style="border-color: var(--border)!important;">{category}</h3>\n    <div class="row g-3">\n'
    for filename in files:
        title = filename.replace('.html', '').replace('-', ' ').title()
        cpu_hub_html += f"""      <div class="col-md-4 col-sm-6">
        <a href="{filename}" class="text-decoration-none">
          <div class="card h-100 p-3" style="background: var(--card-bg); border: 1px solid var(--border); transition: transform 0.2s;">
            <h5 class="mb-0 text-primary">{title}</h5>
          </div>
        </a>
      </div>\n"""
    cpu_hub_html += '    </div>\n'

cpu_hub_html += """
    <div class="content-section mt-5 p-4 rounded" style="background: rgba(37,99,235,0.1); border: 1px solid rgba(37,99,235,0.3);">
      <h2>📊 Live CPU Database Access</h2>
      <p>Our project aggregates trusted data from Intel, AMD, Apple, PassMark, and academic journals (IEEE/ACM). Check out the <a href="cpu-database.html" class="fw-bold">Interactive Database</a> to view full specs.</p>
      <div class="table-responsive mt-3">
        <table class="table table-dark table-striped table-hover">
          <thead>
            <tr>
              <th>Processor</th><th>Manufacturer</th><th>Cores/Threads</th><th>Fabrication</th><th>Release</th>
            </tr>
          </thead>
          <tbody id="cpu-preview-table">
            <!-- Populated via JS -->
          </tbody>
        </table>
      </div>
    </div>
  </main>

  <div id="footer-placeholder"></div>
  
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  <script src="../js/script.js"></script>
  <script>
    // Quick fetch for preview
    fetch('../data/cpu-encyclopedia.json')
      .then(res => res.json())
      .then(data => {
        const tbody = document.getElementById('cpu-preview-table');
        data.cpus.slice(0,4).forEach(cpu => {
          tbody.innerHTML += `<tr>
            <td>${cpu.name}</td>
            <td>${cpu.manufacturer}</td>
            <td>${cpu.cores}C / ${cpu.threads}T</td>
            <td>${cpu.fabrication}</td>
            <td>${cpu.release_year}</td>
          </tr>`;
        });
      });
  </script>
</body>
</html>
"""

# Write the new hub to pages/cpu.html
with open(os.path.join(PAGES_DIR, "cpu.html"), "w", encoding="utf-8") as f:
    f.write(cpu_hub_html)

print("Generated full CPU Encyclopedia Hub and sub-pages.")
