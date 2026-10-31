import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

total = 0
print(f"{'Folder':45s} | {'Questions':10s}")
print('-' * 60)
for d in sorted(os.listdir('e:/ssc')):
    dpath = os.path.join('e:/ssc', d)
    if os.path.isdir(dpath):
        qfile = os.path.join(dpath, 'questions.md')
        cnt = 0
        if os.path.exists(qfile):
            with open(qfile, 'r', encoding='utf-8') as f:
                cnt = len(re.findall(r'^###\s*Q\d+', f.read(), re.MULTILINE))
        print(f"{d:45s} | {cnt:5d}")
        total += cnt
print('-' * 60)
print(f"{'TOTAL QUESTIONS':45s} | {total:5d}")
