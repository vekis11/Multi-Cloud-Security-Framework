# GCP Terraform Setup

This folder contains Terraform code to enable Security Command Center and logging in GCP.

## Usage

1. Set your GCP credentials (via environment variables or gcloud CLI).
2. Initialize Terraform:
   ```bash
   terraform init
   ```
3. Review and apply the plan:
   ```bash
   terraform plan -var="project=your-gcp-project-id"
   terraform apply -var="project=your-gcp-project-id"
   ``` 