import os
import re
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_dir = 'e:/ssc/RAW_HTML'
for fname in sorted(os.listdir(html_dir)):
    if not fname.endswith('.html'): continue
    path = os.path.join(html_dir, fname)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    qids = re.findall(r'QID\s*:\s*(\d+)', html)
    print(f"{fname:30s}: {len(qids):3d} questions (range {qids[0] if qids else 'none'} to {qids[-1] if qids else 'none'})")
