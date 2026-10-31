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
    """Parse QID blocks from text"""
    # Split on QID pattern
    pattern = r'(QID\s*:\s*\d+\s*-.*?)(?=QID\s*:\s*\d+\s*-|\Z)'
    blocks = re.findall(pattern, text, re.DOTALL)
    questions = []
    for block in blocks:
        block = block.strip()
        # Get QID
        qid_match = re.match(r'QID\s*:\s*(\d+)\s*-\s*(.*)', block, re.DOTALL)
        if not qid_match:
            continue
        qid = int(qid_match.group(1))
        rest = qid_match.group(2).strip()
        
        # Split into question text, options, answer
        lines = rest.split('\n')
        q_lines = []
        opts = []
        answer = ""
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
                # option line like "1) text" or "2) text"
                om = re.match(r'^(\d+)\)\s*(.*)', line)
                if om:
                    opts.append(f"({om.group(1)}) {om.group(2)}")
                else:
                    if opts:
                        opts[-1] += ' ' + line
                    else:
                        opts.append(line)
            else:
                q_lines.append(line)
        
        q_text = ' '.join(q_lines).strip()
        questions.append({
            'qid': qid,
            'question': q_text,
            'options': opts,
            'answer': answer
        })
    return questions

def format_question(q, idx):
    lines = [f"\n### Q{idx}. [QID: {q['qid']} | 22 Nov 2017 Shift-2]"]
    lines.append(f"**{q['question']}**")
    for opt in q['options']:
        lines.append(f"- {opt}")
    lines.append(f"\n**Answer:** {q['answer']}")
    return '\n'.join(lines)

# ---- PROCESS PHYSICS PAPER (has GIR + Quant + English + GA sections) ----
phys_text = extract_full(r'e:/ssc/PAPERS/SSC-Scientific-Assistant-IMD-22-Nov-2017-Shift-2-Physics-1.pdf')
elec_text = extract_full(r'e:/ssc/PAPERS/SSC-Scientific-Assistant-IMD-22-Nov-2017-Shift-2-Electronics-1.pdf')

phys_qs = parse_questions(phys_text)
elec_qs = parse_questions(elec_text)

print(f"Physics paper: {len(phys_qs)} questions parsed")
print(f"Electronics paper: {len(elec_qs)} questions parsed")

# Categorize by QID range
# 601-625: GIR, 626-650: Quant, 651-675: English, 676-700: GA, 701+: Technical

categories = {
    'GIR':    (601, 625),
    'Quant':  (626, 650),
    'English':(651, 675),
    'GA':     (676, 700),
    'Tech':   (701, 9999),
}

for name, (lo, hi) in categories.items():
    qs = [q for q in phys_qs if lo <= q['qid'] <= hi]
    print(f"  {name}: {len(qs)} from Physics paper")

# Save GIR questions
gir_qs = [q for q in phys_qs if 601 <= q['qid'] <= 625]
ga_qs  = [q for q in phys_qs if 676 <= q['qid'] <= 700]

# Write to files
def write_questions_to_md(filepath, header, questions, start_idx=1):
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(f"\n\n---\n## 22 Nov 2017 — Shift-2 (Official Paper)\n")
        for i, q in enumerate(questions, start_idx):
            f.write(format_question(q, i))
            f.write('\n')
    print(f"  Written {len(questions)} questions to {filepath}")

write_questions_to_md(r'e:/ssc/00_General_Intelligence_and_Reasoning/questions.md', '', gir_qs, 16)
write_questions_to_md(r'e:/ssc/00_General_Awareness/questions.md', '', ga_qs, 21)

# Also check electronics paper for same QIDs (should be same GIR/GA)
gir_elec = [q for q in elec_qs if 601 <= q['qid'] <= 625]
ga_elec  = [q for q in elec_qs if 676 <= q['qid'] <= 700]
print(f"\nElectronics paper GIR: {len(gir_elec)}, GA: {len(ga_elec)}")
print("(Same paper - skipping duplicates)")

print("\nDone!")
