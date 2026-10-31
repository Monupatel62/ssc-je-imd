from test_chunk_extractor import parse_html_questions
from test_structured_parser import parse_question_chunk
import sys

sys.stdout.reconfigure(encoding='utf-8')

gir_files = [
    ('e:/ssc/RAW_HTML/GIR_22Nov2017_Shift1.html', 'SSC IMD 22 Nov 2017 Shift 1 (GIR)'),
    ('e:/ssc/RAW_HTML/GIR_22Nov2017_Shift2.html', 'SSC IMD 22 Nov 2017 Shift 2 (GIR)'),
    ('e:/ssc/RAW_HTML/GIR_23Nov2017_Shift1.html', 'SSC IMD 23 Nov 2017 Shift 1 (GIR)'),
    ('e:/ssc/RAW_HTML/GIR_23Nov2017_Shift2.html', 'SSC IMD 23 Nov 2017 Shift 2 (GIR)'),
    ('e:/ssc/RAW_HTML/GIR_24Nov2017_Shift2.html', 'SSC IMD 24 Nov 2017 Shift 2 (GIR)'),
    ('e:/ssc/RAW_HTML/GIR_25Nov2017_Shift1.html', 'SSC IMD 25 Nov 2017 Shift 1 (GIR)'),
]

total_gir = 0
for fpath, pname in gir_files:
    raw_qs = parse_html_questions(fpath, pname)
    total_gir += len(raw_qs)
    sample = parse_question_chunk(raw_qs[0]['chunk'], raw_qs[0]['qid'], pname)
    print(f"Sample {pname}: QID {sample['qid']} | {sample['question'][:60]} | Ans: {sample['correct_answer']}")

print(f"\nTotal GIR questions: {total_gir}")

ga_files = [
    ('e:/ssc/RAW_HTML/GA_22Nov2017_Shift1.html', 'SSC IMD 22 Nov 2017 Shift 1 (GA)'),
    ('e:/ssc/RAW_HTML/GA_22Nov2017_Shift2.html', 'SSC IMD 22 Nov 2017 Shift 2 (GA)'),
    ('e:/ssc/RAW_HTML/GA_23Nov2017_Shift1.html', 'SSC IMD 23 Nov 2017 Shift 1 (GA)'),
    ('e:/ssc/RAW_HTML/GA_23Nov2017_Shift2.html', 'SSC IMD 23 Nov 2017 Shift 2 (GA)'),
    ('e:/ssc/RAW_HTML/GA_24Nov2017_Shift2.html', 'SSC IMD 24 Nov 2017 Shift 2 (GA)'),
    ('e:/ssc/RAW_HTML/GA_25Nov2017_Shift1.html', 'SSC IMD 25 Nov 2017 Shift 1 (GA)'),
    ('e:/ssc/RAW_HTML/GA_25Nov2017_Shift2.html', 'SSC IMD 25 Nov 2017 Shift 2 (GA)'),
]

total_ga = 0
for fpath, pname in ga_files:
    raw_qs = parse_html_questions(fpath, pname)
    total_ga += len(raw_qs)
    sample = parse_question_chunk(raw_qs[0]['chunk'], raw_qs[0]['qid'], pname)
    print(f"Sample {pname}: QID {sample['qid']} | {sample['question'][:60]} | Ans: {sample['correct_answer']}")

print(f"\nTotal GA questions: {total_ga}")
