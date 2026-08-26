import urllib.request
import urllib.parse

SITEMAP_URL = 'https://jordanricky1604-ship-it.github.io/awesome-cybersecurity-datasets/sitemap.xml'
PING_URL = 'https://www.google.com/ping?sitemap=' + urllib.parse.quote(SITEMAP_URL)

try:
    print(f"Pinging Google with sitemap: {SITEMAP_URL}")
    req = urllib.request.Request(PING_URL, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    if response.status == 200:
        print("Successfully submitted sitemap to Google!")
    else:
        print(f"Failed to submit. HTTP Status: {response.status}")
except Exception as e:
    print(f"Error pinging sitemap: {e}")
