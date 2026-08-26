import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

KEY_FILE = '../malware-families-catalog/gsc-key.json'
SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']
SITE_URL = 'https://jordanricky1604-ship-it.github.io/'
INSPECT_URL = 'https://jordanricky1604-ship-it.github.io/awesome-cybersecurity-datasets/'

def main():
    try:
        credentials = service_account.Credentials.from_service_account_file(
            KEY_FILE, scopes=SCOPES)
        service = build('searchconsole', 'v1', credentials=credentials)
        
        # Check Index Coverage (Index Status)
        response = service.urlInspection().index().inspect(body={
            'inspectionUrl': INSPECT_URL,
            'siteUrl': SITE_URL,
            'languageCode': 'en-US'
        }).execute()
        
        res = response.get('inspectionResult', {}).get('indexStatusResult', {})
        verdict = res.get('verdict', 'UNKNOWN')
        cov = res.get('coverageState', 'UNKNOWN')
        
        print(f"Index Status for {INSPECT_URL} (using site property {SITE_URL}):")
        print(f"Verdict: {verdict}")
        print(f"Coverage State: {cov}")
        
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == '__main__':
    main()
