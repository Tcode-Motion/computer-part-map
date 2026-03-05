# CPMap Ingest Tool

Automated asset pipeline for the Computer Parts Map research encyclopedia.

## Setup
1. Install dependencies: `pip install -r tools/requirements.txt`
2. (Optional) Create `keys.json`:
   ```json
   {
     "NASA_API_KEY": "YOUR_KEY",
     "YOUTUBE_API_KEY": "YOUR_KEY"
   }
   ```

## Usage Examples

### 1. Add NASA Research to Existing Page
Fetch 3 images related to transistors for the CPU page:
`python tools/cpmap_ingest.py -c cpu --nasa --nasa-query "transistor" --limit 3`

### 2. Create a New Component Page
Create a new NPU page with Google Scholar links:
`python tools/cpmap_ingest.py --add-page "Neural Processor" -c npu --scholar --query "NPU AI architecture"`

### 3. Full Integration (Dry Run)
`python tools/cpmap_ingest.py -c gpu --nasa --nasa-query "silicon wafer" --youtube --yt-query "how gpus work" --scholar --dry-run`

## Environment Variables
- `NASA_API_KEY`
- `YOUTUBE_API_KEY`
