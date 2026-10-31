import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

test_urls = [
    'https://sscportal.in/scientific-assistant/papers/22-nov-2017-shift-1-computer-science',
    'https://sscportal.in/scientific-assistant/papers/22-nov-2017-shift-2-computer-science',
    'https://sscportal.in/scientific-assistant/papers/23-nov-2017-shift-1-computer-science',
    'https://sscportal.in/scientific-assistant/papers/23-nov-2017-shift-2-computer-science',
    'https://sscportal.in/scientific-assistant/papers/24-nov-2017-shift-1-computer-science',
    'https://sscportal.in/scientific-assistant/papers/24-nov-2017-shift-2-computer-science',
    'https://sscportal.in/scientific-assistant/papers/25-nov-2017-shift-1-computer-science',
    'https://sscportal.in/scientific-assistant/papers/25-nov-2017-shift-2-computer-science',
    'https://sscportal.in/scientific-assistant/papers/22-nov-2017-shift-1-general-intelligence-and-reasoning',
    'https://sscportal.in/scientific-assistant/papers/22-nov-2017-shift-2-general-intelligence-and-reasoning',
    'https://sscportal.in/scientific-assistant/papers/23-nov-2017-shift-1-general-intelligence-and-reasoning',
    'https://sscportal.in/scientific-assistant/papers/23-nov-2017-shift-2-general-intelligence-and-reasoning',
    'https://sscportal.in/scientific-assistant/papers/24-nov-2017-shift-1-general-intelligence-and-reasoning',
    'https://sscportal.in/scientific-assistant/papers/24-nov-2017-shift-2-general-intelligence-and-reasoning',
    'https://sscportal.in/scientific-assistant/papers/25-nov-2017-shift-1-general-intelligence-and-reasoning',
    'https://sscportal.in/scientific-assistant/papers/25-nov-2017-shift-2-general-intelligence-and-reasoning',
    'https://sscportal.in/scientific-assistant/papers/22-nov-2017-shift-1-general-awareness',
    'https://sscportal.in/scientific-assistant/papers/22-nov-2017-shift-2-general-awareness',
    'https://sscportal.in/scientific-assistant/papers/23-nov-2017-shift-1-general-awareness',
    'https://sscportal.in/scientific-assistant/papers/23-nov-2017-shift-2-general-awareness',
    'https://sscportal.in/scientific-assistant/papers/24-nov-2017-shift-1-general-awareness',
    'https://sscportal.in/scientific-assistant/papers/24-nov-2017-shift-2-general-awareness',
    'https://sscportal.in/scientific-assistant/papers/25-nov-2017-shift-1-general-awareness',
    'https://sscportal.in/scientific-assistant/papers/25-nov-2017-shift-2-general-awareness',
]

headers = {'User-Agent': 'Mozilla/5.0'}

for u in test_urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as r:
            code = r.getcode()
            html = r.read().decode('utf-8', errors='ignore')
            qids = re.findall(r'QID\s*:\s*\d+', html)
            print(f"EXISTS ({len(qids)} Qs): {u}")
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code}: {u}")
    except Exception as e:
        print(f"Error: {e} for {u}")
