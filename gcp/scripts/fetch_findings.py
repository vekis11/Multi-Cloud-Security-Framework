import os
from google.cloud import securitycenter

project_id = os.environ.get("GCP_PROJECT_ID")
if not project_id:
    raise Exception("Please set the GCP_PROJECT_ID environment variable.")

client = securitycenter.SecurityCenterClient()
org_id = os.environ.get("GCP_ORG_ID")
if not org_id:
    raise Exception("Please set the GCP_ORG_ID environment variable.")

source_name = f"organizations/{org_id}/sources/-"
print(f"Fetching findings from: {source_name}")

findings = client.list_findings(request={"parent": source_name})
for finding in findings:
    print(f"Finding: {finding.finding.name} | State: {finding.finding.state} | Severity: {finding.finding.severity}") 