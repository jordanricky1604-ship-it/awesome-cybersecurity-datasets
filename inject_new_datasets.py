import json
import re

new_datasets = [
    {
        "name": "AndroZoo",
        "url": "https://androzoo.uni.lu/",
        "description": "The absolute gold standard for mobile security research. Contains over 20 million Android applications (APKs) sourced from multiple markets, analyzed by dozens of anti-virus products.",
        "category": "Malware",
        "status": "active"
    },
    {
        "name": "IoT-23 Dataset",
        "url": "https://www.stratosphereips.org/datasets-iot23",
        "description": "A massive benchmark consisting of 20 malicious PCAP captures of real IoT malware (like Mirai and Torii) executing on actual IoT hardware, plus 3 benign captures.",
        "category": "Automotive & IoT Security",
        "status": "active"
    },
    {
        "name": "AWID (Aegean WiFi Intrusion Dataset)",
        "url": "http://icsdweb.aegean.gr/awid/",
        "description": "The most comprehensive public dataset specifically dedicated to wireless network intrusions. Contains millions of labeled 802.11 MAC layer frames capturing WEP/WPA cracking, rogue APs, etc.",
        "category": "Network traffic",
        "status": "active"
    },
    {
        "name": "DEF CON CTF Network Traffic",
        "url": "https://www.defcon.org/html/links/dc-torrent.html",
        "description": "Full PCAP network traffic from DEF CON Capture The Flag competitions. Incredible for analyzing zero-day exploits and active red-team vs. blue-team network warfare.",
        "category": "Network traffic",
        "status": "active"
    },
    {
        "name": "The Enron Email Corpus",
        "url": "http://www.cs.cmu.edu/~enron/",
        "description": "The absolute foundation for digital forensics, e-discovery, and insider-threat detection. Contains half a million emails from Enron executives prior to the company's collapse.",
        "category": "Email",
        "status": "active"
    }
]

with open('datasets.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for ds in new_datasets:
    # avoid duplicates
    if not any(d['name'] == ds['name'] for d in data):
        data.append(ds)

with open('datasets.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

# Now update README.md
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

def inject_in_category(readme, category_header, entry):
    # Find the category header
    pattern = r"(### " + re.escape(category_header) + r"\n)"
    replacement = r"\g<1>" + entry + "\n"
    new_readme = re.sub(pattern, replacement, readme, count=1)
    return new_readme

readme = inject_in_category(readme, "Malware", "- [AndroZoo](https://androzoo.uni.lu/) - The absolute gold standard for mobile security research. Contains over 20 million Android applications (APKs) sourced from multiple markets, analyzed by dozens of anti-virus products.")
readme = inject_in_category(readme, "Automotive & IoT Security", "- [IoT-23 Dataset](https://www.stratosphereips.org/datasets-iot23) - A massive benchmark consisting of 20 malicious PCAP captures of real IoT malware (like Mirai and Torii) executing on actual IoT hardware, plus 3 benign captures.")
readme = inject_in_category(readme, "Network traffic", "- [AWID (Aegean WiFi Intrusion Dataset)](http://icsdweb.aegean.gr/awid/) - The most comprehensive public dataset specifically dedicated to wireless network intrusions. Contains millions of labeled 802.11 MAC layer frames capturing WEP/WPA cracking, rogue APs, etc.")
readme = inject_in_category(readme, "Network traffic", "- [DEF CON CTF Network Traffic](https://www.defcon.org/html/links/dc-torrent.html) - Full PCAP network traffic from DEF CON Capture The Flag competitions. Incredible for analyzing zero-day exploits and active red-team vs. blue-team network warfare.")
readme = inject_in_category(readme, "Email", "- [The Enron Email Corpus](http://www.cs.cmu.edu/~enron/) - The absolute foundation for digital forensics, e-discovery, and insider-threat detection. Contains half a million emails from Enron executives prior to the company's collapse.")

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

print('Injection complete.')
