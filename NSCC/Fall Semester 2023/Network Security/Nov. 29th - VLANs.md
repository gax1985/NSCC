



Today we are breaking up networks into individual networks



If we have 4 computers and a switch, we can define a vlan for each group of computers. We define VLANs , ports and etc. 



**VLANs** are virtual separations of networks. They are not *physically* separated. They are separated by access to ports set for set VLANs. 



Besides breaking a *flat network*, where all the computers are on the same network and they see each other, if we have a computer tryinbg to talk to compyuter 2, it has to send a broadcast message asking whcih computer has the IP address with this MAC address (after checking its ARP table). The request goes to every computer on the flat network. This increases network traffic, and it has nothing really to do with them. 




Ideally, if we have computer 1 wanting to talk to computer 2, the broadcast packet should just be between the two computers



We can do *VLANs* and we can do **Subnetting**




# Subnetting


We want four networks



Each network has its own network ID : 192.168.1.0 -- > Network address

192.168.1.255 --> Goes to everyone

255.255.255.0 -> This is the subnetting we are used to 



Whatever the number of hosts we can have is always -2 . If we can have 8 addresses on the network, we can only have *six hosts*. One address will be a network address, and the other the broadcast address.



Let us say we have been assigned a *network range* of 192.168.1.0 for the entire network for the division. This is what we have to work with. We will devide it into four separate networks. 


One thing to remember, basic powers of 2 , so if we have 8 bits in the host portion of the network address :


255.255.255.0 
1111111.1111111.1111111.0000000


We have one network with 254 possible hosts , with 2 being network and broadcast addresses. 



If instead we use : 


255.255.255.128 


It will turn out that we have 7 bits available for our addresses. We can divide it into two networks, and we can have a 126 hours (actual addresses are +2)



First, to get the 128 netmask, we need to set the last bit from the right to 1 : 


1111111.1111111.1111111.10000000


We have 7 bits we can use for the host addresses. 2^7 = 128 - 2 = 126 hosts.


How come I can have *two networks* ?


We can have a network address of :

192.168.1.0 : First network's address 

Because of the bit of the netmask of 128 :

192.168.1.128


Each of those two networks can have 128 addresses 


We can not tell with the network address alone (192.168.1.0). We need a netmask along with it.


If we have 255.255.255.128, it means we can have 128 addresses per network




What is the range of the available addresses for the first network ?

255.255.255.128

0-127


The network address of the second network is the *next available address* : 


192.168.1.128 


What is the range of that network ? 


128-255


The broadcast address for the subnet is : 


192.168.1.127


The second network's address is : 


192.168.1.128 


And the broadcast address :

192.168.1.255



How does a router know that if it sent a packet to 192.168.1.255, that it has to send the packet to the first host address ?



subnet mask . It takes the IPV4 number with the four octets, and then it gets the subnet mask. The first address on the network begins after the subnet portion, so 192.168.1.129



For each of the subnets, how does the router figure out which host it goes to? we need routers for subnets. The routers have to guard them. The routers will work together to guard the individual subnets, and packets sent to a specific entity will go to the according subnet without going anywhere else




**Subnets** are *logical networks*, because the router has to do math.


Anyt bit turned to 1 is part of the network address. Any bit set to 0 is part of the available addresses.

(Remember: the / number is the number of 1s)

1111111.1111111.1111111.0000000 /24   254 usable hosts (1 is network, 1 is broadcast)

1111111.1111111.1111111.10000000 / 25 



Who is giving the address range? if Ron was all of NSCC, we would have 1 publically facing IP address on the router, and the IT division would say that they need a lot of addresses in there. So they will construct an internal address range that is a /16. This means : 


Netmask : 


255.255.0.0

1111111.1111111.00000000.000000 /16  2^16=55536 available addresses



This should be enough for all of NSCC. Internally, the network range is 255.255.0.0. /16 network might get broken into 6 subnets, and each department can have its own subnet. They can give Ron 192.168.1.0, so 254 available hosts. Everyone on Ron's department can be on the same *flat network*, or break them into subnets. For each router, give it the network address, and for the host, we give the netmask. 

If everyone was on the same network, it will cause too much traffic. So, they decide to divide it into two networks , by adding 1 bit to the network : 


1111111.1111111.1111111.10000000 /25  


The added bit : the network is defined by the first 25 bits. The final bit can be a 0 or a 1. The network address can be a .0 , and the other can have a network address of .1 . 


We split the address into two networks : /24 network split into two 


If more demand for 4 networks : subnets for each department 


How many bits ? 2  are needed 



If Ron's boss wanted three networks ,


If he changed 1 bit , he would have 2 networks


There is no half bit, so he will make the 1st two bits a part of the netmask : 



255.255.255.192  (Why 192? because the addition of all three octets is 192)


On each subnet, how many addresses it will have ? 


we have 6 bits to work with. we can have 4 networks , 62 hosts, and 64 possible addresses. 



What is the network address of the 1st network?


Four routers : each router will have a default gateway for its network address 



255.255.255.192


What is the address of the first network ? 


1111111.1111111.1111111.11000000 /26 (26 bits)



We have 6 bits available for addresses 


We can have 2^6 addresses, which is equal to 64. 


We can have 64 addresses on each subnet, and this will give 62 usable addresses for hosts : 1st is network, last is broadcast. 



What is the address of the ffirst subnet  ? 


192.168.1.0  b  roadcast 63



What will be the address of second subnet 

192.168.1.64   broadcast 127


Wjay will be the network address of the third subnet? 


192.168.1.128    Broadcast address : 191



What will be the network address of the four subnet? 


192.168.1.192 Broadcast address :  255




There is a little trick on how to get this number : 


0+64 = 64 

64+64 = 128

128 + 64 = 

(Slashes / are called CIDR)







To find out the /24 portion


subnets 


1 subnet servers

1 subnet  servers

1 subnet hosts 


Top line Ron has written : 


255.255.255.224 



How many subnets can we make out of the /24 address range ? 



Ron's Boss : he needs 8 






We can build ACLs, do packet collection, IPS here, IDS there, firewall there  ...



Every time we pass through the gateway, you *audit* and *control* everything that passes through the gateway. 



At Lockheed Martin, and after removing electronics from your person, and passing through the gates, you are still in the lobby : but you have had your picture taken, you were logged that you walked in, checked if you had electronics on you, and this is all when you get into the lobby. 

When you move from the lobby to the first floor, your movements are monitored. At every transition point, you have to monitor that transition point. 


Ron would like us for a moment to tell him what will happen if Ron's boss asked Ron to have 64 subnets from a /24. 

Calculate the netmask for a 64 subnet? 



11111111.11111111.11111111.11111100


How many computers we can put on each subnet ? 2 due to the last 2 bits available. 




If the network will be congested with traffic due to 2 nodes on each 64 subet. 


/26
/26
/26 ..


If we want four hosts on each subnet ; just the four printers, just the four computers. 


We do not know hwerre the transition is, bvut we move into something called **micro subnetting**


If we are given a /24 network, whatw will you do to make it secure ? 


I will microsubnet, and I will make each microsubnet to be able to do what it needs to do. 



If we have to have 8 possible hosts on each subnet, and we have been given a /24 network to woprk withj, and we want a maximum of 8 hosts on each subnet. How many actual addresses we need? we would need 10 addresses



Trickier : maximum of 7 usable addresses on each subnet . How many actual addresses we need? 9 ( network address + broadcast address)







11111111.11111111.11111111.












The last assignment : given four subnets with the network address and broadcast address for each




11111111.11111111.11111111.11111100





We need 9 possible addresses. How many bits that would represent 9 ? 


4 bits 


0000 ---> possible addresses


If we have four bits in zeros , we have 4 bits we can use for the network addresses . 


How many addresses we can represent with four bits ? 2^4 = 16. 



This is the maximum number of subnets available. 


It is all about how many hosts we can have on each subnet
 
 
 
 If we need room for 17 usable addresses ( 15 hosts _) 
 
 
 
There is no half bits , so it is 2^3 = 8 




Hint : Leave yourself a little room for expansion. If we have 8 subnets with 30 hosts on each one, and you go to each host, and you give it a subnet mask , what is its subnet mask ? 




8 networks 


Let us start withs the hosts : 



32 addresses , 


We need 5 bits 


The rest are the subnet 


128+64+32

255.255.255.224


11111111.11111111.11111111.11100000






If we are in the same network range, every broadcast packet will hit everyone. 



SUbnetting : You are limiting traffic to only the information that needs to be seen on that traffic. There are a lot of packets flying everywhere in the network, and they are all talkiing to eahc other. You can improve the performance, cut down on congestion, and increase effeciency. Also, the other reason is security ; you get inherit security by limiting access between subnets. Or the machine cannot construct the IP address to find it, because its netmask does not match the netmask on that subnet. The number of the interface is the address on the network. That address is made of your host address and your netmask. 


You get increased security by micro subnetting. The only limitation is the initial allocation of IP addresses. Microsubnetting is the same thing. 




we have 4 networks , which having 64 addresses. We will divide the 64 possible addresses into four subnets. 


We can have a problem if we have a large number of subnets : 



/24  

/25




An interview question : /16 divided into four subnets , what are the addresses? 



Please reflect on how much you have learned. 



Practice subnetting





