# Computer Organization and Architecture - SSC Scientific Assistant IMD CS Questions

**Syllabus Topics:** Instructions, Addressing Modes, ALU, Pipelining, Memory Hierarchy (Cache, Main Memory, Secondary Storage), I/O Interface (Interrupt and DMA mode)

---

## Questions from Previous Year Papers (SSC Scientific Assistant IMD)

---

### Q1. [SSC Scientific Assistant CS 2017 - 22 Nov Shift 1]
**The organization and interconnection of the various components of a computer system is called:**
- (A) Computer architecture
- (B) Computer design
- (C) Computer organization
- (D) System programming

**Answer:** (A) Computer architecture  
**Explanation:** Computer architecture refers to the conceptual design and operational structure — how the components are organized and interconnected.

---

### Q2. [SSC Scientific Assistant CS 2017]
**What is the Von Neumann architecture?**
- (A) Architecture where data and program are stored in different memories
- (B) Architecture where data and instructions are stored in the same memory
- (C) Architecture based on parallel processing
- (D) Architecture with only ROM storage

**Answer:** (B) Architecture where data and instructions are stored in the same memory  
**Explanation:** In Von Neumann architecture, both data and instructions share the same memory and the same bus, unlike Harvard architecture.

---

### Q3. [SSC Scientific Assistant CS 2017]
**A Stack-organized Computer uses instruction of:**
- (A) Two-address
- (B) One-address
- (C) Zero-address
- (D) Three-address

**Answer:** (C) Zero-address  
**Explanation:** In a stack-organized computer, operands are implicitly at the top of the stack, so no address field is required — zero-address instructions.

---

### Q4. [SSC Scientific Assistant CS 2017]
**Content of the program counter is added to the address part of an instruction to obtain effective address. This is:**
- (A) Relative addressing mode
- (B) Indirect addressing mode
- (C) Indexed addressing mode
- (D) Base register addressing mode

**Answer:** (A) Relative addressing mode  
**Explanation:** Relative addressing uses the program counter (PC) value added to the offset in the instruction to calculate the effective address.

---

### Q5. [SSC Scientific Assistant CS 2017]
**Which of the following statements is true about the host-controller interface?**
- (A) The controller sets command-ready bit when a command is available for the controller to execute
- (B) The host sets command-ready bit when a command is available for the controller to execute
- (C) The host clears the busy bit after the command is complete
- (D) The controller sets the error bit to indicate a successful command

**Answer:** (B) The host sets command-ready bit when a command is available for the controller to execute  
**Explanation:** In the host-controller interface, the host (CPU/OS) sets the command-ready bit to indicate that a command is ready for the controller to execute.

---

### Q6. [SSC Scientific Assistant CS 2017]
**Which of the following have the fastest access time?**
- (A) Magnetic tape
- (B) Magnetic disk
- (C) Semiconductor memory (Cache/RAM)
- (D) Compact disk

**Answer:** (C) Semiconductor memory (Cache/RAM)  
**Explanation:** Semiconductor memories (SRAM for cache, DRAM for RAM) have the fastest access times compared to magnetic or optical storage.

---

### Q7. [SSC Scientific Assistant CS 2017]
**If the main memory is of 8K bytes and the cache memory is 2K bytes, how many bits are needed for each cache memory word?**
- (A) 8 bits
- (B) 12 bits
- (C) 16 bits
- (D) 32 bits

**Answer:** (C) 16 bits  
**Explanation:** Main memory = 8K bytes = 8 × 1024 × 8 = 2^16 bits → 16 bits needed.

---

### Q8. [SSC Scientific Assistant CS 2017]
**A computer with a 32-bit wide data bus uses 4K × 8 static RAM chips. What is the minimum memory that can be built using these chips?**
- (A) 4 KB
- (B) 8 KB
- (C) 16 KB
- (D) 32 KB

**Answer:** (C) 16 KB  
**Explanation:** 32-bit bus / 8-bit per chip = 4 chips needed. Minimum memory = 4 × 4KB = 16 KB.

---

### Q9. [SSC Scientific Assistant CS 2017]
**Which of the following is a semi-conductor memory?**
- (A) Magnetic tape
- (B) Magnetic disk
- (C) RAM and ROM
- (D) Compact disk

**Answer:** (C) RAM and ROM  
**Explanation:** RAM (Random Access Memory) and ROM (Read-Only Memory) are semiconductor memories based on transistor technology.

---

### Q10. [SSC Scientific Assistant CS 2017]
**The Central Processing Unit (CPU) includes:**
- (A) ALU and Input unit
- (B) ALU and Control unit
- (C) Memory and ALU
- (D) Control unit and Output unit

**Answer:** (B) ALU and Control unit  
**Explanation:** The CPU comprises the ALU (Arithmetic Logic Unit), Control Unit (CU), and registers. The ALU performs arithmetic/logical operations and the CU directs operations.

---

### Q11. [SSC Scientific Assistant CS 2017]
**What type of work do microcomputers do when they act as client computers?**
- (A) They act as the server and store all data
- (B) They generate requests to the server and receive services from the centralized server
- (C) They process all the data independently without any server
- (D) They act as routers in the network

**Answer:** (B) They generate requests to the server and receive services from the centralized server  
**Explanation:** In client-server architecture, microcomputers (clients) generate requests to the server and receive services/data from it.

---

*Source: SSC Scientific Assistant IMD Previous Year Papers (2017, 2022) | testbook.com*


### Q12 [QID: 304] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which of the following architecture(s) is / are not suitable for realizing SIMD?

**Options:**
1) Vector processor and Array processor
2) Von Neumann
3) Array processor
4) Von Neumann and Array processor

**Correct Answer:** Von Neumann

---

### Q13 [QID: 306] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Bipolar devices are desirable in the fabrication of which of the following components?

**Options:**
1) Main memory
2) Cache memory
3) Microprogram memory
4) Cache and Microprogram memory

**Correct Answer:** Cache and Microprogram memory

---

### Q14 [QID: 307] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
On which of the following is the idea of cache memory based?

**Options:**
1) Property of locality of reference
2) Fact that only a small portion of a program is referenced relatively frequently
3) Fact that references generally tend to cluster
4) All options are correct

**Correct Answer:** Property of locality of reference

---

### Q15 [QID: 320] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which of the following are loaded into main memory when the computer is booted?

**Options:**
1) internal command instructions
2) external command instructions
3) utility programs
4) word processing instructions

**Correct Answer:** internal command instructions

---

### Q16 [QID: 325] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
How do you call the following arrangement? A device P has a cable that plugs into device Q, and device Q has a cable that plugs into device R and device R plugs into a port on the computer.

**Options:**
1) Port
2) Daisy chain
3) Bus
4) Cable

**Correct Answer:** Daisy chain

---

### Q17 [QID: 331] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Spatial locality refers to the problem that once a location is referenced

**Options:**
1) it will not be referenced again
2) it will be referenced again
3) a nearby location will be referenced soon
4) None of these

**Correct Answer:** a nearby location will be referenced soon

---

### Q18 [QID: 336] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
CPU fetches the instruction from memory according to the value of

**Options:**
1) program counter
2) status register
3) instruction register
4) program status word

**Correct Answer:** program counter

---

### Q19 [QID: 302] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
The two kinds of main memory are____.

**Options:**
1) Primary and secondary
2) Random and sequential
3) ROM and RAM
4) All options are correct

**Correct Answer:** ROM and RAM

---

### Q20 [QID: 305] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
The average time required to reach a storage location in memory and obtain its contents is called the___.

**Options:**
1) seek time
2) turnaround time
3) access time
4) transfer time

**Correct Answer:** access time

---

### Q21 [QID: 306] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
In a vectored interrupt:

**Options:**
1) the branch address is assigned to a fixed location in memory.
2) the interrupting source supplies the branch information to the processor through an interrupt vector.
3) the branch address is obtained from a register in the processor.
4) None of these

**Correct Answer:** the interrupting source supplies the

---

### Q22 [QID: 308] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
what is the ‘ORGO’ instruction ?

**Options:**
1) Machine Instruction.
2) Pseudo instruction.
3) High level instruction.
4) Memory instruction.

**Correct Answer:** Pseudo instruction.

---

### Q23 [QID: 310] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
A microprogram sequencer

**Options:**
1) generates the address of next micro instruction to be executed.
2) generates the control signals to execute a microinstruction.
3) sequentially averages all microinstructions in the control memory.
4) enables the efficient handling of a micro program subroutine.

**Correct Answer:** generates the address of next micro

---

### Q24 [QID: 311] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
Content of the program counter is added to the address part of the instruction in order to obtain the effective address is called____.

**Options:**
1) relative address mode.
2) index addressing mode.
3) register mode.
4) implied mode.

**Correct Answer:** relative address mode.

---

### Q25 [QID: 315] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
In most IBM PCs, the CPU, the device drives, memory expansion slots and active components are mounted on a single board. What is the name of this board?

**Options:**
1) Motherboard
2) Breadboard
3) Daughter board
4) Grandmother board

**Correct Answer:** Motherboard

---

### Q26 [QID: 903] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
Which of the following defines the minimum time delay between the initiations of two independent memory operations?

**Options:**
1) Access time
2) Cycle time
3) Transfer rate
4) Latency time

**Correct Answer:** Cycle time

---

### Q27 [QID: 904] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
Which of the following statements about the Program Counter (PC) is true?

**Options:**
1) It is a register
2) It is a cell in ROM
3) During execution of the current instruction, its content does not change
4) None of these

**Correct Answer:** It is a register

---

### Q28 [QID: 906] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
By which of the following can the speed imbalance between memory access and CPU operation be reduced?

**Options:**
1) Cache memory
2) Cache memory or Memory interleaving
3) Reducing the size of memory
4) None of these

**Correct Answer:** Cache memory or Memory interleaving

---

### Q29 [QID: 908] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
Among the below, that does not need extra hardware for DRAM refreshing is

**Options:**
1) 8085
2) Motorola-6800
3) Z-80
4) None of these

**Correct Answer:** Z-80

---

### Q30 [QID: 926] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
For showing which of the following is dirty bit used?

**Options:**
1) Page with corrupted data
2) Wrong page in the memory
3) Page that is modified after being loaded into cache memory
4) Page that is less frequently accessed

**Correct Answer:** Page that is modified after being loaded into cache memory

---

### Q31 [QID: 943] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
The CPU hardware has a wire called __________ that the CPU senses after executing every instruction.

**Options:**
1) Interrupt sending line
2) Interrupt request line
3) Interrupt bus
4) Interrupt receiving line

**Correct Answer:** Interrupt request line

---

### Q32 [QID: 946] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
Which of the following statements is true?

**Options:**
1) The interrupt vector contains the interrupts.
2) The interrupt vector contains the memory addresses of specialized interrupt handlers.
3) The interrupt vector contains the identifiers of interrupts.
4) The interrupt vector contains the device addresses.

**Correct Answer:** The interrupt vector contains the memory addresses of specialized interrupt handlers.

---

### Q33 [QID: 947] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
Which of the following refers to the categorization of division by zero, accessing a protected or non existent memory address, or attempting to execute a privileged instruction from user mode?

**Options:**
1) Errors
2) Exceptions
3) Interrupt handlers
4) All options are correct

**Correct Answer:** Exceptions

---

### Q34 [QID: 948] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
Which of the following is used for large data transfers?

**Options:**
1) DMA
2) programmed I/O
3) controller register
4) None of these

**Correct Answer:** DMA

---

### Q35 [QID: 905] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [EN]

**Question:**
The idea of cache memory is based on___.

**Options:**
1) on the property of locality of reference
2) on the heuristic 90-10 rule
3) on the fact that references generally tend to cluster
4) All options are correct

**Correct Answer:** on the property of locality of reference

---

### Q36 [QID: 909] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [EN]

**Question:**
The load instruction is mostly used to designate a transfer from memory to a processor register known as

**Options:**
1) Accumulator
2) Instruction Register
3) Program counter
4) Memory address Register

**Correct Answer:** Accumulator

---

### Q37 [QID: 901] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
One of the main feature that distinguish microprocessors from micro-computer is

**Options:**
1) Words are usually large in microprocessors
2) Words are shorter in microprocessors
3) Microprocessor does not contain I/O device
4) Exactly the same as the machine cycle time

**Correct Answer:** Microprocessor does not contain I/O device

---

### Q38 [QID: 903] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
What does the Central Processing Unit (CPU) include?

**Options:**
1) Input, output and processing
2) Control unit, primary storage, and secondary storage
3) Control unit, arithmetic-logic unit and primary storage
4) Control unit, processing, and primary storage

**Correct Answer:** Control unit, arithmetic-logic unit and primary storage

---

### Q39 [QID: 907] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
In a program, what will be the necessity of using subroutine call instruction?

**Options:**
1) initialize program counter
2) Clear the accumulator
3) Reset the microprocessor
4) Clear the instruction register

**Correct Answer:** Clear the instruction register

---

### Q40 [QID: 908] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
_________ register keeps tracks of the instructions stored in program stored in memory.

**Options:**
1) AR (Address Register)
2) XR (Index Register)
3) PC (Program Counter)
4) AC (Accumulator)

**Correct Answer:** PC (Program Counter)

---

### Q41 [QID: 911] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
Which quantity is measured by the performance of the cache memory?

**Options:**
1) Miss ratio
2) Hit ratio
3) Latency ratio
4) Read ratio

**Correct Answer:** Hit ratio

---

### Q42 [QID: 987] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
Which mechanism is used by worm process?

**Options:**
1) Trap door
2) Fake process
3) Spawn Process
4) VAX process

**Correct Answer:** Spawn Process

---
