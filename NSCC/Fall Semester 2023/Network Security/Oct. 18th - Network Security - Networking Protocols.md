


Today we will be talking about the **Protocols** and how we can use them to our advantage. 




Two computers need to communicate!


We have the **TCP/IP** Protocol, with one being the **Transport Layer**.





## Transport Layer


It is all about establishing connections. You can fuse different protocols to establish this connection. 


#### TCP 

It is number 6 

There are 256 different protocols

It is also called *Syncronous Communication*, which means both sides need to establish that they want to talk. They would arrange the information that they share, so the sender can send information out in packets, and the packets can arrive in any order they want. 


The receiver has to rebuild them in the same sequence that the sender has sent them in. 


For example, we would like to FTP. The binary executable program can not send more than one packet. So, the sender will cut the program into chunks, and each chunk will be sent as a **Packet**. 


The internet is a collection of routers, so we may have the first router (Eastlink for example). This router can take any one of thousands of paths to get to its destination. The  packet can come in , get sent to a router in Montreal, a router in San Francisco, and finally to Vancuuver. It has to be put back in the same order it originally had, or the program will not work. If the program is run, and it has not been transferred in the right order, it will not work. 


The other packet goes from the Eastlink router, to New York, Chicago and then arrives at Vancuuver. 


The router does that because it keeps track of up-to-the-second statistics on the busy-ness of each path. It is looking for the fastest paths. It can arrive at different times. 


Each packet must have a sequence number, in order for the receiver to put it back in the right order. Packets can be *corrupted*. 


It goes to the fastest nodes. It is about the number of **hops** to reach its destination. Physical distance makes no differece. 

If we are in Vancuuver , and the packet is going to San Fransicso. In order to consider Calgary as a hop, but there might be a quicker way to reach San Francisco. 


Question: Does it re-calculate at every stop? 

Answer : yes it does! There is a bunch of statistics to find the least busy steps : number of hops, traffic on each router ... Routers communicate with each other to figure out the quickest path. It also because it needs to confirm the destination. 


Packets arrive at a different time. It can arrive as 3  | 1 | 4 2 , so it wont run because of the disorganized order of packets. 



When it arrives, the computer who receives it must check if the packet is corrupted. 


At the source where teh paacket is sent, before it is sent it is given something akin to a hash called **Checksum**. 



Packet  (with a hash 356)  --- number is sent -- destination rehashes it, and gets a different number  

	What does that mean? 
	Answer: it has been changed!


The packet has to be discarded in this instance. This computer in San Francisco messages the router in Vancouver to let it know that the packet is damaged. 


The numbers are generated by the sender, and it is called a **Sequence Number**. The receiver has to know which packet is the first, the second etc... In establishing this connection, it lets the receiver know that this is the first packet, such as 3005 for example. The receiver then says I know that 3005 is the *sequence number* for the first packet. Then the second packet is 3006, 3007 and 3008. 


What both computers need to know is : which packet is the first packet in the sequence? 

For packet #2 , it will be looking for the next packet, so the first packet's sequence number is important. 

A *checksum* is added to make sure the packet is not corrupted, the *sequence number*, and so on. 


If something is synchronized, there has to be a start, which is "Hello! I would like to talk to you", then a response "Hello! Yes I would like to talk", then the other computer says "Ok. Here is the first packet, with the sequence number 1", receiving computer says "Sure this is packet #1". If there is a packet corrupted, the receiving computer will say " Hello . The packet is corrupted. Please send it again!" , then the other computer says "Here it comes!"


**Graceful Ending** means *fin* in technical terms, which is a packet sent by the sending computer to let the receiver know that this is the end of the sequence. 


If a computer is not wanting to talk to another, it sends a *Reset* packet, which means " Go away!"

This handshake impacts the speed of the transfer. It is there to prevent any issues with rebuilding a sent program for example. 

TCP stands for *Transport Control Protocol*. 

For Synchronous communication , we have the **TCP Handshake**


![[tcp-3-handshake-process-510894311.png]]



How does a computer say "I would like to speak to you?"


There is another thing called **Flags**, and the flags are a 7-bit number. Each of these flags can be a 0 or a 1. Each flag has a name, for example, for the RESET flag (Go away!), it will set *RST* = 1.

	0000100   Location of specific packet unknown


To close the connection , the *FIN* flag is sent

	0001000
 
 
The response in the *FIN* situation : 

	0000011          FIN + ACKnowledge



The *SYN* flag stands for Synchronization (I would like to talk to you) :


	1000000


Compter 1 speaks to Computer 2, and says "I would like to talk to you". It sends a *SYN* flag. "If you would like to talk to me, this is the sequence number", and the sequence number gets sent as well. 
Computer 2 sends back a *SYN/ACK* flags, 1100000. If the compter 2 does not want to talk, it sends a *RST*. If they start communicating, the sequence number is sent , Y in this example. It would say" I expect the next packet that you send to conform to : 

	Seq X + 1  ---> The next packet should be in sequence according to the sequence number it was sent initially by the sending computer. 


If something goes wrong, and the sending computer sends a packet with the sequence number 3 after the initial 1st packet, then Computer 2 lets it know the sequence number is wrong. 


Sequence numbers apply to every type of packet. It is separated into two things : *SYN*  and *ACK*.. 


This is three steps, and it is called "**TCP Threeway Handshake**".


Ron found a great article on how hippies came up with the Internet, ACT Communications "This is how we found the internet"



When the conversation is over, and they talk for a long time, and the computer #2 says "I am done!", it sends a packet with a *FIN* flag, and then Computer #1 says *FIN/ACK*



What if the first packet is *FIN*? The firewall which is present everywhere, and the firewall is watching. It receives the packet, and it wonders why it has not received a *SYN* or *SYN/ACK*. This is causing the firewall some confusion. The contents of the packet that it sends back reveals information on what type of firewall it is, the OS, manufacturer , etc.. This is a way of not following the rules intentionally. This allows the firewall to leak some information about itself. 


One of Ron's favorites is to send a packet that looks like this 



**Christmas Key Scan**, due to it looking like a string of lights. if you change the flags to something unexpected the firewall leaks information. 


![[packet-design-for-the-xmas-tree-scan-l-2530907833.jpg]]

 
 




 #### UDP 




We see a maximum of three protocols on any network, TCP (6), UDP(17) and ICMP(1)


It is also known as *Asynchronous Communication*, which means that we do not care about what happens to the packet. This increases the speed dramatically. This is known as **Streaming**. The protocol that handles it is UDP.  


UDP stands for **User Datagram Protocol**






The router would have a Database where it keeps track of all the conversations it has. This is to keep track of everything.  Every time a computer sends a *SYN* flag to the firewall : 




Computer 1 --------------------> Computer 2



In the database, the firewall says , I expect a *SYN* flag, and that I should respond with *SYN/ACK*. The firewall 


In the router's database 


DATABASE

1 | SYN
12|SYN/ACK
ACK?|


It is expecting an *ACK* flag, so it keeps the record open, which uses RAM and disk space. If we never send an *ACK* back, and instead, we send another *SYN* back to the server, and the server sends us back a *SYN/ACK*, but then instead we send another *SYN*, and then the firewall sends back a *SYN/ACK*. What happens to the firewall if we keep doing this? it drains the server's memory. This is a version of a **Denial of Service** attack. If a botnet with computers around the world sending a *SYN* packet, this is called a **SYN Flood**. This is abusing the conversation protocol. 


We are using **TCP** for this conversation. **TCP** is going to establish communication with a specific port on the other computer. It might send a connection to a destination port 80, because the computer we are talking to is a web server. We will send a *SYN* to port 80, and it has no web server, it responds with *RST*. If someone is sending a SYN packet to port 80, this is an attacker doing a network scan. 


Port 80 used to be enabled by default on Windows until 2004. Every copy of Windows have an embedded web server that is disabled by default now. You would not have been able to SYN-Flood to a Windows system if the web server did not come embedded. 


Question: By Sending a *RST* flag, then it lets the attacker know the computer exists!
Answer : True!


If we are scanning a series of IP addresses : 

124.56.7.2
124.56.7.3
124.56.7.4
124.56.7.5 ---> Sends back the *RST* flag , which lets the attacker know that the computer exists!


To prevent PING scans, You can disable PING acknowledgements on the computer. 


If you get "Destination host unreachable" tells you that something is blocking your PING packet. 



Ports are like radio channels. Port number in a packet is a *16-Bit Number*, and we are specifically discussing *Destination Ports*


How many ports are there? 65,536


Port 0-1024 ---> **Well-Known Ports**, which are ports specifically associated with a specific purpose : 


80  --> Web Server
443 -> Encrypted Web Server
22 --> SSH
445 -> SMB (Port used by Windows to share things on the network) 

SMB V1 has a weakness in it which was discovered by the NSA in 2012. 
Windows SMB protocol on port 445 had a weakness that allowed the attacker to execute remote code. NSA discovered it by experimenting with Windows. They decided to put malware on Russian computers that used Windows, and they did so for 4-5 years all over the world. They remotely accessed computers , and placed malware on it. In 2016-2017, there was someone who worked for the NSA who copied the code for the malware illicitly, placed it on his home computer, and he was discovered, where they found top-secret information. and he explained it that it was his hobby. At this point, the Russians got their hands on this code. There are two explanations : 


1.  He has Kaspersky Anti-Virus at home. It is a Russians product. The Israelis contacted the NSA< and mentioned that Russia's GRU has compromised Kaspersky Anti-Virus, and are using it to probe other computers. If you have Kaspersky anti-virus, please be aware of it. The Israelis compromised Kaspersky themselves. The Americans now know what happened. They want to tell Microsoft, and they did. Microsoft released a patch, and informed everyone to upgrade to SMB V2. Microsoft published the exploit, and instructed every user to update Windows right away. A lot of people do not update their Windows, so patching on average happens after 90 days. WANNACRY was born, and created by the North Koreans. It was notorious to take down hospitals. The actual exploit created by the NSA was called ETERNALBLUE. Port 445 is within this range. There are other ports specifically used in that range. 








Destination ports : You send a SYN packet, and you send a destination ports. Ports are like radio channels. In the old days, they had CB Radios, so the CB Radio was treated exactly like the internet. They had group activities on the CB radio, and those meeting would agree to meet on the radio on a particular time on a particular channel. Everyone would be on the same channel. Although, with the radio, everyone can listen in. Each channel was used for a different conversation. 



YOU ------ Web Server


You would like to talk to this web server, and if you have multiple websites open, you can be talking up to 2000 simultaneous conversations. The destination port can be the same, for example , port 80 if it was http , or 443 if it was https. If you need some way to separate the conversations on our side in this fashion : 


We are talking on port 80, but just for this conversation, I would like you to talk back on port 5000. 


this is a way to separate simultaneous conversations. We start the conversation on port 80, but continuing on 5000

Source port/SPort ---> 5900

Destination Port -----> 80 


Destination port 3306 might be an Oracle Database software, If you think someone in tyour organization has a database on an IP address, you know that the port assigned is 3306. The same computer could be listening on port 80 if it has a web server. The destination port often indicates the service you are asking for. If you have ever installed a game on your computer, it would usually have a defined port associated with it (for example some random , 3605, it could be different.). If Ron invented a computer game, he could set up a server, and call the game Ron's game. On his computer, it could be on port 10000. He would invite others to play on port 10000 on his IP addesss. 



THere is an organization called **IANA**, and it keeps track of and maintains a list of all possible known *Destination Ports*. We can Google "IANA Portlist". Ron could contact IANA, and mentions to them that he has port 10000 assigned to his game. IANA publishes the list and adds port 10000. Someone else could do the same without telling IANA. Someone else could have some other game on port 10000 and tell them. If noone plays Ron's game, and he never bothers to contact IANA, the port is still listed. If another software uses port 10000, and we look at the traffic , and we see a user going to port 10000, if they check the IANA list, the employer who Ron works for inquires about Ron playing the game. 


The point is, this is a **Best Guess** of what it could be based on previous information. Above 48000 we have **Ephemeral Ports** they are not assigned to software. They are temporary source ports to keep track of conversations you are having. All the previously mentioned source ports are within the range . If a conversation happens on port 50000, and the conversation ends, the operating system takes away this port, and throws it back in the pool of available ephemeral ports. 


Question : Involving web servers, are they always on port 80? 
Answer : if it is not encrypted yes. 



Googe "TCP Header ":

![[tcp-headers-f2c0881ea4c94e919794b7c0677ab90a-3471631692.jpg]]

This is a long series of bits. The first 16 bits are the source port : the next 16 bits are the destination port : the next 16 bits is the sequence number, the next 32 bits are the acknowledge bits.  The Flags section are 1s if the flag corrosponds to the spot. It used to be that the network stack has to push a packet earlier, with is the *URG* flag. The TCP protocol is a reference document mentioning what the first 16 bits corrospond to. If using a different protocol, for example a UDP header : 


 
![[UDP-header-format-1831036548.png]]



It has less information because it is *asynchronous*. 


> [!note] 
> Every packet is like a Russian Doll. 


*Ephemeral Ports* means it is thrown out after use. 



The Packet ( when travelling across your network, while it is using MAC addresses) 



It is on an **Ethernet Header** 
---------------------------------------------------
Underneath, an **IP Header**.
-----------------------------------------------------
Undernearth, the **Protocol Header** 
(If TCP, you use Port Numbers, there is always a SYNCHRONIZATION phase)
(If UDP, we will also use Port Numbers)
-------------------------------------------------------





When doing network analysis to see what your users are doing, a large part is looking at the destination ports. If some oddity happens, where a destination port 15015, it would arise suspicion. If you would look it up, you would see it is a peer-to-peer gaming software, which causes problems due to noise traffic, opening ports in the network. You would go back to the IANA list to check what the port corresponds to. When doing network analysis , he would have the IANA port list open. You would typically assign half a dozen assigned ports, and when you stop using them, you would forget them. 


These are the rules designed by the hippies. if we do not play by the rules, in a confused manner, we could reveal weaknesses in software that would make them crash, elevated privileges, etc. .. It is important to know how they work generally speaking. If we are trying to get inside of a network, one thing we would do is to figure out :


1. WHat computers are on the network ? Enumeration with a ping scan : 

>ping <each ip> in the network range


Either : 

		Destination Host Unreachable --> something is filtering the packets

You can ping an entire /16 network and map it out. Let us say we find a computer that is active and responding to the PING, we want to see which ports are open. We may send SYN packets one at a time starting at destination port 1, and ending with destination 65535, and if we get a SYN/ACK back on one of those ports, we would look up the port in the IANA list. 


Sending a SYN to destination port 3306, and we get SYN/ACK response, then it is a Oracle Database Server running on it. We would check which exploits are available for an Oracle Database Server. You can send other packets to it to see which version it is running. 



Question : How do you scan a private network? 

Answer : If you have a private network that is NATed, you would compromise an endpoint. How? you would wait for them to make a mistake, such as bad web surfing habits, or clicking on a link in a phishing email, and then you would identify services you are interested in compromising and that you have an exploit for , and you do the exploit.


If you have an IPS/IDS (Intrusion Prevention System/Intrusion Detection System), it is very easy to detect. 


Imagine someone sending SYN packets to each port on the 65535 ports, it would be very easy to see. It is usually malicious. It is very easy to discover this sort of activity, because within an hour, you would see that a computer on a network that is pinging other nodes on the network in a mathematical sequence. If you are the attacker, what would you do to make this less detectable? 

1. Randomize the ports
2. Do not do it all at once 
3. Use a low-frequency scanner (send a SYN packet once an hour/once a day. Network administrators will not see a whole bunch of activity. Good security monitoring is how you look at the data. "Let the data speak to you").





We will continue next class. Please work on the ACLs between now and the next class. You would need to know it for the next assignment. Practice with packet tracer. He will release the networking assignment before the weekend. He will evaluate it by going to each of our computers and see if that works/does not work. He will move hell and high water to make sure we do not fail. 