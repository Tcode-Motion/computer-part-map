/**
 * Computer Parts Map - Core Logic 2.0
 * Handles: Navbar/Footer injection, Dark Mode, Search, Smooth Scrolling, and Animations.
 */

// --- Constants & Config ---
const SITE_PAGES = [
    { name: "CPU (Processor)", url: "cpu.html", cat: "Core" },
    { name: "CPU Architecture", url: "cpu-architecture.html", cat: "Core" },
    { name: "CPU History", url: "cpu-history.html", cat: "History" },
    { name: "CPU Benchmarks", url: "cpu-benchmarks.html", cat: "Core" },
    { name: "GPU (Graphics Card)", url: "gpu.html", cat: "Core" },
    { name: "GPU Architecture", url: "gpu-architecture.html", cat: "Core" },
    { name: "GPU Rendering Pipeline", url: "gpu-rendering-pipeline.html", cat: "Core" },
    { name: "NPU (AI Processor)", url: "npu.html", cat: "Core" },
    { name: "RAM (Memory)", url: "ram.html", cat: "Core" },
    { name: "RAM Types", url: "ram-types.html", cat: "Core" },
    { name: "RAM Architecture", url: "ram-architecture.html", cat: "Core" },
    { name: "Motherboard", url: "motherboard.html", cat: "Core" },
    { name: "Motherboard Components", url: "motherboard-components.html", cat: "Core" },
    { name: "Motherboard Chipset", url: "motherboard-chipset.html", cat: "Core" },
    { name: "SSD (Solid State)", url: "ssd.html", cat: "Core" },
    { name: "SSD Architecture", url: "ssd-architecture.html", cat: "Core" },
    { name: "HDD (Hard Drive)", url: "hdd.html", cat: "Core" },
    { name: "PSU (Power Supply)", url: "psu.html", cat: "Core" },
    { name: "Cooling / Fans", url: "cooling.html", cat: "Core" },
    { name: "Monitor", url: "monitor.html", cat: "Output" },
    { name: "Printer", url: "printer.html", cat: "Output" },
    { name: "Projector", url: "projector.html", cat: "Output" },
    { name: "Speakers", url: "speakers.html", cat: "Audio" },
    { name: "Sound Card", url: "sound-card.html", cat: "Audio" },
    { name: "Keyboard", url: "keyboard.html", cat: "Input" },
    { name: "Mouse", url: "mouse.html", cat: "Input" },
    { name: "Webcam", url: "webcam.html", cat: "Input" },
    { name: "Touchpad", url: "touchpad.html", cat: "Input" },
    { name: "Scanner", url: "scanner.html", cat: "Input" },
    { name: "WiFi Adapter", url: "wifi-adapter.html", cat: "Network" },
    { name: "Router", url: "router.html", cat: "Network" },
    { name: "NIC (Lan Card)", url: "nic.html", cat: "Network" },
    { name: "UPS", url: "ups.html", cat: "Power" },
    { name: "Optical Drive", url: "optical-drive.html", cat: "Storage" },
    { name: "Optical Laser Tech", url: "optical-laser.html", cat: "Storage" },
    { name: "Operating Systems", url: "operating-systems.html", cat: "Software" },
    { name: "OS Kernel Architecture", url: "os-kernel-architecture.html", cat: "Software" },
    { name: "Windows", url: "windows.html", cat: "Software" },
    { name: "Windows NT Arch", url: "windows-nt-architecture.html", cat: "Software" },
    { name: "Linux", url: "linux.html", cat: "Software" },
    { name: "Linux Kernel Deep Dive", url: "linux-kernel.html", cat: "Software" },
    { name: "macOS", url: "macos.html", cat: "Software" },
    { name: "Software Types", url: "software-types.html", cat: "Software" },
    { name: "Computer Types", url: "computer-types.html", cat: "History" },
    { name: "History of Computing", url: "computer-history.html", cat: "History" },
    { name: "Server Guide", url: "server-guide.html", cat: "History" },
    { name: "Server Infrastructure", url: "server-infrastructure.html", cat: "History" },
    { name: "Raspberry Pi & SBCs", url: "raspberry-pi.html", cat: "Computing" },
    { name: "Quantum Computing", url: "quantum-computing.html", cat: "Computing" },
    { name: "About Us", url: "about.html", cat: "Misc" }
];

// --- Navbar & Footer Injection ---
const injectCommonElements = () => {
    // Inject lunr.js dynamically
    const lunrScript = document.createElement('script');
    lunrScript.src = 'https://cdnjs.cloudflare.com/ajax/libs/lunr.js/2.3.9/lunr.min.js';
    document.head.appendChild(lunrScript);

    const navbarHTML = `
    <nav class="navbar">
      <div class="nav-container">
        <a href="index.html" class="nav-logo">⚡ Computer<span>Map</span></a>
        
        <ul class="nav-menu">
          <li><a href="index.html">Home</a></li>
          
          <li class="has-dropdown mega-dropdown">
            <a href="#">Hardware ▾</a>
            <div class="sub-nav mega-content">
              <div class="dropdown-column">
                <h4 class="dropdown-header">⚙️ Core Hardware</h4>
                <a href="cpu.html">CPU (Processor)</a>
                <a href="gpu.html">GPU (Graphics)</a>
                <a href="npu.html">NPU (AI Processor)</a>
                <a href="motherboard.html">Motherboard</a>
                <a href="ram.html">RAM (Memory)</a>
                <a href="psu.html">Power Supply</a>
                <a href="cooling.html">Cooling Systems</a>
              </div>
              <div class="dropdown-column">
                <h4 class="dropdown-header">⌨️ Input Devices</h4>
                <a href="keyboard.html">Keyboard</a>
                <a href="mouse.html">Mouse</a>
                <a href="webcam.html">Webcam</a>
                <a href="microphone.html">Microphone</a>
                <a href="scanner.html">Scanner</a>
                <a href="touchpad.html">Touchpad</a>
              </div>
              <div class="dropdown-column">
                <h4 class="dropdown-header">🖥️ Output & Storage</h4>
                <a href="monitor.html">Monitor</a>
                <a href="printer.html">Printer</a>
                <a href="projector.html">Projector</a>
                <a href="ssd.html">SSD Storage</a>
                <a href="hdd.html">HDD Storage</a>
                <a href="optical-drive.html">Optical Drive</a>
              </div>
            </div>
          </li>

          <li class="has-dropdown">
            <a href="#">Software ▾</a>
            <ul class="sub-nav">
              <li class="dropdown-header">Operating Systems</li>
              <li><a href="operating-systems.html">What is OS?</a></li>
              <li><a href="windows.html">Windows</a></li>
              <li><a href="linux.html">Linux</a></li>
              <li><a href="macos.html">macOS</a></li>
              <li class="dropdown-divider"></li>
              <li class="dropdown-header">Categories</li>
              <li><a href="software-types.html">Software Types</a></li>
            </ul>
          </li>

          <li class="has-dropdown">
            <a href="#">Computing ▾</a>
            <ul class="sub-nav">
              <li class="dropdown-header">Modern & Future</li>
              <li><a href="raspberry-pi.html">Raspberry Pi & SBCs</a></li>
              <li><a href="npu.html">Neural Processing Units</a></li>
              <li><a href="quantum-computing.html">Quantum Computing</a></li>
              <li class="dropdown-divider"></li>
              <li><a href="computer-history.html">History of Computing</a></li>
              <li><a href="computer-types.html">Types of Computers</a></li>
              <li><a href="server-guide.html">Server Guide</a></li>
              <li><a href="ups.html">UPS Systems</a></li>
              <li><a href="battery.html">Battery Guide</a></li>
              <li><a href="nic.html">Networking (NIC)</a></li>
              <li><a href="router.html">Routers</a></li>
              <li><a href="wifi-adapter.html">WiFi Adapters</a></li>
            </ul>
          </li>

          <li class="has-dropdown">
            <a href="#">Audio ▾</a>
            <ul class="sub-nav">
              <li><a href="speakers.html">Speakers</a></li>
              <li><a href="sound-card.html">Sound Cards</a></li>
            </ul>
          </li>

          <li><a href="about.html">About</a></li>
        </ul>

        <div class="nav-actions">
          <div class="search-box">
            <input type="text" id="nav-search-input" placeholder="Search...">
            <div id="nav-search-results" class="search-dropdown"></div>
          </div>
          <button id="theme-toggle" title="Toggle Mode">🌓</button>
        </div>
      </div>
    </nav>`;

    const footerHTML = `
    <footer class="main-footer">
      <div class="footer-container">
        <div class="footer-brand">
          <h3>⚡ Computer<span>Map</span></h3>
          <p>The world's most detailed open library for computer hardware and software enthusiasts.</p>
          <div class="footer-social">
            <a href="https://tcode-motion.github.io/computer-part-map/" title="Website">🌐</a>
            <a href="mailto:contact@tcodemotion.com" title="Email">📧</a>
            <a href="https://github.com/Tcode-Motion/computer-part-map/" target="_blank" title="GitHub">🐙</a>
          </div>
        </div>
        <div class="footer-links">
          <h4>Explore</h4>
          <a href="cpu.html">Processors</a>
          <a href="gpu.html">Graphics Cards</a>
          <a href="operating-systems.html">Operating Systems</a>
          <a href="computer-history.html">History</a>
        </div>
        <div class="footer-links">
          <h4>Resources</h4>
          <a href="about.html">About Us</a>
          <a href="https://github.com/Tcode-Motion/computer-part-map/blob/main/README.md">Documentation</a>
          <a href="index.html">Home</a>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 Computer Parts Map. Made by <strong>Tcode Motion</strong>.</p>
      </div>
    </footer>`;

    const navElement = document.getElementById('navbar-placeholder');
    const footerElement = document.getElementById('footer-placeholder');
    
    if (navElement) navElement.innerHTML = navbarHTML;
    if (footerElement) footerElement.innerHTML = footerHTML;
};

// --- Search Logic ---
let searchIndex = null;
let searchDocs = [];

const initSearch = async (inputId, resultsId) => {
    const input = document.getElementById(inputId);
    const results = document.getElementById(resultsId);
    if (!input || !results) return;

    // Load search index if not loaded
    if (!searchIndex) {
        try {
            const res = await fetch('search_index.json');
            searchDocs = await res.json();
            
            // Wait for lunr to be available if injected dynamically
            let retries = 0;
            while(typeof lunr === 'undefined' && retries < 20) {
                await new Promise(r => setTimeout(r, 100));
                retries++;
            }
            
            if (typeof lunr !== 'undefined') {
                searchIndex = lunr(function () {
                    this.ref('id');
                    this.field('title', { boost: 10 });
                    this.field('body');
                    
                    searchDocs.forEach(function (doc) {
                        this.add(doc);
                    }, this);
                });
            }
        } catch (e) {
            console.error("Failed to load search index", e);
        }
    }

    input.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase();
        results.innerHTML = "";
        
        if (query.length < 2) {
            results.classList.remove('active');
            return;
        }

        let matches = [];
        if (searchIndex) {
            try {
                // Fuzzy search
                const lunrResults = searchIndex.search(query + "~1");
                matches = lunrResults.slice(0, 8).map(r => {
                    const doc = searchDocs.find(d => d.id === r.ref);
                    return { name: doc.title, url: doc.url, cat: 'Article' };
                });
            } catch (e) {
                // fallback to old
            }
        } 
        
        if(matches.length === 0) {
            // fallback
            matches = SITE_PAGES.filter(p => p.name.toLowerCase().includes(query) || p.cat.toLowerCase().includes(query)).slice(0, 8);
        }
        
        if (matches.length > 0) {
            matches.forEach(m => {
                const div = document.createElement('div');
                div.className = 'search-item';
                div.innerHTML = `<span>${m.name}</span><span class="cat-tag">${m.cat || 'Page'}</span>`;
                div.onclick = () => window.location.href = m.url;
                results.appendChild(div);
            });
            results.classList.add('active');
        } else {
            results.classList.remove('active');
        }
    });

    document.addEventListener('click', (e) => {
        if (!e.target.closest('.search-box') && !e.target.closest('.hero-search')) {
            results.classList.remove('active');
        }
    });
};

// --- Theme Toggle ---
const initTheme = () => {
    const toggle = document.getElementById('theme-toggle');
    const currentTheme = localStorage.getItem('theme') || 'dark';
    document.body.className = currentTheme === 'dark' ? 'dark-mode' : 'light-mode';

    if (toggle) {
        toggle.addEventListener('click', () => {
            const isDark = document.body.classList.contains('dark-mode');
            const newTheme = isDark ? 'light-mode' : 'dark-mode';
            document.body.className = newTheme;
            localStorage.setItem('theme', isDark ? 'light' : 'dark');
        });
    }
};

// --- Hero Stats Animation ---
const animateStats = () => {
    const stats = document.querySelectorAll('.stat-num');
    stats.forEach(stat => {
        const target = +stat.getAttribute('data-val');
        if (typeof anime !== 'undefined') {
            anime({
                targets: stat,
                innerHTML: [0, target],
                round: 1,
                easing: 'easeOutExpo',
                duration: 2000,
                delay: 500
            });
        }
    });
};

// --- Category Sections Generator ---
const populateCategorySections = () => {
    const anchor = document.getElementById('category-sections-anchor');
    if (!anchor) return;

    const categories = [
        { id: 'core', title: '⚙️ Core Components', filter: 'Core' },
        { id: 'software', title: '💻 Software & OS', filter: 'Software' },
        { id: 'input', title: '⌨️ Input Devices', filter: 'Input' },
        { id: 'output', title: '🖥️ Output Devices', filter: 'Output' }
    ];

    let html = '';
    categories.forEach(cat => {
        const pages = SITE_PAGES.filter(p => p.cat === cat.filter);
        html += `
        <section id="${cat.id}" class="category-detail-section">
            <h2 class="section-title">${cat.title}</h2>
            <div class="pages-grid">
                ${pages.map(p => `
                    <a href="${p.url}" class="page-mini-card">
                        <div class="page-card-icon">${cat.title.split(' ')[0]}</div>
                        <div class="page-card-info">
                            <h4>${p.name}</h4>
                            <p>Technical specifications & guides</p>
                        </div>
                    </a>
                `).join('')}
            </div>
        </section>`;
    });

    anchor.innerHTML = html;
};

// --- Initialization ---
document.addEventListener('DOMContentLoaded', () => {
    injectCommonElements();
    initTheme();
    initSearch('nav-search-input', 'nav-search-results');
    initSearch('hero-search-input', 'hero-search-results');
    populateCategorySections();
    
    // Hide loader
    const loader = document.getElementById('loader');
    if (loader) {
        setTimeout(() => {
            loader.style.opacity = '0';
            setTimeout(() => loader.style.display = 'none', 500);
        }, 800);
    }

    if (document.querySelector('.stat-num')) {
        animateStats();
    }
});
