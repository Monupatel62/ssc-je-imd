import re
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

def test_parse(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Check text
    text = soup.get_text()
    
    # Let's inspect raw html structure around QID
    matches = list(re.finditer(r'QID\s*:\s*(\d+)', html))
    print(f"File: {filepath} -> Found {len(matches)} QID matches")
    
    if matches:
        first_start = matches[0].start()
        second_start = matches[1].start() if len(matches) > 1 else first_start + 1000
        sample_chunk = html[first_start:second_start]
        print("Sample raw HTML:")
        print(sample_chunk[:400])
        print("---")
        sample_soup = BeautifulSoup(sample_chunk, 'html.parser')
        print("Sample stripped text:")
        print(sample_soup.get_text().strip())

test_parse('e:/ssc/RAW_HTML/CS_22Nov2017_Shift1.html')
print("="*50)
test_parse('e:/ssc/RAW_HTML/CS_23Nov2017_Shift2.html')
