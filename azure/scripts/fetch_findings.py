import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.security import SecurityCenter

subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")

if not subscription_id:
    raise Exception(
        "Please set the AZURE_SUBSCRIPTION_ID environment variable."
    )

credential = DefaultAzureCredential()
client = SecurityCenter(credential, subscription_id)

print("Fetching security alerts from Azure Security Center...")
alerts = client.alerts.list()
for alert in alerts:
    print(
        f"Alert: {alert.name} | State: {alert.state} | "
        f"Severity: {alert.severity}"
    ) 
