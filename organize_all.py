import pdfplumber, sys, re, os
sys.stdout.reconfigure(encoding='utf-8')

def extract_full(filepath):
    text = ""
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                text += t + "\n"
    return text

def parse_questions(text):
    pattern = r'(QID\s*:\s*\d+\s*-.*?)(?=QID\s*:\s*\d+\s*-|\Z)'
    blocks = re.findall(pattern, text, re.DOTALL)
    questions = []
    for block in blocks:
        block = block.strip()
        qid_match = re.match(r'QID\s*:\s*(\d+)\s*-\s*(.*)', block, re.DOTALL)
        if not qid_match:
            continue
        qid = int(qid_match.group(1))
        rest = qid_match.group(2).strip()
        lines = rest.split('\n')
        q_lines, opts, answer = [], [], ""
        in_opts = False
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if re.match(r'^Options\s*:', line, re.I):
                in_opts = True
                continue
            if re.match(r'^Correct\s+Answer\s*:', line, re.I):
                answer = re.sub(r'^Correct\s+Answer\s*:\s*', '', line, flags=re.I).strip()
                in_opts = False
                continue
            if in_opts:
                om = re.match(r'^(\d+)\)\s*(.*)', line)
                if om:
                    opts.append(f"({om.group(1)}) {om.group(2)}")
                elif opts:
                    opts[-1] += ' ' + line
            else:
                q_lines.append(line)
        q_text = ' '.join(q_lines).strip()
        if q_text or opts:
            questions.append({'qid': qid, 'question': q_text, 'options': opts, 'answer': answer})
    return questions

def format_q(q, idx, paper_label):
    opts_str = '\n'.join(f'- {o}' for o in q['options']) if q['options'] else '*(image/figure based)*'
    ans = q['answer'] if q['answer'] else '*(see original paper)*'
    return f"""
### Q{idx}. [QID {q['qid']} | {paper_label}]
**{q['question'] if q['question'] else '*(Figure/Image based question)*'}**
{opts_str}

**Answer:** {ans}
"""

def append_to_file(filepath, section_title, questions, paper_label, start_idx):
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(f"\n\n---\n## {section_title}\n")
        for i, q in enumerate(questions, start_idx):
            f.write(format_q(q, i, paper_label))
    print(f"  Appended {len(questions)} questions -> {os.path.basename(filepath)}")
    return start_idx + len(questions)

# ===== Load papers =====
papers = {
    '22 Nov 2017 Shift-2 (Physics stream)': r'e:/ssc/PAPERS/SSC-Scientific-Assistant-IMD-22-Nov-2017-Shift-2-Physics-1.pdf',
    '22 Nov 2017 Shift-2 (Electronics stream)': r'e:/ssc/PAPERS/SSC-Scientific-Assistant-IMD-22-Nov-2017-Shift-2-Electronics-1.pdf',
}

# Track per-folder question count
folder_counts = {
    'GIR': 0, 'GA': 0, 'Quant': 0, 'English': 0,
    'Physics': 0, 'Electronics': 0
}

for label, path in papers.items():
    print(f"\nProcessing: {label}")
    text = extract_full(path)
    qs = parse_questions(text)
    print(f"  Total parsed: {len(qs)}")

    # Classify
    gir  = [q for q in qs if 601 <= q['qid'] <= 625]
    quant = [q for q in qs if 626 <= q['qid'] <= 650]
    eng  = [q for q in qs if 651 <= q['qid'] <= 675]
    ga   = [q for q in qs if 676 <= q['qid'] <= 700]
    tech = [q for q in qs if q['qid'] >= 701]
    print(f"  GIR={len(gir)} Quant={len(quant)} Eng={len(eng)} GA={len(ga)} Tech={len(tech)}")

    stream = label.split('(')[1].replace(' stream)', '').strip()

    # GIR - only from first paper to avoid duplicates (same questions)
    if 'Physics' in label:
        folder_counts['GIR'] = append_to_file(
            r'e:/ssc/00_General_Intelligence_and_Reasoning/questions.md',
            f'Paper: {label}', gir, label, folder_counts['GIR'] + 16
        ) - 16

    # GA - only from first paper
    if 'Physics' in label:
        folder_counts['GA'] = append_to_file(
            r'e:/ssc/00_General_Awareness/questions.md',
            f'Paper: {label}', ga, label, folder_counts['GA'] + 21
        ) - 21

    # Quant - separate folder
    os.makedirs(r'e:/ssc/12_Quantitative_Aptitude', exist_ok=True)
    qa_file = r'e:/ssc/12_Quantitative_Aptitude/questions.md'
    if not os.path.exists(qa_file) or os.path.getsize(qa_file) < 100:
        with open(qa_file, 'w', encoding='utf-8') as f:
            f.write("# Quantitative Aptitude - SSC Scientific Assistant IMD\n\n**Paper-I | 25 Questions | 25 Marks**\n\n---\n")
    if 'Physics' in label:  # same questions in both papers
        append_to_file(qa_file, f'Paper: {label}', quant, label, folder_counts['Quant'] + 1)
        folder_counts['Quant'] += len(quant)

    # English - separate folder
    os.makedirs(r'e:/ssc/13_English_Language', exist_ok=True)
    eng_file = r'e:/ssc/13_English_Language/questions.md'
    if not os.path.exists(eng_file) or os.path.getsize(eng_file) < 100:
        with open(eng_file, 'w', encoding='utf-8') as f:
            f.write("# English Language & Comprehension - SSC Scientific Assistant IMD\n\n**Paper-I | 25 Questions | 25 Marks**\n\n---\n")
    if 'Physics' in label:
        append_to_file(eng_file, f'Paper: {label}', eng, label, folder_counts['English'] + 1)
        folder_counts['English'] += len(eng)

    # Technical section
    if 'Physics' in label:
        os.makedirs(r'e:/ssc/PHYSICS_Technical', exist_ok=True)
        ph_file = r'e:/ssc/PHYSICS_Technical/questions.md'
        if not os.path.exists(ph_file) or os.path.getsize(ph_file) < 100:
            with open(ph_file, 'w', encoding='utf-8') as f:
                f.write("# Physics Technical Questions - SSC Scientific Assistant IMD\n\n**Paper-I Part-F | 100 Questions | 100 Marks**\n\n---\n")
        append_to_file(ph_file, f'Paper: {label}', tech, label, folder_counts['Physics'] + 1)
        folder_counts['Physics'] += len(tech)

    if 'Electronics' in label:
        os.makedirs(r'e:/ssc/ELECTRONICS_Technical', exist_ok=True)
        el_file = r'e:/ssc/ELECTRONICS_Technical/questions.md'
        if not os.path.exists(el_file) or os.path.getsize(el_file) < 100:
            with open(el_file, 'w', encoding='utf-8') as f:
                f.write("# Electronics & Telecommunication Technical Questions - SSC Scientific Assistant IMD\n\n**Paper-I Part-E | 100 Questions | 100 Marks**\n\n---\n")
        append_to_file(el_file, f'Paper: {label}', tech, label, folder_counts['Electronics'] + 1)
        folder_counts['Electronics'] += len(tech)

print("\n=== DONE ===")
print("Folder counts:", folder_counts)
