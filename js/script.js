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

// --- Path Helper (supports nested page directories) ---
const getBasePath = () => {
    const path = window.location.pathname;
    if (!path.includes('/pages/')) return '';
    // Count how many dirs deep we are below the site root
    // /pages/file.html → '../'
    // /pages/cpu/index.html → '../../'
    // /pages/cpu/core/overview.html → '../../../'
    const afterPages = path.split('/pages/')[1] || '';
    const depth = (afterPages.match(/\//g) || []).length;
    return '../'.repeat(depth + 1);
};

const base = getBasePath();
// Helper to link to pages directory correctly (from ANY depth)
const pageLink = (file) => {
    const path = window.location.pathname;
    if (!path.includes('/pages/')) return `pages/${file}`;
    // Calculate relative path from current page to /pages/ directory
    const afterPages = path.split('/pages/')[1] || '';
    const depth = (afterPages.match(/\//g) || []).length;
    return (depth > 0 ? '../'.repeat(depth) : '') + file;
};

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
            <a href="${pageLink('explore.html')}">Hardware ▾</a>
            <div class="sub-nav mega-content" style="grid-template-columns: repeat(4, 1fr);">
              <div class="dropdown-column">
                <h4 class="dropdown-header">⚙️ Core Parts</h4>
                <a href="${pageLink('cpu/index.html')}">CPU (Processors)</a>
                <a href="${pageLink('gpu/index.html')}">GPU (Graphics)</a>
                <a href="${pageLink('motherboard/index.html')}">Motherboard</a>
                <a href="${pageLink('ram/index.html')}">Memory (RAM)</a>
                <a href="${pageLink('storage/index.html')}">Storage (SSD/HDD)</a>
                <a href="${pageLink('hardware/psu.html')}">Power Supply</a>
                <a href="${pageLink('hardware/cooling.html')}">Cooling</a>
              </div>
              <div class="dropdown-column">
                <h4 class="dropdown-header">🔌 Connectivity</h4>
                <a href="${pageLink('motherboard/pcie.html')}">PCI Express</a>
                <a href="${pageLink('storage/nvme.html')}">NVMe / SATA</a>
                <a href="${pageLink('storage/usb.html')}">USB / Thunderbolt</a>
                <a href="${pageLink('networking/ethernet.html')}">Network Adapters</a>
                <a href="${pageLink('hardware/interfaces.html')}">Interface Types</a>
              </div>
              <div class="dropdown-column">
                <h4 class="dropdown-header">⌨️ Peripherals</h4>
                <a href="${pageLink('peripherals/input.html')}">Input Devices</a>
                <a href="${pageLink('peripherals/output.html')}">Output Devices</a>
                <a href="${pageLink('peripherals/monitor.html')}">Displays</a>
                <a href="${pageLink('peripherals/keyboard.html')}">Keyboard & Mouse</a>
                <a href="${pageLink('peripherals/audio.html')}">Audio / Speakers</a>
              </div>
              <div class="dropdown-column">
                <h4 class="dropdown-header">🛠️ Building</h4>
                <a href="${pageLink('hardware/pc-build.html')}">PC Building Guide</a>
                <a href="${pageLink('hardware/case.html')}">Cases & Airflow</a>
                <a href="${pageLink('hardware/battery.html')}">Batteries</a>
                <a href="${pageLink('hardware/ups.html')}">UPS (Power Backup)</a>
              </div>
            </div>
          </li>

          <li class="has-dropdown mega-dropdown">
            <a href="${pageLink('cpu/index.html')}">Processors ▾</a>
            <div class="sub-nav mega-content" style="grid-template-columns: repeat(5, 1fr);">
              <div class="dropdown-column">
                <h4 class="dropdown-header">🧠 Core Basics</h4>
                <a href="${pageLink('cpu/core/overview.html')}">CPU Overview</a>
                <a href="${pageLink('cpu/core/how-it-works.html')}">How a CPU Works</a>
                <a href="${pageLink('cpu/core/architecture.html')}">Architecture Basics</a>
                <a href="${pageLink('cpu/core/history.html')}">General History</a>
                <h4 class="dropdown-header" style="margin-top:12px;">⚡ Performance</h4>
                <a href="${pageLink('cpu/core/comparison.html')}">CPU Comparison</a>
                <a href="${pageLink('cpu/core/benchmarks.html')}">Benchmarks</a>
                <a href="${pageLink('cpu/internals/overclocking.html')}">Overclocking</a>
                <a href="${pageLink('cpu/core/database.html')}">CPU Database</a>
              </div>
              <div class="dropdown-column">
                <h4 class="dropdown-header">⚙️ CPU Internals</h4>
                <a href="${pageLink('cpu/internals/cores-threads.html')}">Cores & Threads</a>
                <a href="${pageLink('cpu/internals/clock-speed.html')}">Clock Speed & IPC</a>
                <a href="${pageLink('cpu/internals/cache.html')}">Cache (L1/L2/L3)</a>
                <a href="${pageLink('cpu/internals/power-consumption.html')}">Power (TDP)</a>
                <a href="${pageLink('cpu/internals/efficiency.html')}">Efficiency</a>
                <a href="${pageLink('cpu/internals/cooling.html')}">Cooling & Thermals</a>
              </div>
              <div class="dropdown-column">
                <h4 class="dropdown-header">🔬 Deep Architecture</h4>
                <a href="${pageLink('cpu/internals/instruction-sets.html')}">Instruction Sets (ISA)</a>
                <a href="${pageLink('cpu/internals/pipeline.html')}">Execution Pipeline</a>
                <a href="${pageLink('cpu/internals/branch-prediction.html')}">Branch Prediction</a>
                <a href="${pageLink('cpu/internals/registers.html')}">Registers</a>
                <a href="${pageLink('cpu/internals/system-bus.html')}">System Bus</a>
              </div>
              <div class="dropdown-column">
                <h4 class="dropdown-header">🏭 Manufacturing</h4>
                <a href="${pageLink('cpu/manufacturing/silicon.html')}">Silicon & Wafers</a>
                <a href="${pageLink('cpu/manufacturing/fabrication.html')}">Fabrication Process</a>
                <a href="${pageLink('cpu/manufacturing/chip-design.html')}">Chip Design</a>
                <a href="${pageLink('cpu/manufacturing/transistors.html')}">Transistors</a>
                <a href="${pageLink('cpu/manufacturing/process-nodes.html')}">Process Nodes (nm)</a>
              </div>
              <div class="dropdown-column">
                <h4 class="dropdown-header">🏛️ Architectures</h4>
                <a href="${pageLink('cpu/families/x86.html')}">x86 Architecture</a>
                <a href="${pageLink('cpu/families/arm.html')}">ARM Architecture</a>
                <a href="${pageLink('cpu/families/apple-silicon.html')}">Apple Silicon</a>
                <a href="${pageLink('cpu/families/risc-v.html')}">RISC-V</a>
                <a href="${pageLink('cpu/families/powerpc.html')}">PowerPC</a>
                <h4 class="dropdown-header" style="margin-top:12px;">🔮 Future Tech</h4>
                <a href="${pageLink('cpu/future-tech/quantum.html')}">Quantum CPUs</a>
                <a href="${pageLink('cpu/future-tech/ai-npu.html')}">AI & NPUs</a>
                <a href="${pageLink('cpu/future-tech/neuromorphic.html')}">Neuromorphic</a>
                <a href="${pageLink('cpu/future-tech/optical.html')}">Optical CPUs</a>
                <a href="${pageLink('cpu/future-tech/3d-stacking.html')}">3D Stacking</a>
              </div>
            </div>
          </li>

          <li class="has-dropdown mega-dropdown">
            <a href="${pageLink('architecture.html')}">Architecture ▾</a>
            <div class="sub-nav mega-content">
              <div class="dropdown-column">
                <h4 class="dropdown-header">🏛️ Architectures</h4>
                <a href="${pageLink('concepts/von-neumann.html')}">Von Neumann</a>
                <a href="${pageLink('concepts/harvard-architecture.html')}">Harvard Arch</a>
                <a href="${pageLink('motherboard/bus-system.html')}">Bus Systems</a>
                <a href="${pageLink('concepts/instruction-cycle.html')}">Fetch-Execute</a>
                <a href="${pageLink('concepts/parallel-computing.html')}">Parallel Computing</a>
              </div>
              <div class="dropdown-column">
                <h4 class="dropdown-header">🔬 Deep Logic</h4>
                <a href="${pageLink('concepts/binary.html')}">Binary & Logic</a>
                <a href="${pageLink('concepts/logic-gates.html')}">Logic Gates</a>
                <a href="${pageLink('concepts/turing-logic.html')}">Turing Machines</a>
                <a href="${pageLink('concepts/transistor.html')}">Transistors</a>
                <a href="${pageLink('concepts/semiconductor.html')}">Semiconductors</a>
              </div>
              <div class="dropdown-column">
                <h4 class="dropdown-header">🚀 Future Systems</h4>
                <a href="${pageLink('systems/quantum-computing.html')}">Quantum Computing</a>
                <a href="${pageLink('systems/neuromorphic.html')}">Neuromorphic</a>
                <a href="${pageLink('systems/optical-computing.html')}">Optical Computing</a>
                <a href="${pageLink('systems/dna-computing.html')}">DNA Computing</a>
              </div>
            </div>
          </li>

          <li class="has-dropdown mega-dropdown">
            <a href="${pageLink('history.html')}">History ▾</a>
            <div class="sub-nav mega-content">
              <div class="dropdown-column">
                <h4 class="dropdown-header">📅 Timelines</h4>
                <a href="${pageLink('timeline.html')}">Interactive Timeline</a>
                <a href="${pageLink('concepts/history.html')}">General History</a>
                <a href="${pageLink('systems/computer-generations.html')}">Generations</a>
              </div>
              <div class="dropdown-column">
                <h4 class="dropdown-header">📜 Evolution</h4>
                <a href="${pageLink('cpu/core/history.html')}">CPU Evolution</a>
                <a href="${pageLink('gpu/history.html')}">GPU Evolution</a>
                <a href="${pageLink('ram/history.html')}">RAM Evolution</a>
                <a href="${pageLink('storage/history.html')}">Storage History</a>
              </div>
            </div>
          </li>

          <li class="has-dropdown mega-dropdown">
            <a href="${pageLink('learn.html')}">Learning ▾</a>
            <div class="sub-nav mega-content">
              <div class="dropdown-column">
                <h4 class="dropdown-header">📖 How It Works</h4>
                <a href="${pageLink('how-computer-works.html')}">Computer Basics</a>
                <a href="${pageLink('boot-process.html')}">Boot Process</a>
                <a href="${pageLink('data-flow.html')}">Data Flow</a>
                <a href="${pageLink('systems/computer-types.html')}">Computer Types</a>
              </div>
              <div class="dropdown-column">
                <h4 class="dropdown-header">🛠️ Practical</h4>
                <a href="${pageLink('hardware/pc-build.html')}">Build a PC</a>
                <a href="${pageLink('hardware-map.html')}">Hardware Map</a>
                <a href="${pageLink('compare.html')}">Compare Parts</a>
                <a href="${pageLink('systems/supercomputing.html')}">Supercomputing</a>
              </div>
              <div class="dropdown-column">
                <h4 class="dropdown-header">📊 Visuals</h4>
                <a href="${pageLink('component-network.html')}">Network Map</a>
                <a href="${pageLink('system-map.html')}">System Map</a>
                <a href="${pageLink('visualize.html')}">Visualizer</a>
              </div>
            </div>
          </li>

          <li class="has-dropdown">
            <a href="#">More ▾</a>
            <ul class="sub-nav">
              <li class="dropdown-header">Software</li>
              <li><a href="${pageLink('os/index.html')}">Operating Systems</a></li>
              <li><a href="${pageLink('software-types.html')}">Software Types</a></li>
              <li class="dropdown-divider"></li>
              <li class="dropdown-header">Computing Systems</li>
              <li><a href="${pageLink('systems/server-guide.html')}">Server Guide</a></li>
              <li><a href="${pageLink('networking/index.html')}">Networking</a></li>
              <li><a href="${pageLink('systems/raspberry-pi.html')}">Raspberry Pi</a></li>
              <li class="dropdown-divider"></li>
              <li class="dropdown-header">Community</li>
              <li><a href="${pageLink('contribute.html')}">How to Contribute</a></li>
              <li><a href="${pageLink('about.html')}">About the Project</a></li>
            </ul>
          </li>

          <li><a href="${pageLink('peripherals/audio.html')}">Audio</a></li>
        </ul>

        <div class="nav-actions">
          <div class="search-box">
            <input type="text" id="nav-search-input" placeholder="Search...">
            <div id="nav-search-results" class="search-dropdown"></div>
          </div>
          <button id="theme-toggle" title="Toggle Mode">🌓</button>
          <button id="nav-hamburger" class="nav-hamburger" aria-label="Toggle Menu">
            <span></span><span></span><span></span>
          </button>
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
            <a href="${pageLink('cpu.html')}">Processors</a>
            <a href="${pageLink('gpu.html')}">Graphics Cards</a>
            <a href="${pageLink('motherboard.html')}">Motherboards</a>
            <a href="${pageLink('ram.html')}">Memory (RAM)</a>
            <a href="${pageLink('storage.html')}">Storage (SSD)</a>
          </div>
          
          <div class="footer-links">
            <h4>Software</h4>
            <a href="${pageLink('operating-systems.html')}">What is OS?</a>
            <a href="${pageLink('windows.html')}">Windows</a>
            <a href="${pageLink('linux.html')}">Linux</a>
            <a href="${pageLink('macos.html')}">macOS</a>
            <a href="${pageLink('android.html')}">Android/iOS</a>
          </div>
          
          <div class="footer-links">
            <h4>Resources</h4>
            <a href="${pageLink('history.html')}">History</a>
            <a href="${pageLink('server-guide.html')}">Servers</a>
            <a href="${pageLink('quantum-computing.html')}">Quantum</a>
            <a href="${pageLink('about.html')}">About Us</a>
            <a href="${pageLink('contribute.html')}">Contribute</a>
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
    
    if (navElement) {
        navElement.innerHTML = navbarHTML;
        highlightCurrentPage();
    }
    if (footerElement) footerElement.innerHTML = footerHTML;
};

// --- Active Page Highlighting ---
const highlightCurrentPage = () => {
    const currentPath = window.location.pathname;
    
    // Find all links in the navbar
    const navLinks = document.querySelectorAll('.nav-menu a');
    
    navLinks.forEach(link => {
        // Strip out the origin to just get the matching path part
        const linkPath = new URL(link.href).pathname;
        
        // Match exact path, or if we are at root index.html
        if (currentPath === linkPath || (currentPath.endsWith('/') && linkPath.endsWith('index.html'))) {
            // Highlight the exact link
            link.classList.add('active');
            
            // If it's inside a dropdown, highlight the parent dropdown toggle as well
            const megaDropdown = link.closest('.has-dropdown');
            if (megaDropdown) {
                const parentToggle = megaDropdown.querySelector('a');
                if (parentToggle) parentToggle.classList.add('active');
                
                // Also highlight the specific column header it belongs to
                const parentColumn = link.closest('.dropdown-column');
                if (parentColumn) {
                    const columnHeader = parentColumn.querySelector('.dropdown-header');
                    if (columnHeader) columnHeader.classList.add('active');
                }
            }
        }
    });
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

// --- Mobile Nav Toggle ---
const initMobileNav = () => {
    const hamburger = document.getElementById('nav-hamburger');
    const navMenu = document.querySelector('.nav-menu');
    if (!hamburger || !navMenu) return;

    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navMenu.classList.toggle('active');
        document.body.classList.toggle('nav-open');
    });

    // On mobile, toggle dropdowns on click instead of hover
    const dropdownParents = navMenu.querySelectorAll('.has-dropdown > a');
    dropdownParents.forEach(link => {
        link.addEventListener('click', (e) => {
            if (window.innerWidth <= 992) {
                e.preventDefault();
                const parent = link.parentElement;
                // Close other open dropdowns
                navMenu.querySelectorAll('.has-dropdown.open').forEach(el => {
                    if (el !== parent) el.classList.remove('open');
                });
                parent.classList.toggle('open');
            }
        });
    });

    // Close menu when a sub-link is clicked
    navMenu.querySelectorAll('.sub-nav a').forEach(link => {
        link.addEventListener('click', () => {
            if (window.innerWidth <= 992) {
                hamburger.classList.remove('active');
                navMenu.classList.remove('active');
                document.body.classList.remove('nav-open');
                navMenu.querySelectorAll('.has-dropdown.open').forEach(el => el.classList.remove('open'));
            }
        });
    });

    // Close menu on clicking a non-dropdown nav link
    navMenu.querySelectorAll(':scope > li > a').forEach(link => {
        link.addEventListener('click', () => {
            const parent = link.parentElement;
            if (!parent.classList.contains('has-dropdown') && window.innerWidth <= 992) {
                hamburger.classList.remove('active');
                navMenu.classList.remove('active');
                document.body.classList.remove('nav-open');
            }
        });
    });
};

// --- Global Animations (Scroll Reveal) ---
const initGlobalAnimations = () => {
    // 1. Auto-tag elements for animation if they aren't already classed
    const sections = document.querySelectorAll('.content-section');
    sections.forEach((sec, index) => {
        if(!sec.classList.contains('reveal') && !sec.classList.contains('reveal-left') && !sec.classList.contains('reveal-scale')) {
            // Alternate animation styles subtly based on index
            if (index % 3 === 0) sec.classList.add('reveal-left');
            else if (index % 5 === 0) sec.classList.add('reveal-scale');
            else sec.classList.add('reveal');
        }
    });

    const revealElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-scale');
    
    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                // Optional: Stop observing once revealed
                // observer.unobserve(entry.target); 
            }
        });
    }, {
        root: null,
        threshold: 0.15, // Trigger when 15% visible
        rootMargin: "0px 0px -50px 0px" // Trigger slightly before it hits bottom
    });
    
    revealElements.forEach(el => revealObserver.observe(el));
};

// --- Gamification (Reading Progress & Fun Facts) ---
const initGamification = () => {
    // 1. Inject Reading Progress Bar HTML into DOM
    if (!document.getElementById('reading-progress-container')) {
        const progressHTML = `
            <div id="reading-progress-container">
                <div id="reading-progress-bar"></div>
            </div>
        `;
        document.body.insertAdjacentHTML('afterbegin', progressHTML);
    }

    const progressBar = document.getElementById('reading-progress-bar');
    
    // 2. Inject Fun Fact Toast HTML
    if (!document.getElementById('fun-fact-toast')) {
        const toastHTML = `
            <div id="fun-fact-toast">
                <div class="toast-header">
                    <span>💡 Did You Know?</span>
                    <button class="toast-close" onclick="document.getElementById('fun-fact-toast').classList.remove('show')">×</button>
                </div>
                <div class="toast-body" id="toast-body-text">Loading fact...</div>
            </div>
        `;
        document.body.insertAdjacentHTML('beforeend', toastHTML);
    }

    const funFacts = [
        "The first 1GB hard drive was as big as a refrigerator and weighed 550 lbs!",
        "The Apollo 11 guidance computer sent man to the moon using less computing power than a modern USB-C charger.",
        "A single Google search requires more computing power than it took to send Apollo 11 to the moon.",
        "Over 90% of the world's currency only exists on computers.",
        "The first computer mouse was made of wood in 1964 by Doug Engelbart.",
        "There are over 700 programming languages in the world.",
        "The first webcam was created simply to check the status of a coffee pot at Cambridge University.",
        "Every day, 2.5 quintillion bytes of data are created.",
        "Your smartphone has millions of times more memory than the Apollo 11 computers.",
        "The word 'robot' comes from the Czech word 'robota', meaning forced labor."
    ];

    // Scroll Logic for Progress Bar and Toast Triggers
    let factShown = false;
    
    window.addEventListener('scroll', () => {
        // Progress Bar Calculation
        const scrollTop = window.scrollY || document.documentElement.scrollTop;
        const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrollRatio = (scrollTop / scrollHeight) * 100;
        
        if (progressBar) {
            progressBar.style.width = scrollRatio + '%';
        }

        // Show Fun Fact Toast around 50% scroll depth (once per page load)
        if (scrollRatio > 45 && scrollRatio < 55 && !factShown) {
            const toast = document.getElementById('fun-fact-toast');
            const toastText = document.getElementById('toast-body-text');
            
            if (toast && toastText) {
                // Pick a random fact
                const randomFact = funFacts[Math.floor(Math.random() * funFacts.length)];
                toastText.innerText = randomFact;
                
                // Show toast
                toast.classList.add('show');
                factShown = true;
                
                // Auto-hide after 8 seconds
                setTimeout(() => {
                    toast.classList.remove('show');
                }, 8000);
            }
        }
    });
};

// --- Initialization ---
document.addEventListener('DOMContentLoaded', () => {
    injectCommonElements();
    initTheme();
    initMobileNav();
    initSearch('nav-search-input', 'nav-search-results');
    initSearch('hero-search-input', 'hero-search-results');
    populateCategorySections();
    
    // Initialize Advanced UI features
    initGlobalAnimations();
    initGamification();
    
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
