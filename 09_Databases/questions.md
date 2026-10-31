# Databases (DBMS) - SSC Scientific Assistant IMD CS Questions

**Syllabus Topics:** ER-model, Relational Model, SQL, Integrity Constraints, Normal Forms, File Organization, Indexing, Transactions, Concurrency Control

---

## Questions from Previous Year Papers (SSC Scientific Assistant IMD)

---

### Q1. [SSC Scientific Assistant CS - 25 Nov 2017 Shift-2]
**The database environment has all of the following components EXCEPT:**
- (A) Users
- (B) Separate files
- (C) Database
- (D) DBMS software

**Answer:** (B) Separate files  
**Explanation:** The relational database environment consists of users, the database, and DBMS software. It does NOT use separate files — it integrates data into a unified database system.

---

### Q2. [SSC Scientific Assistant CS 2017]
**_______ represents raw facts, whereas _______ is data made meaningful:**
- (A) Information; data
- (B) Data; information
- (C) Database; table
- (D) Record; field

**Answer:** (B) Data; information  
**Explanation:** Data represents raw, unprocessed facts and figures. Information is data that has been processed and made meaningful through context and analysis.

---

### Q3. [SSC Scientific Assistant CS - 23 Nov 2017 Shift-1]
**Complex entities can be constructed using the following operations:**
- (A) Union, intersection, and difference
- (B) Aggregation, generalization, and specialization
- (C) Selection, projection, and join
- (D) Insert, update, and delete

**Answer:** (B) Aggregation, generalization, and specialization  
**Explanation:** In ER modeling, complex entities are built using aggregation (combining entities), generalization (combining entities into a higher-level entity), and specialization (breaking entities into sub-entities).

---

### Q4. [SSC Scientific Assistant CS 2017]
**The set of all possible values of data items is called:**
- (A) Attribute
- (B) Domain
- (C) Tuple
- (D) Schema

**Answer:** (B) Domain  
**Explanation:** In the relational model, the domain of an attribute is the set of all possible valid values that the attribute can take.

---

### Q5. [SSC Scientific Assistant CS 2017]
**A view of the database that appears to an application program is called:**
- (A) Schema
- (B) Subschema
- (C) Logical view
- (D) Physical view

**Answer:** (B) Subschema  
**Explanation:** The subschema (also called external schema or view) is the logical view of the data as it appears to a specific application program or user.

---

### Q6. [SSC Scientific Assistant CS 2017]
**A schema describes:**
- (A) Only the structure of tables
- (B) Attributes, data, and the relationships between each of the attributes; also describes files and tables used to represent them
- (C) Only the physical storage of data
- (D) Only the user interface

**Answer:** (B) Attributes, data, and the relationships between each of the attributes; also describes files and tables  
**Explanation:** A schema is a complete description of the database structure — it contains attributes, data types, relationships, and how data is organized.

---

### Q7. [SSC Scientific Assistant CS 2017]
**A top-to-bottom relationship among the items in a database is established by a:**
- (A) Network model
- (B) Relational model
- (C) Hierarchical model
- (D) Object-oriented model

**Answer:** (C) Hierarchical model  
**Explanation:** The hierarchical database model organizes data in a tree-like structure with parent-child (top-to-bottom) relationships between data items.

---

### Q8. [SSC Scientific Assistant CS 2017]
**Which command is used to remove all rows from a table without removing the table structure?**
- (A) DELETE
- (B) DROP
- (C) TRUNCATE
- (D) REMOVE

**Answer:** (C) TRUNCATE  
**Explanation:** The SQL TRUNCATE command removes all rows from a table but retains the table structure (schema). DROP removes the entire table including its structure.

---

### Q9. [SSC Scientific Assistant CS 2017]
**The primary key must be:**
- (A) A foreign key in another table
- (B) Unique and not null
- (C) Only numeric
- (D) Always a single column

**Answer:** (B) Unique and not null  
**Explanation:** A primary key must have a unique value for each record and cannot contain NULL values. It uniquely identifies each row in the table.

---

### Q10. [SSC Scientific Assistant CS 2017]
**The application program typically communicates with a database through:**
- (A) Only SQL directly
- (B) Both JDBC and ODBC
- (C) Only ODBC
- (D) Only JDBC

**Answer:** (B) Both JDBC and ODBC  
**Explanation:** Application programs communicate with databases through standard interfaces: JDBC (Java Database Connectivity) for Java applications and ODBC (Open Database Connectivity) for other applications.

---

### Q11. [SSC Scientific Assistant CS 2017]
**A DBMS that combines a DBMS and an application generator is called:**
- (A) Integrated DBMS
- (B) 4th Generation Language DBMS
- (C) Hybrid DBMS
- (D) Object DBMS

**Answer:** (B) 4th Generation Language (4GL) DBMS  
**Explanation:** A DBMS that combines database management with an application generator is called a 4GL (Fourth Generation Language) DBMS, allowing rapid application development.

---

*Source: SSC Scientific Assistant IMD Previous Year Papers (2017, 2022) | testbook.com*

---

### Q12. [SSC Scientific Assistant CS 2022 - 14/15 Dec 2022]
**Data about data is normally termed as:**
- (A) Big data
- (B) Raw data
- (C) Metadata
- (D) Processed data

**Answer:** (C) Metadata  
**Explanation:** Metadata is "data about data" — it provides information about the characteristics of data (like author, date created, file size, data type). It helps administrators understand and manage databases.

---

### Q13. [SSC Scientific Assistant CS 2017]
**Which type of relationship is a "one-to-many" relationship in databases?**
- (A) One record in Table A relates to only one record in Table B
- (B) One record in Table A can relate to many records in Table B, but each record in Table B relates to only one record in Table A
- (C) Many records in Table A can relate to many records in Table B
- (D) No relationship between tables

**Answer:** (B) One record in Table A can relate to many records in Table B  
**Explanation:** In a one-to-many relationship, a single record on the "one" side can be linked to multiple records on the "many" side. Example: One customer can have many orders.

---


### Q14 [QID: 368] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which of the following about the capabilities of GIS is true? A. Data capture and preparation B. Data management, including storage and maintenance C. Data manipulation and analysis D. Data presentation

**Options:**
1) Only A
2) Only B and C
3) Only A and C
4) All A, B, C and D

**Correct Answer:** All A, B, C and D

---

### Q15 [QID: 374] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
"A GIS is 'a set of tools for collecting, storing, retrieving at will, transforming, and displaying spatial data from the real world for a particular set of purposes" Which of the following list is the key area of GIS functionality missed out by the above definition?

**Options:**
1) Mapping
2) Reprojection
3) Collation
4) Analysis

**Correct Answer:** Analysis

---

### Q16 [QID: 375] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which of the following is not a key concept that is part of our definition of GIS?

**Options:**
1) GIS technologies include GPS and remote sensing.
2) GIS includes both computer systems (hardware) and computer programs (software).
3) GIS can be used in all areas of modern science.
4) People are an important part of GIS.

**Correct Answer:** GIS can be used in all areas of modern science.

---

### Q17 [QID: 376] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which of the following statements is true?

**Options:**
1) The basic data type char(n) is a fixed length character string and varchar (n) is equal length character.
2) The basic data type char(n) is a equal length character string and varchar(n) is variable length character.
3) The basic data type char(n) is a fixed length character string and varchar(n) is variable length character.
4) The basic data type char(n) is a variable length character string and varchar (n) is equal length character.

**Correct Answer:** The basic data type char(n) is a fixed length character

---

### Q18 [QID: 377] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
What type of statement is the following? Insert into instructor values (10211, 'Smith', 'Biology', 66000);

**Options:**
1) Query
2) DML
3) Relational
4) DDL

**Correct Answer:** DML

---

### Q19 [QID: 378] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Select name from instructor where dept name = 'Physics' order by name; By default, the order by clause lists items in ______ order.

**Options:**
1) Descending
2) Any
3) Same
4) Ascending

**Correct Answer:** Ascending

---

### Q20 [QID: 379] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which one of the following attribute can be taken as a primary key?

**Options:**
1) Name
2) Street
3) Id
4) Department

**Correct Answer:** Id

---

### Q21 [QID: 380] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
A attribute in a relation is a foreign key if which of the following keys from one relation is used as an attribute in that relation?

**Options:**
1) Candidate
2) Primary
3) Super
4) Sub

**Correct Answer:** Primary

---

### Q22 [QID: 381] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
The relation with the attribute which is the primary key is referenced in another relation. The relation which has the attribute as primary key is called

**Options:**
1) Referential relation
2) Referencing relation
3) Referenced relation
4) Referred relation

**Correct Answer:** Referencing relation

---

### Q23 [QID: 384] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which one is true about clustered index?

**Options:**
1) Clustered index is not associated with table
2) Clustered index is built by default on unique key columns
3) Clustered index is not built on unique key columns
4) None of these

**Correct Answer:** Clustered index is built by default on unique key columns

---

### Q24 [QID: 385] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
What is true about indexes?

**Options:**
1) Indexes enhance the performance even if the table is updated frequently
2) It makes harder for sql server engines to work to work on index which have large keys
3) It doesn't make harder for sql server engines to work to work on index which have large
4) None of these

**Correct Answer:** It makes harder for sql server engines to work to work on

---

### Q25 [QID: 386] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
A _________________ index is the one which satisfies all the columns requested in the query without performing further lookup into the clustered index.

**Options:**
1) Clustered
2) Non Clustered
3) Covering
4) B-Tree

**Correct Answer:** Covering

---

### Q26 [QID: 388] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Using the ______ clause retains only one copy of such identical tuples.

**Options:**
1) Null
2) Unique
3) Not null
4) Distinct

**Correct Answer:** Distinct

---

### Q27 [QID: 390] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
A relational algebra operation annotated with instructions on how to evaluate it is called

**Options:**
1) Evaluation algebra
2) Evaluation plan
3) Evaluation primitive
4) Evaluation engine

**Correct Answer:** Evaluation primitive

---

### Q28 [QID: 331] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
What is the full form of DBA ?

**Options:**
1) Data Bank Access
2) Database Access
3) Data Bank Administration
4) Database Administrator

**Correct Answer:** Database Administrator

---

### Q29 [QID: 332] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which of these is not TRUE in case of responsibilities of Database Administrator?

**Options:**
1) Acquiring hardware and software resources
2) Authorizing access to database
3) Data entry into the database
4) All options are correct

**Correct Answer:** All options are correct

---

### Q30 [QID: 333] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
DBMS is used to

**Options:**
1) Eliminate data redundancy
2) Maintain data integrity
3) Establish relationships among different files
4) All options are correct

**Correct Answer:** All options are correct

---

### Q31 [QID: 338] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which technique is used to restore a database up to the last consistent state after a system failure? A. Backup B. Recovery

**Options:**
1) Only A
2) Only B
3) Both A and B
4) None of these

**Correct Answer:** Only B

---

### Q32 [QID: 339] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
The command used to create a database user?

**Options:**
1) Make use
2) Create user
3) ADD user to database
4) All options are correct

**Correct Answer:** Create user

---

### Q33 [QID: 340] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which of the following is not an SQL command?

**Options:**
1) CREATE
2) DROP
3) ALTER
4) All are SQL commands

**Correct Answer:** All are SQL commands

---

### Q34 [QID: 342] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
An on-line commercial site such as Amazon.com is an example of ________.

**Options:**
1) single-user database application
2) multiuser database application
3) e-commerce database application
4) data mining database application

**Correct Answer:** e-commerce database application

---

### Q35 [QID: 350] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
For microcomputers, enquiry programs for files used for simple purposes are classified as_____.

**Options:**
1) storage package
2) database package
3) organized package
4) hardware package

**Correct Answer:** database package

---

### Q36 [QID: 396] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
In the world of GIS, another term for the property of connectivity is‌‌‌‌‌‌_____.

**Options:**
1) proximity
2) neighborhood
3) topology
4) Boolean identity

**Correct Answer:** topology

---

### Q37 [QID: 397] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which of the following are true of GIS? A. AM/FM is a specialized GIS B. Tabular data can be both and input and output of GIS

**Options:**
1) Only A
2) Only B
3) Both A and B
4) None of these

**Correct Answer:** Both A and B

---

### Q38 [QID: 398] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
What is the data stream?

**Options:**
1) The process by which maps are transferred between GIS platforms.
2) The flow of data from producer to GIS.
3) The flow of data from one user to another.
4) The process by which raw spatial data is processed into an integrated GIS database.

**Correct Answer:** The process by which raw spatial

---

### Q39 [QID: 400] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
You work for the corporate office of a popular retail company that has recently begun using a GIS system. Which of the following would NOT be a good reason to use this system?

**Options:**
1) To track new retail locations
2) To track store credit card customers who have since closed their accounts
3) To track customers
4) To track existing retail locations

**Correct Answer:** To track store credit card customers

---

### Q40 [QID: 975] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
Which of the following are full-fledged GIS packages? A. ILWIS B. GeoMedia C. ArcGIS D. Corp

**Options:**
1) Only A
2) Only A and B
3) A, B and C only
4) A, B, C and D

**Correct Answer:** A, B, C and D

---

### Q41 [QID: 976] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
What type of statement is the following? Create table employee (name varchar ,id integer)

**Options:**
1) DML
2) DDL
3) View
4) Integrity constraint

**Correct Answer:** DDL

---

### Q42 [QID: 978] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
In the SQL given below, identify the error. Select * from employee where dept_name= "Comp Sci";

**Options:**
1) Dept_name
2) Employee
3) "Comp Sci"
4) From

**Correct Answer:** "Comp Sci"

---

### Q43 [QID: 979] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
In SQL the spaces at the end of the string are removed by which of the following functions?

**Options:**
1) Upper
2) String
3) Trim
4) Lower

**Correct Answer:** Trim

---

### Q44 [QID: 980] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
The subset of super key is a candidate key under what condition?

**Options:**
1) No proper subset is a super key
2) All subsets are super keys
3) Subset is a super key
4) Each subset is a super key

**Correct Answer:** No proper subset is a super key

---

### Q45 [QID: 985] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
How many types of indexes are there in sql server?

**Options:**
1) 4
2) 3
3) 2
4) 5

**Correct Answer:** 2

---

### Q46 [QID: 930] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [EN]

**Question:**
A top-to-bottom relationship among the items in a database is established by a

**Options:**
1) Hierarchical schema
2) Network schema
3) Relational schema
4) All options are correct

**Correct Answer:** Hierarchical schema

---

### Q47 [QID: 931] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [EN]

**Question:**
Which of these is not a database object?

**Options:**
1) Index
2) Sequence
3) Cursor
4) Trigger

**Correct Answer:** Cursor

---

### Q48 [QID: 934] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [EN]

**Question:**
Which of the following is an example of network database?

**Options:**
1) IDBS
2) Ingress
3) Oracle
4) DBMS

**Correct Answer:** IDBS

---

### Q49 [QID: 935] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [EN]

**Question:**
What is used for database security?

**Options:**
1) data encryption
2) a view
3) finger print
4) All options are correct

**Correct Answer:** All options are correct

---

### Q50 [QID: 942] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [HI]

**Question:**
DBMS जो DBMS और एप्लिकेशन प्रबंधक को संयोजित करता है ____ कहलाता है।

**Options:**
1) 2) Microsoft's Access
3) IBM's DB2
4) Oracle Corporation's Oracle

**Correct Answer:** Microsoft's Access

---

### Q51 [QID: 943] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [HI]

**Question:**
नीचे से वह SQL कथन ढूँढें जो निम्नलिखित के बराबर हो: SELECT NAME FROM CUSTOMER WHERE STATE = 'VA';

**Options:**
1) SELECT NAME IN CUSTOMER WHERE STATE IN ('VA');
2) SELECT NAME IN CUSTOMER WHERE STATE = 'VA';
3) SELECT NAME IN CUSTOMER WHERE STATE = 'V';
4) SELECT NAME FROM CUSTOMER WHERE STATE IN ('VA');

**Correct Answer:** SELECT NAME FROM CUSTOMER WHERE STATE IN ('VA');

---

### Q52 [QID: 944] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [HI]

**Question:**
ऑब्जेक्ट-ओरिएंटेड डेटाबेस (ODBMS) के संदर्भ में निम्नलिखित में कौन सा विकल्प सही है?

**Options:**
1) उनमें जटिल डेटा प्रकारों को वेब पर संग्रहीत करने की क्षमता होती है
2) ये सभी एप्लिकेशन के लिए RDBMS को ओवरटेक कर रहे हैं
3) ये पारंपरिक दो-विमिय डेटाबेस तालिका एप्लिकेशन के लिए सबसे अधिक उपयोगी होते हैं
4) सभी विकल्प सही हैं

**Correct Answer:** उनमें जटिल डेटा प्रकारों को वेब पर संग्रहीत करने की क्षमता होती है

---

### Q53 [QID: 996] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [HI]

**Question:**
परिभाषा के आधार पर GIS में क्या सम्मिलित होना आवश्यक है: A. डेटा रिपोर्टिंग एवं उत्पाद निर्माण हेतु एक सबसिस्टम B. डेटा संचयन, पुनः प्राप्ति, एवं निरूपण हेतु एक मेथड C. डेटा विश्लेषण फंक्शन D. स्थानिक और गैर-स्थानिक डेटा प्रविष्ट करने हेतु एक साधन|

**Options:**
1) केवल A और B
2) केवल B और C
3) केवल A, B और D
4) सभी A, B, C और D

**Correct Answer:** सभी A, B, C और D

---

### Q54 [QID: 999] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [HI]

**Question:**
निम्न में से किसे GIS का चौथा आयाम माना जा सकता है?

**Options:**
1) समय
2) स्थान
3) स्केल
4) स्पेस

**Correct Answer:** समय

---

### Q55 [QID: 1000] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [HI]

**Question:**
GIS का प्रयोग किसका अनुमान लगाने के लिए नहीं किया जा सकता?

**Options:**
1) प्रतिरूप
2) टेबल
3) ट्रेंड
4) संबंध

**Correct Answer:** टेबल

---

### Q56 [QID: 931] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
A data model is: A. used to describe structure of a database B. set of basic operations on the database

**Options:**
1) Only A
2) Only B
3) Both A and B
4) None of these

**Correct Answer:** Both A and B

---

### Q57 [QID: 934] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
The database environment has all of the following components except

**Options:**
1) Users
2) separate files
3) database
4) database administrator

**Correct Answer:** separate files

---

### Q58 [QID: 936] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
Prevention of access to the database by unauthorized users is referred to as:

**Options:**
1) Integrity
2) Productivity
3) Security
4) Reliability

**Correct Answer:** Security

---

### Q59 [QID: 939] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
This is an authorization command of SQL:

**Options:**
1) Access
2) Grant
3) Allow
4) None of these

**Correct Answer:** Grant

---

### Q60 [QID: 942] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
Stored procedures have which of the following advantages?

**Options:**
1) It takes a longer time to write them as compared to writing Visual Basic
2) Network traffic increases
3) Data integrity improves as multiple applications access the same stored procedure
4) Result in thicker client and thinner database server

**Correct Answer:** Data integrity improves as multiple applications access the same

---

### Q61 [QID: 943] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
To remove duplicate rows from the results of an SQL SELECT statement, the ________ qualifier specified must be included.

**Options:**
1) ONLY
2) UNIQUE
3) DISTINCT
4) SINGLE

**Correct Answer:** DISTINCT

---

### Q62 [QID: 944] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
________ is an open source DBMS product that runs on UNIX, Linux and Windows.

**Options:**
1) MySQL
2) JSP/SQL
3) JDBC/SQL
4) Sun ACCESS

**Correct Answer:** MySQL

---

### Q63 [QID: 996] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
Considerable information and data for GIS is available on the Internet, which of the following formats must be transmitted in binary format? A. .dxf B. .zip files C. .gif files D. html files E. DLGs and DEMs

**Options:**
1) Only A, B and C
2) Only C, D and E
3) Only D
4) Only D and E

**Correct Answer:** Only A, B and C

---

### Q64 [QID: 997] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
Which of the following are areas of GIS application in commercial industry? A. Oil and gas exploration B. Dispatch of emergency medical services C. Timber and lumber production D. Managing telecommunication networks

**Options:**
1) Only A
2) Only A and B
3) Only B and C
4) Only A, B, and D.

**Correct Answer:** Only A, B, and D.

---

### Q65 [QID: 999] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
Which of the following statements is/are true? A. Keyboard entry is no longer used in GIS projects. B. A pseudonode is a node which can be removed from a vector dataset without affecting the topology.

**Options:**
1) Only A
2) Only B
3) Both A and B
4) None of these

**Correct Answer:** Only B

---

### Q66 [QID: 1000] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
Who is the leading company for GIS business applications?

**Options:**
1) MapInfo Inc
2) ESRI
3) AccuGrade
4) GoogleEarth

**Correct Answer:** ESRI

---
