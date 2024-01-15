


## How does a router stop a flow ? 



1. Use the flags **FIN**,**RST**
2. Use the flags Passive Time Ou t --- Have not seen any packets in 30 seconds
3. Active time out --> You would not shut up! 










#### Packets : 


SIP
DIP
SPORTS
DPORTSS 
PROTO - > Payload




## Flow : 

Uniddirectional set of packewts






FLOW DB : 


FLOW 1 FOR C1
FIVE TUPLE
FLAGSs SYN,, ACK , PSH , FIN
Size in Bytes 660
Start Tiume 00:01
End Time 00:10

-----------------
FLOW FOR C2
Five Tuple
FFLAG SYN/ACH , PSH , FIN/ACK
Size in Bytes 600
Start Time
End TIme






There are two computers, : C1 and C2 


How many flow records for these two computers?

4 Flow records : 

1. Going from C1 to C2 (Out)
2. Going from C2 to C1 (Out)
3. Going from C2 to C1 (IN)
4. Goingfrom C2 to C1 (Out)


The conversation is **Two-Way** or **Bidirectional



All this represents raw data and we will turn it into structured data


With one rouyter, we have **two flow records**. The flow collector takes the two records and turn it into a *birectional conversation*

How does it do that ? How does it match this flow with the other flow (*bi-directional*)?


In order for these to match , **Flow 1 and Flow2


It does into the database sent from the router, and it will sort them into a *conversation*



##### Flow 1  : 

	SUO
	DIP
	S-PORT
	D-PORT

##### Flow 2  : 

SIP
DIP
SPORT
DPORT
PROTO(PROTOCOL)



So , it matches the coorsponding reconds : 


SIP matches DIP (C1 and C2)
DIP matches SIP (C1 and C2)
S-PORT Matches D-PORT (C1 and C2)
D-PORT matches S-PORT
PROTO(Protocol used by C1) = PROTO(Protocol used C2)




WITH DDoS , you get "Never heard back", when you SYN/ACK they do not hear back. All you get is SYN, SYN/ACK, and no responds




There are different Flow Records.


The grandfather from rthem all is **NETFLOW**


#### NetFLOW


CISCO's Standard
There are **V5 and V(



#### SFLOW


Used for higher speed networks, like Telecom infrastructure
It has too much data in there. It does a *sample* of the flow. It gets some packets, and does a **Statistical Sample**, akin to a Bird's Eye View



Every piece of network analysis software uses **NetFlow**



If you get a very nice router, it would do **Netflow**, **SFlow**



We want to build flows, get the raw data, make a *conversation* called **Structured Data** to get an understanding of what is going on.



MySQL is not fast enough. This is a kin to a weather station collecting raw data, then an entity puts them in a structred format to understand it




There is another way of getting an Understanding : 



## Full Packet Capture


With the previously mentioned scenario : 


We have a *packet*



Header (router does not collect it)
=========
Payload






HEADER ---> Five Tuple information is recorded once!

All it accumulates is size, flags, time (small amount)

If there were 1000 packets going from C1 to C2 in the flow records, it records the five tuple once. Theflag is one bit. time is different time stamp.

The record is going to be the same size.


The overall size of the database is small. In full packet capture, we put wireshark on the pc :


C1 --> with Wireshark
We decide to capture the network traffic on C1
It uses full packet capture :


Packet 1 emerges from C1, 
Wireshark saves the entire packet!

Everything is in the Header, everything is in the Payload


Packet 2 emerges, 
Wireshark saves the entire packet (everything in the header + payload)


C1 sends a 1000 packets, 
The information will be huge 

With Full Packet Capture --> Entire Packet


We have a mid-sized network, with 100 machines.
We can do *Full Packet Capture* on every machine, 
maintain the log and the database, 
skim through it, and find malicious behaviour

You would need an external drive (1TB),
and it will be full by the end of the day



VS ....



Flow DB : 


Flow for C1
Five Tuple
.....




When you do full packet capture, you are looking for malicious behaviour, 
and you can not visualize it due to too much data


With Flows, you get a birds eye view,
You buuild them into a *conversation*

With a thousand packets ,
You get 4 conversations



One of the ways to know if the analyst knows their stuff, Ron was initially consulted by a company with a server farm in Sambro. They have 30 high capacity servers that were busy all the time. They suspected criminal activity. They contacted Ron, and requested his services. They contacted someone else, and he offered a much lower price. He showed up in Sambro with a 1tb drive. He did full packet capture, and the drive was full in 15 minutes. He has to examine the behavior over time. IF the malicious activity was there, it had to be within the first 15 minutes. 

When looking for malicious activity in network,s you need the **Broadest View Possible**. Ron looks at a month's data.

Start with Flow collection records (**conversations**), and they contain patterns that you would recognize. You will see it when we do this professionally. Data is scrolling really fast on the screen. In the Matrix movie, there are data flowing. After a while, you would not see the numbers, but emails , SSH , port scans (bingo!), etc ...


The *Conversation* would have data that stands out! If we found the machine doing something malicious, but we can not tell what it is. We cant see what is going on (we see header information, flows , etc --> **Metadata**). When we hear about intelligence agencies collecting data, they are looking at connection information  aka *metadata* for malicious activities. 



Generally, all of the security analysis captures **Metadata**. You have to comfort the user that we are not reading their emails, contents of web sites. ALl we are doing is looking at **Metadata**, as it tends to comfort their privacy concerns. 







What is going on in the slide ?



Email server (Outlook most likely) violates the three-way handshake, so it is going RESET alot .



2nd Slide : 


It is a network scan (what we should not do to faculty at NSCC)



3rd Slide : 

Web traffic. observe the time : 10s 10s 7s 60s, CLICK, ...CLICK .. CLICK (Human web serving). Matches the human pattern, and not software. (Sophisticated agents would try to match/mimc human behavior). 



4th slide : 


At 10 minute intervals, one packet sent, two packets sent ,much later 20 packets sent much more data. It is a *VPN Tunnel*. It is set up to **KEEP ALIVE** a VPN connection. This could be innocent, where data is uploaded certain information. *Keep Alive* is a packet sent to prevent a time-out. 

Or, it could be someone exfiltrating data in the middle of the night. 





#### Patterns useful to look for : 



If we have many days' records on the computer at home doing the same thing : 


#### Baseline Behaviour

	If we have many days' records on the computer at home doing the same thing  


How to categorize it ?


1. Number of Distinct Destination ports emitting from one IP address
2. Number of Distinct IP addresses that the computer talks to in one day.  Any computer on our networks, and we see that the computer spoke to 2000 destination IPs in a day
3. Number of Protocols in a month, which should be three (ICMP, ....), but no more than five. (The person using it, the job nature, ...)


It is what we *expect* it to do! There will be little variations. 


On one day, it contacted 10000 destination ports : something is strange is happening. We want to know *details* : we would switch from *Flow Capture* to *Full Packet Capture* on a certain day : Information sent out, etc... The machine's pattern suddenly changed


If it is talking to 30000 destination IPs on a day 



> [!todo] 
> Nessus Essentials : Piece of Software to Download and USE. We can scan a limited number of hosts. We need an email address associated with the Nessus Essentials' License. Install it on the laptop or virtual machine. Please write down *username* and *password*, as we would need to redo the whole process again.  




There is NO CLASS TOMORROW.







