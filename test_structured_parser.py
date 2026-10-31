import re
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

def parse_question_chunk(chunk, qid, paper_name):
    # Parse HTML
    soup = BeautifulSoup(chunk, 'html.parser')
    
    # Extract clean lines
    text = soup.get_text()
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    
    # We want:
    # 1. Question text: between 'QID : <qid> -' and 'Options:' or '1)'
    # 2. Options: 1), 2), 3), 4)
    # 3. Correct Answer: after 'Correct Answer:'
    
    joined = "\n".join(lines)
    
    # Find Correct Answer
    ans_match = re.search(r'Correct\s*Answer\s*[:\-]?\s*(.*)', joined, re.IGNORECASE)
    correct_ans = ans_match.group(1).strip() if ans_match else ""
    
    # Remove Correct Answer part from joined text to parse question & options
    before_ans = joined[:ans_match.start()] if ans_match else joined
    
    # Question text is after 'QID : <qid> - '
    q_start_match = re.search(r'QID\s*:\s*' + re.escape(qid) + r'\s*[-:]?\s*', before_ans, re.IGNORECASE)
    after_qid = before_ans[q_start_match.end():] if q_start_match else before_ans
    
    # Options usually start with '1)' or 'Options:\n1)'
    # Find where '1)' starts
    opt1_match = re.search(r'(?:Options\s*:?\s*)?(\n|^)\s*1\s*[\)\.]', after_qid, re.IGNORECASE)
    if opt1_match:
        q_text = after_qid[:opt1_match.start()].strip()
        opts_text = after_qid[opt1_match.start():].strip()
    else:
        q_text = after_qid.strip()
        opts_text = ""
        
    # Extract individual options 1), 2), 3), 4)
    opt_matches = list(re.finditer(r'(?:^|\n)\s*([1-4])\s*[\)\.]\s*(.*?)(?=(?:(?:^|\n)\s*[1-4]\s*[\)\.]|$))', opts_text, re.DOTALL))
    options = {}
    for om in opt_matches:
        opt_num = om.group(1)
        opt_val = om.group(2).strip().replace('\n', ' ')
        options[opt_num] = opt_val
        
    return {
        'qid': qid,
        'paper': paper_name,
        'question': q_text.replace('\n', ' '),
        'options': options,
        'correct_answer': correct_ans,
        'raw': joined
    }

# Test on 5 questions from each paper
from test_chunk_extractor import parse_html_questions

for pfile, pname in [
    ('e:/ssc/RAW_HTML/CS_22Nov2017_Shift1.html', '22 Nov Shift-1'),
    ('e:/ssc/RAW_HTML/CS_23Nov2017_Shift2.html', '23 Nov Shift-2'),
    ('e:/ssc/RAW_HTML/CS_24Nov2017_Shift2_en.html', '24 Nov Shift-2 EN'),
    ('e:/ssc/RAW_HTML/CS_25Nov2017_Shift2.html', '25 Nov Shift-2'),
]:
    qs = parse_html_questions(pfile, pname)
    print(f"\n--- Checking {pname} ---")
    for q in qs[:3]:
        parsed = parse_question_chunk(q['chunk'], q['qid'], pname)
        print(f"QID: {parsed['qid']}")
        print(f"  Q: {parsed['question'][:80]}...")
        print(f"  Options count: {len(parsed['options'])} -> {list(parsed['options'].keys())}")
        print(f"  Ans: {parsed['correct_answer']}")
