


![[Pasted image 20231013093452.png]]



We have three VLANS , 4 machines. If we did not put access control on the router, all the VLANs can talk to eachother. We DO NOT want the four VLANS to talk to each other, but the IT vlan should talk to ALL. 


How we regulate it all? **Access Control List** aka. **ACL**.



Now : 


![[Pasted image 20231013095335.png]]

We will ackle VLAN 



#### Access Control Lists (aka. ACLs)

> [!todo] 
>  

We want to :

1. Create the **ACL**
2. Assign **ACL** to **Interface** on the router 

   
   (We are using sub-interfaces)




GIG 0                       GIG1 -------------- VLAN 20     Pc1 PC2 PC3 
 
VLAN10   


|
|
|
|

PC1 


PC2


PC3


- We need an access control list to deny PCs on VLAN 10 to connect to the PCs on VLAN 20


Two types of Access Control Lists :


We were given 99 numbers to Access Control List 1, ACL 2, ACL3 , ...


If we give the ACL a number from 1-99, it is refered to as a **Standard Access Control List**



- If we give the ACL a number from 100-199, it is refered to as a **Extended Access Control List**


- The way the router determines what type of ACL you are working with by the **number we give it**



With a standard ACL, we put it on the interface the *closest* to the destination. 


If we are using an **Extended ACL**, we put it on an interface closest to the source. 





GIG 0                       GIG1 -------------- VLAN 20     Pc1 PC2 PC3     SOURCE
 
VLAN10   


|
|
|
|

PC1 


PC2


PC3




We create an ACL, assign it to an interface on the router, if the SOURCE is the whole network, and we create an ACL to prevent VLAN10 (other Source)



If we are to do this with an extended interface , where do we place it ? GIG1





The command he will use is different from the command outline :

![[Pasted image 20231013100233.png]]



The commands : 


![[Pasted image 20231013100253.png]]


We are denying single IP addresses, s0, 192.168.20.100  0.0.0.0


We will change it! I will keep VLAN 20 out of VLAN10


We cannot have two ACLs


We will be in :

>(router config)# access-list 1

The IP addresses : 

	192.168.20.100
	192.168.20.200


We will deny the whole network! What is the network's address? 

	192.168.20.0


Here is where it gets interesting (This is a common mistake when creating an ACL)


Our subnet mask is :

	255.255.255.0


Let us write that out in binary 

1111111.1111111.1111111..0000000


Whatever the bit is in the subnet mask, we **FLIP IT**!


000000.000000.000000.11111111


This is the inverse of the subnet mask. Does it matter why it is done in this way? No idea, but it does not matter


The result :

	0.0.0.255


So : 


>(router config)# access-list 1 deny 192.168.20.0 0.0.0.255




This is how we deny an entire subnet with that command. 




We are ONLY worried about Eric, and Eric is on 192.168.20.100. We want to keep JUST Eric out.


We say : 

>(router config)# access-list 1 deny 192.168.20.100 0.0.0.0


If we are denying a single IP, this does not matter. This is why we add 0.0.0.0 at the end!


192.168.20.0 ---> Deny a Subnet

192.168.20.100 --> Deny a single IP address



We have to take advantage of Eric and Jonathan before they go. They are the two best offensive security people. They get 1-4 people like them. Any offensive security hacker spend all their time on hacking. One of the best students in the course of the program was a young man on the spectrum, which manifests differently from person to person. He is solely focused on one task. Because he can do that , he became the best offensive security person in the class. If we do not have this superpower, we work at it. If we are to be like him, it takes commitment. He got in trouble due to a RaspberryPi Zero.


If we want to hack a Windows machine, set up a linux VM and windows VM, from the Linux VM, hack the Windows VM. If you hack actual individuals, we get into trouble. If we build equipment from scratch, make it look like a network device, and plug it in, the equipment gets confiscated for 6 months. 


------------------------


This is about creating the **Access Control List**. We still have to place it on an *interface*. So, the next command , we go to the interface 0.0.0.30, we assign it IP Access Group(aka.ACL) #1. The final command is :

>out


He did not write Cisco IOS.

                                             ERIC

 Router    ------------------------X---------------------- VLAN
 | 
IN (UP) |         This us outbound pointing down
 |
 Interface




To prevent Eric, we will assign it to the outbound interface



If Eric was in the network on the bottom , we assign it to the IN



Think of the interface as a doorway ,"You cannot go out of this door"

> [!tldr] 
>  Direction that we are referring to is on the interface we place the ACL on. 


There may be other networks on the router, he can access the internet, but not the VLAN. 


Remember : This is a packet from Eric.



What has he done here ? 


![[Pasted image 20231013102440.png]]


He placed another condition on the access list :

>access list 1 permit any


Eric is NOT allowed, but everyone else is welcome!


The general rule for firewalls : 

>[!tldr]
>The rule that applies is the strictest. In Linux, the order we type it in, that is the order that sticks. 



Someone explain to Ron, what he has done here? 



![[Pasted image 20231013102712.png]]


He denied access to VLAN 30. 




He will place it on the course shell. We get to play with it before Wednesday. Next class, we will implement this!



>[!tldr]
>Be mindful of your surroundings!



