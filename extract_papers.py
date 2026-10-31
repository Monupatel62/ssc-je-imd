import pdfplumber
import sys
import os
sys.stdout.reconfigure(encoding='utf-8')

files = [
    r'e:/ssc/PAPERS/SSC-Scientific-Assistant-IMD-22-Nov-2017-Shift-2-Physics-1.pdf',
    r'e:/ssc/PAPERS/SSC-Scientific-Assistant-IMD-22-Nov-2017-Shift-2-Electronics-1.pdf',
    r'e:/ssc/PAPERS/5_6305600667335526538.pdf',
]
for f in files:
    fname = os.path.basename(f)
    print(f'=== FILE: {fname} ===')
    try:
        with pdfplumber.open(f) as pdf:
            print(f'Pages: {len(pdf.pages)}')
            for i, page in enumerate(pdf.pages[:5]):
                t = page.extract_text()
                if t:
                    print(f'-- Page {i+1} --')
                    print(t[:1000])
    except Exception as e:
        print('Error:', str(e))
    print()
