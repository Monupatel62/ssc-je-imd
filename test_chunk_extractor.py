import re
from bs4 import BeautifulSoup
import html as html_module
import sys

sys.stdout.reconfigure(encoding='utf-8')

def parse_html_questions(file_path, paper_title):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by QID pattern
    # Looking for: QID\s*:\s*(\d+)
    matches = list(re.finditer(r'QID\s*:\s*(\d+)', content, re.IGNORECASE))
    print(f"[{paper_title}] Found {len(matches)} QIDs in {file_path}")
    
    questions = []
    for i, m in enumerate(matches):
        qid = m.group(1)
        start_pos = m.start()
        end_pos = matches[i+1].start() if i+1 < len(matches) else len(content)
        chunk = content[start_pos:end_pos]
        
        # In case there are footer/ad blocks at the end of the last question
        if i == len(matches) - 1:
            for footer_marker in ['<div id="block-', '<ul class="links inline"', '<!-- added -->', '<footer']:
                f_pos = chunk.find(footer_marker)
                if f_pos != -1:
                    chunk = chunk[:f_pos]
        
        # Clean html tags using BeautifulSoup
        soup = BeautifulSoup(chunk, 'html.parser')
        text = soup.get_text()
        
        # Normalize whitespace and newlines
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        full_text = "\n".join(lines)
        
        questions.append({
            'qid': qid,
            'paper': paper_title,
            'raw_text': full_text,
            'chunk': chunk
        })
    return questions

# Test parsing on each file
p1 = parse_html_questions('e:/ssc/RAW_HTML/CS_22Nov2017_Shift1.html', 'SSC IMD 22 Nov 2017 Shift 1 (CS)')
p2 = parse_html_questions('e:/ssc/RAW_HTML/CS_23Nov2017_Shift1.html', 'SSC IMD 23 Nov 2017 Shift 1 (CS)')
p3 = parse_html_questions('e:/ssc/RAW_HTML/CS_23Nov2017_Shift2.html', 'SSC IMD 23 Nov 2017 Shift 2 (CS)')
p4_en = parse_html_questions('e:/ssc/RAW_HTML/CS_24Nov2017_Shift2_en.html', 'SSC IMD 24 Nov 2017 Shift 2 (CS) [EN]')
p4_hi = parse_html_questions('e:/ssc/RAW_HTML/CS_24Nov2017_Shift2_hi.html', 'SSC IMD 24 Nov 2017 Shift 2 (CS) [HI]')
p5 = parse_html_questions('e:/ssc/RAW_HTML/CS_25Nov2017_Shift2.html', 'SSC IMD 25 Nov 2017 Shift 2 (CS)')

print(f"Total parsed CS question objects: {len(p1) + len(p2) + len(p3) + len(p4_en) + len(p5)}")
