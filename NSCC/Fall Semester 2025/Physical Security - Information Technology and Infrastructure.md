


Back in 1994, Ron was instrumental in forming Masters of Digital Networking. His company convinced CISCO to donate equipment. They are generous to educational programs. 

When he formed his last company in 2010, he knew that he will go into three years of research and development. He needed the best research scientist to hire for the company. 

## OSI 7-Layer Model 


Every operating system produces its own version of the OSI Model. The requirement for the different networking models is *matching the functionality of the original OSI Model*. When you do this work, you have to understand the networking stack used by your operating system. In Microsoft Windows, the system that is used is **.NET**. Windows changes all the time, including its architecture and  *Memory Models*. The programming language that gave the functionality is the **C# Language**, which is designed to interact with **.NET**.  

When it comes to the OSI 7-layer model, we start with the lowest layer of the networking stack : 


### Application  

Our machine --> Descends down from the **Application Layer**. This is the most misunderstood layer of the OSI model. People think commonly that the *Application Layer* involves application. The best way to demonstrate it is **APIs**. You can take data from one source, and convert it to something else. One example is taking a JSON file and converting it to a CSV file. The API allows you to extract data from that system unto a different format matching your requirements. This is the layer used to enter data into the Networking Stack. 

If there is traffic emerging from your network stack, and bound to an application (email , etc ...), it exports the data from the network stack unto how it will be used. Ron came up with a new idea :

>[!question]
>"How do you stop traffic completely except for the traffic you want?"
>
>>[!answer]
>>`1. We can reach into the stack, capture the packet and check the IP address in the packet. If Ron wants our computers to send him back responses via software capable of intercepting packets that come in, Any arriving packet would be dropped if not coming from my network stack by limiting the acceptable IP addresses to local IP addresses. PCAP was not used by Ron, but he came up with a stack that gave him full control of the network stack`.
>>`2. If you use a VPN, all data transferred is encrypted in the Transport Layer. So, he could tap the data in the Transport Layer before encryption`.
>>`3. if you spoof your IP address, he can inject a signature/signing to every packet that leaves your system`. 

## Presentation

Data can use different encoding schemes, depending on the operating system it comes from. If you are using a Mac, it would have a unique encoding. It takes the encoding from a different system, and encodes it in a way that enables the host to understand it. 

## Session 

It has a bunch of functions that are critical for security, and represent a vulnerability, which involves obtaining *session-keys*, thus enabling an *end-to-end* connection. For example, Ron checks geographical locations for the internet service provider. You can not see the host server inside the ISP. 

## Transport

Controls the flow of information through different protocols. It uses the **Transport Layer Protocol**, which has synchronization/sequencing.

It is designed to transport information error-free, and if they exist, it has to be re-sent. The **UDP Protocol** is *asynchronous*, which means it does not care if the information arrived safely or not. It is used to in VOIP applications, streaming and so on. 

## Network 

It uses IP addresses. It is designed to find a computer that is not on the local segment, such as in a different building. 

## Data Link

Address Resolution Protocol is used to map out MAC addresses to devices. 

## Physical

This is the layer that the packet leaves our system to the destination system. When it is received, it ascends to the very top layer by passing through each layer. It works on the concept of *Encapsulation*


----------------
### Unmanaged Switches/Hubs
In cheap switches, every packet that came in to the switch got sent over to every computer plugged in to the switch --> **Unmanaged Switch/Hub**. Tapping networks was really simple, as every bit of traffic got sent to every single hub. 
### Managed Switch

The most common switch you can buy right now. You can plug in an *Unmanaged Switch* to the Managed Switch, and due to it depending on computers themselves for addressing, that means that it will act as a very cheap **Network Tap**. 


--------

# Network Tapping Strategies

#### Port Mirroring 

You can take any port on the Managed Switch, and turn it into a hub. The port is configured in *Promiscuous Mode*, which captures every piece of traffic that passes through the network card.

#### Promiscuous Host

It takes every packet that comes by and captures the packet. It does not stop the packet from reaching its destination. 

#### Network Tapping 

Most popular taps are created by a company called *Barracuda*. It takes 30 seconds to connect it to a network. 

#### Unmanaged Switch/Hub

### Full Packet Capture vs. Capture the Header



>[!note]
>For each of these methods, we are doing *Full Packet Capture*, which include the **Header** and the **Packet**. There are a lot of data!


We can do that with **Netflow**. It involves changing the router capturing **header information** , and outputting it to a collector. The compression ratio is 20:1. This is most efficient, but it is limited in terms of the things it can do. You need two different systems to do so. In Ron's system, his method did not involve two systems, but it involves Header capture as well as Full Packet Capture on demand. 

>[!tip]
>
>To see the forest for the trees, start examining the **Header Captures**. If there is something of interest, do a **Full Packet Capture**. 

You can also use any of the network capture methods, and to throw away the payload and keep the header. You can convert a full packet into a flow, such as specific fields of interest. 

----------

# Intrusion Prevention + Detection Systems

You should have both!
## Intrusion Prevention System 

In the case of a honeypot, it is not recommended to use an **Intrusion Prevention System**. Also, in an environment involving critical infrastructure, it may be disconnected due to the IPS thinking that it is a part of a botnet, when someone in fact is playing an online multiplayer game. 

>[!question]
>
>When are situations where a top IPS would be useful?
>
>>[!answer]
>>1. If you detect a connection made to a known malicious entity ...
>>2. Privilege Escalation
>>3. Situations where your network apparatus controls non-computing devices like IoT, phones, TVs, security cameras, etc...

---

## Tapping Physical Mediums 

### Coaxial Cables :

Rubber on the outside, Copper cables on the inside. Tapping it was a problem. C-Clamp-like devices would grab the cable, had a needle that descended unto the cable and tapped  the copper fiber. 

### Fiber-Optic Cables 

Difficult to tap


Fiber to desktops --> fiber passes through a metal conduit (where it passes through the door, and it is visible always. This prevents any network taps from being hidden) --> from the back of the computer to the server --> Zinc

Renovations have been done in buildings in security installations. That lead to the discovery of listening devices inserted into the concrete. You can sit outside the building, send an RF signal and it starts transmitting. any possible technique you can think of has been certainly done before. 



There are building systems that are responsible for other things beside your computers. The whole process of subnetting, done in a simple way using Packet Tracer, the incident response class involves implementing this in the lab. You are making it very difficult to find your way through your system. There is a report released last week, where if you are familiar with the Attack Chain, you compromise a system to get in,  you are at the Access and Privilege level (lateral movement and enumeration) and you run into a problem, you can set up persistence, elevation of privilege (including propagating to a system where privilege escalation is allowed). 

The Chinese are using AI in their malware to do this automatically and efficiently. This leads to the reduction of the time of the Attack Chain, and thus cutting down on opportunities for discovery of the attack. 

Subnets prevent you from moving from room to room easily. 