/**
 * CPU Interactive — Anti-Boring UI Engine
 * Scroll Animations, Tooltip Engine, Cache Diagram, Chart.js, Counters
 */

(function () {
  'use strict';

  // ============================================================
  // 1. SCROLL-TRIGGERED REVEAL ANIMATIONS (IntersectionObserver)
  // ============================================================
  const initScrollReveal = () => {
    const els = document.querySelectorAll('.reveal-on-scroll');
    if (!els.length) return;

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -50px 0px' });

    els.forEach(el => observer.observe(el));
  };

  // ============================================================
  // 2. JARGON TOOLTIP ENGINE
  // ============================================================
  const JARGON_DEFINITIONS = {
    'isa': 'Instruction Set Architecture — the set of commands a CPU understands.',
    'ipc': 'Instructions Per Clock — how many operations a CPU completes per tick.',
    'tdp': 'Thermal Design Power — the maximum heat a CPU generates under load.',
    'lithography': 'The process of printing circuit patterns onto silicon wafers using light.',
    'euv': 'Extreme Ultraviolet Lithography — uses 13.5nm wavelength light for sub-7nm chips.',
    'smt': 'Simultaneous Multi-Threading — lets one core run two threads at once.',
    'hyper-threading': 'Intel\'s brand name for SMT. Each core appears as two logical processors.',
    'cache': 'Ultra-fast memory inside the CPU (L1/L2/L3) that stores frequently used data.',
    'pipeline': 'Breaking instruction execution into stages so multiple instructions overlap.',
    'mosfet': 'Metal-Oxide-Semiconductor FET — the transistor type used in all modern CPUs.',
    'finfet': 'A 3D transistor where the gate wraps around a raised "fin" of silicon.',
    'gaafet': 'Gate-All-Around FET — the gate fully surrounds the channel for better control.',
    'alu': 'Arithmetic Logic Unit — performs math and logic operations inside a CPU core.',
    'fpu': 'Floating Point Unit — handles decimal math (used heavily in games and science).',
    'ooo': 'Out-of-Order Execution — CPU reorders instructions to keep all units busy.',
    'branch prediction': 'CPU guesses which code path will execute next to keep the pipeline full.',
    'speculative execution': 'CPU runs predicted code before knowing if the prediction is correct.',
    'chiplet': 'A small die that\'s combined with others to form a complete processor.',
    'process node': 'Manufacturing generation (e.g., 5nm) indicating transistor density.',
    'die': 'The actual silicon chip cut from a wafer, containing all the transistors.',
    'wafer': 'A thin slice of ultra-pure silicon crystal used to manufacture chips.',
    'risc': 'Reduced Instruction Set Computer — simpler instructions, more efficient execution.',
    'cisc': 'Complex Instruction Set Computer — powerful single instructions (e.g., x86).',
    'arm': 'Advanced RISC Machines — the architecture powering 99% of smartphones.',
    'avx-512': 'Advanced Vector Extensions — Intel\'s 512-bit SIMD instructions for heavy math.',
    'npu': 'Neural Processing Unit — dedicated hardware for AI/ML inference.',
    'qubit': 'Quantum bit — can be 0, 1, or both simultaneously (superposition).',
    'dram': 'Dynamic RAM — main memory that needs constant refreshing to hold data.',
    'sram': 'Static RAM — ultra-fast memory used in CPU caches (no refresh needed).',
    'clock speed': 'How many cycles per second a CPU runs, measured in GHz.',
    'boost clock': 'Maximum frequency a CPU can reach for short bursts under light load.',
    'base clock': 'The guaranteed minimum frequency a CPU runs at under any condition.',
    'microarchitecture': 'The specific internal design of a CPU generation (e.g., Zen 4, Golden Cove).',
    'interconnect': 'The high-speed bus connecting chiplets or CPU to memory (e.g., Infinity Fabric).',
    'pcie': 'PCI Express — the primary high-speed interface for GPUs, SSDs, and add-in cards.'
  };

  const initTooltips = () => {
    document.querySelectorAll('[data-jargon]').forEach(el => {
      const term = el.getAttribute('data-jargon').toLowerCase();
      const definition = JARGON_DEFINITIONS[term];
      if (!definition) return;

      const tooltip = document.createElement('div');
      tooltip.className = 'jargon-tooltip';
      tooltip.textContent = definition;
      el.appendChild(tooltip);
    });

    // Auto-detect and annotate terms in page text
    const contentSections = document.querySelectorAll('.content-section p, .content-section td');
    const termRegex = new RegExp(
      '\\b(' + Object.keys(JARGON_DEFINITIONS).join('|') + ')\\b', 'gi'
    );

    contentSections.forEach(el => {
      if (el.querySelector('[data-jargon]')) return; // Skip already annotated
      const html = el.innerHTML;
      // Only annotate first occurrence per element
      let annotated = false;
      const newHtml = html.replace(termRegex, (match) => {
        if (annotated) return match;
        const def = JARGON_DEFINITIONS[match.toLowerCase()];
        if (!def) return match;
        annotated = true;
        return `<span data-jargon="${match.toLowerCase()}" class="auto-tooltip">${match}<div class="jargon-tooltip">${def}</div></span>`;
      });
      if (newHtml !== html) el.innerHTML = newHtml;
    });
  };

  // ============================================================
  // 3. INTERACTIVE CACHE DIAGRAM (SVG)
  // ============================================================
  const initCacheDiagram = () => {
    const container = document.getElementById('cache-interactive-diagram');
    if (!container) return;

    const data = {
      L1: { size: '80 KB', latency: '~1 ns (4 cycles)', speedLabel: 'Speed of Light', color: '#ef4444', width: 120 },
      L2: { size: '1.25 MB', latency: '~3-5 ns (12 cycles)', speedLabel: 'Very Fast', color: '#f59e0b', width: 200 },
      L3: { size: '32-96 MB', latency: '~10-20 ns (40 cycles)', speedLabel: 'Fast', color: '#2563eb', width: 300 },
      RAM: { size: '16-64 GB', latency: '~50-80 ns (200 cycles)', speedLabel: 'Moderate', color: '#6b7280', width: 400 }
    };

    let svg = `<svg viewBox="0 0 500 320" xmlns="http://www.w3.org/2000/svg" style="max-width:500px; margin:0 auto; display:block;">`;
    let y = 20;
    for (const [name, d] of Object.entries(data)) {
      const x = (500 - d.width) / 2;
      svg += `
        <g class="svg-block cache-block" data-cache="${name}" style="cursor:pointer;">
          <rect x="${x}" y="${y}" width="${d.width}" height="55" rx="8" fill="${d.color}" opacity="0.2" stroke="${d.color}" stroke-width="1.5"/>
          <text x="250" y="${y + 25}" text-anchor="middle" fill="#fff" font-family="Space Grotesk,sans-serif" font-weight="600" font-size="14">${name} Cache</text>
          <text x="250" y="${y + 42}" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="11">${d.size}</text>
        </g>`;
      y += 72;
    }
    svg += `</svg>`;

    container.innerHTML = svg + `
      <div id="cache-info-panel" style="margin-top:20px; padding:20px; background:rgba(17,24,39,0.7); border:1px solid rgba(255,255,255,0.08); border-radius:12px; text-align:center; min-height:80px;">
        <p style="color:rgba(255,255,255,0.4); font-size:0.9rem;">👆 Click a cache level to see latency and performance details</p>
      </div>`;

    container.querySelectorAll('.cache-block').forEach(block => {
      block.addEventListener('click', () => {
        const name = block.getAttribute('data-cache');
        const d = data[name];
        container.querySelectorAll('.cache-block rect').forEach(r => r.setAttribute('opacity', '0.2'));
        block.querySelector('rect').setAttribute('opacity', '0.5');
        document.getElementById('cache-info-panel').innerHTML = `
          <h4 style="color:${d.color}; margin:0 0 8px; font-family:'Space Grotesk',sans-serif;">${name} Cache</h4>
          <p style="color:rgba(255,255,255,0.7); margin:4px 0;"><strong>Size:</strong> ${d.size}</p>
          <p style="color:rgba(255,255,255,0.7); margin:4px 0;"><strong>Latency:</strong> ${d.latency}</p>
          <p style="color:rgba(255,255,255,0.7); margin:4px 0;"><strong>Speed Rating:</strong> ${d.speedLabel}</p>
          <div style="margin-top:12px; height:8px; background:rgba(255,255,255,0.05); border-radius:4px; overflow:hidden;">
            <div style="height:100%; width:${name === 'L1' ? '100%' : name === 'L2' ? '70%' : name === 'L3' ? '40%' : '15%'}; background:${d.color}; border-radius:4px; transition:width 0.6s;"></div>
          </div>`;
      });
    });
  };

  // ============================================================
  // 4. ANIMATED COUNTERS
  // ============================================================
  const initCounters = () => {
    const counters = document.querySelectorAll('[data-count-to]');
    if (!counters.length) return;

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el = entry.target;
          const target = parseInt(el.getAttribute('data-count-to'));
          const suffix = el.getAttribute('data-count-suffix') || '';
          const duration = 2000;
          const start = performance.now();

          const animate = (now) => {
            const progress = Math.min((now - start) / duration, 1);
            const eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
            el.textContent = Math.floor(target * eased).toLocaleString() + suffix;
            if (progress < 1) requestAnimationFrame(animate);
          };
          requestAnimationFrame(animate);
          observer.unobserve(el);
        }
      });
    }, { threshold: 0.5 });

    counters.forEach(el => observer.observe(el));
  };

  // ============================================================
  // 5. FABRICATION SCROLL STEPS
  // ============================================================
  const initFabSteps = () => {
    const steps = document.querySelectorAll('.fab-step');
    if (!steps.length) return;

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
        }
      });
    }, { threshold: 0.3, rootMargin: '0px 0px -20% 0px' });

    steps.forEach(step => observer.observe(step));
  };

  // ============================================================
  // 6. CHART.JS COMPARISON CHARTS
  // ============================================================
  const initComparisonCharts = () => {
    const chartCanvas = document.getElementById('cpu-comparison-chart');
    if (!chartCanvas || typeof Chart === 'undefined') return;

    new Chart(chartCanvas, {
      type: 'bar',
      data: {
        labels: ['Ryzen 9 7950X', 'Core i9-14900K', 'Apple M3 Max', 'Ryzen 7 7800X3D', 'Core i5-13600K'],
        datasets: [
          {
            label: 'Multi-Thread (Cinebench R23)',
            data: [38255, 40539, 21636, 17100, 17640],
            backgroundColor: 'rgba(37, 99, 235, 0.7)',
            borderColor: '#2563eb',
            borderWidth: 1,
            borderRadius: 4
          },
          {
            label: 'TDP (Watts)',
            data: [170, 253, 78, 120, 181],
            backgroundColor: 'rgba(239, 68, 68, 0.5)',
            borderColor: '#ef4444',
            borderWidth: 1,
            borderRadius: 4
          }
        ]
      },
      options: {
        responsive: true,
        animation: { duration: 1500, easing: 'easeOutQuart' },
        plugins: {
          legend: { labels: { color: 'rgba(255,255,255,0.7)', font: { family: 'Inter' } } }
        },
        scales: {
          x: { ticks: { color: 'rgba(255,255,255,0.5)', font: { size: 11 } }, grid: { color: 'rgba(255,255,255,0.04)' } },
          y: { ticks: { color: 'rgba(255,255,255,0.5)' }, grid: { color: 'rgba(255,255,255,0.04)' } }
        }
      }
    });
  };

  // ============================================================
  // INIT ALL
  // ============================================================
  document.addEventListener('DOMContentLoaded', () => {
    initScrollReveal();
    initTooltips();
    initCacheDiagram();
    initCounters();
    initFabSteps();

    // Delay Chart.js init to ensure the library is loaded
    if (document.getElementById('cpu-comparison-chart')) {
      const chartScript = document.createElement('script');
      chartScript.src = 'https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js';
      chartScript.onload = initComparisonCharts;
      document.head.appendChild(chartScript);
    }
  });
})();
