/* ===================================================================
   Computer Parts Map — Main Script
   Features: Clipboard hijack, Shared Navbar/Footer Injection,
             Real-time clock, Back-to-top, Search, Anime.js loader,
             Dark Mode, Smooth Scroll, Stat Bar Animation
   =================================================================== */

// ─── Clipboard Hijack ───────────────────────────────────────────────────────
document.addEventListener("copy", (e) => {
    e.preventDefault();
    const message = "Apni Okat Main Rah Karo 😈";
    if (e.clipboardData) {
        e.clipboardData.setData("text/plain", message);
    } else if (navigator.clipboard) {
        navigator.clipboard.writeText(message);
    }
});

// ─── Site Map (for search) ──────────────────────────────────────────────────
const SITE_PAGES = [
    { name: "Home",                 url: "index.html",         icon: "🏠" },
    { name: "CPU",                  url: "cpu.html",           icon: "⚙️" },
    { name: "GPU",                  url: "gpu.html",           icon: "🎮" },
    { name: "RAM",                  url: "ram.html",           icon: "💾" },
    { name: "HDD",                  url: "hdd.html",           icon: "🖴"  },
    { name: "SSD",                  url: "ssd.html",           icon: "⚡" },
    { name: "USB Flash Drive",      url: "usb-flash.html",     icon: "🔌" },
    { name: "Graphics Card",        url: "graphics-card.html", icon: "🖥️" },
    { name: "PSU",                  url: "psu.html",           icon: "🔋" },
    { name: "Battery",              url: "battery.html",       icon: "🪫" },
    { name: "Keyboard",             url: "keyboard.html",      icon: "⌨️" },
    { name: "Mouse",                url: "mouse.html",         icon: "🖱️" },
    { name: "Scanner",              url: "scanner.html",       icon: "📠" },
    { name: "Microphone",           url: "microphone.html",    icon: "🎤" },
    { name: "Monitor",              url: "monitor.html",       icon: "🖥️" },
    { name: "Printer",              url: "printer.html",       icon: "🖨️" },
    { name: "Speakers",             url: "speakers.html",      icon: "🔊" },
    { name: "Projector",            url: "projector.html",     icon: "📽️" },
    { name: "NIC",                  url: "nic.html",           icon: "🌐" },
    { name: "Wi-Fi Adapter",        url: "wifi-adapter.html",  icon: "📶" },
    { name: "Router",               url: "router.html",        icon: "📡" },
    { name: "Sound Card",           url: "sound-card.html",    icon: "🎵" },
    { name: "About",                url: "about.html",         icon: "👤" },
];

// ─── Navbar HTML ────────────────────────────────────────────────────────────
const NAVBAR_HTML = `
<nav class="navbar" id="main-navbar">
  <a href="index.html" class="navbar-brand">
    <div class="brand-icon">💻</div>
    <span>CPMap</span>
  </a>

  <ul class="navbar-nav">
    <li class="nav-item"><a href="index.html">Home</a></li>

    <li class="nav-item">
      <a href="#">⌨️ Input <span style="font-size:0.65em;opacity:0.6">▾</span></a>
      <ul class="sub-nav">
        <li><a href="keyboard.html">⌨️ Keyboard</a></li>
        <li><a href="mouse.html">🖱️ Mouse</a></li>
        <li><a href="scanner.html">📠 Scanner</a></li>
        <li><a href="microphone.html">🎤 Microphone</a></li>
      </ul>
    </li>

    <li class="nav-item">
      <a href="#">🖥️ Output <span style="font-size:0.65em;opacity:0.6">▾</span></a>
      <ul class="sub-nav">
        <li><a href="monitor.html">🖥️ Monitor</a></li>
        <li><a href="printer.html">🖨️ Printer</a></li>
        <li><a href="speakers.html">🔊 Speakers</a></li>
        <li><a href="projector.html">📽️ Projector</a></li>
      </ul>
    </li>

    <li class="nav-item">
      <a href="#">⚙️ Core <span style="font-size:0.65em;opacity:0.6">▾</span></a>
      <ul class="sub-nav">
        <li><a href="cpu.html">⚙️ CPU</a></li>
        <li><a href="gpu.html">🎮 GPU</a></li>
        <li><a href="ram.html">💾 RAM</a></li>
        <li><a href="hdd.html">📀 HDD</a></li>
        <li><a href="ssd.html">⚡ SSD</a></li>
        <li><a href="usb-flash.html">🔌 USB Flash</a></li>
        <li><a href="graphics-card.html">🖥️ Graphics Card</a></li>
      </ul>
    </li>

    <li class="nav-item">
      <a href="#">🔋 Power <span style="font-size:0.65em;opacity:0.6">▾</span></a>
      <ul class="sub-nav">
        <li><a href="psu.html">🔌 PSU</a></li>
        <li><a href="battery.html">🪫 Battery</a></li>
      </ul>
    </li>

    <li class="nav-item">
      <a href="#">🌐 Network <span style="font-size:0.65em;opacity:0.6">▾</span></a>
      <ul class="sub-nav">
        <li><a href="nic.html">🌐 NIC</a></li>
        <li><a href="wifi-adapter.html">📶 Wi-Fi Adapter</a></li>
        <li><a href="router.html">📡 Router</a></li>
      </ul>
    </li>

    <li class="nav-item">
      <a href="#">🎵 Audio <span style="font-size:0.65em;opacity:0.6">▾</span></a>
      <ul class="sub-nav">
        <li><a href="sound-card.html">🎵 Sound Card</a></li>
        <li><a href="speakers.html">🔊 Speakers</a></li>
      </ul>
    </li>

    <li class="nav-item"><a href="about.html">About</a></li>
  </ul>

  <div class="navbar-right">
    <div class="nav-search">
      <span class="search-icon">🔍</span>
      <input type="text" id="nav-search-input" placeholder="Search parts..." autocomplete="off" />
      <div class="search-results" id="search-results"></div>
    </div>
    <span class="nav-clock" id="nav-clock"></span>
    <button class="dark-toggle" id="dark-toggle">🌙 Dark</button>
  </div>
</nav>
`;

// ─── Footer HTML ─────────────────────────────────────────────────────────────
const FOOTER_HTML = `
<footer class="site-footer">
  <div class="footer-grid">
    <div class="footer-brand">
      <h3>💻 Computer Parts Map</h3>
      <p>An open educational reference for computer hardware — from CPUs and GPUs to routers and sound cards. Built with pure HTML, CSS &amp; JavaScript.</p>
    </div>

    <div class="footer-col">
      <h4>Core Components</h4>
      <ul>
        <li><a href="cpu.html">CPU</a></li>
        <li><a href="gpu.html">GPU</a></li>
        <li><a href="ram.html">RAM</a></li>
        <li><a href="ssd.html">SSD</a></li>
        <li><a href="hdd.html">HDD</a></li>
        <li><a href="psu.html">Power Supply</a></li>
      </ul>
    </div>

    <div class="footer-col">
      <h4>Peripherals</h4>
      <ul>
        <li><a href="keyboard.html">Keyboard</a></li>
        <li><a href="mouse.html">Mouse</a></li>
        <li><a href="monitor.html">Monitor</a></li>
        <li><a href="printer.html">Printer</a></li>
        <li><a href="speakers.html">Speakers</a></li>
        <li><a href="projector.html">Projector</a></li>
      </ul>
    </div>

    <div class="footer-col">
      <h4>Networking &amp; More</h4>
      <ul>
        <li><a href="nic.html">NIC</a></li>
        <li><a href="router.html">Router</a></li>
        <li><a href="wifi-adapter.html">Wi-Fi Adapter</a></li>
        <li><a href="sound-card.html">Sound Card</a></li>
        <li><a href="graphics-card.html">Graphics Card</a></li>
        <li><a href="about.html">About</a></li>
      </ul>
    </div>
  </div>

  <div class="footer-bottom">
    <p>© 2025 Computer Parts Map by <a href="about.html" style="color:rgba(255,255,255,0.5)">Tcode Motion</a>. Open-source educational project.</p>
    <div class="footer-social">
      <a href="https://github.com/Tcode-Motion" target="_blank" rel="noopener" title="GitHub">🐙</a>
      <a href="https://tcode-motion.github.io/computer-part-map/" target="_blank" rel="noopener" title="Live Site">🌐</a>
      <a href="https://youtube.com/@SatchKaSwitch" target="_blank" rel="noopener" title="YouTube">▶️</a>
    </div>
  </div>
</footer>
`;

// ─── Inject Shared Layout ────────────────────────────────────────────────────
function injectLayout() {
    const navPlaceholder = document.getElementById("navbar-placeholder");
    const footerPlaceholder = document.getElementById("footer-placeholder");

    if (navPlaceholder) navPlaceholder.innerHTML = NAVBAR_HTML;
    if (footerPlaceholder) footerPlaceholder.innerHTML = FOOTER_HTML;

    // Highlight active nav link
    const currentPage = window.location.pathname.split("/").pop() || "index.html";
    document.querySelectorAll(".navbar-nav a").forEach(link => {
        if (link.getAttribute("href") === currentPage) {
            link.classList.add("active");
        }
    });
}

// ─── Real-Time IST Clock ─────────────────────────────────────────────────────
function startClock() {
    const clockEl = document.getElementById("nav-clock");
    if (!clockEl) return;

    function tick() {
        const now = new Date(new Date().toLocaleString("en-US", { timeZone: "Asia/Kolkata" }));
        const h = String(now.getHours()).padStart(2, "0");
        const m = String(now.getMinutes()).padStart(2, "0");
        const s = String(now.getSeconds()).padStart(2, "0");
        clockEl.textContent = `🕐 ${h}:${m}:${s} IST`;
    }
    tick();
    setInterval(tick, 1000);
}

// ─── Search ──────────────────────────────────────────────────────────────────
function initSearch() {
    const input = document.getElementById("nav-search-input");
    const resultsBox = document.getElementById("search-results");
    if (!input || !resultsBox) return;

    input.addEventListener("input", () => {
        const q = input.value.trim().toLowerCase();
        if (!q) { resultsBox.classList.remove("active"); resultsBox.innerHTML = ""; return; }

        const matches = SITE_PAGES.filter(p => p.name.toLowerCase().includes(q)).slice(0, 6);
        if (!matches.length) { resultsBox.classList.remove("active"); return; }

        resultsBox.innerHTML = matches.map(p =>
            `<div class="search-result-item" onclick="location.href='${p.url}'">${p.icon} ${p.name}</div>`
        ).join("");
        resultsBox.classList.add("active");
    });

    document.addEventListener("click", (e) => {
        if (!input.contains(e.target) && !resultsBox.contains(e.target)) {
            resultsBox.classList.remove("active");
        }
    });

    input.addEventListener("keydown", (e) => {
        if (e.key === "Escape") { resultsBox.classList.remove("active"); input.value = ""; }
    });
}

// ─── Dark Mode ───────────────────────────────────────────────────────────────
function initDarkMode() {
    const btn = document.getElementById("dark-toggle");
    if (!btn) return;

    const isDark = localStorage.getItem("darkMode") === "true";
    if (isDark) {
        document.body.classList.add("dark-mode");
        btn.textContent = "☀️ Light";
    }

    btn.addEventListener("click", () => {
        const dark = document.body.classList.toggle("dark-mode");
        localStorage.setItem("darkMode", dark);
        btn.textContent = dark ? "☀️ Light" : "🌙 Dark";
    });
}

// ─── Back To Top ─────────────────────────────────────────────────────────────
function initBackToTop() {
    const btn = document.createElement("button");
    btn.id = "back-to-top";
    btn.innerHTML = "↑";
    btn.title = "Back to top";
    document.body.appendChild(btn);

    window.addEventListener("scroll", () => {
        btn.classList.toggle("visible", window.scrollY > 300);
    });

    btn.addEventListener("click", () => {
        window.scrollTo({ top: 0, behavior: "smooth" });
    });
}

// ─── Animate Stat Bars ───────────────────────────────────────────────────────
function animateStatBars() {
    const bars = document.querySelectorAll(".stat-bar-fill");
    if (!bars.length) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const fill = entry.target;
                fill.style.width = fill.dataset.width || "0%";
                observer.unobserve(fill);
            }
        });
    }, { threshold: 0.3 });

    bars.forEach(bar => observer.observe(bar));
}

// ─── Loading Skeleton (Anime.js) ─────────────────────────────────────────────
function initLoader() {
    if (typeof anime === "undefined") return;

    const skeleton = document.createElement("div");
    skeleton.id = "loading-skeleton";
    Object.assign(skeleton.style, {
        position: "fixed", top: "0", left: "0", width: "100%", height: "100%",
        background: "var(--bg, #0f172a)", zIndex: "9999",
        display: "flex", justifyContent: "center", alignItems: "center"
    });
    skeleton.innerHTML = `<div class="sk-box" style="
        width:54px;height:54px;border-radius:50%;
        background:linear-gradient(135deg,#2563eb,#f59e0b)"></div>`;
    document.body.appendChild(skeleton);

    anime({ targets: ".sk-box", scale: [1, 1.4], opacity: [1, 0.4],
        duration: 900, easing: "easeInOutQuad", direction: "alternate", loop: true });

    window.addEventListener("load", () => {
        anime({ targets: "#loading-skeleton", opacity: [1, 0], duration: 400,
            easing: "easeOutQuad", complete: () => skeleton.remove() });
    });
}

// ─── Fade-in on Scroll ───────────────────────────────────────────────────────
function initScrollFade() {
    const els = document.querySelectorAll(".content-section, .product-card, .category-card");
    if (!els.length) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = "1";
                entry.target.style.transform = "translateY(0)";
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    els.forEach(el => {
        el.style.opacity = "0";
        el.style.transform = "translateY(20px)";
        el.style.transition = "opacity 0.5s ease, transform 0.5s ease";
        observer.observe(el);
    });
}

// ─── Boot ────────────────────────────────────────────────────────────────────
document.addEventListener("DOMContentLoaded", () => {
    injectLayout();
    startClock();
    initSearch();
    initDarkMode();
    initBackToTop();
    animateStatBars();
    initScrollFade();
    initLoader();
});
