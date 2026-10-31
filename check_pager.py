import urllib.request
from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = 'https://sscportal.in/scientific-assistant/papers/24-nov-2017-shift-2-computer-science'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=15) as r:
    html = r.read().decode('utf-8', errors='ignore')
    soup = BeautifulSoup(html, 'html.parser')
    pager = soup.find('ul', {'class': 'pager'}) or soup.find(class_=re.compile(r'page|pagination|pager'))
    if pager:
        print('Pager links:')
        for a in pager.find_all('a'):
            print(a.get('href'), a.get_text().strip())
    else:
        print('No pager found')
