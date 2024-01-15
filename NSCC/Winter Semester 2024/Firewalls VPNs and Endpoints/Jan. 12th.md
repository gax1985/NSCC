



In the olden days, there were **NOT** any *firewalls* at all! 



If one downloads a virus accidently, there was  **NOT** any protections




## Network Traffic 




When we are considering blocking traffic, here we have the **Five-Tople** , aka .. **Five Key Element** : 



#### Source IP (**SIP**)



#### Destination IP(**DIP**)




#### Source Port (**Sport**)



#### Destination Port (**Dport**)****




#### Protocol (**Proto**)







It does not matter what firewall you are working with, when you edit the firewall rules, we would see these terms!





- HTTP (Port **80**) is Un-Encrypted! Any website using plain old HTTP is unsecure. Chromium wont accept the HTTP Protocol 


- When HTTPS (Port **443**) was released, it was wonderful because traffic is Encrypted!


------------


# OSI Model


Networking is broken into **layers** :




## Application Layer




## Presentation Layer




## Session Layer


>[!note]
>
>ICMP Header can be read by the **Firewall**. What is the most blocked ICMP tool on the network? ... **PING!** it is a simple 3-second test to see if the device is online or not. Blocking **PING** entirely is a bad idea. But externally, **PING** can block incoming *ICMP Packets*. Although, blocking **PING** will not completely obfuscate the node.


## Transport Layer

>[!note]
	We would block ports here! We do not care about the IP Address, Just block the Port!

The **TCP Header** lives there ! It was the gold standard for Internet Transmission. **Sequence Numbers** are very important. Computer processing was slow. He could not run UDP applications, so they would rely on TCP instead. 

>[!note]
>
>40% of TCP's traffic is not actually the transferred data


What UDP does is use the *Application Layer* to check for incoming data. When *BitTorrent* first came out, one could not open more than 3-4 torrents back in the day. The application was dealing with the data transmission (TCP is *much faster*) 

## Network Layer 


>[!note]
>	(In the Beginning, Firewalls operated there!)



If we are hosts on a network, and we are sending traffic outbound, the firewall **will allow outgoing traffic**!

Ebery single packet has an IP header : 

What is the **Source Address**?

What is the **Destination Address**? 


**IP HEADER** lives there

## Data Link Layer





## Physical Layer






------------------




#### Example Five Tuple : 



SIP : 10.0.05

Sport : 50000

DIP : 10.0.0.8

DPort : 80


Proto : 6 ( aka **TCP**)





>[!example]
>
>Back in the day, a technician would come and install VOIP systems. The technician would configure Firewalls, and most firewalls allow :
>
>Any SIP
>Any SPORT
>Any DIP
>Any DPORT
>Any Proto





---------------------------------




# Types of Firewalls 





## Packet Filters (1987)





## Stateful (1990)




## Host-Based 

#### The Pros : 

>It is based on the host as a **Running Application**. It is *user-configurable*! It can be *tailored to the OS* , It is the *last line of defence* before the endpoint protection system. It *may have to stop outgoing traffic from the host*. It can also *make connections between **Process IDs** and the network traffic. 


#### The Cons : 


>We should **NOT LET THE USER TAKE CONTROL!*



## Network-Based 



#### Pros : 


>It **keeps unwelcome traffic out**, contain **specialized solutions on top of** *Packet Filtering*. 





## NextGen Forewa;; 



> It combines several types of firewalls such as : 
> 
> 1. Packet FIltetring 
> 2. Intrusion Protection System
> 3. Deep Packet Inspection 
> 4. Identity Management
> 5. Application Filtering




-----------------------



### Linux Firewalls 





##### *ipfw*



*iptables*


	sudo iptables -L --line-numbers
	sudo iptables -D <CHAIN> <line number>
	sudo iptables -D INPUT 3


>[!important]
>
>Research *iptables* urgently! 







