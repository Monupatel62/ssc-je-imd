# Computer Networks - SSC Scientific Assistant IMD CS Questions

**Syllabus Topics:** ISO/OSI Model, LAN, WAN, IP addressing, TCP/UDP, DNS, Routing, Firewalls, Network Security

---

## Questions from Previous Year Papers (SSC Scientific Assistant IMD)

---

### Q1. [SSC Scientific Assistant CS 2017]
**Why is IP protocol considered unreliable?**
- (A) Because it uses encryption
- (B) Because it does not guarantee delivery, ordering, or error checking of packets
- (C) Because it requires a dedicated connection
- (D) Because it is very slow

**Answer:** (B) Because it does not guarantee delivery, ordering, or error checking of packets  
**Explanation:** IP (Internet Protocol) is a connectionless, unreliable protocol — it does not guarantee delivery, packet ordering, or data integrity. These are handled by higher-layer protocols like TCP.

---

### Q2. [SSC Scientific Assistant CS 2017]
**How many layers are present in the TCP/IP Reference model?**
- (A) 7
- (B) 5
- (C) 4
- (D) 3

**Answer:** (C) 4  
**Explanation:** The TCP/IP model has 4 layers: (1) Network Access Layer, (2) Internet Layer, (3) Transport (Host-to-Host) Layer, and (4) Application Layer.

---

### Q3. [SSC Scientific Assistant CS 2017]
**What does the port number in a TCP connection specify?**
- (A) The IP address of the destination
- (B) The communication process on the two end systems
- (C) The routing path for data packets
- (D) The physical address of the network card

**Answer:** (B) The communication process (application) on the two end systems  
**Explanation:** Port numbers identify specific processes/applications on the end systems. They allow multiple applications to use the network simultaneously on the same IP address.

---

### Q4. [SSC Scientific Assistant CS 2017]
**The data field in an IP datagram can carry which of the following?**
- (A) Only TCP segments
- (B) Transport layer segments (TCP/UDP) or ICMP messages
- (C) Only application data directly
- (D) Only UDP datagrams

**Answer:** (B) Transport layer segments (TCP/UDP) or ICMP messages  
**Explanation:** The IP datagram's data field typically carries transport layer segments (TCP or UDP). It can also carry ICMP messages. Application layer data (like SMTP) must first pass through the transport layer.

---

### Q5. [SSC Scientific Assistant CS 2017]
**Which of the following are protocols of the Application Layer?**
- (A) TCP, UDP, IP
- (B) HTTP, FTP, SMTP, DNS
- (C) ARP, RARP, ICMP
- (D) Ethernet, Wi-Fi

**Answer:** (B) HTTP, FTP, SMTP, DNS  
**Explanation:** HTTP (web), FTP (file transfer), SMTP (email), and DNS (name resolution) are application layer protocols. TCP/UDP are transport layer; IP is network layer.

---

### Q6. [SSC Scientific Assistant CS 2017]
**Controlling access to a network by analyzing the incoming and outgoing packets and allowing or rejecting them depending on the source and destination IP addresses is called:**
- (A) Intrusion Detection
- (B) Packet filtering
- (C) Encryption
- (D) NAT (Network Address Translation)

**Answer:** (B) Packet filtering  
**Explanation:** Packet filtering is a firewall technique that examines incoming and outgoing packets and allows or blocks them based on rules like source/destination IP, port numbers, etc.

---

### Q7. [SSC Scientific Assistant CS 2017]
**Routing tables of a router keep track of:**
- (A) IP addresses of connected devices
- (B) Routes to use for forwarding data to its destination
- (C) The speed of each network interface
- (D) The MAC addresses of neighboring routers

**Answer:** (B) Routes to use for forwarding data to its destination  
**Explanation:** Routing tables contain information about network paths — they store routes (destination networks and next-hop addresses) to forward data packets to their destination.

---

### Q8. [SSC Scientific Assistant CS 2017]
**What does a Router do in a network?**
- (A) Connects devices within the same LAN segment
- (B) Forwards data packets between different networks using packet switching, filtering, and path selection
- (C) Only amplifies network signals
- (D) Converts digital to analog signals

**Answer:** (B) Forwards data packets between different networks  
**Explanation:** Routers forward data packets between different networks (internetworking). They provide packet switching, packet filtering, network communication, and path selection services.

---

### Q9. [SSC Scientific Assistant CS 2017]
**Which of the following principles do most packet switches use?**
- (A) Circuit switching
- (B) Store-and-forward transmission
- (C) Dedicated path connection
- (D) Synchronous transmission

**Answer:** (B) Store-and-forward transmission  
**Explanation:** Packet switches use store-and-forward transmission — they receive the complete packet before forwarding it. Messages are broken into packets, each forwarded independently based on source/destination address.

---

### Q10. [SSC Scientific Assistant CS 2017]
**Which of the following statements cannot be associated with layered network architecture?**
- (A) Each layer communicates with the layer above and below it
- (B) Functionality at one layer in NO WAY requires information from another layer
- (C) Layers provide services to the layer above
- (D) Each layer has a specific role/function

**Answer:** (B) Functionality at one layer in NO WAY requires information from another layer  
**Explanation:** This is FALSE about layered architecture — layers DO depend on each other. Each layer provides services to the layer above and uses services of the layer below. Total independence between layers is not possible.

---

### Q11. [SSC Scientific Assistant CS 2017]
**Which of the following is NOT capable of storing binary data (in network context — about network devices)?**
- (A) Router
- (B) Switch
- (C) Hub
- (D) Buffer

**Answer:** (C) Hub (or Switch depending on context)  
**Explanation:** A hub is a simple device that does not store data — it just broadcasts signals. Switches store MAC address tables. Routers and buffers store packet data.

---

*Source: SSC Scientific Assistant IMD Previous Year Papers (2017, 2022) | testbook.com*


### Q12 [QID: 301] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which of the following units can be used to measure the speed of a computer?

**Options:**
1) Both SYPS and MIPS
2) Both MIPS and FLOP
3) BAUD
4) Both BAUD and SYPS

**Correct Answer:** Both MIPS and FLOP

---

### Q13 [QID: 311] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which of the following refers to anonymous FTP?

**Options:**
1) Internet file transfer protocol
2) Protocol that requires password
3) None access files
4) None of these

**Correct Answer:** Internet file transfer protocol

---

### Q14 [QID: 356] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Among the optical-distribution architectures which of the following is essentially switched Ethernet?

**Options:**
1) AON
2) PON
3) NON
4) None of these

**Correct Answer:** AON

---

### Q15 [QID: 358] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
By which of the following layers is delimiting and synchronization of data exchange provided?

**Options:**
1) Application layer
2) Session layer
3) Transport layer
4) Link layer

**Correct Answer:** Session layer

---

### Q16 [QID: 359] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which of the following statements is not true?

**Options:**
1) Framing task is not done by data link layer.
2) Error control task is not done by data link layer.
3) Flow control task is not done by data link layer.
4) Channel coding task is not done by data link layer.

**Correct Answer:** Channel coding task is not done by data link layer.

---

### Q17 [QID: 360] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which of the following statements is true?

**Options:**
1) CRC stands for cyclic redundancy check.
2) CRC stands for code repeat check.
3) CRC stands for code redundancy check.
4) CRC stands for cyclic repeat check.

**Correct Answer:** CRC stands for cyclic redundancy check.

---

### Q18 [QID: 366] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
There is a network that needs 29 subnets while maximizing the number of host addresses available on each subnet. How many bits must be borrowed from the host field to provide the correct subnet mask?

**Options:**
1) 3
2) 4
3) 6
4) 5

**Correct Answer:** 5

---

### Q19 [QID: 367] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
If the TTL field has value 10, then which of the following statements is true?

**Options:**
1) 11 routers (max) can process this datagram.
2) 5 routers (max) can process this datagram.
3) 10 routers (max) can process this datagram.
4) 1 router (max) can process this datagram.

**Correct Answer:** 10 routers (max) can process this datagram.

---

### Q20 [QID: 382] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which of the following does Html code contain?

**Options:**
1) Tags
2) Attributes
3) Elements
4) All options are correct

**Correct Answer:** All options are correct

---

### Q21 [QID: 383] - SSC IMD 22 Nov 2017 Shift 1 (Computer Science)

**Question:**
A __________ is a program running on the server machine, which accepts requests from a Web browser and sends back results in the form of HTML documents.

**Options:**
1) HTML
2) HTTP
3) Web Server
4) Web browser

**Correct Answer:** Web Server

---

### Q22 [QID: 309] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
The time interval between adjacent bits is called the.

**Options:**
1) Word-time
2) Bit-time
3) Turn around time
4) Slice time

**Correct Answer:** Bit-time

---

### Q23 [QID: 313] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
Office LANS, which are scattered geographically on large scale, can be connected by the use of corporate__________.

**Options:**
1) CAN
2) LAN
3) DAN
4) WAN

**Correct Answer:** WAN

---

### Q24 [QID: 316] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
What is the full form of AJAX ?

**Options:**
1) asynchronous javascript and xml
2) advanced JSP and xml
3) asynchronous JSP and xml
4) advanced javascript and xml

**Correct Answer:** asynchronous javascript and xml

---

### Q25 [QID: 317] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
For error detection ________ is used by the higher layer protocols (TCP/IP).

**Options:**
1) Bit-sum
2) Checksum
3) Data-sum
4) Error-bit

**Correct Answer:** Checksum

---

### Q26 [QID: 318] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
What is a Firewall in Computer Network?

**Options:**
1) The physical boundary of Network
2) An operating System of Computer Network
3) A system designed to prevent unauthorized access
4) A web browsing Software

**Correct Answer:** A system designed to prevent

---

### Q27 [QID: 319] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
Why IP Protocol is considered as unreliable?

**Options:**
1) A packet may be lost
2) Packets may arrive out of order
3) Duplicate packets may be generated
4) All options are correct

**Correct Answer:** All options are correct

---

### Q28 [QID: 320] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
What is the size of MAC Address?

**Options:**
1) 16-bits
2) 32-bits
3) 48-bits
4) 64-bits

**Correct Answer:** 48-bits

---

### Q29 [QID: 321] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
Which of the following is / are Protocols of Application layer?

**Options:**
1) FTP
2) DNS
3) Telnet
4) All options are correct

**Correct Answer:** All options are correct

---

### Q30 [QID: 322] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
In Satellite based communication, VSAT stands for?

**Options:**
1) Very Small Aperture Terminal
2) Varying Size Aperture Terminal
3) Very Small Analog Terminal
4) None of these

**Correct Answer:** Very Small Aperture Terminal

---

### Q31 [QID: 323] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
Comments in XML document is given by:

**Options:**
1) 2)
3) 4)

**Correct Answer:** 3

---

### Q32 [QID: 324] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
The latest HTML standard is

**Options:**
1) XML
2) SGML
3) HTML 4.0
4) HTML 5.0

**Correct Answer:** HTML 5.0

---

### Q33 [QID: 325] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
In fiber optic communications, the signal source is___.

**Options:**
1) Light
2) Radio
3) Very low frequency
4) Microwave frequency

**Correct Answer:** Light

---

### Q34 [QID: 328] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
In Cascading Style Sheets (CSS) what does “font-size” can be called as?

**Options:**
1) Selector
2) Rule
3) Property
4) Property-Name

**Correct Answer:** Property-Name

---

### Q35 [QID: 345] - SSC IMD 23 Nov 2017 Shift 1 (Computer Science)

**Question:**
The data field can carry which of the following?

**Options:**
1) TCP segment
2) UDP segment
3) ICMP messages
4) None of these

**Correct Answer:** ICMP messages

---

### Q36 [QID: 958] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
In Internet protocol stack, which of the following is the 5th layer to receive data at B, when data is sent from device A to device B?

**Options:**
1) Application layer
2) Transport layer
3) Link layer
4) Session layer

**Correct Answer:** Application layer

---

### Q37 [QID: 963] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
Which of the following statements is true with respect to TCP?

**Options:**
1) Connection-oriented
2) Process-to-process
3) Transport layer protocol
4) All options are correct

**Correct Answer:** All options are correct

---

### Q38 [QID: 964] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
Which of the following refers to a piece of icon or image on a web page associated with another webpage?

**Options:**
1) url
2) hyperlink
3) plugin
4) None of these

**Correct Answer:** hyperlink

---

### Q39 [QID: 966] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
The maximum number of IP addresses that can be assigned to hosts on a local subnet that uses the 255.255.255.224 subnet mask are

**Options:**
1) 17
2) 18
3) 19
4) 30

**Correct Answer:** 30

---

### Q40 [QID: 982] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
How many levels of headings are in html?

**Options:**
1) 3
2) 6
3) 8
4) 5

**Correct Answer:** 6

---

### Q41 [QID: 984] - SSC IMD 23 Nov 2017 Shift 2 (Computer Science)

**Question:**
Which of the following is a valid uniform resource locator?

**Options:**
1) http://www.acm.org/sigmod
2) www.google.com
3) www.ann.in
4) http:/www.acm.org/sigmod/

**Correct Answer:** http://www.acm.org/sigmod

---

### Q42 [QID: 916] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [EN]

**Question:**
What is the subnetwork number of a host with an IP address of 172.16.66.0/21?

**Options:**
1) 172.16.36.0
2) 172.16.48.0
3) 172.16.64.0
4) 172.16.0.0

**Correct Answer:** 172.16.64.0

---

### Q43 [QID: 917] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [EN]

**Question:**
Controlling access to a network by analyzing the incoming and outgoing packets is called

**Options:**
1) IP Filtering
2) Data Filtering
3) Packet Filtering
4) Firewall Filtering

**Correct Answer:** Packet Filtering

---

### Q44 [QID: 918] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [EN]

**Question:**
DNS is the abbreviation of

**Options:**
1) Dynamic Name System
2) Dynamic Network System
3) Domain Name System
4) Domain Network Service

**Correct Answer:** Domain Name System

---

### Q45 [QID: 919] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [EN]

**Question:**
What does Router do in a network?

**Options:**
1) Forwards a packet to all outgoing links
2) Forwards a packet to the next free outgoing link
3) Determines on which outing link a packet is to be forwarded
4) Forwards a packet to all outgoing links except the originated link

**Correct Answer:** Determines on which outing link a packet is to be forwarded

---

### Q46 [QID: 920] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [EN]

**Question:**
Routing tables of a router keeps track of

**Options:**
1) MAC Address Assignments
2) Port Assignments to network devices
3) Distribute IP address to network devices
4) Routes to use for forwarding data to its destination

**Correct Answer:** Routes to use for forwarding data to its destination

---

### Q47 [QID: 921] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [EN]

**Question:**
What does the port number in a TCP connection specify?

**Options:**
1) It specifies the communication process on the two end systems
2) It specifies the quality of the data & connection
3) It specifies the size of data
4) All options are correct

**Correct Answer:** It specifies the communication process on the two end systems

---

### Q48 [QID: 923] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [EN]

**Question:**
Choose the correct HTML code to create an email link?

**Options:**
1) <A HREF = “user1@business.com”></A>
2) <A HREF = “mailto:“user1@business.com”></A>
3) <MAIL>“user1@business.com </MAIL>
4) <A MAILHREF = “user1@business.com”></A>

**Correct Answer:** <A HREF = “mailto:“user1@business.com”></A>

---

### Q49 [QID: 924] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [EN]

**Question:**
Which topology is used in Ethernet?

**Options:**
1) Bus Topology
2) Ring Topology
3) Tree Topology
4) Mesh Topology

**Correct Answer:** Bus Topology

---

### Q50 [QID: 925] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [EN]

**Question:**
Ethernet is a standard for

**Options:**
1) LAN
2) MAN
3) WAN
4) All options are correct

**Correct Answer:** LAN

---

### Q51 [QID: 927] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [EN]

**Question:**
What is a web browser?

**Options:**
1) a program that can display a web page
2) a program used to view html documents
3) it enables user to access the resources of internet
4) All options are correct

**Correct Answer:** All options are correct

---

### Q52 [QID: 928] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [EN]

**Question:**
What is the latest version of CSS available?

**Options:**
1) CSS2
2) CSS3
3) CSS3.1
4) CSS4

**Correct Answer:** CSS4

---

### Q53 [QID: 929] - SSC IMD 24 Nov 2017 Shift 2 (Computer Science) [EN]

**Question:**
How many layers are present in the TCP/IP Reference model?

**Options:**
1) 6
2) 7
3) 5
4) 4

**Correct Answer:** 4

---

### Q54 [QID: 916] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
What is document object model (DOM)?

**Options:**
1) Method for representing and interacting with objects in html documents
2) An application programming interface
3) Hierarchy of objects in ASP.NET
4) None of these

**Correct Answer:** Method for representing and interacting with objects in html

---

### Q55 [QID: 919] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
Router operates in which layer of OSI Reference Model?

**Options:**
1) Layer 1 (Physical Layer)
2) Layer 3 (Network Layer)
3) Layer 4 (Transport Layer)
4) Layer 7 (Application Layer)

**Correct Answer:** Layer 3 (Network Layer)

---

### Q56 [QID: 920] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
Repeater operates in which layer of the OSI model?

**Options:**
1) Physical layer
2) Data link layer
3) Network layer
4) Transport layer

**Correct Answer:** Physical layer

---

### Q57 [QID: 921] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
What is the size of Host bits in Class B of IP address?

**Options:**
1) 04
2) 08
3) 16
4) 32

**Correct Answer:** 16

---

### Q58 [QID: 923] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
Which statement is true?

**Options:**
1) An XML document can have one root element
2) An XML document can have one child element
3) XML elements have to be in lower case
4) All options are correct

**Correct Answer:** An XML document can have one root element

---

### Q59 [QID: 927] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
What is the access point (AP) in wireless LAN? A. device that allows wireless devices to connect to a wired network B. wireless devices itself

**Options:**
1) ONLY A
2) ONLY B
3) Both A and B
4) None of these

**Correct Answer:** ONLY A

---

### Q60 [QID: 928] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
Which of the following is the open source software version of the desktop web browser

**Options:**
1) Google Chrome
2) Mozilla FireFox
3) Internet Explorer
4) Erwise

**Correct Answer:** Mozilla FireFox

---

### Q61 [QID: 929] - SSC IMD 25 Nov 2017 Shift 2 (Computer Science)

**Question:**
The complete form of SMTP is ________

**Options:**
1) Service Message Transmission Permission
2) Secure Message Transfer Protocol
3) Simple Mail Transfer Protocol
4) Simple Message Transfer Protocol

**Correct Answer:** Simple Mail Transfer Protocol

---
