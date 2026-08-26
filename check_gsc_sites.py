import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

KEY_FILE = '../malware-families-catalog/gsc-key.json'
SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']

def main():
    try:
        credentials = service_account.Credentials.from_service_account_file(
            KEY_FILE, scopes=SCOPES)
        service = build('searchconsole', 'v1', credentials=credentials)
        
        # List all sites
        site_list = service.sites().list().execute()
        sites = site_list.get('siteEntry', [])
        
        print("Sites accessible by this service account:")
        for site in sites:
            print(f"- {site['siteUrl']} (Permission: {site['permissionLevel']})")
            
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == '__main__':
    main()
