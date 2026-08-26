import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

KEY_FILE = '../malware-families-catalog/gsc-key.json'
SCOPES = ['https://www.googleapis.com/auth/webmasters']
SITE_URL = 'https://jordanricky1604-ship-it.github.io/'
SITEMAP_URL = 'https://jordanricky1604-ship-it.github.io/awesome-cybersecurity-datasets/sitemap.xml'

def main():
    try:
        credentials = service_account.Credentials.from_service_account_file(
            KEY_FILE, scopes=SCOPES)
        service = build('searchconsole', 'v1', credentials=credentials)
        
        print(f"Submitting sitemap: {SITEMAP_URL} via Search Console API...")
        service.sitemaps().submit(siteUrl=SITE_URL, feedpath=SITEMAP_URL).execute()
        print("Successfully submitted sitemap via GSC API!")
        
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == '__main__':
    main()
