import re
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

def classify_question_v2(q_text, opts_text, ans_text):
    full = f" {q_text} {opts_text} {ans_text} ".lower()
    
    # Priority 1: Theory of Computation
    if re.search(r'\b(turing machine|decidab|undecidab|halting problem|pumping lemma|chomsky|context[\s\-]free|cfg|pushdown|pda|regular expression|regular grammar|regular language|finite automat|dfa|nfa)\b', full):
        return "06_Theory_of_Computation"

    # Priority 2: Compiler Design
    if re.search(r'\b(compiler|cross compiler|interpreter|lexical analy|token|lexeme|lexer|parser|parsing|ll\(1\)|lr\(0\)|slr\(1\)|lalr|lr\(1\)|shift[\s\-]reduce|syntax directed|syntax tree|parse tree|ast|abstract syntax|three[\s\-]address|activation record|symbol table|code optimiz|dead code|peephole|liveness analy|constant propagat|common subexpression|code generation|intermediate code)\b', full):
        return "07_Compiler_Design"

    # Priority 3: Databases
    if re.search(r'\b(sql|database|dbms|rdbms|relation(?:al)? schema|relational algebra|tuple calculus|foreign key|primary key|candidate key|super key|functional dependenc|normal form|1nf|2nf|3nf|bcnf|4nf|acid propert|serializab|two[\s\-]phase lock|2pl|b\+?\s*tree|er[\s\-]model|entity relationship|select\s+.*from|insert into|drop table|alter table|create table|update\s+.*set|referential integrity|weak entity|concurrency control)\b', full):
        return "09_Databases"

    # Priority 4: Computer Networks
    if re.search(r'\b(osi model|tcp/ip|protocol stack|data link layer|transport layer|network layer|application layer|physical layer|presentation layer|session layer|ipv4|ipv6|ip address|subnet|subnetting|cidr|arp|rarp|icmp|dhcp|dns|http|https|ftp|smtp|pop3|imap|telnet|ssh|snmp|mime|router|routing|distance vector|link state|ospf|rip|bgp|csma|aloha|ethernet|802\.3|802\.11|token ring|sliding window|go[\s\-]back[\s\-]n|stop[\s\-]and[\s\-]wait|crc|cyclic redundancy|hamming code|framing|mac address|circuit switch|packet switch|virtual circuit|port number|baud|bandwidth|guided media|twisted pair|coaxial|optical fiber|firewall|proxy server|three[\s\-]way handshake)\b', full):
        return "10_Computer_Networks"

    # Priority 5: Algorithms
    if re.search(r'\b(time complexity|space complexity|asymptotic|big\s*o|omega|theta|bubble sort|insertion sort|selection sort|merge sort|quick sort|heap sort|radix sort|counting sort|binary search|linear search|divide and conquer|dynamic programming|greedy method|greedy algorithm|dijkstra|bellman|kruskal|prim\'?s|floyd|topological sort|hash function|hash table|collision resol|linear probing|quadratic probing|recurrence relation|master theorem)\b', full):
        return "05_Algorithms"

    # Priority 6: Programming and Data Structures
    if re.search(r'\b(linked list|singly linked|doubly linked|circular linked|stack|postfix|prefix|infix|circular queue|priority queue|binary tree|avl tree|binary search tree|bst|binary heap|traversal|inorder|preorder|postorder|recursion|recursive function|pointer|malloc|calloc|realloc|c program|null pointer|struct\b|typedef|union\b|header file|preprocessor|storage class|call by value|call by reference|array index|subscript)\b', full):
        return "04_Programming_and_Data_Structures"

    # Priority 7: Operating System
    if re.search(r'\b(operating system|system call|multiprogramming|multitasking|process control block|pcb|round robin|fcfs|sjf|srtf|priority scheduling|cpu schedul|deadlock|banker\'?s|mutex|semaphore|critical section|race condition|paging|page table|inverted page table|segmentation|virtual memory|demand paging|page fault|fifo page|lru|belady|thrashing|disk schedul|scan|c-scan|look|c-look|sstf|inode|fork\(\)|exec\(\)|spooling|working set|starvation|context switch|cooperating process|logical address|physical address|protection domain|file system|directory structure)\b', full):
        return "08_Operating_System"

    # Priority 8: Digital Logic
    if re.search(r'\b(boolean|boolean algebra|k[\s\-]map|karnaugh|logic gate|and gate|or gate|nand|nor|xor|xnor|universal gate|multiplexer|demultiplexer|decoder|encoder|priority encoder|flip[\s\-]flop|jk flip|sr flip|d flip|t flip|latch|ripple counter|synchronous counter|shift register|half adder|full adder|combinational circuit|sequential circuit|truth table|2\'s complement|1\'s complement|minterm|maxterm|sop|pos|gray code|excess[\s\-]3|bcd\b|binary addition|binary multiplication|radix|hexadecimal|octal|base[\s\-]2|base[\s\-]8|base[\s\-]16)\b', full):
        return "02_Digital_Logic"

    # Priority 9: Engineering Mathematics
    if re.search(r'\b(eigenvalue|eigenvector|matrix|matrices|determinant|rank of matrix|differential equation|calculus|maxima|minima|integration|derivative|limit|probability|poisson distribution|binomial distribution|normal distribution|standard deviation|variance|combinatorics|permutation|discrete math|lattice|monoid|group theory|graph coloring|planar graph|tautology|predicate logic)\b', full):
        return "01_Engineering_Mathematics"

    # Priority 10: Computer Organization and Architecture
    if re.search(r'\b(computer organization|architecture|instruction cycle|addressing mode|opcode|operand|alu\b|control unit|microprogram|microprocessor|8085|8086|accumulator|program counter|instruction register|stack pointer|pipelining|pipeline hazard|branch prediction|cache memory|cache hit|cache miss|direct mapped|set associative|dma\b|interrupt|vectored interrupt|trap\b|bus arbitration|daisy chain|memory mapped i/o|dram|sram|memory cycle|cycle time|bus width|word length|spatial locality|temporal locality|device controller|data out register|machine cycle)\b', full):
        return "03_Computer_Organization_and_Architecture"

    # Catch-all: Computer Fundamentals and Basics
    return "11_Computer_Fundamentals_and_Basics"

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
    raw_qs = parse_html_questions(pfile, pname)
    for q in raw_qs:
        if '24Nov2017_Shift2_hi' in pfile and int(q['qid']) < 940:
            continue
        parsed = parse_question_chunk(q['chunk'], q['qid'], pname)
        cat = classify_question_v2(parsed['question'], " ".join(parsed['options'].values()), parsed['correct_answer'])
        cat_counts[cat] = cat_counts.get(cat, 0) + 1

print("\n=== CLASSIFICATION SUMMARY (V2) ===")
for cat, cnt in sorted(cat_counts.items()):
    print(f"  {cat:45s}: {cnt:3d} questions")
print(f"Total: {sum(cat_counts.values())}")
