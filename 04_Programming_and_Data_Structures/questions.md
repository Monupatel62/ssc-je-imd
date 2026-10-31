# Programming and Data Structures - SSC Scientific Assistant IMD CS Questions

**Syllabus Topics:** Programming in C, Recursion, Arrays, Stacks, Queues, Linked Lists, Trees, Binary Search Trees, Binary Heaps, Graphs

---

## Questions from Previous Year Papers (SSC Scientific Assistant IMD)

---

### Q1. [SSC Scientific Assistant CS 2017]
**What is the output of this program?**
```c
main()
{
    int a = 0;
    if (a = 0)
        printf("True");
    else
        printf("False");
}
```
- (A) True
- (B) False
- (C) Compilation error
- (D) No output

**Answer:** (B) False  
**Explanation:** The `=` operator is an assignment operator (not comparison `==`). `a = 0` assigns 0 to `a`, which is falsy (0), so the `else` branch executes, printing "False".

---

### Q2. [SSC Scientific Assistant CS 2017]
**What is the output of this program?**
```c
main()
{
    char str[] = "ABCDEFGHIJ";
    printf("%s", str);
}
```
- (A) A
- (B) ABCDEFGHIJ
- (C) Address of array
- (D) Compilation error

**Answer:** (B) ABCDEFGHIJ  
**Explanation:** The `%s` format specifier prints the entire string until the null terminator `\0`. So it prints all characters: ABCDEFGHIJ.

---

### Q3. [SSC Scientific Assistant CS 2017]
**Sending a copy of data to a program module is called:**
- (A) Pass by reference
- (B) Pass by value
- (C) Pass by pointer
- (D) Recursion

**Answer:** (B) Pass by value  
**Explanation:** Pass by value means a copy of the data is sent to the function. The original data is not modified. Pass by reference sends the address, allowing modification of the original data.

---

### Q4. [SSC Scientific Assistant CS 2017]
**Which of the following statements is true about a Binary Search Tree (BST)?**
- (A) Left child is always greater than the parent
- (B) Right child is always less than the parent
- (C) For every node, the left subtree contains values less than the node and right subtree contains values greater than the node
- (D) BST always has a fixed height

**Answer:** (C) For every node, the left subtree contains values less than the node and right subtree contains values greater  
**Explanation:** In a BST, for any node: all values in the left subtree are smaller, and all values in the right subtree are larger. This property enables efficient searching (O(log n) average case).

---

### Q5. [SSC Scientific Assistant CS 2017]
**The predictive parsers can be:**
- (A) Iterative only
- (B) Recursive
- (C) Bottom-up only
- (D) Non-deterministic

**Answer:** (B) Recursive  
**Explanation:** Predictive parsers are a type of top-down parser that can be implemented recursively (recursive descent parser). They predict which production to use based on the current input token.

---

### Q6. [SSC Scientific Assistant CS 2017]
**In a linked list, the address of the first node is stored in:**
- (A) Header node
- (B) Tail pointer
- (C) Head pointer
- (D) Stack pointer

**Answer:** (C) Head pointer  
**Explanation:** In a linked list, the head pointer (or start pointer) stores the address of the first node. If the list is empty, the head pointer is NULL.

---

### Q7. [SSC Scientific Assistant CS 2017]
**Which data structure uses LIFO (Last In, First Out) principle?**
- (A) Queue
- (B) Linked list
- (C) Stack
- (D) Tree

**Answer:** (C) Stack  
**Explanation:** A stack follows the LIFO (Last In, First Out) principle — the last element inserted is the first to be removed. Operations: Push (insert) and Pop (remove from top).

---

### Q8. [SSC Scientific Assistant CS 2017]
**Which data structure uses FIFO (First In, First Out) principle?**
- (A) Stack
- (B) Queue
- (C) Tree
- (D) Graph

**Answer:** (B) Queue  
**Explanation:** A queue follows the FIFO (First In, First Out) principle — the first element inserted is the first to be removed. Operations: Enqueue (insert at rear) and Dequeue (remove from front).

---

### Q9. [SSC Scientific Assistant CS 2017]
**Recursion is:**
- (A) A method where a function calls another function repeatedly
- (B) A method of function call through which a function invokes itself until a base condition is reached
- (C) An iterative technique for loops
- (D) A type of data structure

**Answer:** (B) A method of function call through which a function invokes itself until a base condition is reached  
**Explanation:** Recursion is a programming technique where a function calls itself. It must have a base case to stop recursion, otherwise it leads to infinite recursion (stack overflow).

---

### Q10. [SSC Scientific Assistant CS 2017]
**In a binary tree, each node can have at most:**
- (A) 1 child
- (B) 2 children
- (C) 3 children
- (D) Any number of children

**Answer:** (B) 2 children  
**Explanation:** A binary tree is a tree data structure where each node has at most 2 children — typically called the left child and right child.

---

*Source: SSC Scientific Assistant IMD Previous Year Papers (2017, 2022) | testbook.com*


### Q11 [QID: 313] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which of the following statements is true?

**Options:**
1) ROM is a read/write memory.
2) PC points to the last instruction that was executed.
3) Stack works on the principle of LIFO.
4) All instructions affect the flag.

**Correct Answer:** Stack works on the principle of LIFO.

---

### Q12 [QID: 317] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
The register or main memory location which contains the effective address of the operand is known as

**Options:**
1) pointer
2) indexed register
3) special location
4) scratch pad

**Correct Answer:** pointer

---

### Q13 [QID: 338] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
The address of a page table in memory is pointed by

**Options:**
1) stack pointer
2) page table base register
3) page register
4) program counter

**Correct Answer:** page table base register

---

### Q14 [QID: 393] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
In a FORTRAN program it is been set that x =2.0 , a =2.0 and b = 4.0. What is the value of 'y' if y = a*x+b**2/x?

**Options:**
1) 8
2) 12
3) 16
4) 64

**Correct Answer:** 12

---

### Q15 [QID: 394] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
"What will be the output after compiling the FORTRAN statement: y = c/d + a*x**2-5"

**Options:**
1) /
2) +
3) *
4) **

**Correct Answer:** **

---

### Q16 [QID: 397] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
What is the size of wchar_t in C++?

**Options:**
1) 2
2) 4
3) 2 or 4
4) based on the number of bits in the system

**Correct Answer:** based on the number of bits in the system

---

### Q17 [QID: 399] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which data type is used to represent the absence of parameters?

**Options:**
1) int
2) short
3) float
4) void

**Correct Answer:** void

---

### Q18 [QID: 400] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
What does a escape code represent?

**Options:**
1) alert
2) backslash
3) tab
4) form feed

**Correct Answer:** alert

---

### Q19 [QID: 307] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
A Stack-organized Computer uses instruction of____.

**Options:**
1) Indirect addressing
2) Two-addressing
3) Zero addressing
4) Index addressing

**Correct Answer:** Zero addressing

---

### Q20 [QID: 334] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
Complex entities can be constructed using the following operation

**Options:**
1) SUM
2) Union
3) Aggregation
4) Collection

**Correct Answer:** Aggregation

---

### Q21 [QID: 372] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
A ‘C’ data structure called a structure is a group of items in which each item is identified by its own identifier, each of which known as number of a structure members is also known as

**Options:**
1) information
2) field
3) record
4) data type

**Correct Answer:** field

---

### Q22 [QID: 374] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which type of parameter is passed in a function for faster execution?

**Options:**
1) call by value
2) Call by address
3) Call by name
4) Call by string

**Correct Answer:** call by value

---

### Q23 [QID: 911] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
Which of the following is / are register(s)?

**Options:**
1) Buffer
2) Stack pointer
3) Both stack pointer and program counter
4) None of these

**Correct Answer:** Both stack pointer and program counter

---

### Q24 [QID: 990] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
The user defined data type can be created using

**Options:**
1) Create datatype
2) Create data
3) Create define type
4) Create type

**Correct Answer:** Create type

---

### Q25 [QID: 993] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
What are the basic data types in Fortran?

**Options:**
1) Integer, Real, Double Precision, Character
2) Integer, Real, Character, Logical
3) Integer, Real, Complex, Character
4) interger, Real, Character,Double precision,complex and logical

**Correct Answer:** interger, Real, Character,Double precision,complex and logical

---

### Q26 [QID: 994] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
In which column does the code start in Fortran 77 fixed format?

**Options:**
1) 6
2) 9
3) 8
4) 7

**Correct Answer:** 7

---

### Q27 [QID: 998] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
Which of the following is the correct option? string* x, y;

**Options:**
1) x is a pointer to a string, y is a string
2) y is a pointer to a string, x is a string
3) both x and y are pointer to string types
4) None of these

**Correct Answer:** x is a pointer to a string, y is a string

---

### Q28 [QID: 999] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
Which one of the following is not a possible state for a pointer?

**Options:**
1) hold the address of the specific object
2) point one past the end of an object
3) zero
4) None of these

**Correct Answer:** None of these

---

### Q29 [QID: 911] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [EN]

**Question:**
What is the content of Stack Pointer (SP)?

**Options:**
1) Address of the current instruction
2) Address of the next instruction
3) Address of the top element of the stack
4) Size of the stack.

**Correct Answer:** Address of the top element of the stack

---

### Q30 [QID: 915] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [EN]

**Question:**
___________ is an OOP principle.

**Options:**
1) Structured programming
2) Procedural programming
3) Inheritance
4) Linking

**Correct Answer:** Inheritance

---

### Q31 [QID: 972] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
What is the similarity between a structure, union and enumeration?

**Options:**
1) All of them let your define new values
2) All of them let you define new data types
3) All of them let you define new pointers
4) All of the let you define new structure\

**Correct Answer:** All of them let you define new data types

---

### Q32 [QID: 975] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
You declare a function with a function _______, which is typically entered at the beginning of the program, below the # include directives.

**Options:**
1) call
2) prototype declaration
3) definition
4) pointer

**Correct Answer:** prototype declaration

---

### Q33 [QID: 978] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
JVM is a virtual machine that can execute

**Options:**
1) C language
2) .net programming
3) RDMS
4) java byte code

**Correct Answer:** java byte code

---

### Q34 [QID: 984] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
There is a set of page replacement algorithms that can never exhibit Belady’s Anomaly, called :

**Options:**
1) queue algorithms
2) stack algorithms
3) string algorithms
4) None of these

**Correct Answer:** stack algorithms

---
