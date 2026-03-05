import os
import json
from pathlib import Path

DATA_DIR = Path('data')
DATA_DIR.mkdir(exist_ok=True)

HIST_TYPES = {
    'computer-history': {
        'name': 'History of Computing',
        'definition': 'The chronological development of mechanical and electronic devices used for automated calculation and data processing.',
        'overview': 'Computing history spans from ancient counting tools to modern quantum processors. It is defined by the transition from mechanical systems to vacuum tubes, then transistors, integrated circuits, and finally microprocessors.',
        'history': "Early milestones include the Abacus, Babbage's Analytical Engine, and the ENIAC (1945). The invention of the transistor at Bell Labs in 1947 is the single most important event, leading to the Silicon Age.",
        'architecture': 'Evolved from fixed-function mechanical gears to Von Neumann stored-program architecture, which remains the standard for modern digital computers.',
        'working_principle': 'The shift from decimal/analog logic to binary (0 and 1) logic allowed for the creation of stable, programmable electronic systems.',
        'applications': ['Military ballistic calculations (Early)', 'Business automation', 'Global telecommunications', 'Scientific discovery'],
        'manufacturing': 'Started with hand-soldered vacuum tubes, moving to automated photolithography on silicon wafers.',
        'benchmarks': ['FLOPS (Floating Point Operations Per Second)', 'Instruction throughput'],
        'future_research': 'DNA computing, light-based (photonic) computing, and bio-electronic integration.',
        'references': [
            {'text': 'Computer History Museum', 'url': 'https://computerhistory.org/'},
            {'text': 'The Silicon Engine (CHM)', 'url': 'https://www.computerhistory.org/siliconengine/'}
        ],
        'subpages': [
            {'title': 'The Five Generations of Computers', 'slug': 'computer-generations.html'},
            {'title': 'Alan Turing & Foundational Logic', 'slug': 'turing-logic.html'}
        ]
    },
    'computer-types': {
        'name': 'Types of Computers',
        'definition': 'The classification of computing systems based on their size, power, and intended purpose.',
        'overview': 'Computers are not just PCs. They range from tiny microcontrollers in appliances to massive supercomputers that occupy entire buildings and perform trillions of calculations per second.',
        'history': 'Classification emerged as computers specialized for different tasks—mainframe for big data, workstations for engineering, and personal computers for individuals.',
        'architecture': 'Varies greatly: Supercomputers use massively parallel clusters; Mainframes use high-reliability redundant logic; Microcontrollers use ultra-low-power integrated designs.',
        'working_principle': 'All use basic logic gates but differ in throughput, parallelization, and fault tolerance requirements.',
        'applications': ['Weather forecasting (Supercomputer)', 'Banking transactions (Mainframe)', 'Smart home devices (Microcontroller)'],
        'manufacturing': 'Optimized for scale (Mobile/IoT) or absolute performance (HPC/Server).',
        'benchmarks': ['TOP500 List (Supercomputers)', 'SPECint'],
        'future_research': 'Edge computing architectures and sustainable, low-energy supercomputing.',
        'references': [
            {'text': 'TOP500 Supercomputer Sites', 'url': 'https://www.top500.org/'},
            {'text': 'Embedded Systems Overview', 'url': 'https://en.wikipedia.org/wiki/Embedded_system'}
        ],
        'subpages': [
            {'title': 'Supercomputer Architectures', 'slug': 'supercomputing.html'},
            {'title': 'The Rise of IoT Devices', 'slug': 'iot-types.html'}
        ]
    }
}

def main():
    print("Expanding History and Types data...")
    for slug, data in HIST_TYPES.items():
        json_path = DATA_DIR / f"{slug}.json"
        existing_data = {}
        if json_path.exists():
            try:
                with open(json_path, 'r', encoding='utf-8') as f:
                    existing_data = json.load(f)
            except Exception: pass
        merged_data = {**existing_data, **data}
        if 'media' not in merged_data:
            merged_data['media'] = {'images': [], 'videos': [], 'audio': []}
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(merged_data, f, indent=2)
        print(f"Updated {json_path}")

if __name__ == '__main__':
    main()
