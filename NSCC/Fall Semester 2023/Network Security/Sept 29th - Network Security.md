


We will set up a **Switch**, **two computers** and  make them *speak to eachother*!


We always start with a **design diagram**! 


In a network, we will forget things! We will do this in packet tracer. If designing a network, it is a good idea to do this in Packet Tracer. It is building a *BluePrint*. We have *two computers* on the same network, and we have to give them IP addresses :


1. PC1 and PC2 
		
		C1 : 192.168.10.100
		PC2: 192.168.10.200
		Netmark : 255..255.255.0 ---> the Network Address : 192.168.10


2. It will be via the **Ethernet Port** on both computers.
3. We will put 100 in FastEthernet 0/1, and 200 in FastEthernet0/2



Whenever we connect a PC to a LAN, it does not use the IP address to communicate. We think it does. As far as we are concerend, it  should work as intended. It is using an **ARP Address** which is a *48-Bit Address*. 


#### ARP 

aka...

	Address Resoultion Protocol 



Each of these machines has a **ARP Table**


What is included with a ARP Table ? 


All the IP addresses that are associated with a MAC address, and all the MAC addresses associated with an IP Address


Imagine a Table : 

								PC1                           PC2

A pc is looking for another, it sends an ARP broadcast announcing that it is looking, and it is waiting (ORANGE LIGHT IN PACKET TRACER). The message is received by the receipient (This is my IP Address. Here is the MAC ADDRESS : ,,,,,,). The other computer has its own ARP table, and it will store the IP address of the other pc and associate it with the other computer's MAC address. 


We will do a **Static IP Assignment**. A PC will say : 


This is my MAC address everyone! Please give me an IP Address ! 


The router : 


Here you go ! Everybody! This is this new pc, its MAC address is .... and its IP address is .... 


All of them will update their own **ARP Tables**. 

How do we know that this computer is telling the truth ? 

We assume it is telling the truth, because this system was designed by hippies. We can lie about the details. We can announce "This is my MAC address (a different pc's MAC address) everyone!". Whenever we change anything in these tables (which was placed by the hippies) to something malicious, we refer to that as an **ARP Poisoning Attack**. We poison the database. What can we do if we are doing an **ARP Poisoning Attack**? We have a critical server, on my computer, I produce a login screen, and send it to everyone. Then they type in their login credentials. We can do a **Man in the Middle** attack.


When the lines are Orange, the system is sorting this out. In a simulator like *Packet Tracer*, there is magic in the background while it simulates the network. 



Let us try pinging between them !



What Ron was mentioning was to ALWAYS start with the design first. These are two computers and a switch. Imagine a massive network! When it comes to actually configuring machines, you know exactly what to type in. 


IP ADDRESS IS


MAC ADDRESS



We did not call any of these pcs the following IP addresses :


192.168.10.0 (Network's )
192.168.10.1 (Gateway)
192.168.10.255 (Broadcast)





We do not end IP addresses with something easy such as 2, 3 , 4 , 5 , etc ... because malicious actors will start scanning the lowest IP addresses first. Remember the Castle example with its hallways...



If someone is scanning computers on my network, and they are not supposed to be there, we can tell because they are scanning for computers that do not exist. 


**Honeypots** : Placed on the network where there is nothing there. If someone is talking to the **Honeypot**, then we know they do not belong there. We do not just do it on one computer; we do it for the *Entire Network*! We can create a **subnet** or a separate **network**. A **Dark Telescpe** is an entire subnet range that has **NO COMPUTERS**. if someone is on it, then we can identify them.


If we have a /8 network, first 8 bits is a network address. The reamining 24-bits are used for computers that could be on this network. We can have 2^24 devices on that network. /8 Networks are used by Google and other companies.  We can subnet a /8 network or take a portion for it for assigning. 


If you give away 2^24 addresses, you would give a huge chunk of your network away! Government agencies would have gigantic **Dark Telescopes**. If someone goes there, it is one of two possibilities : 


1. Spider : an entity mapping the internet for Google for example.
2. People looking for things : An entity doing a massive scan such as the Chinese. 

No one should be knocking on these doors ever! Unless they are a malicioius actor. We always try to make the network as *confusing as possible!*




#### Setting a honeypot is DANGEROUS! 


###### Why?


1. You would attract malicious actors. 
2. It is public-facing 


You must be careful in preventing them from using the honeypot to access the internet. It could be used for a botnet, or any other purposes. 


Where does the term "Honeypot" come from?


Winnie the Pooh! He places the hand in, and can't get it out!


Honeypots CANNOT connect to anything else on the network. 


Dalhouse University's researchers wanted to do Honeypot research! Dalhousie refused, so Ron built them an office off campus. 


Commit to memory : Honeypot is the category , Dark Telescopes are entire subnets !


Malicious actors always test if they were in a honeypot or not!



There was a virus we will examine in Cyber Crime Survey called **WannaCry** from North Korea. It shut down medical institutions in the UK. It spread like wildfire, and noone knew how to stop it. a Security researcher reverse-engineered it via analysis. The reasearcher discovered a strange URL with 42 characters.  He thought that he should register the URL to get redirection from all instances of WannaCry, and instantly shut it down due to WannaCry instances being trapped in a honey pot. It looked to the North Koreans that they are accessing the internet.  It wanted a URL that does not exist, and when registering the
domain, Wannacry thought the domain exists, and instantly thought it was a honeypot. 




We try to confuse them by not using a sequential addressing scheme in the subnet, we left gabs and holes that have no computers, but this is not the confusing hallways in a castle. It is a hallway with some locked doors. We want to segment this network because we want the peolple in the segments to belong in these segments. 




#### VLANs


We would like to have PC1 and PC3 on one VLAN, and PC2 and PC4 on the other VLAN so that we can not get out from the VLAN to another VLAN



Look up SHOWRUN --> It shows him all of the fast ethernet ports available. At the bottom, if we look carefully, interface VLAN1 has no IP address. Another thing that we notice is every switch come preconfigured with VLAN1. When we turn on the switch, and plug devices into it, all the interfaces are on VLAN1. Let us do : 


Show VLAN in packet tracer : 



VLAN 1


Port1

Port 2 



We have other VLANs with a much higher number. Click on the Switch, and click on "Show VLAN" : 





We use ethernet for everything these days. Peolle think that RJ45 is ethernet. Ethernet is a protocol. *Protocols* are a *set of rules*. Hippies made them, and imagined that everyone will follow them. Morse code is a protocol, due to it having rules translating one thing to another. 


We have a lot of computers on our network, and everytime we are on the network , we are the only ones using it. We are sending electrical pulses on the wire. If everyone sends messages on the wire, it crashes it. 


How do we make sure we are the only ones there? Token Ring (there is a little packet that passes by every computer. If you want to send a message, grab the token, change it, and put it back on the wire. This token says "I am talking now" so noone else is allowed to talk`). This is NOT the most effecient way! 


What happens with Ethernet instead? We talk right away on the wire, and everyone is sending signals on the wire, which causes interference, and we talk again. We wait for a random amount of time, such as 5 micro seconds, and everuone else that tries to talk and cause interference, and they want to talk to, and everyone else is waiting for a random amount of time. This is ineffecient because we are thinking in human speeds. Ethernet is a set of rules : when you try to access a network, you send a signal, if the signal does not get through, send it again. Every other node on the network is doing the exact same thing. Multiple access with collision detection = Ethernet. It sounds like chaos! 


Token Ring is extremely inefficient. A microsecond is forever for a computer. Your computer's NIC still supports token ring. Attackers have the option to generate it too. A token ring network could be completely invisible to the user. manufacturers would add a VLAN for a token ring network. 




#### Bandwidth 


When using a wire, it is electrons moving on the surface of the copper wire. The bigger the wire, the bigger the surface area. Over the years, there are limits to the capacity of the wire. 

so in essence ...

###### Bandwidth : 

	it is about how much data you can send in a particular time 
##### Fiber-Optic cables


Light moves data! Sending a ping-pong ball on the hallway and it bounces off the glass along the way, and another ball is thrown , and they both move freely without interfering with each other's path. 


The limiting factor is the networking equipmernt such as PCs, routers , switches etc , not the fibre-optic cables. 



#### Quantum Computing


Physics give an approximation about it. It is on another level. 






Work on DATABASES! When we come back on Wednesday, we will build VLANs  after a quick review. 