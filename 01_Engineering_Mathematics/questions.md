# Engineering Mathematics - SSC Scientific Assistant IMD CS Questions

**Syllabus Topics:** Discrete Mathematics (Logic, Sets, Relations, Functions, Graph Theory, Combinatorics), Linear Algebra (Matrices, Eigenvalues), Calculus, Probability & Statistics

---

## Questions from Previous Year Papers (SSC Scientific Assistant IMD)

---

### Q1. [SSC Scientific Assistant CS 2017]
**Which of the following statements is true (about Boolean algebra / logic)?**
- (A) A statement can be both true and false simultaneously
- (B) The complement of a complement gives the original value (Double negation: ¬(¬A) = A)
- (C) In Boolean algebra, A + A = 2A
- (D) The AND of anything with 0 is 1

**Answer:** (B) The complement of a complement gives the original value  
**Explanation:** In Boolean algebra, double negation law states: ¬(¬A) = A. Also: A + 0 = A; A · 1 = A; A + A = A; A · 0 = 0; A + 1 = 1.

---

### Q2. [SSC Scientific Assistant CS 2017]
**In a graph, if every vertex has even degree, then:**
- (A) The graph is disconnected
- (B) The graph has an Eulerian circuit
- (C) The graph is a tree
- (D) The graph has no edges

**Answer:** (B) The graph has an Eulerian circuit  
**Explanation:** Euler's theorem states: A connected graph has an Eulerian circuit (a path that visits every edge exactly once and returns to start) if and only if every vertex has even degree.

---

### Q3. [SSC Scientific Assistant CS 2017]
**The number of edges in a complete graph with n vertices is:**
- (A) n
- (B) n - 1
- (C) n(n-1)/2
- (D) n²

**Answer:** (C) n(n-1)/2  
**Explanation:** In a complete graph Kₙ, every vertex is connected to every other vertex. The number of edges = C(n,2) = n(n-1)/2. For example, K₄ has 4×3/2 = 6 edges.

---

### Q4. [SSC Scientific Assistant CS 2017]
**The probability that at least one of two independent events A and B occurs is:**
- (A) P(A) + P(B)
- (B) P(A) × P(B)
- (C) P(A) + P(B) - P(A ∩ B)
- (D) P(A) - P(B)

**Answer:** (C) P(A) + P(B) - P(A ∩ B)  
**Explanation:** By inclusion-exclusion principle: P(A ∪ B) = P(A) + P(B) - P(A ∩ B). For independent events: P(A ∩ B) = P(A) × P(B).

---

### Q5. [SSC Scientific Assistant CS 2017]
**A relation R on set A is said to be an equivalence relation if it is:**
- (A) Reflexive only
- (B) Symmetric and transitive only
- (C) Reflexive, symmetric, and transitive
- (D) Anti-symmetric and transitive

**Answer:** (C) Reflexive, symmetric, and transitive  
**Explanation:** An equivalence relation must satisfy all three properties: Reflexive (aRa for all a), Symmetric (if aRb then bRa), and Transitive (if aRb and bRc then aRc). Example: equality relation (=).

---

### Q6. [SSC Scientific Assistant CS 2017]
**The number of ways to arrange n distinct objects in a row is:**
- (A) n
- (B) n²
- (C) 2ⁿ
- (D) n! (n factorial)

**Answer:** (D) n! (n factorial)  
**Explanation:** The number of permutations of n distinct objects is n! = n × (n-1) × (n-2) × ... × 2 × 1. For example, 3 objects can be arranged in 3! = 6 ways.

---

### Q7. [SSC Scientific Assistant CS 2017]
**The eigenvalues of a diagonal matrix are:**
- (A) Always 0
- (B) Always 1
- (C) The diagonal elements themselves
- (D) The sum of all elements

**Answer:** (C) The diagonal elements themselves  
**Explanation:** For a diagonal matrix, the eigenvalues are exactly the diagonal entries. This is because the characteristic polynomial of a diagonal matrix is the product of (λ - dᵢᵢ) for each diagonal element dᵢᵢ.

---

*Source: SSC Scientific Assistant IMD Previous Year Papers (2017, 2022) | testbook.com*


### Q8 [QID: 340] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which of the following does global table implementation of matrix table contain?

**Options:**
1) domain
2) object
3) right-set
4) All options are correct

**Correct Answer:** All options are correct

---

### Q9 [QID: 993] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
What are the three additional operations to change the contents of the access-matrix? A. copy B. owner C. deny D. control

**Options:**
1) Only A
2) Only A and B
3) Only A, B and D
4) All A, B, C and D

**Correct Answer:** Only A, B and D

---
