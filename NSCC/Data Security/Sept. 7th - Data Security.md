

Binary 



1 1 1 1 

2to the zero | 2 to the one |  2 to the 2 |  2 to3 





0 1 2 3 4 5 6 7 8 9 



Maximum number of digits possibly represented  = 10 


What is the range of numbers that can be represented? 0-15





#### HEX 


Hexadecimal numbers are 0 1 2 3 4 5 6 7 8 9 A B C D E F 

In Hex, the digits go from 0 to F where A stands for 10 B for 11 C for 12 D for 13 E for 14 F for 15 


If we have four biunary digits we can represent : 



1 1 1 1 ( in binary) = write it in HEX 

15 in Binary = F (for 15)


 
If we are given A in Hex = 10    = 0101



2 to the zero = 1 

2 to the one = 2 

2 to the 2 = 4 

2 to the 3 = 6





We deal with **IP addresses**

*IP* or **Internet Protocol** is the method we use to find computers around the world 


192.168.2.1


The dots separate **octets* = **Oc** for 8 , for each column there are 8 binary digits


The last part of the address, the last octet rather, is a 1 


The computer uses 8 binary digits to represent that 


This arrangement is a bit different than what he has shown 


First position in binary is 0000 000 **0**

How would we represent a 1 ? 0000 0001 

What is the hex equivalent of 1? 0001 = 1


We will see a number that reads 0x01 

The 0x = the following number is in hex

The actual value is 0x **01**


If the number is 01. and we change it to binary, 0000 0001 

First position is always on the **right**


What is the binary equivalent of 0x4A


Each hex decimal can represent from 0 to 15, we use four binary digits to do this 


we have four binary digits of 0x4 = 0 0 1 0 we start from the right , 2to the power of 0 =1 (we do not have one), 2 to the power of 1 

0010 | 1010 is the answer 

explanation : values are 

0 0 0 0 
8 4 2 1 


if we do not have the 1 on the end we would have 14 


If we look at our screen and data, data is represented in 8-bit binary number.


When doing network traffic capture, data is represented in hex, and you will get more comfortable in hex than binary 


Ip Addresses, each of the octet mean something 

192.168.2.1 how many binary digits to represent each of the four octets 

8 8 8 8 = 32 binary digits or aka... bit


8 bits = 1 byte 


When he mentioned that computer technology is invented by hippies in an altered state of conciousness ...


They made chips 


When we look inside the computer we see pieces soldered to the board, the chips are actually inside 


The hippie had bits, bytes, chips , and dip 

They needed to explain **dip** (they did things backwards) 

Dual Inline Processors


8 bits = 1 byte , thus in one octet we have 1 byte (8 bits )


4 bytes for an IP address = 1 byte for each octet 


192.168.2.1 = 32 bits for the whole address 


2N = all possible ip addresses can be represented in a maximum of 2 to the power of 32 

When the internet protocol was invented, and it was decided that IP addresses needed 32 bits, that was the maximum possible 


**The Internet Protocol definition** was defined by an international institution 


When the internet was developed , they did not have many standards, so they agreed on one system; one protocol , thus a maximum of 2 to the power of 32 = IP (Internet Protocol) Version 4 = IPV4 (This is all they needed at the time, it gave plenty of internet addresses)


The world is running out of IP addresses, thus **IPV6** is developed 


In 2006-2007 , he was consulting in Las Vegas, he was examining their network security. There was an average of 8 IP addresses per hotel room. Why ? The AC unit had an IP address , the phone , door , plugins for computers, and WIFI router. One hotel room had **8 Drops**


**Drop** = internet line with one IP address associated with it. Each wire goes to a switch, and each port on the switch (they used the same name for the same thing). 


The switchboard had cables, and the cable goes to a computer = 1 IP address = 1 Drop


15 years ago, it was obvious that the world is running out of IP addresses. They never imaged that the world would have this many devices 


2 to the 32 is not enough 

**Internet consortium of scientists** came up with **IPV6** = 2 to the 64 ( a huge number, evbery individial person born between now and until the sun blows up , each person would have one IP address)

The addressing system was really difficult to monitor, log and understand.


The world thought otherwise ... 


Could you explain how the binary system works , and how the hex system works ? please show me how to convert binary to hex and hex to binary 




#### NAT (Network Address Translation)


Internet ---> Home (WIFI router)


As for the rest of the world, the router's IP address is 223.168.9.12 (whatever Bell gave)

Each device connected to the router has an individual IP address that the world cannot see 


When streaming over the internet, Disney would see the public IP address

If someone else is connected to the network, the world would see the public IP address for the router 


There are a series of IP addresses that are private that exist on the router only


Every time a device requests a connection to the internet, the router has a database that keeps track of which IP address is making the connection , the protocol etc 


When the response comes back from the internet, the private IP address is removed and replaced with the public IP address (belonging to the router)

The router checks the response, and routers the response back to the device 


2 results : we can have 2 to the 32 internal devices (millions of devices with a unique IP address), but we would use one public IP address 


When the Internet Consortium there were a few people who love following the rules. The person in charge of the networking in SMU is a member of this cult and insisted that they move to IPV6


NATing has another interesting feature. If a malicious actor is trying to attach my parents' computer while banking, there is a level of security inherit in NATing, which makes the private IP address is invisible to him/her, as they would only see the router's public IP address


IPV6 addresses are visible to the world (each single device's IP is public facing)


He can not get to my machine if it is a private IP address 


SMU's original security consultant (we might meet him)


NATing arrived , 2 to the 32 was not enough anymore. Only Public IP addresses are visible. 


If we get an IP address through the guest wireless network in SMU, the IP is publically facing. If we monitor the computer, we would be instantly hacked. Malicious actors in China are attacking every publically facing IP address in the world the same moment it is connected to the internet. 


There was a company that transferred healthcare data from Canada to the UK every night. They had an FTP server in their data bank. The records were sent in plain text, and the server was publically facing. This is intensly dangerous (It is not SFTP). He put a monitor on this machine, he guessed the password, there was a password cracking attempt 3-4 times a second every minute. He was not hacked because his password was super long. Long passwords over 24 characters would be essentially impossible.


China, Russia, and others do this. China has specific divisions doing this. 



#### NATing


Network address translation that you would have 1 public ip address translated into multiple local ip addresses


He never used IPV6. He will teach us only IPV4. 


WHen you buy a computer, it duplicates packets into IPV4 and IPV6 based on the assumption that IPV6 will become a reality. This is slowing things down.


It is frustrating to monitor traffic from a security perspective because everything is duplicated. 


The networking instructor might explain IPV6


Question about 5G having a public-facing IP address, cellular network uses a radio address

Do not do banking on phones. No security software for phones until 2016

Phones are NOT secure. Android is the least secure, only because on iphones a malware will have a more difficult time spreading on a phone's operating system. Iphones are monitored so closely that is very difficult for something to spread in the operating system. 


WAN = Wide Area Network 
LAN = our room's network 

We can have other builldings in the province connected to this building on a private network, and sometimes referred to as WAN. Intranet is a large private network. 




He will send us one page on binary and hex. The quiz is a puzzle!



Here is our computer on this network (the class, along with a switch) --> NICs (each computer there is a wire from the switchboard back to the computer)    


Switch --> lots of ports, may be connected to another switch to another switch , there is a limited number of ports, you leave a couple of ports free to connect another switch 


Hypothetically if all the computers are in the same LAN, 3 computers on the same LAN, connected to a switch , which is connected to a router, which is connected to the internet. The router is NATed (has a public facing IP address), and the rest have private IP addresses.

If one computer 192.168.2.4 wants to talk to another 192.168.2.5, you would think this other network would use the IP address to find it, it would appear as if it is using the IP address but it is **NOT**


IP addresses are used to find computers outside of the local network. If the computer you are trying to reach is in the same private network that you are on, they do not use IP addresses. What it does via **ARP** aka Address Resolution Protocol, what it is a database that exists on every computer , on every switch and every router, and has 2 entries in the database: IP address and ...


**MAC address** (48 bit number, it is the unique identifier, burned into the NIC when it is made)


Each NIC had a unique MAC address (aka media access control), and this number is unique in the world. We would not run out of them (2 to the 48 possibilities)


The NAT's database is the IP address and the MAC address. When we type in an IP address, there is what happens

1. Checks IP address in the database is the system on my local network, and do I have its MAC address? If the IP address is not on the local network, it sends a rewquest to the router/switch inquiring about the foreign IP address (it could be on another network in the same building), and the router routes the connection there


ARP/MAC Spoofing : we can change the number in the packets that the computer sends out. 


If we are malicious actors ( intentionally or unintentionally by clicking on a bad link), when NAT databases look for your address, the malicious actor changes the MAC address to his NIC's MAC address

When we talk about spoofing, we pretend to be an address that we are NOT


IP spoofing is really easy. You can pretend to be anybody!


MAC spoofing, anyone on your local network will reach your system if you spoofed the MAC address to another system's (target)


MitM (Man in the Middle Attack) :


He iwll send notes on Binary/Hex conversions. Next week will be a paper quiz in the room Next Thursday (he calculates the time it takes him to solve the riddle, doubles the time, and doubles the time an average student would do it) = 40 minutes (if you need extra time everyone gets double). Results are unveiled right away.

Multiple objectives : 

1. think of the presence of databases in the cyber world. We will interact with databases at all times, and are a fundamental part in everything we do. Why is it possible to change the MAC address of the database on the machine? It was designed to be open who never believed the possibility of the existance of evil.
2. When thinking of HEX and Binary, we will see patterns everywhere 


IP addresses : if all we have is an IP address (public or private) (192,168,3,4), he would not be able to find my computer. IP addresses are made of two parts: addresses of my network, and the address of my machine on this network (Address of my network -192.168.2. 0=zero is the address of my network always and not the machine). We are machine #4 on this network. If that is true, the 192,168,3 is the address of the network 


How many possible values of the last octet ? 2 to the power of 8 , it cannot be 255 the range is 0-255


0 is the address of the network 
255 is a special address --> broadcast address (if we send a message to 255, every computer will get the message , we lost 2 addresses 0 and 255 , we can have a maximum of 254 machines on this network. The last octet is the machine's address|  2 to the 8=256


How many bits make up the network address? 24 bits for the network , 8 bits for the address = /24 network capable of storing 254 machines. 


If he wanted a /16 network , two octets for the network address , 16 bits for the network, and 8 for the address 


Large networks = /8 = 2 to the 24 possible machines




Net Mask = puts a 1 in every position that is part of the network address

255.255.255.0 

1    1      1      (only last octet is used for the machine)


We need the IP address, and the netmask (which tells which bits are used for the network address)


For /24 networks, 255.255.255.0   2 to the 8 machines


These are all puzzles, and no math!


For four hours of outside 


IPV4 , IPV6 , HEX , phone's public ip address , explain Netmask , Mac Spoofing 


Videos are better than reading 


Next week we will get the **first assignment**. Setup MySQL on the computer. He will provide the instructions. Every software we work with will be described, will be handed a set of instructions with it. We need to do the first step. 