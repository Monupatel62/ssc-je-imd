import urllib.request
import re
import sys

url = 'https://sscportal.in/scientific-assistant/papers'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print(f"Fetched {len(html)} bytes from {url}")
        
        # Save html for inspection
        with open('sscportal_papers.html', 'w', encoding='utf-8') as f:
            f.write(html)
            
        links = re.findall(r'href=["\']([^"\']+)["\']', html)
        paper_links = [l for l in links if 'paper' in l.lower() or 'scientific' in l.lower()]
        print(f"Total links: {len(links)}, paper/scientific links: {len(paper_links)}")
        for l in sorted(set(paper_links)):
            print(l)
except Exception as e:
    print("Error:", e)
