from test_chunk_extractor import parse_html_questions
from test_structured_parser import parse_question_chunk
from test_classifier import classify_question
import sys

sys.stdout.reconfigure(encoding='utf-8')

papers = [
    ('e:/ssc/RAW_HTML/CS_22Nov2017_Shift1.html', 'SSC IMD 22 Nov 2017 Shift 1 (CS)'),
    ('e:/ssc/RAW_HTML/CS_23Nov2017_Shift1.html', 'SSC IMD 23 Nov 2017 Shift 1 (CS)'),
    ('e:/ssc/RAW_HTML/CS_23Nov2017_Shift2.html', 'SSC IMD 23 Nov 2017 Shift 2 (CS)'),
    ('e:/ssc/RAW_HTML/CS_24Nov2017_Shift2_en.html', 'SSC IMD 24 Nov 2017 Shift 2 (CS) [EN]'),
    ('e:/ssc/RAW_HTML/CS_24Nov2017_Shift2_hi.html', 'SSC IMD 24 Nov 2017 Shift 2 (CS) [HI]'),
    ('e:/ssc/RAW_HTML/CS_25Nov2017_Shift2.html', 'SSC IMD 25 Nov 2017 Shift 2 (CS)'),
]

fundamentals = []
for pfile, pname in papers:
    raw_qs = parse_html_questions(pfile, pname)
    for q in raw_qs:
        if '24Nov2017_Shift2_hi' in pfile and int(q['qid']) < 940:
            continue
        parsed = parse_question_chunk(q['chunk'], q['qid'], pname)
        cat = classify_question(parsed['question'], " ".join(parsed['options'].values()), parsed['correct_answer'])
        if cat == "11_Computer_Fundamentals_and_Basics":
            fundamentals.append(parsed)

print(f"Total in fundamentals: {len(fundamentals)}")
print("\nSample 20 questions in fundamentals:")
for q in fundamentals[:25]:
    print(f"[{q['qid']}] {q['question'][:100]} | Ans: {q['correct_answer'][:40]}")
