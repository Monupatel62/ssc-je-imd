import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

urls = [
    'https://sscportal.in/hindi/scientific-assistant/papers/22-nov-2017-shift-1-computer-science',
    'https://sscportal.in/scientific-assistant/papers/23-nov-2017-shift-2-computer-science',
    'https://sscportal.in/hindi/scientific-assistant/papers/23-nov-2017-shift-1-computer-science',
    'https://sscportal.in/hindi/scientific-assistant/papers/25-nov-2017-shift-2-computer-science',
]

headers = {'User-Agent': 'Mozilla/5.0'}
for u in urls:
    req = urllib.request.Request(u, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as r:
        html = r.read().decode('utf-8', errors='ignore')
        qids = re.findall(r'QID\s*:\s*\d+.*?(?=Options:)', html, re.DOTALL)
        slug = u.split('/')[-1]
        sample = qids[0][:150].replace('\n', ' ') if qids else 'None'
        print(f"{slug}: {sample}")
