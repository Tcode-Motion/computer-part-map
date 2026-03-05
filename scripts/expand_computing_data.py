import os
import json
from pathlib import Path

DATA_DIR = Path('data')
DATA_DIR.mkdir(exist_ok=True)

COMPUTING_COMPONENTS = {
    'raspberry-pi': {
        'name': 'Raspberry Pi & Single Board Computers',
        'definition': 'A series of small single-board computers developed in the United Kingdom by the Raspberry Pi Foundation.',
        'overview': 'Single Board Computers (SBCs) like the Raspberry Pi pack a CPU, GPU, RAM, and I/O onto one credit-card-sized board. They are revolutionary for education, DIY electronics, and edge computing due to their low cost and GPIO accessibility.',
        'history': 'The first Raspberry Pi launched in 2012. It was intended to promote basic computer science in schools. Since then, it has evolved from the Model B to the powerful Raspberry Pi 5, spawning a massive ecosystem of HATs and clones.',
        'architecture': 'Typically based on ARM architecture (System-on-a-Chip). Includes GPIO pins for physical computing, microSD or NVMe storage, and various connectivity options like HDMI, USB, and Ethernet.',
        'working_principle': 'Operates like a standard computer but with highly integrated components. The SoC handles most logic, while the user interacts via Linux-based OSs like Raspberry Pi OS (formerly Raspbian).',
        'applications': ['IoT Gateways', 'Media Centers', 'Retro Gaming', 'Robotics', 'Industrial Controllers'],
        'manufacturing': 'Designed by Raspberry Pi Ltd and manufactured primarily in the UK (Sony UK Technology Centre) using advanced SMT lines.',
        'benchmarks': ['Sysbench', 'UnixBench', 'IOzone'],
        'future_research': 'Integration of dedicated NPUs for edge AI, transition to more efficient ARM designs, and improved PCIe support for high-speed peripherals.',
        'references': [
            {'text': 'Raspberry Pi Foundation', 'url': 'https://www.raspberrypi.org/'},
            {'text': 'MagPi Magazine', 'url': 'https://magpi.raspberrypi.com/'}
        ],
        'subpages': [
            {'title': 'SBC Architecture Deep Dive', 'slug': 'sbc-architecture.html'},
            {'title': 'GPIO & Physical Computing', 'slug': 'gpio-guide.html'}
        ]
    },
    'npu': {
        'name': 'Neural Processing Unit',
        'definition': 'A specialized circuit that implements all the necessary control and arithmetic logic necessary to execute machine learning algorithms.',
        'overview': 'NPUs are dedicated AI accelerators. Unlike general-purpose CPUs or graphics-focused GPUs, NPUs are designed specifically for the matrix math required for deep learning and neural network inference.',
        'history': "AI acceleration started with GPUs, but Google's TPU (2016) and Apple's Neural Engine (2017) proved that dedicated silicon could perform AI tasks much faster and with less power.",
        'architecture': 'Consists of massive arrays of Multiply-Accumulate (MAC) units, local memory buffers, and specialized controllers for tensor operations.',
        'working_principle': 'Optimized for high-throughput, low-precision arithmetic (INT8, FP16). They process large blocks of data (tensors) simultaneously rather than individual values.',
        'applications': ['Facial Recognition', 'Voice Assistants', 'Generative AI (LLMs)', 'Real-time Video Enhancement'],
        'manufacturing': 'Fabricated on cutting-edge nodes (3nm, 5nm) to maximize efficiency. Often integrated into SoCs (like Snapdragon, Apple Silicon, or Intel Core Ultra).',
        'benchmarks': ['MLPerf', 'Geekbench AI', 'AI Benchmark (Android)'],
        'future_research': 'Neuromorphic computing (mimicking brain neurons), in-memory computing, and quantized model acceleration.',
        'references': [
            {'text': 'Tensor Processing Units (Google Cloud)', 'url': 'https://cloud.google.com/tpu'},
            {'text': 'Apple Neural Engine Overview', 'url': 'https://developer.apple.com/machine-learning/'}
        ],
        'subpages': [
            {'title': 'NPU vs GPU Math', 'slug': 'npu-math.html'},
            {'title': 'AI Accelerators in Mobile', 'slug': 'mobile-ai.html'}
        ]
    },
    'quantum-computing': {
        'name': 'Quantum Computing',
        'definition': 'A type of computing that uses quantum-mechanical phenomena, such as superposition and entanglement.',
        'overview': 'Quantum computers use qubits instead of bits. This allows them to solve specific complex problems—like molecular simulation or breaking RSA encryption—exponentially faster than any classical supercomputer.',
        'history': 'Theoretical foundations laid in the 1980s by Richard Feynman and David Deutsch. Google claimed "Quantum Supremacy" in 2019 with its 53-qubit Sycamore processor.',
        'architecture': 'Built using superconducting loops, trapped ions, or photonic circuits. Requires extreme environments, often cooled to near absolute zero (-273°C).',
        'working_principle': 'Leverages superposition (being in multiple states at once) and entanglement (instant correlation) to perform multi-dimensional calculations via quantum gates.',
        'applications': ['Drug Discovery', 'Financial Modeling', 'Cybersecurity', 'Logistics Optimization'],
        'manufacturing': 'Highly specialized fabrication involving dilution refrigerators and precision microwave control systems.',
        'benchmarks': ['CLOPS (Circuit Layer Operations Per Second)', 'Quantum Volume'],
        'future_research': 'Error correction (NISQ era), room-temperature quantum dots, and topological qubits.',
        'references': [
            {'text': 'IBM Quantum', 'url': 'https://www.ibm.com/quantum'},
            {'text': 'Quantum Computing on Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Quantum_computing'}
        ],
        'subpages': [
            {'title': 'Qubits & Gates', 'slug': 'quantum-logic.html'},
            {'title': 'Quantum Error Correction', 'slug': 'quantum-errors.html'}
        ]
    },
    'nic': {
        'name': 'Network Interface Card (NIC)',
        'definition': 'A computer hardware component that connects a computer to a computer network.',
        'overview': 'The NIC (or LAN Card) is the physical interface between your computer and the network. It handles data framing, MAC addressing, and signal conversion for Ethernet or Fiber.',
        'history': 'Evolved from expensive add-in cards in the 1980s to being integrated into every motherboard by the early 2000s.',
        'architecture': 'Includes a controller chip (ASIC), specialized buffer memory, and physical ports (RJ45, SFP+).',
        'working_principle': 'The NIC receives data from the OS, encapsulates it into frames, and transmits it over the physical medium using CSMA/CD or full-duplex protocols.',
        'applications': ['Internet access', 'Local area networks', 'Data center interconnects'],
        'manufacturing': 'Produced by companies like Intel, Realtek, and Mellanox using standard semiconductor processes.',
        'benchmarks': ['Iperf3', 'Netperf'],
        'future_research': 'SmartNICs (DPUs) that offload CPU tasks, and 400Gbps/800Gbps Ethernet standards.',
        'references': [
            {'text': 'IEEE 802.3 Standard', 'url': 'https://en.wikipedia.org/wiki/IEEE_802.3'}
        ]
    },
    'router': {
        'name': 'Router',
        'definition': 'A networking device that forwards data packets between computer networks.',
        'overview': 'Routers act as traffic police for the internet. They connect multiple networks together and use routing tables to decide the best path for data to reach its destination.',
        'history': 'The first modern routers were developed at Stanford in the 1980s. Today, they range from small home WiFi units to massive core routers used by ISPs.',
        'architecture': 'Features a CPU, specialized NPU for packet forwarding, RAM for routing tables, and multiple LAN/WAN ports.',
        'working_principle': 'Operates at Layer 3 of the OSI model. It examines IP addresses, checks its routing table, and forwards packets across different network segments.',
        'applications': ['Home WiFi', 'Enterprise Networking', 'ISP Backbone'],
        'manufacturing': 'Built by Cisco, TP-Link, ASUS, and Juniper focusing on thermal management and signal integrity.',
        'benchmarks': ['Throughput (Mbps)', 'Latency (ms)', 'NAT Sessions'],
        'future_research': 'WiFi 7 (802.11be), AI-driven traffic shaping, and SD-WAN (Software-Defined WAN).',
        'references': [
            {'text': 'How Routers Work', 'url': 'https://en.wikipedia.org/wiki/Router_(computing)'}
        ]
    },
    'wifi-adapter': {
        'name': 'WiFi Adapter',
        'definition': 'A device that allows a computer to connect to a wireless network.',
        'overview': 'WiFi adapters translate radio waves into data. They come as internal PCIe cards, M.2 modules in laptops, or portable USB dongles.',
        'history': 'WiFi (802.11) launched in 1997 with 2Mbps speeds. It has evolved through 802.11n (WiFi 4), ac (WiFi 5), ax (WiFi 6/6E), and now be (WiFi 7).',
        'architecture': 'Includes a radio transceiver, an antenna system (MIMO), and a baseband processor.',
        'working_principle': 'Modulates data onto carrier waves in the 2.4GHz, 5GHz, or 6GHz bands using OFDM/OFDMA techniques.',
        'applications': ['Laptop mobility', 'Smartphones', 'Desktop wireless connectivity'],
        'manufacturing': 'Dominated by Intel, Broadcom, and Qualcomm.',
        'benchmarks': ['Throughput tests', 'Signal-to-Noise Ratio (SNR)'],
        'future_research': 'Millimeter-wave frequencies and ultra-reliable low-latency communication (URLLC).',
        'references': [
            {'text': 'WiFi Alliance', 'url': 'https://www.wi-fi.org/'}
        ]
    }
}

def main():
    print("Expanding Computing data in JSON files...")
    for slug, data in COMPUTING_COMPONENTS.items():
        json_path = DATA_DIR / f"{slug}.json"
        
        existing_data = {}
        if json_path.exists():
            try:
                with open(json_path, 'r', encoding='utf-8') as f:
                    existing_data = json.load(f)
            except Exception:
                pass
                
        merged_data = {**existing_data, **data}
        if 'media' not in merged_data:
            merged_data['media'] = {'images': [], 'videos': [], 'audio': []}
            
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(merged_data, f, indent=2)
        print(f"Updated {json_path}")

if __name__ == '__main__':
    main()
