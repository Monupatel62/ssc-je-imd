import os
import re
import sys
from bs4 import BeautifulSoup
from test_structured_parser import parse_question_chunk
from test_classifier_v3 import classify_question_v3

sys.stdout.reconfigure(encoding='utf-8')

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

def normalize_text(t):
    return re.sub(r'\W+', '', t.lower())

def append_to_topic(topic_folder, new_q_list):
    q_file = os.path.join(topic_folder, 'questions.md')
    os.makedirs(topic_folder, exist_ok=True)
    
    existing_content = ""
    if os.path.exists(q_file):
        with open(q_file, 'r', encoding='utf-8') as f:
            existing_content = f.read()
            
    # Find existing question numbers
    q_nums = [int(n) for n in re.findall(r'^###\s*Q(\d+)', existing_content, re.MULTILINE)]
    curr_q_num = max(q_nums) if q_nums else 0
    
    # Existing normalized snippets for deduplication
    existing_norms = set()
    for qb in re.findall(r'\*\*Question:\*\*\s*(.*?)(?=\*\*Options:\*\*|\n\d+\)|$)', existing_content, re.DOTALL):
        norm = normalize_text(qb)
        if len(norm) > 15:
            existing_norms.add(norm[:80])
            
    added_count = 0
    buffer = []
    
    for q in new_q_list:
        norm = normalize_text(q['question'])
        if len(norm) > 15 and norm[:80] in existing_norms:
            continue
            
        curr_q_num += 1
        added_count += 1
        existing_norms.add(norm[:80])
        
        # Format options
        opts_formatted = []
        if q['options']:
            for k in sorted(q['options'].keys()):
                opts_formatted.append(f"{k}) {q['options'][k]}")
        else:
            opts_formatted.append("(Options embedded in question text or diagram)")
            
        opts_str = "\n".join(opts_formatted)
        
        entry = f"""
### Q{curr_q_num} [QID: {q['qid']}] - {q['paper']}

**Question:**
{q['question']}

**Options:**
{opts_str}

**Correct Answer:** {q['correct_answer']}

---
"""
        buffer.append(entry)
        
    if buffer:
        with open(q_file, 'a', encoding='utf-8') as f:
            f.write("\n" + "".join(buffer))
            
    return added_count, curr_q_num

# Collect all new questions
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

print("=== EXECUTING APPEND TO ALL FOLDERS ===")
total_added = 0
for folder_name, folder_path in folders.items():
    added, total_in_file = append_to_topic(folder_path, new_questions[folder_name])
    total_added += added
    print(f"Added {added:3d} new questions -> {folder_name:45s} (New total: {total_in_file})")

print("=" * 65)
print(f"Total new questions successfully written: {total_added}")
