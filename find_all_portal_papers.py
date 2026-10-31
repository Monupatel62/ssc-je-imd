import urllib.request
from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Search for all links on sscportal.in/scientific-assistant/papers and related pages
urls_to_crawl = [
    'https://sscportal.in/scientific-assistant/papers',
    'https://sscportal.in/hindi/scientific-assistant-papers',
    'https://sscportal.in/hindi/scientific-assistant/papers',
    'https://sscportal.in/scientific-assistant',
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
discovered = set()

for u in urls_to_crawl:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as r:
            html = r.read().decode('utf-8', errors='ignore')
            links = re.findall(r'href=["\']([^"\']+)["\']', html)
            for link in links:
                if 'scientific-assistant' in link.lower() and ('paper' in link.lower() or 'shift' in link.lower()):
                    if link.startswith('/'):
                        link = 'https://sscportal.in' + link
                    discovered.add(link)
    except Exception as e:
        print(f"Error crawling {u}: {e}")

print(f"Total discovered candidate links: {len(discovered)}")
for link in sorted(discovered):
    print(link)
