# Operating System - SSC Scientific Assistant IMD CS Questions

**Syllabus Topics:** Processes, Threads, CPU Scheduling, Memory Management (Segmentation, Paging, Virtual Memory), File Systems, I/O Systems, Deadlocks

---

## Questions from Previous Year Papers (SSC Scientific Assistant IMD)

---

### Q1. [SSC Scientific Assistant CS - 24 Nov 2017 Shift-2]
**Operating system is responsible for:**
- (A) Only managing files
- (B) Disk initialization, booting from disc, bad-block recovery, and connecting hardware with software
- (C) Only CPU scheduling
- (D) Only memory allocation

**Answer:** (B) Disk initialization, booting from disc, bad-block recovery, and connecting hardware with software  
**Explanation:** An OS is software that connects a computer user to its hardware. It handles disk initialization, booting, bad-block recovery, and overall hardware-software communication.

---

### Q2. [SSC Scientific Assistant CS 2017]
**The operating system software and data the computer is currently working with are stored in:**
- (A) Secondary storage
- (B) Hard disk
- (C) ROM
- (D) RAM

**Answer:** (D) RAM  
**Explanation:** RAM (Random Access Memory) stores the OS software and current data so the processor can access them rapidly. Data in RAM is lost when the computer is turned off.

---

### Q3. [SSC Scientific Assistant CS - 25 Nov 2017 Shift-1]
**Thrashing:**
- (A) Increases the CPU efficiency
- (B) Occurs when there is too much paging activity, causing the CPU to spend more time swapping pages than executing processes
- (C) Happens only with single-user systems
- (D) Can never be prevented

**Answer:** (B) Occurs when there is too much paging activity, causing the CPU to spend more time swapping pages than executing processes  
**Explanation:** Thrashing has a negative impact on OS performance. When the CPU is underutilized, the scheduler loads more processes, increasing paging, which then degrades performance further.

---

### Q4. [SSC Scientific Assistant CS 2017]
**Thrashing can be avoided if:**
- (A) The number of processes is maximized
- (B) Virtual memory resources are exhausted
- (C) The pages needed are kept in memory (working set model is used)
- (D) Context switching is increased

**Answer:** (C) The pages needed are kept in memory (working set model is used)  
**Explanation:** Thrashing is avoided by using the working set model — keeping the pages that a process currently needs (its working set) in memory, preventing excessive page faults.

---

### Q5. [SSC Scientific Assistant CS 2017]
**A page fault:**
- (A) Occurs when a page is found in main memory
- (B) Occurs when a program accesses a page that is not currently in main memory
- (C) Is a hardware failure
- (D) Results in immediate termination of the process

**Answer:** (B) Occurs when a program accesses a page that is not currently in main memory  
**Explanation:** A page fault occurs when the CPU tries to access a page that is not present in the physical memory (RAM) and must be loaded from secondary storage.

---

### Q6. [SSC Scientific Assistant CS 2017]
**_______ is based on the use of one or both of two basic techniques of virtual memory:**
- (A) Segmentation or paging
- (B) Caching or buffering
- (C) FIFO or LRU
- (D) Spooling or multiprogramming

**Answer:** (A) Segmentation or paging  
**Explanation:** Virtual memory is implemented using paging (fixed-size pages) or segmentation (variable-size segments), or a combination of both.

---

### Q7. [SSC Scientific Assistant CS 2017]
**The implementation of the LFU and the MFU page replacement algorithm is:**
- (A) Simple and cheap
- (B) Very expensive and rarely used
- (C) Same as LRU algorithm
- (D) Used only in real-time systems

**Answer:** (B) Very expensive and rarely used  
**Explanation:** LFU (Least Frequently Used) and MFU (Most Frequently Used) page replacement algorithms are expensive to implement and hence are not commonly used.

---

### Q8. [SSC Scientific Assistant CS 2017]
**In Round Robin CPU scheduling, as the time quantum is increased:**
- (A) Context switch time decreases steadily
- (B) Turnaround time decreases
- (C) Performance varies irregularly
- (D) It becomes equivalent to FIFO/FCFS

**Answer:** (C) Performance varies irregularly (or D - It approaches FCFS with very large quantum)  
**Explanation:** In Round Robin scheduling, as time quantum increases, it eventually approaches FCFS (First Come First Serve) behavior. The answer accepted is that performance varies irregularly.

---

### Q9. [SSC Scientific Assistant CS 2017]
**The number of processes completed per unit time is known as:**
- (A) Turnaround time
- (B) Throughput
- (C) Waiting time
- (D) Response time

**Answer:** (B) Throughput  
**Explanation:** Throughput is the number of processes that are completed by a system per unit time. It is one of the key performance metrics of CPU scheduling.

---

### Q10. [SSC Scientific Assistant CS 2017]
**To avoid the race condition, the number of processes that may be simultaneously inside the critical section is:**
- (A) 2
- (B) 3
- (C) 0
- (D) 1

**Answer:** (D) 1  
**Explanation:** To avoid race conditions, only 1 process can be inside the critical section at a time. This is the mutual exclusion requirement of the critical section problem.

---

### Q11. [SSC Scientific Assistant CS 2017]
**Run-time mapping from virtual to physical address is done by:**
- (A) CPU
- (B) Operating system
- (C) Memory Management Unit (MMU)
- (D) Compiler

**Answer:** (C) Memory Management Unit (MMU)  
**Explanation:** The MMU (Memory Management Unit) is a hardware device responsible for the run-time mapping of virtual addresses to physical addresses.

---

### Q12. [SSC Scientific Assistant CS 2017]
**The three major methods of allocating disk space are:**
- (A) Contiguous, linked, and indexed allocation
- (B) Paged, segmented, and direct allocation
- (C) Sequential, random, and direct allocation
- (D) Fixed, dynamic, and variable allocation

**Answer:** (A) Contiguous, linked, and indexed allocation  
**Explanation:** The three major file allocation methods are: Contiguous (files stored in consecutive disk blocks), Linked (blocks linked with pointers), and Indexed (an index block holds pointers to all file blocks).

---

### Q13. [SSC Scientific Assistant CS 2017]
**_______ mounts is when a file system can be mounted over another file system:**
- (A) Normal mount
- (B) Cascading mounts
- (C) Stack mount
- (D) Virtual mount

**Answer:** (B) Cascading mounts  
**Explanation:** Cascading mounts allow a file system to be mounted over another already-mounted file system, creating a chain of mount points.

---

### Q14. [SSC Scientific Assistant CS 2017]
**On systems where there are multiple operating systems, the device responsible for deciding which OS to load is the:**
- (A) BIOS
- (B) Boot loader / Bootloader
- (C) Kernel
- (D) Shell

**Answer:** (B) Boot loader / Bootloader  
**Explanation:** The bootloader is responsible for loading the operating system. On multi-OS systems, it provides a menu to choose which OS to boot.

---

*Source: SSC Scientific Assistant IMD Previous Year Papers (2017, 2022) | testbook.com*


### Q15 [QID: 312] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
The technique of using disk space to make programs believe that the system contains more random access memory (RAM) than is actually available is called

**Options:**
1) Virtual memory
2) Secondary memory
3) Primary memory
4) Dual memory

**Correct Answer:** Virtual memory

---

### Q16 [QID: 316] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
The principle of locality of reference justifies the use of

**Options:**
1) re-enterable
2) non reusable
3) virtual memory
4) cache memory

**Correct Answer:** cache memory

---

### Q17 [QID: 321] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which of the following statements is true?

**Options:**
1) A process is thrashing if it spends a lot of time executing, rather than paging.
2) A process is thrashing if it spends a lot of time paging, rather than executing.
3) A process is thrashing if it has not memory allocated to it.
4) None of these

**Correct Answer:** A process is thrashing if it spends a lot of time paging,

---

### Q18 [QID: 324] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Consider the following page reference string : 1 2 3 4 2 1 5 6 2 1 2 3 7 6 3 2 1 2 3 6 For FIFO page replacement algorithms with 4 frames (first unique pages will all cost one fault each), the number of page faults is

**Options:**
1) 14
2) 15
3) 11
4) 12

**Correct Answer:** 14

---

### Q19 [QID: 329] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which of the following statements is true? A: To create a file one has to allocate the space in file system. B: To create a file, one has to make an entry for new file in directory.

**Options:**
1) Only A
2) Only B
3) Both A and B
4) Neither A and nor B

**Correct Answer:** Both A and B

---

### Q20 [QID: 332] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Page fault occurs when

**Options:**
1) the page is corrupted by application software
2) the page is in main memory
3) the page is not in main memory
4) one tries to divide a number by 0

**Correct Answer:** the page is not in main memory

---

### Q21 [QID: 333] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which process can be affected by other processes executing in the system?

**Options:**
1) cooperating process
2) child process
3) parent process
4) init process

**Correct Answer:** cooperating process

---

### Q22 [QID: 334] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which one of the following is a synchronization tool?

**Options:**
1) thread
2) pipe
3) semaphore
4) socket

**Correct Answer:** semaphore

---

### Q23 [QID: 337] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which one of the following is the address generated by CPU?

**Options:**
1) physical address
2) absolute address
3) logical address
4) physiological address

**Correct Answer:** logical address

---

### Q24 [QID: 339] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
The protection domain of a process contains

**Options:**
1) object name
2) rights-set
3) both object name and rights-set
4) None of these

**Correct Answer:** both object name and rights-set

---

### Q25 [QID: 341] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Those processes should be aborted on occurrence of a deadlock, the termination of which

**Options:**
1) is more time consuming
2) incurs minimum cost
3) safety is not hampered
4) All options are correct

**Correct Answer:** incurs minimum cost

---

### Q26 [QID: 342] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
The solution to starvation is :

**Options:**
1) the number of rollbacks must be included in the cost factor
2) the number of resources must be included in resource preemption
3) resource preemption be done instead
4) All options are correct

**Correct Answer:** the number of rollbacks must be included in the cost factor

---

### Q27 [QID: 343] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which of the following is used as an index into the page table?

**Options:**
1) Frame bit
2) Page number
3) Page offset
4) Frame offset

**Correct Answer:** Page number

---

### Q28 [QID: 345] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
With paging there is no ________ fragmentation.

**Options:**
1) internal
2) external
3) both internal and external
4) None of these

**Correct Answer:** external

---

### Q29 [QID: 387] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
The deadlock in a set of transaction can be determined by

**Options:**
1) Read-only graph
2) Wait graph
3) Wait-for graph
4) All options are correct

**Correct Answer:** Read-only graph

---

### Q30 [QID: 391] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which command is used to remove a directory?

**Options:**
1) rd
2) rmdir
3) dldir
4) rdir

**Correct Answer:** rmdir

---

### Q31 [QID: 312] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
A page fault

**Options:**
1) Occurs when there is an error in a specific page.
2) Occurs when a program accesses a page of main memory.
3) Occurs when a program accesses a page not currently in main memory.
4) Occurs when a program accesses a page belonging to another program.

**Correct Answer:** Occurs when a program accesses a

---

### Q32 [QID: 346] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
What is the mounting of file system?

**Options:**
1) creating of a filesystem
2) deleting a filesystem
3) attaching portion of the file system into a directory structure
4) removing portion of the file system into a directory structure

**Correct Answer:** attaching portion of the file system

---

### Q33 [QID: 348] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
A machine in Network file system (NFS) can be ________. A. Client B. Server

**Options:**
1) ONLY A
2) ONLY B
3) Both A and B
4) None of these

**Correct Answer:** Both A and B

---

### Q34 [QID: 354] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
If the extents are too large, then the problem that comes in is :

**Options:**
1) internal fragmentation
2) external fragmentation
3) starvation
4) All options are correct

**Correct Answer:** internal fragmentation

---

### Q35 [QID: 355] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
Unix Operating System is a __________.

**Options:**
1) Time Sharing Operating System
2) Multi-User Operating System
3) Multi-tasking Operating System
4) All options are correct

**Correct Answer:** All options are correct

---

### Q36 [QID: 357] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
An optimal scheduling algorithm in terms of minimizing the average waiting time of a given set of processes is ________.

**Options:**
1) FCFS scheduling algorithm
2) Round robin scheduling algorithm
3) Shortest job - first scheduling algorithm
4) None of these

**Correct Answer:** Shortest job - first scheduling

---

### Q37 [QID: 359] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
Super computers typically employ _______.

**Options:**
1) Real time Operating system
2) Multiprocessors OS
3) desktop OS
4) None of these

**Correct Answer:** Multiprocessors OS

---

### Q38 [QID: 360] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
The ___________ requirement must be satisfied by the processor rather than the operating system, because the operating system cannot anticipate all of the memory references that the program will make.

**Options:**
1) memory relocation
2) memory protection
3) memory sharing
4) memory organization

**Correct Answer:** memory protection

---

### Q39 [QID: 361] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
___________ is based on the use of one or both of two basic techniques: segmentation and paging.

**Options:**
1) memory partitioning
2) virtual memory
3) real memory
4) memory organization

**Correct Answer:** virtual memory

---

### Q40 [QID: 362] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
In ___________ , there is an inefficient use of processor due to the need for compaction to counter external fragmentation.

**Options:**
1) Fixed partitioning
2) Dynamic partitioning
3) Virtual memory paging
4) Simple segmentation

**Correct Answer:** Fixed partitioning

---

### Q41 [QID: 363] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
Select one option which chooses one job among all the jobs submitted to the system.

**Options:**
1) Traffic controller
2) File system
3) Job scheduler
4) Dispatcher

**Correct Answer:** Job scheduler

---

### Q42 [QID: 365] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which of the following error will be handled by the operating system?

**Options:**
1) Power failure
2) Lack of paper in printer
3) Connection failure in the network
4) All options are correct

**Correct Answer:** All options are correct

---

### Q43 [QID: 367] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
The operating system software and data, the computer is currently using, are stored in___.

**Options:**
1) PC
2) ACP
3) USB
4) RAM

**Correct Answer:** RAM

---

### Q44 [QID: 381] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which of the following page replacement algorithms suffers from Belady’s Anomaly ?

**Options:**
1) Optimal replacement
2) LRU
3) FIFO
4) Both optimal replacement and FIFO

**Correct Answer:** FIFO

---

### Q45 [QID: 383] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
For 3 page frames, the following is the reference string : 7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1 How many page faults does the LRU page replacement algorithm produce ?

**Options:**
1) 10
2) 15
3) 11
4) 12

**Correct Answer:** 12

---

### Q46 [QID: 384] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
Applying the LRU page replacement to the following reference string : 1 2 4 5 2 1 2 4 The main memory can accommodate 3 pages and it already has pages 1 and 2. Page 1 came in before page 2. How many page faults will occur ?

**Options:**
1) 2
2) 3
3) 4
4) 5

**Correct Answer:** 4

---

### Q47 [QID: 391] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which algorithm of disk scheduling selects the request with the least seek time from the current head positions?

**Options:**
1) SSTF scheduling
2) FCFS scheduling
3) SCAN scheduling
4) LOOK scheduling

**Correct Answer:** SSTF scheduling

---

### Q48 [QID: 916] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
Which of the following statements refers to virtual memory?

**Options:**
1) It is an extremely large main memory.
2) It is an extremely large secondary memory.
3) It is an illusion of an extremely large memory.
4) It is a type of memory that is used in supercomputers.

**Correct Answer:** It is an illusion of an extremely large memory.

---

### Q49 [QID: 917] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
Which of the following statements refers to 'Overlay'?

**Options:**
1) It is a part of an operating system.
2) It is a specific memory location.
3) It is a single contiguous memory that was used in the olden days for running large programs by swapping.
4) It is overloading the system with many user files.

**Correct Answer:** It is a single contiguous memory that was used in the olden days for running large programs by swapping.

---

### Q50 [QID: 919] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
The page replacement policy that sometimes leads to more page faults when the size of the memory is increased is

**Options:**
1) FIFO
2) LRU
3) No such policy exists
4) None of these

**Correct Answer:** FIFO

---

### Q51 [QID: 922] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
An operating system contains 3 user processes each requiring 2 units of resource R. The minimum number of unit of R such that no deadlock will ever occur is

**Options:**
1) 2
2) 4
3) 7
4) 5

**Correct Answer:** 4

---

### Q52 [QID: 924] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
Memory protection is of no use in a

**Options:**
1) single user system
2) non-multiprogramming system
3) non-multitasking system
4) None of these

**Correct Answer:** None of these

---

### Q53 [QID: 927] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
Which of the following is a service not supported by the operating system?

**Options:**
1) Protection
2) Accounting
3) Compilation
4) I/O operation

**Correct Answer:** Compilation

---

### Q54 [QID: 929] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
Which of the following is/are single-user operating system(s)?

**Options:**
1) MS-DOS
2) UNIX
3) Both MS-DOS and UNIX
4) None of these

**Correct Answer:** MS-DOS

---

### Q55 [QID: 930] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
In a multiprogramming environment

**Options:**
1) the processor executes more than one process at a time
2) the programs are developed by more than one person
3) more than one process resides in the memory
4) a single user can execute many programs at the same time

**Correct Answer:** more than one process resides in the memory

---

### Q56 [QID: 931] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
The size of virtual memory depends on the size of the

**Options:**
1) data bus
2) main memory
3) address bus
4) None of these

**Correct Answer:** address bus

---

### Q57 [QID: 936] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
Which of the following is the most suitable scheduling scheme in a real-time operating system?

**Options:**
1) round-robin
2) first-come-first-served
3) preemptive scheduling
4) random scheduling

**Correct Answer:** preemptive scheduling

---

### Q58 [QID: 937] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
If there are 32 segments, each of size 1 kbytes, then the logical address should have

**Options:**
1) 13 bits
2) 14 bits
3) 15 bits
4) 16 bits

**Correct Answer:** 15 bits

---

### Q59 [QID: 939] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
Consider the following page reference string : 1 2 3 4 2 1 5 6 2 1 2 3 7 6 3 2 1 2 3 6 For LRU page replacement algorithm with 4 frames, the number of page faults is :

**Options:**
1) 14
2) 5
3) 10
4) 11

**Correct Answer:** 10

---

### Q60 [QID: 944] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
Which of the following is a unique tag, usually a number that identifies the file within the file system?

**Options:**
1) File identifier
2) File name
3) File type
4) None of these

**Correct Answer:** File identifier

---

### Q61 [QID: 987] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
What are the ways of dealing with deadlock?

**Options:**
1) Deadlock prevention
2) Deadlock recovery
3) Deadlock detection
4) All options are correct

**Correct Answer:** All options are correct

---

### Q62 [QID: 906] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [EN]

**Question:**
Write Through technique is used in which memory for updating the data?

**Options:**
1) Virtual memory
2) Main memory
3) Auxiliary memory
4) Cache memory

**Correct Answer:** Cache memory

---

### Q63 [QID: 907] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [EN]

**Question:**
When CPU is executing a Program that is part of the Operating System, it is said to be in

**Options:**
1) Interrupt mode
2) System mode
3) Half mode
4) Simplex mode

**Correct Answer:** System mode

---

### Q64 [QID: 937] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [EN]

**Question:**
Assume transaction A holds a share lock R. If a transaction B also requests for a shared lock on R.

**Options:**
1) it will result in a deadlock situation.
2) it will immediately be granted.
3) it will immediately be rejected.
4) it will be granted as soon as it is released by A.

**Correct Answer:** it will immediately be granted.

---

### Q65 [QID: 987] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [HI]

**Question:**
किसने 1988 का प्रसिद्द वर्म आक्रमण किया था जिसने UNIX सिस्टम्स को प्रभावित कर लाखों का नुक्सान किया था?

**Options:**
1) रोबर्ट मोरिस
2) बॉब मिलानो
3) मार्क जुकरबर्ग
4) बिल गेट्स

**Correct Answer:** रोबर्ट मोरिस

---

### Q66 [QID: 946] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
Mapping of file is managed by

**Options:**
1) File metadata
2) Page table
3) Virtual memory
4) File system

**Correct Answer:** File metadata

---

### Q67 [QID: 947] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
On systems where there are multiple operating system, the decision to load a particular one is done by

**Options:**
1) boot loader
2) boot strap
3) process control block
4) file control block

**Correct Answer:** boot loader

---

### Q68 [QID: 955] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
The host repeatedly checks if the controller is busy until it is not. It is in a loop that status register's busy bit becomes clear. This is called _________ ____ and a mechanism for the hardware controller to notify the CPU that it is ready is called ___________.

**Options:**
1) Interrupt and Polling
2) Polling and spooling
3) Polling and interrupt
4) Deadlock and Interrupt

**Correct Answer:** Polling and interrupt

---

### Q69 [QID: 956] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
Which file system does DOS typically use ?

**Options:**
1) FAT16
2) FAT32
3) NTFS
4) WNFS

**Correct Answer:** FAT16

---

### Q70 [QID: 957] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
In ______ OS, the response time is very critical.

**Options:**
1) Multitasking
2) Batch
3) Online
4) Real-time

**Correct Answer:** Real-time

---

### Q71 [QID: 958] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
Which of the following refers to PCB?

**Options:**
1) Program Control Block
2) Process Control Block
3) Process Communication Block
4) None of these

**Correct Answer:** Process Control Block

---

### Q72 [QID: 959] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
Which of the following is contained in Process Control Block (PCB)?

**Options:**
1) Process Number
2) List of Open files
3) Memory Limits
4) All options are correct

**Correct Answer:** All options are correct

---

### Q73 [QID: 961] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
In almost all modern multi programming systems, principal operation of memory management involves a sophisticated scheme known as_____________.

**Options:**
1) memory partitioning
2) virtual memory
3) real memory
4) memory organization

**Correct Answer:** virtual memory

---

### Q74 [QID: 962] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
In ___________ , there is a inefficient use of memory due to internal fragmentation.

**Options:**
1) Fixed partitioning
2) Simple Paging
3) Virtual memory paging
4) Simple segmentation

**Correct Answer:** Fixed partitioning

---

### Q75 [QID: 963] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
The operating system as a device management keeps track of devices, channels and control units. This is typically called ________.

**Options:**
1) I / O manager
2) I / O traffic controller
3) I / O dispatch
4) All options are correct

**Correct Answer:** I / O traffic controller

---

### Q76 [QID: 967] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
The hardware mechanism that enables a device to notify the CPU is called A. polling B. Interrupt C. System call

**Options:**
1) Only A
2) Only B
3) Both A and B
4) Only C

**Correct Answer:** Only B

---

### Q77 [QID: 983] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
LRU page – replacement algorithm associates with each page the ______

**Options:**
1) time it was brought into memory
2) the time of that page’s last use
3) page after and before it
4) All options are correct

**Correct Answer:** the time of that page’s last use

---

### Q78 [QID: 988] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
Which is not a valid port scan type?

**Options:**
1) ACK scanning
2) Window scanning
3) IGMP scan
4) FIN scanning

**Correct Answer:** IGMP scan

---
