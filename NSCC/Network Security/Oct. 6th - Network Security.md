




We are going to send traffic from two different VLANs across the **Crossover** cable. 



We would like to have multiple VLANs across these cables, so we would not having 10 cables to allow communication between each VLAN 


So, we will create a **Trunk Line**, which uses an *Encapsulation Protocol*, which works like this : 







VLAN 20                                                                                          VLAN 20

       Message gets encapsulated                                            2. Gets passed on 
                                                                                             3. 
       (this packet is from 
                                         VLAN 20)


                 Switch 1                  ===================sWItch 2
                                                  (Trunk Line)

                           Message goes from Trunk                         
                           Port on Switch 1 

VLAN 30                                                                                           VlAN30




Data has to be encapsulated to travel from VLAN 20 to VLAN 30 .



If a message is sent from VLAN 20 to VLAN 3 :


1. Message gets encapsulated before hitting the Trunk Port on Switch 1, saying it is from VLAN 20 (Switches keep track of which IP is on which port)

 (switchport mode trunk) 
 
 
 Switchport mode access 


	en
	conf t :
	> Enter configuration commands one per line
	> int fa 0/5
	> Switchport mode trunk
	> switchport trunk allowed vlan 1-30
	> exit
	> show vlan
	> show interface trunk 
	
801.q is a protocol, just like *Ethernet* is a protocol 


801.q is an **Encapsulation Protocol**. 


Setting up VLANs

>conf t
>inf fa 0/3
>switchport mode access
>vlan 20 
>Name sales
>vlan 30
>name admin
>exit


>int fa 0/3
>switchport mode access 
>switchport access vlan 20
>






>config 
>int fa 0/4 
>switchport mode access
>switchport access vlan 30



![[Pasted image 20231006093010.png]]



If we put two more PCs , they will be available on VLAN 1 automatically. They would be able to transfer data. 


He will leave Hands-On Packet Tracer for today. He wants us to add a router, with an **Access Control List** or aka. **ACL** from a router perspective : 


Anyone from that VLAN can talk to the other VLAN, or this machine can talk to the other VLAN. 


It is a way of regulating access on your network. If one machine on one VLAN would like to talk to another machine on another VLAN, it would have to be specifically allowed to do so 


The principle of *Access Control* especially under NIST does not ONLY apply to networks, but applies to everything!


If someone comes in to the building, are they on the guest list ? This is **Access Control**. 



Card-Access for instructors at NSCC allows access with a keyfob. 



**Access Control** to everything and to everywhere. We istitute that for security right from the Parking Lot in the building to a server. As we transit to each boundary, we would have to be allowed in by the **ACL** or **Access Control List**. 


A slang : "I want you to **ACL** this network"



Building a Router into the system, and setting up an **Access Control List**. It is complicated



For the second half of the class, he would like to cover a*Theoritical  Side* to Networking. On Fridays, we will have hands-on for the first half, and the next half is Networking Theory. 



## Theory Portion


#### OSI Model 


1. Does every computer that accesses a network is government by the OSI model ? 
Answer : No!



A Computer ---? When any application has to access a network, or send a packet --> Packet gets built --> sends it through the **Network Stack** --> 



Application on Ron's OS

on 

**Application Layer** (Some people confuse the **Application Layer** with actual applications. In truth, it speaks the same language as applications. )

(Message gets encapsulated by the *Application Layer*  and gets passed down to the **Presentation Layer**)
|

**Presentation Layer**
(Computer Science is bad at naming, with a lack of imagination. It is a language translator. Ron's system could be a Windows PC, and the destination is a Linux Server for example. PC application asks the pc to do something/communicate, and asks the presentation layer to translate for the other PC's **Presentation Layer**. Operating Systems may translate Bytes differently, **Big Ending/Little Ending**. The **Presentation Layer** understands this, and makes the translation. "Presenting the message to the Application Layer"  )

|

**Session Layer**

(Have you ever left your pc and locked it, come back from the washroom, and you get greeted with a message "Your session has expired". This is due to rules pertaining to who and how long they can be idle for)
|

**Transport Layer** 

(VERY important later. As far as this layer is concerned, it is unaware of any intervening network. As far as it is concerned, it is speaking directly to the destination PC's Transport Layer. In TCP/IP network, it means it has a Transport layer and an Internet Protocol layer. At the **Transport Layer**, we have *source ports*, *destination ports*, *Protocols*. )
|

**Network Layer**

|


(We use it to find other computers in the world. This is where the **IP Address** is. The **Network Layer** will take the *IP addresses of Source and Destination* and everything it receives from the transport layer, encapsulates it, and sends it off. This layer IS aware of your network. It will know the private IP address on the destination computer)


|


**DATA Link Layer


(Used to talk to ALL the local machhines. Local networks do NOT use IP addresses. The **Data Link Layer** uses MAC addresses. At this point in the stack, it is accessing the **ARP Table**  to look at the IP address that was requested, and to see if the IP address exists on the network "ANyo e at this network with this IP address?" , and if the answer is "No?" The **Data Link Layer** sends it to the *Router*. "No computer on this local network has told me that it has THIS ip address. It must be somewhere else in the world, and I will pass it on to the gateway." The IP Address could be on another VLAN , or segment, or country etc... It has to get to the router, and talk to all the other PCs on its segment)



| 


**Physical Layer**


(How is your computer connected to the network ? COAX? Bluetooth ? 
Whatever you are connected as, it is known as the **Physical Layer** prepares the electrical signal to go on the wire. Infrared networks utilizes Light Pulses to send the signal. Ron mentioned that when he was at DAL, he could not string cables due to high costs. They placed an oinfrared receiver and a countering sender between the two buildings. Fog hinders infrared. There were ALOT of packet loss. Throughput is : HOW MUCH DATA YOU CAN TRANSFER SUCCESSFULLY? The data did not always make it to the other end. )




------------------------


                   ---   Destination Computer                         


                 |

|U P

Session Layer 

| UP   ( Transport Layer  transfers the message for the session latyer)


Transport Layer


|UP


Network Layer

|  UP  (When leaving the DATA LINK LAYER , it has reached its destination, where the contents of the envolope are handed to the TRANSPORT layer, which is why he mentioned that "The Transport Layer thinks of itself as talking to another TRansport Layer")

Data Link Layer

|   UP 

Physical Layer



Message  --- Bottom of the other stack 
from ROn's OS 






(Ladder with hhuge steps can have little steps added)



-----------------



We should have a high level and general idea about how it works. 



From a Network Security Perspective, we are focused on the **NETWORK LAYER**. 



We have an equal attention to the **Transport Layer**, as it governs which ports are open. If someone is trying to access a port that is not open, we would see it. 


When dealing with VPNs, VPNs are encrypted channels. Someone listens on other layers, and you are on a VPN, they cant see what you are doing, as it is ENCRYPTED at the **NETWORK LAYER**. If a message is received, it gets decrypted, re-encrypted and gets passed on to the **DATA LINK LAYER**. 



When the packet arrives via the VPN, it arrived encrypted, it gets decrypted at the **NETWORK LAYER**. 


If someone is on a VPN, you can monitor what they are sending from 8the computer, you can monitor what comes out of the **TRANSPORT LAYER**, it is NOT encrypted. 


When Ron was developing Network Security products, the listening monitoring on the arriving computers was at the Physical Layer. He developed a software that captures traffic between Transport and Network layers. On the receiving machine, he would see it by capturing traffic midway through the stack (He can monitor traffic that is connected to a VPN). 




Question: At the physical layer, we can see traffic that is for a particular IP Address, You would not be able to find out what is being sent.



As an example, you have a computer on a network that spans the city. You are monitoring a computer that is at the docks. You want to stop the computer from accessing the network right away (for example, it is shipping information to an unwanted destination.). You can call a worker at the Docks to pull the electrical cable. You may use a remote admin to disconnect the computer from the network. In Ron's system, if you were to click one button, nothing can go from the network layer to the transport layer. You can instantly stop traffic coming out of that computer because it will NOT allow anything from the network layter tyo the transport layer. 



When we are in a situation llike this, or a malware on a machine, you have disconnected it from the network. You want to keep the machine on for the purposes of **Forensics**. If it is powered off, we lose any information about the malware.' We want to maintain its running state'. Image the disk, capture the RAM's memory etc.. What Ron did was to prevent anything from leaving the computer unless it is going to Ron's computer. He COMPLETELY blocked anything from leaving or going to and from it unless the communication is to Ron's machine. The computer is in Solitary confinement. 


He looks at the IP address in the envelop from the network layer, and if it is not coming for the machine's ip address, it is prevented from going or l




In Advanced Networking Midterm at TUNs, it asked " How many layers are in the OSI model?". The question was designed to say "We want to see if you actually understand it". The answer "7 layers".


OSI model was not built for any operating system. It is just a conceptual document. Computeras have to talk to each other from different languages countries languages etc... OSI model was developed with the intention " we do not care how you do this. standardize it!". The first company to ignore this notion was Microsoft. They have combined "Application + Presentation + session layers" into one layer. So they made it 5 layers, and by layers we mean programs. 


What matters is "What comes in? what goes out?"



We do have to understand the network stack on each computer that we are developing for, monitoring etc... There are evolutions from the developing company's side that will impact your security operations. From Windows XP to Windows Vista, until 2006, Microsoft's stack was exactly the same, but then changed it to what it is today. 


Investigate : How many layers are Microsoft's networking stack? 

They made it work exactly like if they had 7 layers. In the OSI model, each layer was a separate program. So Microsoft made it function the same as a multilayer stack, but how you implement inside the box does not matter. 


When Ron developed this program, there was **OpenVPN**, and alot of companies werew using it for communications. Tehre was a bug that allowed you to see encrypted traffic. it was not discovered until 2013. There was a big coproporation that moved their cyber operations to mexico because mexico's cyber laws are very lax. They have been monitoring their employees' communications for years, and they have used this bug to do it. When the bug was patched, they could no longer spy on their employees. Through a third party, they asked Ron to implement a solution to spy onb their employees, and Ron refused. 


We can use encryption that is very difficult to crack. SSL Encryption or the modern version of it , TLS Encryption (Transport layer security) . These are **Application Encryption**. We use it every day! Every time we put HTTPS, it is either SSL or TLS. What it does is, for VPNs the encryption happened in the transport layer. SSL TLS the encryption happens at the **APPLICATION** or the browser, and before it enters the stack. The only way to see it if we have the **Decryption Key**. The key sits in the OS, and it is used by the application to encrypt and decrypt traffic. 

End-To-End-Application-Layer-Encryption/Decryption. 


When the source thinks that it is talking to a wewbsite , and enrypting traffic for that destination, if you have a proxy , it is actually talking to YOUR server, and you have a Computer-In-The-Middle. Data is examined by the sender, gets decrypted, reencrypts it, sends it to destination . 




Question : what encryption is used by SSH?




If we have Ron looking inside VPNs, 




Next time : We cover how to encrypt/decrypt at different layer. 



If we have a web proxy inside the company, and someone is using HTTPS, you can still see the contents of the data. 



NEXT Week:  We will put a router in our network . 