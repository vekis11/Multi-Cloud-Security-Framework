# Azure Security Scripts

This folder contains Python scripts to fetch and aggregate security alerts from Azure Security Center (Defender for Cloud).

## Usage

1. Install dependencies:
   ```bash
   pip install -r ../../requirements.txt
   ```
2. Set your Azure credentials and subscription ID:
   ```bash
   export AZURE_SUBSCRIPTION_ID=your-subscription-id
   az login
   ```
3. Run the script:
   ```bash
   python fetch_findings.py
   ``` 