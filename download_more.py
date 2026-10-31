import urllib.request, os

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120'}

# Known base paths on adda247
# Pattern from known URLs:
# sites/12/2022/10/29171120/ -> Physics 22Nov2017 Shift2
# sites/12/2022/10/29171434/ -> Electronics 22Nov2017 Shift2
# Let's try other dates with similar folder IDs

# Try many possible URLs for other dates/shifts
base = 'https://www.adda247.com/jobs/wp-content/uploads/sites/12/'

candidates = [
    # Different folder IDs for other dates
    '2022/10/29171120/SSC-Scientific-Assistant-IMD-23-Nov-2017-Shift-1-Physics-1.pdf',
    '2022/10/29171120/SSC-Scientific-Assistant-IMD-23-Nov-2017-Shift-2-Physics-1.pdf',
    '2022/10/29171120/SSC-Scientific-Assistant-IMD-24-Nov-2017-Shift-1-Physics-1.pdf',
    '2022/10/29171120/SSC-Scientific-Assistant-IMD-24-Nov-2017-Shift-2-Physics-1.pdf',
    '2022/10/29171120/SSC-Scientific-Assistant-IMD-25-Nov-2017-Shift-1-Physics-1.pdf',
    '2022/10/29171120/SSC-Scientific-Assistant-IMD-25-Nov-2017-Shift-2-Physics-1.pdf',
    '2022/10/29171434/SSC-Scientific-Assistant-IMD-23-Nov-2017-Shift-2-Electronics-1.pdf',
    '2022/10/29171434/SSC-Scientific-Assistant-IMD-24-Nov-2017-Shift-2-Electronics-1.pdf',
    '2022/10/29171434/SSC-Scientific-Assistant-IMD-25-Nov-2017-Shift-2-Electronics-1.pdf',
    # Computer Science papers
    '2022/10/29171434/SSC-Scientific-Assistant-IMD-22-Nov-2017-Shift-2-Computer-Science-1.pdf',
    '2022/10/29171120/SSC-Scientific-Assistant-IMD-22-Nov-2017-Shift-1-Computer-Science-1.pdf',
    '2022/10/29172345/SSC-Scientific-Assistant-IMD-22-Nov-2017-Shift-2-Computer-Science-1.pdf',
    # Try with CS in the name
    '2022/10/29171120/SSC-Scientific-Assistant-IMD-23-Nov-2017-Shift-1-Computer-Science-1.pdf',
    '2022/10/29171434/SSC-Scientific-Assistant-IMD-23-Nov-2017-Shift-2-Computer-Science-1.pdf',
    '2022/10/29171120/SSC-Scientific-Assistant-IMD-24-Nov-2017-Shift-1-Computer-Science-1.pdf',
    '2022/10/29171434/SSC-Scientific-Assistant-IMD-24-Nov-2017-Shift-2-Computer-Science-1.pdf',
    '2022/10/29171120/SSC-Scientific-Assistant-IMD-25-Nov-2017-Shift-1-Computer-Science-1.pdf',
    '2022/10/29171434/SSC-Scientific-Assistant-IMD-25-Nov-2017-Shift-2-Computer-Science-1.pdf',
    # Also try CS-IT variant
    '2022/10/29171120/SSC-Scientific-Assistant-IMD-22-Nov-2017-Shift-1-CS-IT-1.pdf',
    '2022/10/29171434/SSC-Scientific-Assistant-IMD-22-Nov-2017-Shift-2-CS-IT-1.pdf',
    # 2022 papers
    '2023/01/16183245/SSC-Scientific-Assistant-IMD-2022-Computer-Science.pdf',
    '2023/01/16183245/SSC-Scientific-Assistant-IMD-14-Dec-2022-Shift-1-Computer-Science.pdf',
    '2023/01/16183245/SSC-Scientific-Assistant-IMD-15-Dec-2022-Shift-2-Computer-Science.pdf',
]

out_dir = r'e:/ssc/PAPERS'
found = []
for path in candidates:
    url = base + path
    fname = path.split('/')[-1]
    fpath = os.path.join(out_dir, fname)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as r:
            data = r.read()
            if len(data) > 50000:  # real PDF
                with open(fpath, 'wb') as f:
                    f.write(data)
                print(f'OK: {fname} ({len(data)//1024}KB)')
                found.append(fpath)
            else:
                print(f'small/404: {fname} ({len(data)} bytes)')
    except Exception as e:
        err = str(e)[:50]
        print(f'FAIL: {fname} -> {err}')

print(f'\nDownloaded {len(found)} new papers')
