# AWS Security Scripts

This folder contains Python scripts to fetch and aggregate security findings from AWS Security Hub and GuardDuty.

## Usage

1. Install dependencies:
   ```bash
   pip install -r ../../requirements.txt
   ```
2. Configure your AWS credentials (via environment variables or AWS CLI).
3. Run the script:
   ```bash
   python fetch_findings.py
   ``` 