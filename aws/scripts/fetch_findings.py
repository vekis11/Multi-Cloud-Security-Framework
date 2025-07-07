import boto3
import json


def fetch_security_hub_findings():
    client = boto3.client('securityhub')
    response = client.get_findings(MaxResults=50)
    return response['Findings']


def fetch_guardduty_findings(detector_id):
    client = boto3.client('guardduty')
    findings = client.list_findings(DetectorId=detector_id, MaxResults=50)
    if findings['FindingIds']:
        details = client.get_findings(
            DetectorId=detector_id, FindingIds=findings['FindingIds']
        )
        return details['Findings']
    return []


def main():
    print("Fetching Security Hub findings...")
    sh_findings = fetch_security_hub_findings()
    print(json.dumps(sh_findings, indent=2))

    print("Fetching GuardDuty findings...")
    gd_client = boto3.client('guardduty')
    detectors = gd_client.list_detectors()['DetectorIds']
    for detector_id in detectors:
        gd_findings = fetch_guardduty_findings(detector_id)
        print(json.dumps(gd_findings, indent=2))


if __name__ == "__main__":
    main()
