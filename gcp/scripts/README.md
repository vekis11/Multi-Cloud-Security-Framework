# GCP Security Scripts

This folder contains Python scripts to fetch and aggregate security findings from GCP Security Command Center.

## Usage

1. Install dependencies:
   ```bash
   pip install -r ../../requirements.txt
   ```
2. Set your GCP credentials and environment variables:
   ```bash
   export GCP_PROJECT_ID=your-gcp-project-id
   export GCP_ORG_ID=your-gcp-org-id
   gcloud auth application-default login
   ```
3. Run the script:
   ```bash
   python fetch_findings.py
   ``` 