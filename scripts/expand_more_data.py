import os
import json
from pathlib import Path

DATA_DIR = Path('data')
DATA_DIR.mkdir(exist_ok=True)

MORE_COMPONENTS = {
    'ssd': {
        'name': 'Solid State Drive',
        'definition': 'A solid-state storage device that uses integrated circuit assemblies to store data persistently.',
        'overview': 'SSDs have revolutionized storage by replacing moving magnetic platters with NAND flash memory, offering exponentially faster read/write speeds, lower latency, and greater physical durability.',
        'history': 'Early SSDs using RAM appeared in the 1970s and 1980s, but modern flash-based SSDs gained commercial traction in the late 2000s, rapidly overtaking HDDs as the primary boot drive.',
        'architecture': 'Consists of a controller, NAND flash memory chips (SLC, MLC, TLC, QLC), and often DRAM cache. Interfaces evolved from SATA to high-bandwidth NVMe over PCIe.',
        'working_principle': 'Data is written by applying voltage to floating-gate or charge-trap transistors within memory cells, trapping electrons to represent bits of data.',
        'applications': ['Primary OS boot drive', 'High-performance gaming', 'Enterprise database storage', 'Thin laptops'],
        'manufacturing': 'Involves complex 3D NAND fabrication, stacking memory cell layers vertically (e.g., 176+ layers) to increase density and reduce cost per gigabyte.',
        'benchmarks': ['CrystalDiskMark', 'AS SSD Benchmark', 'ATTO Disk Benchmark'],
        'future_research': 'Future research focuses on PLC (Penta-Level Cell) NAND for higher density, PCIe 5.0/6.0 controller efficiency, and specialized computational storage where processing happens directly on the drive.',
        'references': [
            {'text': 'NVM Express Base Specification', 'url': 'https://nvmexpress.org/'},
            {'text': '3D NAND Flash Memory Architecture', 'url': 'https://en.wikipedia.org/wiki/Flash_memory'}
        ],
        'subpages': [
            {'title': 'SSD Architecture', 'slug': 'ssd-architecture.html'}
        ]
    },
    'operating-systems': {
        'name': 'Operating Systems',
        'definition': 'System software that manages computer hardware, software resources, and provides common services for computer programs.',
        'overview': 'The Operating System (OS) is the most critical software in a computer. It bridges the gap between hardware and user applications, handling memory management, process scheduling, file systems, and hardware abstraction.',
        'history': 'Early computers lacked OSs, requiring manual batch processing. Key milestones include GM-NAA I (1956), Unix (1969), MS-DOS (1981), and Windows 1.0 (1985).',
        'architecture': 'Modern OS architecture centers around the Kernel (Monolithic, Microkernel, or Hybrid). It includes the hardware abstraction layer (HAL), system call interface, and user space applications.',
        'working_principle': 'The OS kernel operates in privileged mode (Ring 0), directly controlling CPU scheduling, memory allocation (paging/segmentation), and hardware interrupts via device drivers.',
        'applications': ['Personal computing', 'Server management', 'Embedded systems', 'Mobile devices'],
        'manufacturing': 'Developed by large engineering teams utilizing languages like C, C++, and increasingly Rust for memory safety. Relies on extensive version control and continuous integration.',
        'benchmarks': ['Phoronix Test Suite', 'UnixBench', 'Sysbench'],
        'future_research': 'Research involves microkernel stability, verified OS kernels (seL4), isolation via unikernels, and AI-driven predictive resource allocation.',
        'references': [
            {'text': 'Operating Systems: Three Easy Pieces', 'url': 'https://pages.cs.wisc.edu/~remzi/OSTEP/'},
            {'text': 'The Linux Kernel Archives', 'url': 'https://www.kernel.org/'}
        ],
        'subpages': [
            {'title': 'OS Kernel Architecture', 'slug': 'os-kernel-architecture.html'}
        ]
    },
    'linux': {
        'name': 'Linux Operating System',
        'definition': 'A family of open-source Unix-like operating systems based on the Linux kernel.',
        'overview': 'Linux dominates the server, supercomputer, and smartphone (Android) markets. Its open-source nature allows for unparalleled customization, security auditing, and lightweight performance.',
        'history': 'Created by Linus Torvalds in 1991 as a free alternative to MINIX. It rapidly gained adoption in enterprise environments and is now maintained by thousands of contributors globally.',
        'architecture': 'Features a monolithic kernel that handles CPU, memory, and IPC. It interfaces with GNU core utilities and various desktop environments (GNOME, KDE) running on display servers (X11, Wayland).',
        'working_principle': 'Everything in Linux is considered a file. It uses POSIX standards for system calls, robust permission models (rwx), and advanced file systems like ext4, Btrfs, and ZFS.',
        'applications': ['Cloud computing infrastructure', 'Web servers', 'Android mobile OS', 'IoT and embedded systems'],
        'manufacturing': 'Developed collaboratively across the globe. Managed via Git (which Torvalds also created) and hosted/reviewed on platforms like the Linux Kernel Mailing List.',
        'benchmarks': ['Phoronix Test Suite', 'Geekbench (Linux)'],
        'future_research': 'Integration of Rust into the kernel for memory safety, eBPF for advanced observability and networking, and real-time kernel preemptions.',
        'references': [
            {'text': 'The Linux Kernel Documentation', 'url': 'https://www.kernel.org/doc/html/latest/'},
            {'text': 'Linux Foundation', 'url': 'https://www.linuxfoundation.org/'}
        ],
        'subpages': [
            {'title': 'Linux Kernel Deep Dive', 'slug': 'linux-kernel.html'}
        ]
    },
    'windows': {
        'name': 'Microsoft Windows',
        'definition': 'A group of several proprietary graphical operating system families developed and marketed by Microsoft.',
        'overview': 'Windows is the dominant OS for personal computers. It offers vast software compatibility, extensive hardware support, and a user-friendly graphical interface.',
        'history': 'Introduced in 1985 as a graphical shell for MS-DOS. The shift to the robust Windows NT kernel with Windows XP (and later Windows 2000, 7, 10, 11) marked its modern era.',
        'architecture': 'Uses a hybrid kernel architecture (Windows NT kernel). It separates user mode (applications, subsystems) from kernel mode (executive, microkernel, HAL, device drivers).',
        'working_principle': 'Employs a heavily API-driven environment (Win32 API). It uses the NTFS file system, the Windows Registry for configuration, and highly complex driver models (WDDM/WDF).',
        'applications': ['PC Gaming', 'Enterprise workstations', 'Creative professional software', 'General consumer use'],
        'manufacturing': 'Developed internally at Microsoft using massive codebases (C, C++, C#). Released via rings (Windows Insider) for telemetry and telemetry-driven stability testing.',
        'benchmarks': ['PCMark 10', 'Cinebench', '3DMark'],
        'future_research': 'Integration of AI directly into the OS shell (Windows Copilot), ARM architecture transition (Windows on ARM), and cloud-streamed OS capabilities (Windows 365).',
        'references': [
            {'text': 'Windows Internals', 'url': 'https://learn.microsoft.com/en-us/sysinternals/'},
            {'text': 'Microsoft Developer Network (MSDN)', 'url': 'https://developer.microsoft.com/'}
        ],
        'subpages': [
            {'title': 'Windows NT Architecture', 'slug': 'windows-nt-architecture.html'}
        ]
    },
    'server-guide': {
        'name': 'Server Hardware & Architecture',
        'definition': 'Computers or systems that provide resources, data, services, or programs to other computers, known as clients, over a network.',
        'overview': 'Servers are the backbone of the internet and enterprise computing. They are engineered for 24/7 reliability, massive I/O throughput, and high-density compute.',
        'history': 'Evolved from massive mainframe computers to rack-mounted x86 servers in the 1990s, and now to ultra-dense blade servers and hyper-converged infrastructure in modern data centers.',
        'architecture': 'Features multi-socket motherboards, ECC (Error-Correcting Code) RAM, redundant power supplies (PSUs), hardware RAID controllers, and baseboard management controllers (BMCs) for out-of-band management.',
        'working_principle': 'Servers run specialized OSs (Linux, Windows Server) to host hypervisors (ESXi, Proxmox) or container engines (Docker, Kubernetes) to maximize hardware utilization across multiple virtual instances.',
        'applications': ['Web hosting', 'Database management', 'Cloud computing (AWS, Azure)', 'High-Performance Computing (HPC)'],
        'manufacturing': 'Built by OEMs like Dell, HPE, and Lenovo, or custom-designed by hyperscalers (Google, Meta) focusing on thermal dynamics and power efficiency at scale.',
        'benchmarks': ['SPECjbb', 'Sysbench', 'VMmark'],
        'future_research': 'Liquid cooling adoption, photonics networking, specialized ASIC/NPU integration for AI workloads, and composable infrastructure via CXL (Compute Express Link).',
        'references': [
            {'text': 'Open Compute Project (OCP)', 'url': 'https://www.opencompute.org/'},
            {'text': 'Data Center Architecture', 'url': 'https://en.wikipedia.org/wiki/Data_center'}
        ],
        'subpages': [
            {'title': 'Server Infrastructure', 'slug': 'server-infrastructure.html'}
        ]
    },
    'optical-drive': {
        'name': 'Optical Drive',
        'definition': 'A computer drive that uses a laser to read from and write to optical discs like CDs, DVDs, and Blu-rays.',
        'overview': 'While now a legacy component for mainstream users, optical drives use precise laser technology to access data encoded as microscopic pits and lands on a polycarbonate disc.',
        'history': 'CD-ROMs revolutionized software distribution in the 1990s, replacing floppy disks. DVDs introduced movie-quality video, followed by Blu-ray for HD and 4K content.',
        'architecture': 'Consists of a spindle motor, a tracking mechanism, and an optical pickup head containing a semiconductor laser diode and photodiode sensor.',
        'working_principle': 'A laser beam is focused onto the spinning disc. Changes in reflection from pits (indentations) and lands (flat areas) are detected by the photodiode and translated into binary data.',
        'applications': ['Archival data backup', 'Legacy software installation', 'High-fidelity audio/video playback (Blu-ray)'],
        'manufacturing': 'Requires high-precision optics and laser diode alignment, manufactured by companies like LG, Pioneer, and Asus.',
        'benchmarks': ['Nero DiscSpeed', 'Opti Drive Control'],
        'future_research': 'Holographic versatile discs (HVD) and 5D optical data storage seeking to store terabytes of data in glass for centuries.',
        'references': [
            {'text': 'Optical Disc Drive Mechanism', 'url': 'https://en.wikipedia.org/wiki/Optical_disc_drive'},
            {'text': 'Blu-ray Disc Association', 'url': 'http://www.blu-raydisc.com/'}
        ],
        'subpages': [
            {'title': 'Optical Laser Technology', 'slug': 'optical-laser.html'}
        ]
    }
}

def main():
    print("Expanding more component data in JSON files...")
    for slug, data in MORE_COMPONENTS.items():
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
