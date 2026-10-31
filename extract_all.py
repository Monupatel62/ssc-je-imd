import pdfplumber
import sys
import os
import re

sys.stdout.reconfigure(encoding='utf-8')

def extract_paper(filepath, outfile):
    fname = os.path.basename(filepath)
    questions = []
    current_q = []
    
    with pdfplumber.open(filepath) as pdf:
        full_text = ""
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                full_text += t + "\n"
    
    # Write full text
    with open(outfile, 'w', encoding='utf-8') as f:
        f.write(full_text)
    
    print(f"Extracted {len(full_text)} chars from {fname} -> {outfile}")

files = {
    r'e:/ssc/PAPERS/SSC-Scientific-Assistant-IMD-22-Nov-2017-Shift-2-Physics-1.pdf': 
        r'e:/ssc/PAPERS/22Nov2017_Shift2_Physics_text.txt',
    r'e:/ssc/PAPERS/SSC-Scientific-Assistant-IMD-22-Nov-2017-Shift-2-Electronics-1.pdf': 
        r'e:/ssc/PAPERS/22Nov2017_Shift2_Electronics_text.txt',
    r'e:/ssc/PAPERS/5_6305600667335526538.pdf': 
        r'e:/ssc/PAPERS/2022_result_text.txt',
}

for src, dst in files.items():
    try:
        extract_paper(src, dst)
    except Exception as e:
        print(f"Error {src}: {e}")
