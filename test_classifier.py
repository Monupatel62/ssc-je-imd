import re
from bs4 import BeautifulSoup
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

def classify_question(q_text, opts_text, ans_text):
    full = f"{q_text} {opts_text} {ans_text}".lower()
    
    # Check 06_Theory_of_Computation
    if re.search(r'\b(turing machine|decidab|undecidab|halting problem|pumping lemma|chomsky|context[\s\-]free|cfg|pushdown|pda|regular expression|regular grammar|finite automat|dfa|nfa)\b', full):
        return "06_Theory_of_Computation"
        
    # Check 07_Compiler_Design
    if re.search(r'\b(compiler|interpreter|lexical analy|token|lexeme|ll\(|lr\(|lalr|slr|shift[\s\-]reduce|syntax directed|syntax tree|parse tree|three[\s\-]address|activation record|code optimiz|dead code|peephole|liveness analy|constant propagat)\b', full):
        return "07_Compiler_Design"
        
    # Check 09_Databases
    if re.search(r'\b(sql|database|dbms|rdbms|relation(?:al)? schema|relational algebra|tuple calculus|foreign key|primary key|candidate key|super key|functional dependenc|normal form|1nf|2nf|3nf|bcnf|acid propert|serializab|two[\s\-]phase lock|b\+?\s*tree|er[\s\-]model|entity relationship|select\s+.*from|insert into|drop table|alter table|create table|update\s+.*set)\b', full):
        return "09_Databases"
        
    # Check 10_Computer_Networks
    if re.search(r'\b(osi model|tcp|udp|ipv4|ipv6|ip address|subnet|cidr|arp|rarp|icmp|dhcp|dns|http|https|ftp|smtp|pop3|imap|telnet|router|routing|distance vector|link state|ospf|rip|bgp|csma|aloha|ethernet|token ring|sliding window|go[\s\-]back[\s\-]n|stop[\s\-]and[\s\-]wait|crc|parity check|framing|mac address|circuit switch|packet switch|virtual circuit|data link layer|transport layer|network layer|application layer|physical layer|port number|baud|bandwidth|transmission medium|twisted pair|coaxial|optical fiber)\b', full):
        return "10_Computer_Networks"
        
    # Check 08_Operating_System
    if re.search(r'\b(operating system|system call|multiprogramming|multitasking|process control block|pcb|round robin|fcfs|sjf|srtf|priority scheduling|cpu schedul|deadlock|banker\'?s|mutex|semaphore|critical section|race condition|paging|page table|segmentation|virtual memory|demand paging|page fault|fifo page|lru|belady|thrashing|disk schedul|scan|c-scan|look|c-look|sstf|inode|fork\(\)|exec\(\)|spooling)\b', full):
        return "08_Operating_System"
        
    # Check 05_Algorithms
    if re.search(r'\b(algorithm|time complexity|space complexity|asymptotic|big\s*o|omega|theta|bubble sort|insertion sort|selection sort|merge sort|quick sort|heap sort|radix sort|binary search|linear search|divide and conquer|dynamic programming|greedy method|dijkstra|bellman|kruskal|prim\'?s|floyd|topological sort|hashing|hash table|hash function|collision resol|linear probing|quadratic probing)\b', full):
        return "05_Algorithms"
        
    # Check 04_Programming_and_Data_Structures
    if re.search(r'\b(data structure|array|linked list|singly linked|doubly linked|stack|queue|circular queue|deque|binary tree|avl tree|binary search tree|bst|binary heap|traversal|inorder|preorder|postorder|recursion|recursive|pointer|malloc|calloc|struct|printf|scanf|\bint\b|\bfloat\b|\bchar\b|c program|null pointer)\b', full):
        return "04_Programming_and_Data_Structures"
        
    # Check 02_Digital_Logic
    if re.search(r'\b(boolean|boolean algebra|k[\s\-]map|karnaugh|logic gate|and gate|or gate|nand|nor|xor|xnor|multiplexer|demultiplexer|decoder|encoder|flip[\s\-]flop|jk flip|sr flip|d flip|t flip|counter|ripple counter|shift register|half adder|full adder|combinational circuit|sequential circuit|truth table|2\'s complement|1\'s complement|minterm|maxterm|sop|pos)\b', full):
        return "02_Digital_Logic"
        
    # Check 01_Engineering_Mathematics
    if re.search(r'\b(eigenvalue|eigenvector|matrix|matrices|determinant|differential equation|calculus|maxima|minima|integration|derivative|limit|probability|poisson|binomial distribution|normal distribution|standard deviation|variance|combinatorics|permutation|discrete math|lattice|monoid|group theory|recurrence relation|graph coloring)\b', full):
        return "01_Engineering_Mathematics"
        
    # Check 03_Computer_Organization_and_Architecture
    if re.search(r'\b(computer organization|architecture|instruction cycle|addressing mode|opcode|operand|alu|control unit|microprogram|microprocessor|8085|8086|accumulator|pipelining|pipeline hazard|branch prediction|cache memory|cache hit|cache miss|direct mapped|set associative|dma|interrupt|vectored interrupt|trap|bus arbitration|memory mapped i/o|dram|sram|memory cycle|cycle time|bus width|word length)\b', full):
        return "03_Computer_Organization_and_Architecture"
        
    # Fallback to Fundamentals
    return "11_Computer_Fundamentals_and_Basics"

# Test classification on all CS papers
from test_chunk_extractor import parse_html_questions
from test_structured_parser import parse_question_chunk

papers = [
    ('e:/ssc/RAW_HTML/CS_22Nov2017_Shift1.html', 'SSC IMD 22 Nov 2017 Shift 1 (CS)'),
    ('e:/ssc/RAW_HTML/CS_23Nov2017_Shift1.html', 'SSC IMD 23 Nov 2017 Shift 1 (CS)'),
    ('e:/ssc/RAW_HTML/CS_23Nov2017_Shift2.html', 'SSC IMD 23 Nov 2017 Shift 2 (CS)'),
    ('e:/ssc/RAW_HTML/CS_24Nov2017_Shift2_en.html', 'SSC IMD 24 Nov 2017 Shift 2 (CS) [EN]'),
    ('e:/ssc/RAW_HTML/CS_24Nov2017_Shift2_hi.html', 'SSC IMD 24 Nov 2017 Shift 2 (CS) [HI]'),
    ('e:/ssc/RAW_HTML/CS_25Nov2017_Shift2.html', 'SSC IMD 25 Nov 2017 Shift 2 (CS)'),
]

cat_counts = {}
for pfile, pname in papers:
    # If 24 nov hi, only take QID 940 onwards
    raw_qs = parse_html_questions(pfile, pname)
    for q in raw_qs:
        if '24Nov2017_Shift2_hi' in pfile and int(q['qid']) < 940:
            continue
        parsed = parse_question_chunk(q['chunk'], q['qid'], pname)
        cat = classify_question(parsed['question'], " ".join(parsed['options'].values()), parsed['correct_answer'])
        cat_counts[cat] = cat_counts.get(cat, 0) + 1

print("\n=== CLASSIFICATION SUMMARY OF ALL 500 CS QUESTIONS ===")
total_classified = sum(cat_counts.values())
for cat, cnt in sorted(cat_counts.items()):
    print(f"  {cat:45s}: {cnt:3d} questions")
print(f"Total classified: {total_classified}")
