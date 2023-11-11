



> [!note] 
> Today, we will be covering **Nessus Essentials** and a bit on **Wireshark**


#### Brute Forcing : 

	We would keep trying passwords to see if we can get in . 

#### Rainbow Table : 

	A table full of hashes. 





#### The Hacker Database Assignment : 



The key is to **focus on the design!** We can do so from an *ERD Diagram* for example.  



## Nessus 



It has the ability to check the registry if we are doing a **Credential-Based Scan**. It will check each software that one has, and it would compare its vulnerabilities.  All the types of tests are contained in **Policies**. 


We have a **Host-Discovery Scan**, akin to *Nmap*. 


We would give our scan a name 


**Discovery** by default has all the standard ports, but we can do a custom scan. We can scan **ALL PORTS**. General resettings, where **Fast Network Scanning** would scan for open ports and if there aren't any 


Under the Advanced section, it will scan 30 maximum hosts. 




Authentication : It should be a real administrator account vs a regular user accoutn with administrative privileges. 


We can give it a ./ to let it know it is a local domain. We can choose to log in on our local macvhine to 



START REMOTE REGISTRY DURING SURFACE SCAN : The registry stores information on all the installed programs, For scanning ,i t needs to do it remotelyt : We have tp clickl on "Star t the remote rewgistry rservice dutring the scan"  and "Allow Remote Registrty " is off  obn the com[puter by default. 


If we choose to click on the SSH 



SETTINGS-ADVANCED - We have **Safe Checks** enabled : Nessus can be very aggresive, so it will test for a potential vulnerability. IT can cause problems in a production environment. If we have **Safe Checks** on, it will not be aggresive. We should leave it on! If we have a machine disconnected from the production system, and we want to check it, we can disable this option. There is danger associated with it


Policies : We can create a new Policy, make adjustments, and save the policy under a new name . 



We can do "Host Discovery " , call it "Ron's Host Discovery ", Port Scan , AlL ports. 


Two Componenets : Policies the scanner will use, and the Scan. We can use a template of the policy, make some changes, and save it. 



New Scan -- User Defined Policies - Ron's Basic Discovery. 



We can choose a Schedule - We can do a Daily Scan, and choose 4AM to scan all the nodes on the network. 



We can set it to email me once a vulnerabiltiy is detected. 







TODO : 


CHeck the **Policies** available for us , and we can click on them to see them. 




Packet has a header and a payload, and encapsubales another header and a payloard. 



In Wireshark, we are looking at a Frame, which is shipped across the cable . 


Header is a first protocol header used to find another machine we are looking for.  

Source IP 

destination IP  111111.111111.1.111111.1111111 Broadcast IP address : this is going to all the machienes on the local network. IT tries to ffind the desitnation's mac address. All the FFFFFFFFFFFF in the Mac address is equivalent to the 255.255.255.255 . It has Type IPV4 . if we look at the packet, we will find a hexadecimal number there. What it says this ethernet frame contains an IPV4 packet. 




What is Wireshark Doing ? it is doing a Full Packet Capture 



Something emerges/ arrives from ouyr netwokr card. Whaever is leaving or coming has to be inside an Eethernet packet. The 1st header 





1st Header : Ethernet 2 Header  : has source mac address, destination mac address,  (inside my payload, there is another packet : gives hexadecimal number , and we can look it up to find what it is . Wireshark does that for you, and it says " I have an embedded IPV4 Packet")


(We can open it up annd have a look  : Source address / Destination Address , it has a 255, which means it is a Broadcast Packet) . Flags are set as 0x2, 010 is the binary number for 2, it has a "Time to live", which is the number of routers it is allowed to pass through before the packet dies. Every time it passes through a router, it decrements the time by 1 




Local Network --(with computers ) ----------------------router (connected to the external network. Ron is not on the segment to this room, as it is on wireless )  ------------------------- other segments 


Router is thus called a gateway (somewhere other than the local segment )




This packet originated on some machine in the local network. It was given a "Time to Live " of "1". It never wantos to leave the local segmnent. It does not want to broadcast to the internet; just the local segment. Whebn it reaches the router, it sets "Time to live - 1"= At the router, time to live becomes 0, and thus it dies. 



Something cool to try : Go out to an Administrative command prompt in windows.  We know about "ping". We will ping cnn.com. It translates it to an IP address. It sended 32 bytes, it took 71 miliseconds to go through the route. It found it, and the time to live is 55 router jumps before it dies. 


If we want it to go to a long complex location, we would want it to  ste it to a large number



Traceroute will provide the IP address of every router it encounters on the way. From Ron's computer, it went to the first wireless gateway (since he is on wifi)

then 10.0

then 10 , 0


this is NSCC's infrastructrure. 


It kept going through internal router,s, and then 


it got out to the internet. to an eastlink router


then it hops to another ewastlink router


then another eastyink trouter


then another router that was not eastlink (204. )



it wqent to a US-based address. 

Then it reached CNN.comn


This is thorugh 8Tracert ., hwo does it do this >? 



When a Ping packetTTL goes to 0, it sends a reply  back to the host with the IP address of teh router it died on. Trace Route sends pings constantly, and it starts with a tTL of 1. It sent a puing to send to cnn , and it gave it a TTL of 1. and  it sends the IP addrtess pof the router it died on . Then traceroute sends another ping packet with a TTL of 2, and then it dies, and it sends back the IP address. 



Question : it is not exactly the same route ? The ping packet at the very end of the traceroute might not necessarily have passed through the long list of nodes. 



Trace Route is A CLUJ : aka a trick or a cluje. If we are to have some fun with networking, we can open Wirteshark and at the command line window, we can tracewroute to CNN.com, and in Wireshark wer will see all the ping packets going ouyt, and it would show the TTL increasing by 1 each tuime. It uysed to be an assigbnment. 0


-----------------------------------

The router picks the best path. A spegetti connection on the web 







In the ethernety header , the time to live is 1, if it does not want to leave the local segmewnt , as it wants to die at the gateway. We have an :



IPV4 HeadeR : TTL of 1 , Source/Destination Address ---> This IPV4 Packet contains a protocol header, and it tells us it contains a UDP packet inside of it (inettestihng that it is sending a bropadcast UDP packeht) 



---



We go look at its UDP header : 



At the top level;, source 3300, Ron asked us to look it up to see what it is associated with ---> (EMC Patrol Agent )


There will not be anything facinating  due to it being on a local segment. It could be that this port number would be from an local machine that is compromised., so this is why we look it up .
4



The paylload : showing at the bottom of the captyred packet (UDP is 23 bytes long , it is represented in Hex. On the data window, the part that is highlighted would be the payload. On the right hand side of the data window, we have an ASCII translatoipnm of the Binary.) Wireshark does one-leve translaation of bvinary to hex., The data portion : it takes one more step, and it translates HEX into ASCII., If we are transmitting clear text, we would be able to read it on the ASCII side. 



ROn diud a demonstration , where individuals had to search teh network tranffic for an encrtpted code, and to analyze the traffic's data portion, and this would contain the cleartext kety to disarm the bomb. 



Ibnb that situation, it is not understandable (the ASCII bit). 



They useds to try to break the licernse code for a video gamne, and they would capture the traffic to investigate the licensing packet, and then capture it on another machien to try to break it










EWthernet Header " Imbedded UIPPV4 Packewr : 
----------

IPV4 Heasdewr : TTL 1   | UDP
---------------


UDP Header


------------


DATA



{this is the pakcket that hit Ron's machine } : it had a header, payload (which contained a header + payload, which contained a header + payload)


(if this was a TCP packet, we would see the Ethernmet 2 header + IPV4 + TCP etc)


In the 1980s there was a game where it was in text : "Please Login " , wehre it would give clues by tyuping HELP



We can do a version of this where it would give an output from a data paCKET, and then try to decern what it says



When doing foreinsics, in hex, we would have cluies. 




--------------------------------------------




On an average day, the d esktop talks to 2000 destination IPs, Compyuetrs are always talking to other computers. When you look at a computer that is on , we can look inside and see that it is incredibly busy..




----------------------


Ron did a Nessus scan, observed the activity in Packet Tracer, 

We were looking at the IPV4 Frame -- it showed the machines talking to eachother. 
 



He wanted to know which pc his computer was speaking to . His IP address ended with 248. 





When a flow is built it records the size in bytes, and the number of packets. Using the five rtuples, wirehark matches them together, and  rebuilt them for Ron. Since it is a UDP packet, it had no flags. There are a number of filters that we can apply, such as an IP address, specific type of packet, and it eliminates the other packets on the screen (akin to a WHERE clause). 




Ron went back to Nessus. 



Scan Standard Template ab\gainst our own address, or a neighbour's IP address. 




> [!check] 
> Write down the admin user name, admin password, if you lose it, therte is no way to recover it.  



> [!todo] 
>  
>  Next week : we will get an assignment that will require the use of Nessus and NMap. 