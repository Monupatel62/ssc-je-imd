import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = 'https://sscportal.in/hindi/scientific-assistant/papers/22-nov-2017-shift-1-computer-science'
headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=15) as r:
    html = r.read().decode('utf-8', errors='ignore')
    print('Length:', len(html))
    pos = html.find('QID')
    if pos != -1:
        print('Snippet around QID:')
        print(html[pos:pos+500])
    else:
        print('No QID found')
