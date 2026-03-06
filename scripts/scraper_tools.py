#!/usr/bin/env python3
"""
CPU Encyclopedia — Web Scraper Tools
Collects CPU specifications from multiple trusted sources.

Sources:
  - TechPowerUp CPU Database (most scraper-friendly)
  - CPU-World (fallback)
  - Intel ARK & AMD Specs (JS-rendered, may need Selenium — manual fallback included)

Output: public/data/cpu_database.json

Usage:
  python scripts/scraper_tools.py               # Scrape all sources
  python scripts/scraper_tools.py --source tpu   # Scrape TechPowerUp only
  python scripts/scraper_tools.py --manual        # Enter data manually
"""

import json
import time
import argparse
import os
from pathlib import Path

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("⚠️  Missing dependencies. Install with:")
    print("    pip install requests beautifulsoup4")
    print("    pip install pandas  # optional, for CSV export")
    exit(1)

# --- Config ---
OUTPUT_PATH = Path(__file__).parent.parent / "public" / "data" / "cpu_database.json"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
RATE_LIMIT = 2  # seconds between requests


def load_existing():
    """Load existing CPU database if it exists."""
    if OUTPUT_PATH.exists():
        with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_database(data):
    """Save CPU database to JSON file."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✅ Saved {len(data)} CPUs to {OUTPUT_PATH}")


def scrape_techpowerup():
    """
    Scrape TechPowerUp CPU Database.
    URL: https://www.techpowerup.com/cpu-specs/
    """
    print("\n🔍 Scraping TechPowerUp CPU Database...")
    cpus = []
    base_url = "https://www.techpowerup.com/cpu-specs/"

    try:
        resp = requests.get(base_url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        # TechPowerUp lists CPUs in a table
        table = soup.find("table", class_="cputable")
        if not table:
            print("  ⚠️  Could not find CPU table. Page structure may have changed.")
            return cpus

        rows = table.find_all("tr")[1:]  # Skip header
        for row in rows[:100]:  # Limit to first 100 for safety
            cols = row.find_all("td")
            if len(cols) < 7:
                continue

            try:
                name = cols[0].get_text(strip=True)
                manufacturer = "Intel" if "intel" in name.lower() else "AMD" if "amd" in name.lower() else "Unknown"

                cpu_entry = {
                    "name": name,
                    "manufacturer": manufacturer,
                    "codename": cols[1].get_text(strip=True) if len(cols) > 1 else "",
                    "cores": cols[2].get_text(strip=True) if len(cols) > 2 else "",
                    "clock_base": cols[3].get_text(strip=True) if len(cols) > 3 else "",
                    "clock_boost": cols[4].get_text(strip=True) if len(cols) > 4 else "",
                    "tdp": cols[5].get_text(strip=True) if len(cols) > 5 else "",
                    "process": cols[6].get_text(strip=True) if len(cols) > 6 else "",
                    "source": "TechPowerUp"
                }
                cpus.append(cpu_entry)
            except Exception as e:
                continue

        print(f"  ✅ Found {len(cpus)} CPUs from TechPowerUp")

    except requests.RequestException as e:
        print(f"  ❌ Network error: {e}")

    return cpus


def scrape_cpuworld():
    """
    Scrape CPU-World database.
    URL: https://www.cpu-world.com/
    Note: CPU-World is well-structured but may block scrapers.
    """
    print("\n🔍 Scraping CPU-World...")
    cpus = []

    urls = [
        "https://www.cpu-world.com/CPUs/Core_i9/",
        "https://www.cpu-world.com/CPUs/Core_i7/",
        "https://www.cpu-world.com/CPUs/Ryzen_9/",
        "https://www.cpu-world.com/CPUs/Ryzen_7/",
    ]

    for url in urls:
        try:
            time.sleep(RATE_LIMIT)
            resp = requests.get(url, headers=HEADERS, timeout=15)
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, "html.parser")

            # Try to find spec tables
            tables = soup.find_all("table", class_="table")
            for table in tables:
                rows = table.find_all("tr")[1:]
                for row in rows[:25]:
                    cols = row.find_all("td")
                    if len(cols) >= 3:
                        cpus.append({
                            "name": cols[0].get_text(strip=True),
                            "source": "CPU-World"
                        })

            print(f"  ✅ Found {len(cpus)} entries from {url.split('/')[-2]}")
        except Exception as e:
            print(f"  ⚠️  Error on {url}: {e}")

    return cpus


def manual_entry():
    """Interactive manual CPU data entry."""
    print("\n📝 Manual CPU Entry Mode")
    print("Enter CPU specs (type 'done' to finish):\n")

    cpus = []
    while True:
        name = input("CPU Name (or 'done'): ").strip()
        if name.lower() == 'done':
            break

        cpu = {
            "name": name,
            "manufacturer": input("  Manufacturer (Intel/AMD/Apple/Qualcomm): ").strip(),
            "architecture": input("  Architecture (e.g., Zen 4, Golden Cove): ").strip(),
            "cores": input("  Core Count: ").strip(),
            "threads": input("  Thread Count: ").strip(),
            "clock_base": input("  Base Clock (GHz): ").strip(),
            "clock_boost": input("  Boost Clock (GHz): ").strip(),
            "cache_l1": input("  L1 Cache: ").strip(),
            "cache_l2": input("  L2 Cache: ").strip(),
            "cache_l3": input("  L3 Cache: ").strip(),
            "tdp": input("  TDP (W): ").strip(),
            "process": input("  Process Node (nm): ").strip(),
            "year": input("  Release Year: ").strip(),
            "source": "Manual"
        }
        cpus.append(cpu)
        print(f"  ✅ Added {name}\n")

    return cpus


def merge_databases(existing, new_entries):
    """Merge new entries into existing database, avoiding duplicates."""
    existing_names = {cpu.get("name", "").lower() for cpu in existing}
    added = 0
    for entry in new_entries:
        if entry.get("name", "").lower() not in existing_names:
            existing.append(entry)
            existing_names.add(entry["name"].lower())
            added += 1
    print(f"  ℹ️  Added {added} new entries ({len(new_entries) - added} duplicates skipped)")
    return existing


def main():
    parser = argparse.ArgumentParser(description="CPU Encyclopedia Scraper")
    parser.add_argument("--source", choices=["tpu", "cpuworld", "all"], default="all",
                       help="Data source to scrape")
    parser.add_argument("--manual", action="store_true", help="Manual data entry mode")
    parser.add_argument("--output", type=str, help="Custom output path")
    args = parser.parse_args()

    global OUTPUT_PATH
    if args.output:
        OUTPUT_PATH = Path(args.output)

    existing = load_existing()
    print(f"📦 Existing database: {len(existing)} CPUs")

    if args.manual:
        new = manual_entry()
    else:
        new = []
        if args.source in ["tpu", "all"]:
            new.extend(scrape_techpowerup())
        if args.source in ["cpuworld", "all"]:
            new.extend(scrape_cpuworld())

    if new:
        merged = merge_databases(existing, new)
        save_database(merged)
    else:
        print("\n⚠️  No new data collected.")
        if not existing:
            print("   Tip: Run with --manual to enter data by hand.")


if __name__ == "__main__":
    main()
