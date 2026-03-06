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
    { name: "Android", url: "android.html", cat: "Software" },
    { name: "iOS", url: "ios.html", cat: "Software" },
    { name: "Software Types", url: "software-types.html", cat: "Software" },
    { name: "Computer Types", url: "computer-types.html", cat: "History" },
    { name: "History of Computing", url: "computer-history.html", cat: "History" },
    { name: "Server Guide", url: "server-guide.html", cat: "History" },
    { name: "Server Infrastructure", url: "server-infrastructure.html", cat: "History" },
    { name: "Raspberry Pi & SBCs", url: "raspberry-pi.html", cat: "Computing" },
    { name: "Quantum Computing", url: "quantum-computing.html", cat: "Computing" },
    { name: "About Us", url: "about.html", cat: "Misc" }
];

// --- Path Helper ---
// Detects if we are in the root or a subdirectory (like /pages/)
const getBasePath = () => {
    const path = window.location.pathname;
    if (path.includes('/pages/')) {
        return '../';
    }
    return '';
};

const base = getBasePath();

// --- Navbar & Footer Injection ---
const injectCommonElements = () => {
    // Inject lunr.js dynamically
    const lunrScript = document.createElement('script');
    lunrScript.src = 'https://cdnjs.cloudflare.com/ajax/libs/lunr.js/2.3.9/lunr.min.js';
    document.head.appendChild(lunrScript);

    const navbarHTML = `
    <nav class="navbar">
      <div class="nav-container">
        <a href="${base}index.html" class="nav-logo">⚡ Computer<span>Map</span></a>
        
        <ul class="nav-menu">
          <li><a href="${base}index.html">Home</a></li>
          
          <li class="has-dropdown mega-dropdown">
            <a href="${base}pages/explore.html">Hardware ▾</a>
            <div class="sub-nav mega-content">
              <div class="dropdown-column">
                <h4 class="dropdown-header">⚙️ Core Parts</h4>
                <a href="${base}pages/cpu.html">CPU (Processor Hub)</a>
                <a href="${base}pages/gpu.html">GPU (Graphics)</a>
                <a href="${base}pages/motherboard.html">Motherboard</a>
                <a href="${base}pages/ram.html">Memory (RAM)</a>
                <a href="${base}pages/storage.html">Storage (SSD/HDD)</a>
                <a href="${base}pages/psu.html">Power Supply</a>
                <a href="${base}pages/cooling.html">Cooling Systems</a>
              </div>
              <div class="dropdown-column">
                <h4 class="dropdown-header">🔌 Standards</h4>
                <a href="${base}pages/pcie.html">PCI Express</a>
                <a href="${base}pages/nvme.html">NVMe / SATA</a>
                <a href="${base}pages/usb.html">USB / Thunderbolt</a>
                <a href="${base}pages/ports.html">I/O Ports</a>
                <a href="${base}pages/chips.html">Chipsets</a>
              </div>
              <div class="dropdown-column">
                <h4 class="dropdown-header">⌨️ Peripherals</h4>
                <a href="${base}pages/monitor.html">Monitor</a>
                <a href="${base}pages/keyboard.html">Keyboard</a>
                <a href="${base}pages/mouse.html">Mouse</a>
                <a href="${base}pages/printer.html">Printer</a>
                <a href="${base}pages/webcam.html">Webcam</a>
                <a href="${base}pages/scanner.html">Scanner</a>
              </div>
            </div>
          </li>

          <li class="has-dropdown mega-dropdown">
            <a href="${base}pages/cpu.html">Processors ▾</a>
            <div class="sub-nav mega-content">
              <div class="dropdown-column">
                <h4 class="dropdown-header">🧠 CPU Core</h4>
                <a href="${base}pages/cpu-overview.html">Overview</a>
                <a href="${base}pages/cpu-core.html">Cores & Threads</a>
                <a href="${base}pages/cpu-cache.html">Cache Memory</a>
                <a href="${base}pages/cpu-clock-speed.html">Clock Speed</a>
                <a href="${base}pages/cpu-instruction-set.html">Instruction Sets</a>
              </div>
              <div class="dropdown-column">
                <h4 class="dropdown-header">🏭 Manufacturing</h4>
                <a href="${base}pages/cpu-fabrication.html">Fabrication</a>
                <a href="${base}pages/cpu-nanometer.html">Nanometer Nodes</a>
                <a href="${base}pages/cpu-transistor.html">Transistors</a>
                <a href="${base}pages/x86-architecture.html">x86 Architecture</a>
                <a href="${base}pages/arm-architecture.html">ARM Architecture</a>
              </div>
              <div class="dropdown-column">
                <h4 class="dropdown-header">📊 Data & History</h4>
                <a href="${base}pages/cpu-database.html">CPU Database</a>
                <a href="${base}pages/cpu-benchmark.html">Benchmarks</a>
                <a href="${base}pages/intel-cpu-history.html">Intel History</a>
                <a href="${base}pages/amd-cpu-history.html">AMD History</a>
                <a href="${base}pages/apple-silicon-history.html">Apple Silicon</a>
              </div>
            </div>
          </li>

          <li class="has-dropdown mega-dropdown">
            <a href="${base}pages/architecture.html">Architecture ▾</a>
            <div class="sub-nav mega-content">
              <div class="dropdown-column">
                <h4 class="dropdown-header">🏛️ Systems</h4>
                <a href="${base}pages/von-neumann.html">Von Neumann</a>
                <a href="${base}pages/harvard-architecture.html">Harvard Arch</a>
                <a href="${base}pages/bus-system.html">Bus Systems</a>
                <a href="${base}pages/pipeline.html">Pipelining</a>
              </div>
              <div class="dropdown-column">
                <h4 class="dropdown-header">🔬 Deep Logic</h4>
                <a href="${base}pages/binary.html">Binary & Logic</a>
                <a href="${base}pages/logic-gates.html">Logic Gates</a>
                <a href="${base}pages/transistor.html">Transistors</a>
                <a href="${base}pages/semiconductor.html">Semiconductors</a>
              </div>
              <div class="dropdown-column">
                <h4 class="dropdown-header">🚀 Future Tech</h4>
                <a href="${base}pages/quantum-computing.html">Quantum Computing</a>
                <a href="${base}pages/neuromorphic.html">Neuromorphic</a>
                <a href="${base}pages/optical-computing.html">Optical Computing</a>
                <a href="${base}pages/dna-computing.html">DNA Computing</a>
              </div>
            </div>
          </li>

          <li class="has-dropdown mega-dropdown">
            <a href="${base}pages/history.html">History ▾</a>
            <div class="sub-nav mega-content">
              <div class="dropdown-column">
                <h4 class="dropdown-header">📅 Timelines</h4>
                <a href="${base}pages/timeline.html">Interactive Timeline</a>
                <a href="${base}pages/computer-history.html">General History</a>
                <a href="${base}pages/computer-generations.html">Generations</a>
              </div>
              <div class="dropdown-column">
                <h4 class="dropdown-header">📜 Evolution</h4>
                <a href="${base}pages/history-cpu.html">CPU Evolution</a>
                <a href="${base}pages/history-gpu.html">GPU Evolution</a>
                <a href="${base}pages/history-ram.html">RAM Evolution</a>
                <a href="${base}pages/history-storage.html">Storage History</a>
              </div>
            </div>
          </li>

          <li class="has-dropdown mega-dropdown">
            <a href="${base}pages/learn.html">Learning ▾</a>
            <div class="sub-nav mega-content">
              <div class="dropdown-column">
                <h4 class="dropdown-header">📖 How It Works</h4>
                <a href="${base}pages/how-computer-works.html">Computer Basics</a>
                <a href="${base}pages/boot-process.html">Boot Process</a>
                <a href="${base}pages/instruction-cycle.html">Fetch-Execute</a>
                <a href="${base}pages/data-flow.html">Data Flow</a>
              </div>
              <div class="dropdown-column">
                <h4 class="dropdown-header">🛠️ Practical</h4>
                <a href="${base}pages/pc-build.html">Build a PC</a>
                <a href="${base}pages/hardware-map.html">Hardware Map</a>
                <a href="${base}pages/compare.html">Compare Parts</a>
              </div>
              <div class="dropdown-column">
                <h4 class="dropdown-header">📊 Visuals</h4>
                <a href="${base}pages/component-network.html">Network Map</a>
                <a href="${base}pages/system-map.html">System Map</a>
                <a href="${base}pages/visualize.html">Visualizer</a>
              </div>
            </div>
          </li>

          <li class="has-dropdown">
            <a href="#">More ▾</a>
            <ul class="sub-nav">
              <li class="dropdown-header">Software</li>
              <li><a href="${base}pages/operating-systems.html">Operating Systems</a></li>
              <li><a href="${base}pages/software-types.html">Software Types</a></li>
              <li class="dropdown-divider"></li>
              <li class="dropdown-header">Computing</li>
              <li><a href="${base}pages/server-guide.html">Server Guide</a></li>
              <li><a href="${base}pages/network.html">Networking</a></li>
              <li><a href="${base}pages/raspberry-pi.html">Raspberry Pi</a></li>
              <li class="dropdown-divider"></li>
              <li class="dropdown-header">Community</li>
              <li><a href="${base}pages/contribute.html">How to Contribute</a></li>
              <li><a href="${base}pages/about.html">About the Project</a></li>
            </ul>
          </li>

          <li><a href="${base}pages/audio.html">Audio</a></li>
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
          <a href="${base}index.html" class="footer-logo">⚡ Computer<span>Map</span></a>
          <p>The world's most detailed open library for computer hardware and software enthusiasts. Explore every component from transistors to cloud servers.</p>
          <div class="footer-social">
            <a href="https://github.com/Tcode-Motion" target="_blank" rel="noopener"><span>🐙</span> GitHub</a>
            <a href="https://tcode-motion.github.io/computer-part-map/" target="_blank" rel="noopener"><span>🌐</span> Site</a>
            <a href="mailto:contact@tcodemotion.com"><span>📧</span> Contact</a>
          </div>
        </div>
        
        <div class="footer-links-group">
          <div class="footer-links">
            <h4>Hardware</h4>
            <a href="${base}pages/cpu.html">Processors</a>
            <a href="${base}pages/gpu.html">Graphics Cards</a>
            <a href="${base}pages/motherboard.html">Motherboards</a>
            <a href="${base}pages/ram.html">Memory (RAM)</a>
            <a href="${base}pages/storage.html">Storage (SSD)</a>
          </div>
          
          <div class="footer-links">
            <h4>Software</h4>
            <a href="${base}pages/operating-systems.html">What is OS?</a>
            <a href="${base}pages/windows.html">Windows</a>
            <a href="${base}pages/linux.html">Linux</a>
            <a href="${base}pages/macos.html">macOS</a>
            <a href="${base}pages/android.html">Android/iOS</a>
          </div>
          
          <div class="footer-links">
            <h4>Resources</h4>
            <a href="${base}pages/history.html">History</a>
            <a href="${base}pages/server-guide.html">Servers</a>
            <a href="${base}pages/quantum-computing.html">Quantum</a>
            <a href="${base}pages/about.html">About Us</a>
            <a href="${base}pages/contribute.html">Contribute</a>
          </div>
        </div>
      </div>
      
      <div class="footer-bottom">
        <div class="footer-bottom-content">
          <p>&copy; 2026 Computer Parts Map. All rights reserved.</p>
          <p>Made with ❤️ by <strong>Tcode Motion</strong>.</p>
        </div>
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
