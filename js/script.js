/**
 * Computer Parts Map - Core Logic 2.0
 * Handles: Navbar/Footer injection, Dark Mode, Search, Smooth Scrolling, and Animations.
 */

// --- Constants & Config ---
const SITE_PAGES = [
    { name: "CPU (Processor)", url: "cpu.html", cat: "Core" },
    { name: "GPU (Graphics Card)", url: "gpu.html", cat: "Core" },
    { name: "RAM (Memory)", url: "ram.html", cat: "Core" },
    { name: "Motherboard", url: "motherboard.html", cat: "Core" },
    { name: "SSD (Solid State)", url: "ssd.html", cat: "Core" },
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
    { name: "Operating Systems", url: "operating-systems.html", cat: "Software" },
    { name: "Windows", url: "windows.html", cat: "Software" },
    { name: "Linux", url: "linux.html", cat: "Software" },
    { name: "macOS", url: "macos.html", cat: "Software" },
    { name: "Software Types", url: "software-types.html", cat: "Software" },
    { name: "Computer Types", url: "computer-types.html", cat: "History" },
    { name: "History of Computing", url: "computer-history.html", cat: "History" },
    { name: "Server Guide", url: "server-guide.html", cat: "History" },
    { name: "About Us", url: "about.html", cat: "Misc" }
];

// --- Navbar & Footer Injection ---
const injectCommonElements = () => {
    const navbarHTML = `
    <nav class="navbar">
      <div class="nav-container">
        <a href="index.html" class="nav-logo">⚡ Computer<span>Map</span></a>
        
        <ul class="nav-menu">
          <li><a href="index.html">Home</a></li>
          <li class="has-dropdown">
            <a href="#">Hardware ▾</a>
            <ul class="sub-nav">
              <li><a href="cpu.html">CPU</a></li>
              <li><a href="gpu.html">GPU</a></li>
              <li><a href="ram.html">RAM</a></li>
              <li><a href="ssd.html">SSD / Storage</a></li>
              <li><a href="motherboard.html">Motherboard</a></li>
              <li><a href="psu.html">Power Supply (PSU)</a></li>
              <li><a href="cooling.html">Cooling</a></li>
            </ul>
          </li>
          <li class="has-dropdown">
            <a href="#">Input/Output ▾</a>
            <ul class="sub-nav">
              <li><a href="monitor.html">Monitor</a></li>
              <li><a href="keyboard.html">Keyboard</a></li>
              <li><a href="mouse.html">Mouse</a></li>
              <li><a href="printer.html">Printer</a></li>
              <li><a href="webcam.html">Webcam</a></li>
            </ul>
          </li>
          <li class="has-dropdown">
            <a href="#">Software & OS ▾</a>
            <ul class="sub-nav">
              <li><a href="operating-systems.html">What is OS?</a></li>
              <li><a href="windows.html">Windows</a></li>
              <li><a href="linux.html">Linux</a></li>
              <li><a href="macos.html">macOS</a></li>
              <li><a href="software-types.html">Software Types</a></li>
            </ul>
          </li>
          <li class="has-dropdown">
            <a href="#">More ▾</a>
            <ul class="sub-nav">
              <li><a href="computer-types.html">Types of Computers</a></li>
              <li><a href="computer-history.html">Computing History</a></li>
              <li><a href="server-guide.html">Server Guide</a></li>
              <li><a href="ups.html">UPS</a></li>
              <li><a href="optical-drive.html">Optical Drives</a></li>
              <li><a href="about.html">About project</a></li>
            </ul>
          </li>
        </ul>

        <div class="nav-actions">
          <div class="search-box">
            <input type="text" id="nav-search-input" placeholder="Search components...">
            <div id="nav-search-results" class="search-dropdown"></div>
          </div>
          <button id="theme-toggle" title="Toggle Dark/Light Mode">🌓</button>
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
            <a href="#">🌐</a>
            <a href="#">📧</a>
            <a href="https://github.com/Tcode-Motion/computer-part-map/" target="_blank">🐙</a>
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
          <a href="https://tcode-motion.github.io/computer-part-map/">Live Demo</a>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 Computer Parts Map. Built for the community. "Apni Okat Main Rah Karo 😈"</p>
      </div>
    </footer>`;

    const navElement = document.getElementById('navbar-placeholder');
    const footerElement = document.getElementById('footer-placeholder');
    
    if (navElement) navElement.innerHTML = navbarHTML;
    if (footerElement) footerElement.innerHTML = footerHTML;
};

// --- Copy Protection ---
const initCopyBlocker = () => {
    document.addEventListener('copy', (e) => {
        const selectedText = window.getSelection().toString();
        if (selectedText) {
            e.clipboardData.setData('text/plain', "Apni Okat Main Rah Karo 😈");
            e.preventDefault();
        }
    });
};

// --- Search Logic ---
const initSearch = (inputId, resultsId) => {
    const input = document.getElementById(inputId);
    const results = document.getElementById(resultsId);
    if (!input || !results) return;

    input.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase();
        results.innerHTML = "";
        
        if (query.length < 1) {
            results.classList.remove('active');
            return;
        }

        const matches = SITE_PAGES.filter(p => p.name.toLowerCase().includes(query) || p.cat.toLowerCase().includes(query)).slice(0, 8);
        
        if (matches.length > 0) {
            matches.forEach(m => {
                const div = document.createElement('div');
                div.className = 'search-item';
                div.innerHTML = `<span>${m.name}</span><span class="cat-tag">${m.cat}</span>`;
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
        anime({
            targets: stat,
            innerHTML: [0, target],
            round: 1,
            easing: 'easeOutExpo',
            duration: 2000,
            delay: 500
        });
    });
};

// --- Initialization ---
document.addEventListener('DOMContentLoaded', () => {
    injectCommonElements();
    initTheme();
    initCopyBlocker();
    initSearch('nav-search-input', 'nav-search-results');
    initSearch('hero-search-input', 'hero-search-results');
    
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
