import os
import json
from pathlib import Path

DATA_DIR = Path('data')
DATA_DIR.mkdir(exist_ok=True)

COMPONENTS = {
    'cpu': {
        'name': 'Central Processing Unit',
        'definition': 'The primary component of a computer that acts as its brain.',
        'overview': 'The CPU performs most of the processing inside the computer. It executes instructions of a computer program by performing basic arithmetic, logic, controlling, and input/output operations.',
        'history': "The first commercial microprocessor was the Intel 4004, released in 1971. Over decades, CPUs evolved from single-core processors to multi-core giants, adhering to Moore's Law for many years.",
        'architecture': 'Modern CPUs use the Von Neumann or Harvard architectures. Key components include the ALU (Arithmetic Logic Unit), CU (Control Unit), Registers, and Cache hierarchy (L1, L2, L3).',
        'working_principle': 'CPUs operate on the fetch-decode-execute cycle. The Control Unit fetches an instruction from memory, decodes it into commands, and the ALU executes them.',
        'applications': ['General-purpose computing', 'Server processing', 'Embedded systems', 'Mobile devices'],
        'manufacturing': 'CPUs are manufactured on silicon wafers using photolithography. Billions of transistors are etched into the silicon at nanometer scales (e.g., 3nm, 5nm nodes).',
        'benchmarks': ['Cinebench R23', 'Geekbench 6', 'PassMark', 'SPEC CPU'],
        'future_research': 'Future research directions include quantum computing integration, advanced 3D packaging (chiplets), and photonics for interconnects.',
        'references': [
            {'text': 'Intel Microprocessor History', 'url': 'https://www.intel.com/'},
            {'text': 'Computer Architecture: A Quantitative Approach', 'url': 'https://en.wikipedia.org/wiki/Computer_Architecture:_A_Quantitative_Approach'}
        ],
        'subpages': [
            {'title': 'CPU Architecture', 'slug': 'cpu-architecture.html'},
            {'title': 'CPU History', 'slug': 'cpu-history.html'},
            {'title': 'CPU Benchmarks', 'slug': 'cpu-benchmarks.html'}
        ]
    },
    'gpu': {
        'name': 'Graphics Processing Unit',
        'definition': 'A specialized electronic circuit designed to manipulate and alter memory to accelerate the creation of images.',
        'overview': 'GPUs are highly parallel processors originally designed for rendering graphics, now widely used for AI, machine learning, and scientific simulations.',
        'history': 'Early graphics accelerators emerged in the 1980s. Nvidia coined the term GPU in 1999 with the GeForce 256. The advent of CUDA in 2007 unlocked General Purpose GPU computing (GPGPU).',
        'architecture': "GPUs consist of thousands of smaller, simpler cores compared to CPUs. Architectures like Nvidia's Hopper or AMD's RDNA feature Streaming Multiprocessors, Tensor Cores, and RT Cores.",
        'working_principle': 'GPUs excel at SIMD (Single Instruction, Multiple Data) operations, applying the same instruction to multiple data points simultaneously, ideal for pixel rendering and matrix math.',
        'applications': ['3D Gaming', 'Video Editing', 'Deep Learning / AI', 'Cryptocurrency Mining'],
        'manufacturing': 'Manufactured using advanced nodes (like TSMC 4N), featuring large die sizes and massive transistor counts, often paired with HBM (High Bandwidth Memory).',
        'benchmarks': ['3DMark Time Spy', 'FurMark', 'Blender Benchmark', 'MLPerf'],
        'future_research': 'Future GPU research focuses on AI integration, path tracing efficiency, multi-chip-module (MCM) designs, and lower power consumption.',
        'references': [
            {'text': 'Nvidia CUDA Programming Guide', 'url': 'https://docs.nvidia.com/cuda/'},
            {'text': 'GPU Rendering Pipeline', 'url': 'https://en.wikipedia.org/wiki/Graphics_pipeline'}
        ],
        'subpages': [
            {'title': 'GPU Architecture', 'slug': 'gpu-architecture.html'},
            {'title': 'GPU Rendering Pipeline', 'slug': 'gpu-rendering-pipeline.html'}
        ]
    },
    'ram': {
        'name': 'Random Access Memory',
        'definition': 'A form of computer memory that can be read and changed in any order, typically used to store working data and machine code.',
        'overview': 'RAM provides high-speed, volatile data storage for the CPU. It is essential for multitasking and quick data retrieval during program execution.',
        'history': "Early RAM included magnetic-core memory. Dynamic RAM (DRAM) was invented in 1968. SDRAM became the standard in the 1990s, evolving through DDR to today's DDR5.",
        'architecture': 'RAM consists of memory cells built from a capacitor and a transistor. Cells are organized into arrays (banks), accessed via rows and columns by memory controllers.',
        'working_principle': 'The CPU sends a memory address to the memory controller, which activates the corresponding row and column. The data is read by sense amplifiers and sent to the CPU.',
        'applications': ['System working memory', 'VRAM in graphics cards', 'Cache systems', 'In-memory databases'],
        'manufacturing': 'Manufactured primarily by Samsung, SK Hynix, and Micron, involving complex multi-layer silicon fabrication focusing on capacitor density and retention time.',
        'benchmarks': ['AIDA64 Memory Benchmark', 'MemTest86', 'MaxxMem2'],
        'future_research': 'Research includes MRAM (Magnetoresistive RAM), phase-change memory, and computing-in-memory (CIM) paradigms.',
        'references': [
            {'text': 'JEDEC DDR5 Standard', 'url': 'https://www.jedec.org/'},
            {'text': 'Dynamic Random-Access Memory', 'url': 'https://en.wikipedia.org/wiki/Dynamic_random-access_memory'}
        ],
        'subpages': [
            {'title': 'RAM Types', 'slug': 'ram-types.html'},
            {'title': 'RAM Architecture', 'slug': 'ram-architecture.html'}
        ]
    },
    'motherboard': {
        'name': 'Motherboard',
        'definition': 'The main printed circuit board (PCB) in general-purpose computers and other expandable systems.',
        'overview': 'The motherboard holds and allows communication between many of the crucial electronic components of a system, such as the CPU and memory, and provides connectors for other peripherals.',
        'history': 'Before motherboards, computers consisted of multiple printed circuit boards plugged into a backplane. The original IBM PC motherboard (the planar) established the standard.',
        'architecture': 'Includes the CPU socket, RAM slots, PCIe slots, chipset (Northbridge/Southbridge historically, now highly integrated PCH), VRMs (Voltage Regulator Modules), and I/O ports.',
        'working_principle': 'Traces on the PCB act as buses, routing data and power. The chipset manages data flow between the CPU, memory, and peripherals using protocols like PCIe, SATA, and USB.',
        'applications': ['Desktop PCs', 'Servers', 'Laptops', 'Embedded computing'],
        'manufacturing': 'Constructed from fiberglass and copper in multiple layers (often 6 to 12 layers for modern boards). Surface-mount technology (SMT) is used to attach thousands of tiny components.',
        'benchmarks': ['DPC Latency Checker', 'PassMark System Test'],
        'future_research': 'Focus on signal integrity for PCIe 6.0/7.0, integrated optical interconnects, and advanced power delivery for high-TDP processors.',
        'references': [
            {'text': 'ATX Specification', 'url': 'https://en.wikipedia.org/wiki/ATX'},
            {'text': 'PCI Express Standard', 'url': 'https://pcisig.com/'}
        ],
        'subpages': [
            {'title': 'Motherboard Components', 'slug': 'motherboard-components.html'},
            {'title': 'Motherboard Chipset', 'slug': 'motherboard-chipset.html'}
        ]
    }
}

def main():
    print("Expanding component data in JSON files...")
    for slug, data in COMPONENTS.items():
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
