


# Network Computing - Intro Part 1: Architecture

## What is the Internet?
### 1. Nuts and Bolts View (Hardware)
- **[[Hosts]]** (aka End Systems):
    - Clients (Smartphones, Laptops) and Servers.
    - [cite_start]*Source:* Slide 5 
- **[[Communication Links]]**:
    - Physical media: Fiber optics, copper cables, radio spectrum.
    - [cite_start]*Source:* Slide 11 
- **[[Packet Switches]]**:
    - Hardware (Routers, Link-layer switches) that forwards packets.
    - [cite_start]*Source:* Slide 9 

### 2. Service View (Software/Utility)
- **Infrastructure**: Provides services to distributed applications (Web, VoIP, Gaming).
- **Programming Interface**: Hooks that allow sending/receiving data.
- [cite_start]*Source:* Slide 6 

## Network Structure
The Internet is a "Network of Networks".
- **[[Network Edge]]**:
    - Where users connect (Home networks, Enterprise networks, Mobile networks).
    - [cite_start]*Source:* Slide 10 [cite: 2287]
- **[[Network Core]]**:
    - Mesh of interconnected routers.
    - **[[ISP]]** (Internet Service Provider) Hierarchy:
        - **Access ISP**: Your direct connection.
        - **Regional ISP**: Connects access networks.
        - **Tier 1 ISP**: Global coverage.
    - [cite_start]*Source:* Slide 11 [cite: 2304]


#### **Cheat Sheet (Memory Hooks)**

- **Nuts & Bolts** = Hardware (Devices + Wires + Routers).
    
- **Service View** = Plumbing for Apps (Web, Email).
    
- **ISP Hierarchy**: Access (Local) $\rightarrow$ Regional (City/State) $\rightarrow$ Tier 1 (Global).


# Network Computing - Intro Part 2: Protocols & Context

## 1. Protocols
- **Definition**: Defines the **format**, **order**, and **actions** taken for message exchange.
- **Human Analogy**: A conversation ("Hi" -> "Hi" -> "Time?").
- **Network Analogy**: TCP Handshake (Connection request -> Ack).
- [cite_start]*Source:* Slide 22 

## 2. The Layered Model (Encapsulation)
The data changes names as it moves down the stack (like Russian Dolls):
1. [cite_start]**Application Layer**: Payload = **Message**[cite: 1240].
2. [cite_start]**Transport Layer**: Message + Header ($H_t$) = **Segment**[cite: 1244].
3. [cite_start]**Network Layer**: Segment + Header ($H_n$) = **Datagram**[cite: 1251].
4. [cite_start]**Link Layer**: Datagram + Header ($H_l$) = **Frame**[cite: 1257].

> **Note**: The "Packet Switch" (Router) generally operates up to the Network Layer (Datagrams), while "Link Switches" operate at the Link Layer (Frames).

## 3. Digital Context
- [cite_start]**Digital Divide**: 2.2 billion people remain offline[cite: 949].
- [cite_start]**Affordability**: Low-income users pay ~22x more relative to income.


#### **Cheat Sheet (Memory Hooks)**

- **Mnemonics for Data Units:** **S**ome **D**ogs **F**ly ( **S**egment $\rightarrow$ **D**atagram $\rightarrow$ **F**rame).
    
- **Protocol:** It's not just "talking"; it's the **rules** of talking.
    
- **Encapsulation:** Putting a letter (Application) $\rightarrow$ Envelope (Transport) $\rightarrow$ Mailbag (Network) $\rightarrow$ Truck (Link).



# Network Computing - Edge & Core

## 1. Network Edge (Access Networks)
- **[[DSL]]**: Uses telephone copper. Dedicated line. Speed decays with distance.
- **[[Cable Internet]]**: Uses TV coax. Shared medium (congestion possible). Asymmetric speeds.
- **[[Fiber (FTTH)]]**: Uses light. Symmetric, high speed.
- **[[Net Neutrality]]**: Principle that ISPs treat all data equally.
    - *Violations*: Throttling specific apps, Zero-rating (e.g., free data for specific music apps).
    - *Source*: 1_2_edge Slides 11, 18

## 2. Network Core (Packet Switching)
- **[[Packet Switching]]**: Breaking messages into packets to share network resources.
- **Core Functions**:
    1. **[[Forwarding]]**: Local action. Moving packet from Router Input $\rightarrow$ Router Output.
    2. **[[Routing]]**: Global action. Determining the source-destination path.
    - *Source*: 1_3_core Slide 7

#### **Cheat Sheet (Memory Hooks)**

- **Forwarding vs. Routing:** Forwarding is **tactical** (this intersection); Routing is **strategic** (the whole map).
    
- **Cable vs. DSL:** Cable = **Party Line** (Shared); DSL = **Private Call** (Dedicated).