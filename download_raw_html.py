import urllib.request
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

urls = {
    # CS Papers (English)
    'CS_22Nov2017_Shift1': 'https://sscportal.in/scientific-assistant/papers/22-nov-2017-shift-1-computer-science',
    'CS_23Nov2017_Shift1': 'https://sscportal.in/scientific-assistant/papers/23-nov-2017-shift-1-computer-science',
    'CS_23Nov2017_Shift2': 'https://sscportal.in/scientific-assistant/papers/23-nov-2017-shift-2-computer-science',
    'CS_24Nov2017_Shift2_en': 'https://sscportal.in/scientific-assistant/papers/24-nov-2017-shift-2-computer-science',
    'CS_24Nov2017_Shift2_hi': 'https://sscportal.in/hindi/scientific-assistant-papers/computer-science-24-nov-2017-shift2',
    'CS_25Nov2017_Shift2': 'https://sscportal.in/scientific-assistant/papers/25-nov-2017-shift-2-computer-science',
    
    # GIR Papers (Reasoning)
    'GIR_22Nov2017_Shift2': 'https://sscportal.in/scientific-assistant/papers/22-nov-2017-shift-2-general-intelligence-and-reasoning',
    'GIR_23Nov2017_Shift2': 'https://sscportal.in/scientific-assistant/papers/23-nov-2017-shift-2-general-intelligence-and-reasoning',
    'GIR_24Nov2017_Shift2': 'https://sscportal.in/scientific-assistant/papers/24-nov-2017-shift-2-general-intelligence-and-reasoning',
    'GIR_22Nov2017_Shift1': 'https://sscportal.in/hindi/scientific-assistant/papers/22-nov-2017-shift-1-reasoning',
    'GIR_23Nov2017_Shift1': 'https://sscportal.in/hindi/scientific-assistant/papers/23-nov-2017-shift-1-reasoning',
    'GIR_25Nov2017_Shift1': 'https://sscportal.in/hindi/scientific-assistant/papers/25-nov-2017-shift-1-reasoning',

    # GA Papers (General Awareness)
    'GA_22Nov2017_Shift1': 'https://sscportal.in/scientific-assistant/papers/22-nov-2017-shift-1-general-awareness',
    'GA_22Nov2017_Shift2': 'https://sscportal.in/scientific-assistant/papers/22-nov-2017-shift-2-general-awareness',
    'GA_23Nov2017_Shift1': 'https://sscportal.in/scientific-assistant/papers/23-nov-2017-shift-1-general-awareness',
    'GA_23Nov2017_Shift2': 'https://sscportal.in/scientific-assistant/papers/23-nov-2017-shift-2-general-awareness',
    'GA_24Nov2017_Shift2': 'https://sscportal.in/scientific-assistant/papers/24-nov-2017-shift-2-general-awareness',
    'GA_25Nov2017_Shift1': 'https://sscportal.in/scientific-assistant/papers/25-nov-2017-shift-1-general-awareness',
    'GA_25Nov2017_Shift2': 'https://sscportal.in/scientific-assistant/papers/25-nov-2017-shift-2-general-awareness',
}

os.makedirs('e:/ssc/RAW_HTML', exist_ok=True)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

for name, url in urls.items():
    file_path = f'e:/ssc/RAW_HTML/{name}.html'
    if os.path.exists(file_path) and os.path.getsize(file_path) > 1000:
        print(f"Already have {name}")
        continue
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=20) as r:
            content = r.read()
            with open(file_path, 'wb') as f:
                f.write(content)
            print(f"Downloaded {name}: {len(content)} bytes")
    except Exception as e:
        print(f"Failed {name}: {e}")
