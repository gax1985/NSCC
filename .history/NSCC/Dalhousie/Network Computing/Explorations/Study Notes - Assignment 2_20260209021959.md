# 🌐 Network Computing: The Complete Course (Week 1-2)

## 📚 Module 1: Introduction to the Internet

### 1.1 What is the Internet?
The Internet can be defined in two ways: the "Nuts and Bolts" (Hardware) and the "Service" (Software).

#### 🛠️ The "Nuts and Bolts" View (Hardware)
* **End Systems (Hosts):** The billions of connected computing devices (smartphones, laptops, servers, IoT).
* **Communication Links:** The physical media that transmit bits.
    * **Fiber Optics:** Uses light pulses; high speed, low error rate.
    * **Copper (Coax/Twisted Pair):** Uses electrical signals; cheaper but higher attenuation.
    * **Radio Spectrum:** Wireless transmission (Wi-Fi, 5G, Satellite).
* **Packet Switches:** Hardware that forwards data chunks (packets) toward their destination.
    * **Routers:** Typically operate in the **Network Core** (Layer 3).
    * **Link-Layer Switches:** Typically operate in Access Networks (Layer 2).

#### 💁‍♀️ The "Service" View (Software)
* **Infrastructure:** A global platform that provides services to distributed applications (Web, VoIP, Gaming, Email).
* **Socket Interface:** The API (Application Programming Interface) that allows software to "ask" the network to deliver data. It is analogous to a postal drop-box.

---

### 1.2 The Network Structure
The Internet is a "Network of Networks". No single entity owns it; it is a hierarchy of ISPs (Internet Service Providers).



#### 🏠 The Network Edge
* **Definition:** The part of the network where end systems (users) connect.
* **Components:** Home networks, Enterprise networks, Mobile networks.

#### 🧠 The Network Core
* **Definition:** The mesh of interconnected routers that moves data across the globe.
* **The ISP Hierarchy:**
    1.  **Access ISP (Tier 3):** The "Last Mile" provider (e.g., Bell, Rogers, Comcast). Connects directly to the user.
    2.  **Regional ISP (Tier 2):** Connects Access ISPs to the backbone.
    3.  **Tier 1 ISP (The Backbone):** The global "superhighways" (e.g., AT&T, NTT, Level 3). They treat each other as equals and do not pay each other for traffic (peering).

---

### 1.3 Protocols & Layers
This is the "Language" of the Internet.

#### 🗣️ What is a Protocol?
A protocol defines the **format** and **order** of messages exchanged between two or more communicating entities, as well as the **actions taken** on the transmission and/or receipt of a message or other event.
* *Human Analogy:* "Hi" $\to$ "Hi" $\to$ "What time is it?" $\to$ "2:00 PM".
* *Network Analogy:* TCP Connection Request $\to$ TCP Connection Response.

#### 📦 The Layered Model (Encapsulation)
To manage complexity, the Internet uses a 5-layer model. Data changes its name (Protocol Data Unit - PDU) as it moves down the stack.



| Layer | PDU Name | Analogy | Function |
| :--- | :--- | :--- | :--- |
| **5. Application** | **Message** | The Letter | Supporting network applications (HTTP, SMTP, FTP). |
| **4. Transport** | **Segment** | The Envelope | Process-process data transfer (TCP, UDP). Adds reliability/flow control headers. |
| **3. Network** | **Datagram** | Mailbag | Routing of datagrams from source to destination (IP). |
| **2. Link** | **Frame** | The Truck | Data transfer between neighboring network elements (Ethernet, Wi-Fi). |
| **1. Physical** | **Bits** | The Road | Bits "on the wire". |

> **Encapsulation:** Sending = **Adding** headers (moving down). Receiving = **Stripping** headers (moving up).

---

## 📡 Module 2: The Network Edge (Access Networks)

How do we actually connect to the Edge Router?

### ☎️ DSL (Digital Subscriber Line)
* **Medium:** Uses existing **telephone copper wires**.
* **Architecture:** Dedicated line to the Central Office (DSLAM).
* **Pros:** Guaranteed bandwidth (not shared with neighbors).
* **Cons:** Speed degrades significantly with distance from the central office.

### 📺 Cable Internet
* **Medium:** Hybrid Fiber Coax (HFC) - Uses existing **Cable TV cabling**.
* **Architecture:** **Shared broadcast medium**. All homes in a neighborhood connect to the same head-end.
* **Pros:** Often higher peak speeds than DSL.
* **Cons:** **Congestion**. If neighbors download massive files, your speed drops. Asymmetric (Download >> Upload).

### 💡 Fiber to the Home (FTTH)
* **Medium:** Optical fiber (glass) all the way to the home.
* **Pros:** Highest speeds, low latency, symmetric bandwidth. Future-proof.

### ⚖️ Net Neutrality
* **Principle:** ISPs must treat all Internet communications equally, without discrimination based on content, user, or platform.
* **Violations:** Throttling (slowing down specific apps), Blocking, Zero-rating (exempting specific apps from data caps).

---

## 🧠 Module 3: The Network Core

The Core is a mesh of packet switches and links.



[Image of Packet switching vs circuit switching]


### 📦 Packet Switching
* **Definition:** Hosts break application-layer messages into packets. These packets travel link-by-link to the destination.
* **Store-and-Forward:** The router must receive the **entire** packet before it can begin transmitting it to the next link.
    * *Result:* This causes **Transmission Delay** at every hop.

### 🚦 Two Key Core Functions
Every router performs two distinct tasks:
1.  **Forwarding (The "Local" Action):**
    * Moving a packet from a router's input link to the appropriate output link.
    * *Analogy:* Driving through a single intersection.
2.  **Routing (The "Global" Action):**
    * Determining the route taken by packets from source to destination.
    * *Analogy:* Planning the trip from Halifax to Vancouver using a map.

---

## 🧮 Module 4: Performance Math (The Physics)

### ⏱️ Delays
Total Nodal Delay = $d_{proc} + d_{queue} + d_{trans} + d_{prop}$

1.  **Processing Delay ($d_{proc}$):** Time to check bit errors and determine output link. (Usually negligible).
2.  **Queueing Delay ($d_{queue}$):** Time waiting at output link for transmission. Depends on congestion.
3.  **Transmission Delay ($d_{trans}$):** Time to push the packet onto the wire.
    * Formula: $$d_{trans} = \frac{L}{R}$$
    * $L$ = Packet length (bits)
    * $R$ = Link bandwidth (bps)
4.  **Propagation Delay ($d_{prop}$):** Time for the signal to travel the physical distance.
    * Formula: $$d_{prop} = \frac{Distance}{Speed}$$

### 💧 Throughput (Bottleneck)
* **Throughput:** The rate (bits/sec) at which data is transferred between sender and receiver.
* **Bottleneck Link:** The link on the end-end path that constrains the end-end throughput.
    * *Rule:* Throughput is `Min(R_1, R_2, ..., R_n)`.
    * *Shared Links:* If a link $R$ is shared by $N$ flows, the available bandwidth is $R/N$.