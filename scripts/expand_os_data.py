import os
import json
from pathlib import Path

DATA_DIR = Path('data')
DATA_DIR.mkdir(exist_ok=True)

OS_COMPONENTS = {
    'windows': {
        'name': 'Microsoft Windows',
        'definition': 'A group of several proprietary graphical operating system families developed and marketed by Microsoft.',
        'overview': 'Windows is the most widely used desktop operating system globally. It provides a user-friendly interface, vast software compatibility, and support for a huge range of hardware peripherals.',
        'history': 'Launched in 1985 as a GUI for MS-DOS. Windows NT (1993) introduced the modern 32-bit/64-bit architecture. Key versions include Windows 95, XP, 7 (beloved for stability), 10 (universal OS), and 11 (modern overhaul). Note: Windows 9 was skipped to avoid confusion with Windows 95/98 legacy code checks.',
        'architecture': 'Hybrid Kernel (Windows NT). Uses subsystems (Win32, POSIX, OS/2 historically) and a Hardware Abstraction Layer (HAL). It employs the NTFS file system and the Windows Registry for system-wide configuration.',
        'working_principle': 'Interrupt-driven architecture. The executive layer handles memory management, process management, and I/O. The user-mode environment facilitates application execution via APIs.',
        'applications': ['PC Gaming (DirectX)', 'Enterprise Infrastructure (Active Directory)', 'Creative Workstations', 'General Consumer Computing'],
        'manufacturing': 'Proprietary source code maintained by Microsoft. Developed using C, C++, and C#.',
        'benchmarks': ['PCMark 10', 'Cinebench', 'UserBenchmark OS Latency'],
        'future_research': 'Cloud-integrated OS (Windows 365), AI-first shell (Copilot), and transition to ARM-based high-performance computing.',
        'references': [
            {'text': 'Windows Internals Documentation', 'url': 'https://learn.microsoft.com/en-us/sysinternals/resources/windows-internals'},
            {'text': 'Microsoft History Museum', 'url': 'https://www.microsoft.com/en-us/museum'}
        ],
        'subpages': [
            {'title': 'Windows 7, 10, 11 Comparison', 'slug': 'windows-versions.html'},
            {'title': 'Windows NT Kernel Deep Dive', 'slug': 'windows-nt-architecture.html'}
        ]
    },
    'linux': {
        'name': 'Linux Operating System',
        'definition': 'An open-source, Unix-like operating system kernel created by Linus Torvalds.',
        'overview': 'Linux is the backbone of the internet, powering millions of servers, supercomputers, and embedded devices. It is known for its stability, security, and the concept of "Distributions" (Distros) which package the kernel with different software.',
        'history': 'Linus Torvalds released the first kernel in 1991. It combined with the GNU project tools to create a functional free OS. Today, it has thousands of variants catering to different needs.',
        'architecture': 'Monolithic Kernel. Highly modular, allowing drivers to be loaded/unloaded at runtime. Everything is treated as a file. Uses the root user model for security.',
        'working_principle': 'The kernel manages hardware resources. System calls provide the interface for user-space applications (like the shell or desktop environment) to interact with hardware.',
        'applications': ['Web Servers (Apache/Nginx)', 'Cybersecurity (Kali Linux)', 'Software Development', 'Scientific Computing (Supercomputers)', 'IoT Devices'],
        'manufacturing': 'Open-source development managed via Git. Maintained by the Linux Foundation and a global community of volunteers and companies.',
        'benchmarks': ['Phoronix Test Suite', 'UnixBench', 'Sysbench'],
        'future_research': 'Real-time kernel improvements, Rust integration for memory safety, and eBPF for advanced networking/observability.',
        'references': [
            {'text': 'The Linux Foundation', 'url': 'https://www.linuxfoundation.org/'},
            {'text': 'Kernel.org', 'url': 'https://www.kernel.org/'}
        ],
        'subpages': [
            {'title': 'Top 15 Linux Distributions', 'slug': 'linux-distros.html'},
            {'title': 'Linux Kernel Architecture', 'slug': 'linux-kernel.html'}
        ]
    },
    'macos': {
        'name': 'macOS',
        'definition': 'A Unix-based operating system developed and marketed by Apple Inc. since 2001.',
        'overview': 'macOS is designed specifically for Apple hardware (Macintosh). It is famous for its elegant user interface (Aqua), tight integration with the Apple ecosystem, and high performance for creative professionals.',
        'history': 'Evolved from NeXTSTEP and the classic Mac OS. Shifted from PowerPC to Intel in 2006, and recently to Apple Silicon (M1/M2/M3) in 2020, significantly boosting efficiency.',
        'architecture': 'XNU Kernel (Hybrid). Combines the Mach microkernel and components from FreeBSD. Uses the APFS file system and Metal API for graphics acceleration.',
        'working_principle': 'Built on a Unix foundation (Darwin). Uses the Cocoa framework for applications. Employs "Rosetta 2" to translate Intel apps for Apple Silicon hardware.',
        'applications': ['Graphic Design', 'Video Editing (Final Cut Pro)', 'Software Development (Xcode)', 'Music Production (Logic Pro)'],
        'manufacturing': 'Proprietary development by Apple Inc. High vertical integration between software and hardware.',
        'benchmarks': ['Geekbench 6', 'Speedometer 3.0', 'Final Cut Render Times'],
        'future_research': 'Deeper AI integration (Apple Intelligence), unified architecture with iPadOS/iOS, and advanced neural engine utilization.',
        'references': [
            {'text': 'Apple Developer Documentation', 'url': 'https://developer.apple.com/documentation/'},
            {'text': 'macOS History on Wikipedia', 'url': 'https://en.wikipedia.org/wiki/MacOS'}
        ],
        'subpages': [
            {'title': 'macOS Hardware Integration', 'slug': 'macos-hardware.html'},
            {'title': 'Darwin Kernel Explained', 'slug': 'macos-darwin.html'}
        ]
    },
    'android': {
        'name': 'Android OS',
        'definition': 'A mobile operating system based on a modified version of the Linux kernel and other open-source software.',
        'overview': "Android is the world's most popular mobile OS. It is open-source (AOSP) and highly customizable, used by manufacturers like Samsung, Google, and Xiaomi.",
        'history': 'Developed by Android Inc. and bought by Google in 2005. The first commercial device was the T-Mobile G1 (2008). It has evolved from simple smartphone use to tablets, TVs, and cars.',
        'architecture': 'Layered architecture: Linux Kernel at the bottom, followed by Hardware Abstraction Layer (HAL), Android Runtime (ART/Dalvik), Native C++ libraries, and the Java/Kotlin Application Framework.',
        'working_principle': 'Uses a sandboxed environment for apps. Each app runs in its own process with a unique user ID. Uses Intents for inter-process communication.',
        'applications': ['Smartphones', 'Tablets', 'Android Auto', 'Wearables (Wear OS)', 'Smart TVs'],
        'manufacturing': 'Managed by Google via the Open Handset Alliance. Source code released as Android Open Source Project (AOSP).',
        'benchmarks': ['AnTuTu', 'Geekbench (Mobile)', 'GFXBench'],
        'future_research': 'Project Mainline for modular updates, improved privacy sandboxing, and Foldable/Multi-screen optimization.',
        'references': [
            {'text': 'Android Open Source Project', 'url': 'https://source.android.com/'},
            {'text': 'Android Developer Portal', 'url': 'https://developer.android.com/'}
        ],
        'subpages': [
            {'title': 'Android Architecture Layers', 'slug': 'android-architecture.html'},
            {'title': 'History of Android Versions', 'slug': 'android-history.html'}
        ]
    },
    'ios': {
        'name': 'iOS',
        'definition': 'A mobile operating system created and developed by Apple Inc. exclusively for its hardware.',
        'overview': 'iOS is known for its smooth performance, strict security model, and seamless integration with other Apple devices. It powers the iPhone and serves as the basis for iPadOS.',
        'history': 'Unveiled with the original iPhone in 2007. Originally called "iPhone OS", it shared much of its foundation with macOS. It revolutionized mobile computing with the App Store in 2008.',
        'architecture': 'Derived from the Darwin (Unix) foundation of macOS. Layers include Core OS, Core Services, Media Layer, and Cocoa Touch.',
        'working_principle': 'Highly optimized for specific Apple hardware. Uses strict app sandboxing and code signing. Managed by the XNU kernel with high energy efficiency.',
        'applications': ['iPhone', 'iPad (via iPadOS variant)', 'Apple TV (via tvOS variant)'],
        'manufacturing': 'Proprietary development by Apple Inc. tightly coupled with custom SoC (System on a Chip) designs.',
        'benchmarks': ['Geekbench (iOS)', 'JetStream 2', '3DMark Mobile'],
        'future_research': 'Apple Intelligence integration, advanced biometric security (FaceID evolutions), and satellite-based communication systems.',
        'references': [
            {'text': 'Apple iOS Security Guide', 'url': 'https://support.apple.com/guide/security/welcome/web'},
            {'text': 'iOS Developer Center', 'url': 'https://developer.apple.com/ios/'}
        ],
        'subpages': [
            {'title': 'iOS Security Architecture', 'slug': 'ios-security.html'},
            {'title': 'App Store Ecosystem', 'slug': 'ios-appstore.html'}
        ]
    }
}

def main():
    print("Expanding OS data in JSON files...")
    for slug, data in OS_COMPONENTS.items():
        json_path = DATA_DIR / f"{slug}.json"
        
        existing_data = {}
        if json_path.exists():
            try:
                with open(json_path, 'r', encoding='utf-8') as f:
                    existing_data = json.load(f)
            except Exception:
                pass
                
        # Merge
        merged_data = {**existing_data, **data}
        
        if 'media' not in merged_data:
            merged_data['media'] = {'images': [], 'videos': [], 'audio': []}
            
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(merged_data, f, indent=2)
            
        print(f"Updated {json_path}")
        
if __name__ == '__main__':
    main()
