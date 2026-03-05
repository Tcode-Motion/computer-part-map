# ⚡ Computer Parts Map (CPMap) — Version 2.0 🚀

[![Live Site](https://img.shields.io/badge/Live-Encyclopedia-brightgreen?style=for-the-badge&logo=google-chrome)](https://tcode-motion.github.io/computer-part-map/)
[![Version](https://img.shields.io/badge/Version-2.0%20Premium-blue?style=for-the-badge)](https://github.com/Tcode-Motion/computer-part-map)
[![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)](LICENSE)
[![Tech](https://img.shields.io/badge/Tech-Pure%20Web-red?style=for-the-badge)](https://developer.mozilla.org/en-US/docs/Web/HTML)

> **The world's most detailed interactive encyclopedia for computer hardware and software.**  
> Designed for students, engineers, and researchers to bridge the gap between basic guides and academic papers.

---

## 📖 Project Vision

**CPMap** is more than just a list of parts. It is a **Research-Grade Educational Platform**. While Version 1.0 focused on basic hardware definitions, **Version 2.0 (Premium)** transforms the site into a high-density knowledge base with automated media ingestion, academic referencing, and advanced computing sections.

### 🔬 What's New in Version 2.0?
*   **Academic Integration**: Every page features a "Research Hub" with direct query links to **Google Scholar** and **IEEE Xplore**.
*   **Modern Paradigms**: Dedicated deep-dives into **NPU (AI)**, **Quantum Computing**, and **SBC (Raspberry Pi)** architecture.
*   **Data Enrichment**: Expanded to **70+ total pages**, including 30+ detailed technical sub-pages.
*   **Interactive Search**: Migrated from basic filters to a full-text inverted index search powered by **Lunr.js**.
*   **Automation Suite**: Integrated Python tools to fetch public-domain media from NASA and Wikimedia automatically.

---

## ✨ Premium Features

### 🧭 Advanced Navigation
A **Mega-Dropdown Navbar** categorizes the entire computing landscape:
*   **Hardware**: Core (CPU/GPU/NPU), Input (Webcam/Touchpad), and Output/Storage.
*   **Software**: Comprehensive guides for Windows, Linux, macOS, Android, and iOS.
*   **Computing**: Timeline of History, Server Infrastructure, and Future Tech.

### 🖼️ Automated Visual Galleries
Every component page includes a high-resolution gallery of technical diagrams and real-world screenshots, sourced automatically from open libraries like **Wikimedia Commons** and **NASA**.

### 🎥 Embedded University Lectures
Instead of broken video links, CPMap dynamically surfaces university-level CS lectures and engineering demonstrations directly related to the topic being studied.

### 🌙 Premium UI/UX
*   **Glassmorphism Navbar**: Sticky, blurred glass effect for modern aesthetics.
*   **Stats Counter**: Animated counters on the homepage showing the library's growth.
*   **Pure Dark Mode**: A custom-engineered dark theme optimized for long study sessions.

---

## 🗂️ Knowledge Architecture

| Category | High-Level Topics | Research Sub-pages |
|:---|:---|:---|
| **Core Hardware** | CPU, GPU, NPU, RAM, Motherboard | Architecture, Benchmarks, Logic |
| **Mobile & OS** | Android, iOS, Windows, Linux, macOS | Kernels, NT Architecture, Distros |
| **Networking** | Router, NIC, WiFi-7, Server Infrastructure | Protocols, Signal Physics |
| **Storage** | SSD, HDD, NVMe, Optical/Laser | Flash Physics, Laser Tech |
| **Future Tech** | Quantum Computing, Neural Engines | Qubits, Tensor Math, SBCs |

---

## 🛠️ Tech Stack & Automation

### Frontend
*   **Core**: Semantic HTML5, Modular CSS3 (Custom Design System).
*   **Logic**: Vanilla JavaScript (ES6+).
*   **Search**: [Lunr.js](https://lunrjs.com/) for site-wide full-text indexing.
*   **Animations**: [Anime.js](https://animejs.com/) for high-end UI feedback.

### Automation (The Ingest Suite)
Located in `/tools` and `/scripts`, these Python tools maintain the library's depth:
*   `cpmap_ingest.py`: Idempotent asset downloader (NASA/YouTube).
*   `build_search_index.py`: Rebuilds the Lunr index across all 70+ pages.
*   `generate_detail_pages.py`: Uses Jinja2 templates to create technical sub-pages from JSON datasets.

---

## 🚀 Deployment & Local Setup

### 1. Hard Refresh (Live Site)
If you are visiting the [Live Site](https://tcode-motion.github.io/computer-part-map/) and see old content, please perform a **Hard Refresh**:
*   **Windows**: `Ctrl + F5`
*   **Mac**: `Cmd + Shift + R`

### 2. Local Development
```bash
# Clone the repo
git clone https://github.com/Tcode-Motion/computer-part-map.git

# Install Ingest Tools dependencies
pip install -r tools/requirements.txt

# Run local server
python -m http.server 8000
```

---

## 👨‍💻 Developed By

**Tcode Motion**  
*Building the future of open-source computer education.*

*   **GitHub**: [@Tcode-Motion](https://github.com/Tcode-Motion)
*   **Live Library**: [Computer Parts Map](https://tcode-motion.github.io/computer-part-map/)

---

<div align="center">
  <sub>CPMap is an Open Source project. "Truth through Data." — Made by Tcode Motion.</sub>
</div>
