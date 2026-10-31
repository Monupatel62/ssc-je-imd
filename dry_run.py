import os
import re
import sys
from bs4 import BeautifulSoup
from test_structured_parser import parse_question_chunk
from test_classifier_v3 import classify_question_v3

sys.stdout.reconfigure(encoding='utf-8')

def get_existing_question_texts(folder_path):
    q_file = os.path.join(folder_path, 'questions.md')
    if not os.path.exists(q_file):
        return set(), 0
    with open(q_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract existing question texts (normalized)
    # Questions usually appear after **Question:** or in ### Q...
    q_blocks = re.findall(r'\*\*Question:\*\*\s*(.*?)(?=\*\*Options:\*\*|\n\d+\)|$)', content, re.DOTALL)
    existing_texts = set()
    for qb in q_blocks:
        norm = re.sub(r'\W+', '', qb.strip().lower())
        if len(norm) > 10:
            existing_texts.add(norm[:80])
            
    q_count = len(re.findall(r'^###\s*Q\d+', content, re.MULTILINE))
    return existing_texts, q_count

def parse_html_file(fpath, pname):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    matches = list(re.finditer(r'QID\s*:\s*(\d+)', content, re.IGNORECASE))
    qs = []
    for i, m in enumerate(matches):
        qid = m.group(1)
        start_pos = m.start()
        end_pos = matches[i+1].start() if i+1 < len(matches) else len(content)
        chunk = content[start_pos:end_pos]
        if i == len(matches) - 1:
            for footer in ['<div id="block-', '<ul class="links inline"', '<!-- added -->', '<footer']:
                f_pos = chunk.find(footer)
                if f_pos != -1:
                    chunk = chunk[:f_pos]
        parsed = parse_question_chunk(chunk, qid, pname)
        qs.append(parsed)
    return qs

# Dry run simulation
folders = {
    '00_General_Awareness': os.path.join('e:/ssc', '00_General_Awareness'),
    '00_General_Intelligence_and_Reasoning': os.path.join('e:/ssc', '00_General_Intelligence_and_Reasoning'),
    '01_Engineering_Mathematics': os.path.join('e:/ssc', '01_Engineering_Mathematics'),
    '02_Digital_Logic': os.path.join('e:/ssc', '02_Digital_Logic'),
    '03_Computer_Organization_and_Architecture': os.path.join('e:/ssc', '03_Computer_Organization_and_Architecture'),
    '04_Programming_and_Data_Structures': os.path.join('e:/ssc', '04_Programming_and_Data_Structures'),
    '05_Algorithms': os.path.join('e:/ssc', '05_Algorithms'),
    '06_Theory_of_Computation': os.path.join('e:/ssc', '06_Theory_of_Computation'),
    '07_Compiler_Design': os.path.join('e:/ssc', '07_Compiler_Design'),
    '08_Operating_System': os.path.join('e:/ssc', '08_Operating_System'),
    '09_Databases': os.path.join('e:/ssc', '09_Databases'),
    '10_Computer_Networks': os.path.join('e:/ssc', '10_Computer_Networks'),
    '11_Computer_Fundamentals_and_Basics': os.path.join('e:/ssc', '11_Computer_Fundamentals_and_Basics'),
}

existing_counts = {}
for name, fpath in folders.items():
    _, cnt = get_existing_question_texts(fpath)
    existing_counts[name] = cnt

# Count new questions
new_questions = {k: [] for k in folders}

# 1. CS papers
cs_files = [
    ('e:/ssc/RAW_HTML/CS_22Nov2017_Shift1.html', 'SSC IMD 22 Nov 2017 Shift 1 (Computer Science)'),
    ('e:/ssc/RAW_HTML/CS_23Nov2017_Shift1.html', 'SSC IMD 23 Nov 2017 Shift 1 (Computer Science)'),
    ('e:/ssc/RAW_HTML/CS_23Nov2017_Shift2.html', 'SSC IMD 23 Nov 2017 Shift 2 (Computer Science)'),
    ('e:/ssc/RAW_HTML/CS_24Nov2017_Shift2_en.html', 'SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [EN]'),
    ('e:/ssc/RAW_HTML/CS_24Nov2017_Shift2_hi.html', 'SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [HI]'),
    ('e:/ssc/RAW_HTML/CS_25Nov2017_Shift2.html', 'SSC IMD 25 Nov 2017 Shift 2 (Computer Science)'),
]

for fpath, pname in cs_files:
    qs = parse_html_file(fpath, pname)
    for q in qs:
        if '24Nov2017_Shift2_hi' in fpath and int(q['qid']) < 940:
            continue
        cat = classify_question_v3(q['question'], " ".join(q['options'].values()), q['correct_answer'])
        new_questions[cat].append(q)

# 2. GIR papers
gir_files = [
    ('e:/ssc/RAW_HTML/GIR_22Nov2017_Shift1.html', 'SSC IMD 22 Nov 2017 Shift 1 (Reasoning)'),
    ('e:/ssc/RAW_HTML/GIR_22Nov2017_Shift2.html', 'SSC IMD 22 Nov 2017 Shift 2 (Reasoning)'),
    ('e:/ssc/RAW_HTML/GIR_23Nov2017_Shift1.html', 'SSC IMD 23 Nov 2017 Shift 1 (Reasoning)'),
    ('e:/ssc/RAW_HTML/GIR_23Nov2017_Shift2.html', 'SSC IMD 23 Nov 2017 Shift 2 (Reasoning)'),
    ('e:/ssc/RAW_HTML/GIR_24Nov2017_Shift2.html', 'SSC IMD 24 Nov 2017 Shift 2 (Reasoning)'),
    ('e:/ssc/RAW_HTML/GIR_25Nov2017_Shift1.html', 'SSC IMD 25 Nov 2017 Shift 1 (Reasoning)'),
]
for fpath, pname in gir_files:
    qs = parse_html_file(fpath, pname)
    for q in qs:
        new_questions['00_General_Intelligence_and_Reasoning'].append(q)

# 3. GA papers
ga_files = [
    ('e:/ssc/RAW_HTML/GA_22Nov2017_Shift1.html', 'SSC IMD 22 Nov 2017 Shift 1 (General Awareness)'),
    ('e:/ssc/RAW_HTML/GA_22Nov2017_Shift2.html', 'SSC IMD 22 Nov 2017 Shift 2 (General Awareness)'),
    ('e:/ssc/RAW_HTML/GA_23Nov2017_Shift1.html', 'SSC IMD 23 Nov 2017 Shift 1 (General Awareness)'),
    ('e:/ssc/RAW_HTML/GA_23Nov2017_Shift2.html', 'SSC IMD 23 Nov 2017 Shift 2 (General Awareness)'),
    ('e:/ssc/RAW_HTML/GA_24Nov2017_Shift2.html', 'SSC IMD 24 Nov 2017 Shift 2 (General Awareness)'),
    ('e:/ssc/RAW_HTML/GA_25Nov2017_Shift1.html', 'SSC IMD 25 Nov 2017 Shift 1 (General Awareness)'),
    ('e:/ssc/RAW_HTML/GA_25Nov2017_Shift2.html', 'SSC IMD 25 Nov 2017 Shift 2 (General Awareness)'),
]
for fpath, pname in ga_files:
    qs = parse_html_file(fpath, pname)
    for q in qs:
        new_questions['00_General_Awareness'].append(q)

print("=== DRY RUN SUMMARY ===")
print(f"{'Folder':45s} | {'Exist':5s} | {'New Extracted':13s} | {'Projected Total':15s}")
print("-" * 85)
grand_exist = 0
grand_new = 0
for name, fpath in folders.items():
    ex = existing_counts[name]
    nw = len(new_questions[name])
    grand_exist += ex
    grand_new += nw
    print(f"{name:45s} | {ex:5d} | {nw:13d} | {ex + nw:15d}")
print("-" * 85)
print(f"{'TOTAL':45s} | {grand_exist:5d} | {grand_new:13d} | {grand_exist + grand_new:15d}")
