import urllib.request
from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

urls = [
    'https://sscportal.in/scientific-assistant/papers/23-nov-2017-shift-2-computer-science',
    'https://sscportal.in/scientific-assistant/papers/24-nov-2017-shift-2-computer-science',
    'https://sscportal.in/scientific-assistant/papers/15-dec-2022-shift-2-IT',
    'https://sscportal.in/scientific-assistant/papers/22-nov-2017-shift-2-general-intelligence-and-reasoning',
    'https://sscportal.in/scientific-assistant/papers/23-nov-2017-shift-2-general-intelligence-and-reasoning',
    'https://sscportal.in/scientific-assistant/papers/24-nov-2017-shift-2-general-intelligence-and-reasoning',
    'https://sscportal.in/scientific-assistant/papers/22-nov-2017-shift-2-general-awareness',
    'https://sscportal.in/scientific-assistant/papers/23-nov-2017-shift-2-general-awareness',
    'https://sscportal.in/scientific-assistant/papers/24-nov-2017-shift-2-general-awareness',
    'https://sscportal.in/hindi/scientific-assistant/papers/22-nov-2017-shift-1-computer-science',
    'https://sscportal.in/hindi/scientific-assistant/papers/23-nov-2017-shift-1-computer-science',
    'https://sscportal.in/hindi/scientific-assistant/papers/25-nov-2017-shift-2-computer-science',
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as r:
            html = r.read().decode('utf-8', errors='ignore')
            qids = re.findall(r'QID\s*:\s*(\d+)', html)
            print(f"{u.split('/')[-1]}: {len(qids)} questions (range: {qids[0] if qids else 'none'} - {qids[-1] if qids else 'none'})")
    except Exception as e:
        print(f"{u.split('/')[-1]}: Error {e}")
