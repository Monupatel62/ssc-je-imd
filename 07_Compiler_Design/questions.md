# Compiler Design - SSC Scientific Assistant IMD CS Questions

**Syllabus Topics:** Lexical Analysis, Parsing, Syntax-directed Translation, Runtime Environments, Intermediate Code Generation, Code Generation, Code Optimization

---

## Questions from Previous Year Papers (SSC Scientific Assistant IMD)

---

### Q1. [SSC Scientific Assistant CS 2017]
**The errors that can be pointed out by the compiler are:**
- (A) Logical errors
- (B) Syntax errors
- (C) Runtime errors
- (D) Semantic errors only

**Answer:** (B) Syntax errors  
**Explanation:** A compiler can detect and report syntax errors (violations of grammatical rules of the programming language). Logical errors and most runtime errors cannot be detected at compile time.

---

### Q2. [SSC Scientific Assistant CS 2017]
**The predictive parsers can be:**
- (A) Only bottom-up
- (B) Recursive
- (C) Non-deterministic
- (D) Only right-to-left

**Answer:** (B) Recursive  
**Explanation:** Predictive parsers use lookahead to predict which production rule to apply. They can be implemented as recursive descent parsers (recursive) or as table-driven parsers.

---

### Q3. [SSC Scientific Assistant CS 2017]
**What is a lexical analyzer (lexer/scanner)?**
- (A) It checks the syntactic structure of a program
- (B) It reads the source code and breaks it into tokens (lexical units)
- (C) It generates machine code
- (D) It optimizes the intermediate code

**Answer:** (B) It reads the source code and breaks it into tokens  
**Explanation:** The lexical analyzer (scanner) is the first phase of a compiler. It reads the source code character by character and groups them into tokens (keywords, identifiers, operators, literals, etc.).

---

### Q4. [SSC Scientific Assistant CS 2017]
**Syntax analysis (parsing) checks:**
- (A) Whether the program logic is correct
- (B) Whether the sequence of tokens conforms to the grammar of the programming language
- (C) Whether the program will run without runtime errors
- (D) The memory usage of the program

**Answer:** (B) Whether the sequence of tokens conforms to the grammar  
**Explanation:** The parser (syntax analyzer) is the second phase of a compiler. It takes the token stream from the lexer and verifies that it follows the grammatical rules (grammar) of the language, building a parse tree.

---

### Q5. [SSC Scientific Assistant CS 2017]
**Which of the following is an intermediate code representation?**
- (A) Machine code
- (B) Assembly language
- (C) Three-address code (TAC) / Quadruples
- (D) Source code

**Answer:** (C) Three-address code (TAC) / Quadruples  
**Explanation:** Three-address code is a common intermediate representation used in compilers. Each instruction has at most three operands: `result = operand1 op operand2`. Other forms include quadruples, triples, and abstract syntax trees.

---

### Q6. [SSC Scientific Assistant CS 2017]
**A compiler translates:**
- (A) High-level language to machine language directly in one step
- (B) High-level language into a lower-level language (assembly/machine code)
- (C) Machine code to high-level language
- (D) Assembly language to high-level language

**Answer:** (B) High-level language into a lower-level language  
**Explanation:** A compiler translates an entire source program written in a high-level language (like C, Java) into a lower-level language (assembly or machine code) before execution.

---

### Q7. [SSC Scientific Assistant CS 2017]
**An interpreter differs from a compiler in that:**
- (A) An interpreter translates the entire program before execution
- (B) An interpreter translates and executes the program line by line
- (C) An interpreter produces machine code
- (D) An interpreter is faster than a compiler for repeated executions

**Answer:** (B) An interpreter translates and executes the program line by line  
**Explanation:** An interpreter reads, translates, and executes source code line by line at runtime. A compiler translates the entire source program first, then executes the machine code.

---

*Source: SSC Scientific Assistant IMD Previous Year Papers (2017, 2022) | testbook.com*


### Q8 [QID: 319] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
A system program that sets up an executable program in main memory ready for execution is

**Options:**
1) assembler
2) linker
3) loader
4) compiler

**Correct Answer:** loader

---

### Q9 [QID: 355] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
In which of the following does the assembler store all the names and their corresponding values?

**Options:**
1) Special purpose Register
2) Symbol Table
3) Value map Set
4) None of these

**Correct Answer:** Symbol Table

---

### Q10 [QID: 389] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which of the following are steps in query processing?

**Options:**
1) Parsing and translation
2) Optimization
3) Evaluation
4) All options are correct

**Correct Answer:** All options are correct

---

### Q11 [QID: 395] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Java Compiler translates the source code into?

**Options:**
1) Machine code
2) Assembly code
3) Byte code
4) JVM code

**Correct Answer:** Byte code

---

### Q12 [QID: 356] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
The program is known as _________ which interacts with the inner part of called kernel.

**Options:**
1) Compiler
2) Device Driver
3) Protocol
4) Shell

**Correct Answer:** Shell

---

### Q13 [QID: 358] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
Software is a program that directs the overall operation of the computer, facilitates its use and interacts with the user. What are the different types of this software ?

**Options:**
1) Operating system
2) Language compiler
3) Utilities
4) All options are correct

**Correct Answer:** All options are correct

---

### Q14 [QID: 368] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which of the following loader is executed. When a system is first turned ON or restarted?

**Options:**
1) Boot loader
2) Compiler and Go and loader
3) Bootstrap loader
4) Relating loader

**Correct Answer:** Bootstrap loader

---

### Q15 [QID: 926] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [EN]

**Question:**
What is a compiler?

**Options:**
1) A compiler does a conversion line by line as the program is run
2) A compiler converts the whole of a high-level program code into machine code in one step
3) A compiler is a general-purpose language providing very efficient execution
4) None of these

**Correct Answer:** A compiler converts the whole of a high-level program code into machine code in one step

---
