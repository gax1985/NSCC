



# Software-Defined Networks




In the beginning, users used to do programming for Network interfaces, switches and routers

It involves configuring each piece of hardware on its own




## Present Day ...



The structure is not scalable. Why ? 


1. The network infrastructures now is very vast. Nowadays, it involves pushing policies, so **Software Managing a *Network***.

2. 50 Access Points : 
   
   
	   He was on site in Capre Breton, installing a wireless network for Central SUpplies ( some company). They put the devices in, provided a spreadsheet to the technician. It required the technician with credentials to configure for each access point. The technician does it. When checking, nothing connected. The technician tested it in labs. When copying and pasting, there is an extra " " at the end. 




#### Software Defined Networking : 


Unifi is NOT the only game in town


We are getting a demonstration for this feature common now to all hardware manufacturers. 


Nowdays, it does not involve being physically-present on site. Things are done remotely now. 



###### The Demonstration :



Back in the day, he had to have the host connect directly to a network. We spoke about AAA security. We are based remotely, but we have a *Unifi* node. 
(This is how we will be configuring networks from now on ...)

We have our network : 



Technician : 



Technician wants to configure nertwork. Network is copnnected to a cloud, and tghje cloud is connecting to secure server. Network is authenticating to the secure server in the cloud. It is similar to AAA, both technician and network have an internet connection, but what is happening is that the device is reacing out to the cloud. What do firewalls do? they drop traffic. The network reaches out gets a protected tunnel to the server. This is a two factor connection, where the device we intend on managing is also connecting to the secure server in the clouds. The software part sits in the cloud. 


You can place the Unifi software on a local server if you wish! 



What would happen if the Internet connection went down? 

All of the equipment that has this software will continue to operate, albeit without internet access. When pushing the program to the device, the device retains the programming. This makes it resilient. Networking has become an application!
The software now manages the device. 



In order to manage the device, the device had to be configured to connect to unifi, to the cloud and to us connected to unifi


On the main Unifi page, the examined traffic is inspected by the firewall via **Deep Packet Inspection**. What it is NOT doing is looking at *encrypted traffic*, but the header of the traffic will identify which site is coming from. The confidential information remains encrypted. 


We spoke about *topology*, in terms of the old-way :


He used to launch a design software to design networks. The software nowadays knows which service provider it is, which device is connected to which port, and it knows what device is on the other end via hardware identifiers. 


The experience column tells you what connection performance to expect. If a phone goes to sleep, it does not necessarily know. It may say that it is an iffy connection .  It is not completely accurate ( as in "how does it arrive to this conclusion?" or "which connection it considers to be best? ")


In the olden days, you would have to find the MAC ADDRESS for the device, login to the access point, issue commands via the terminal ... 

When examing a device, it knows what kidn of iphone it is, which network it joined, which channel, how wide the channel, what kindd of signal , transfer/receive rates etc ... 
If the phone is sleeping, we would see a high Tx (transfer rate) , and a low Rx (Receiving) rate

-46db in wireless signal is almost immediately under the access point (which means it is a strong signal). 

Devices connected to the network :  We see the firewall appliance (routing DNS DHCP, layer 3 on steriods) , network switches , and finally wireless access points. The site is two physical buildings connected wirelessly via a bridge. The connection is a dish called a "Bridge Kit", and they automatically coordinate a secure link between the two points. Every day all day, anytime you link something wirelessly, it has to be in the line-of-sight. Building Bridge - $667 - (These are NOT CLIENT ACCESS RADIOS). It is meant to be a Bridge only. They are sold as a pair, and you cannot add a third one in the middle. Client access radios are for clients to connect to. This Bridge is for connecting two buildings together. for 60ghz the $667 price is great. The higher the frequency, the better the transfer speed.  (signals attenuate through solid objects) 

Google **Pernnel Zone**


Unify can identify threats, but it is NOT RELIABLE AS THE SOLE defensive firewall. You can block certain countries, block imposter DNS, block suspicious activities. 

Unifi is a good system for school networks. Unifi got caught (same as Mictrosoft) sending the users' data elsewhere to make money, as they would use it in advertising. Unifi retained everything (not banking informaiton) back to Unifi to sell to third parties. Info such as who is accessing which site etc ... thus, there is an OPTOUT option. If you chose this, it would retain what device accessed the network, and see the device's connection/history. 

Power-Over-Ethernet-Lightening : POwer injector (48V X 1.5 A). The way they work: we have a port that goes to a device (access point), which provides a power and ethernet connection. The switch when connect gets its network connectivity. Now, the switch port itself provides network connectivity AND power. The NSPower builiding on the waterfront ( and the Tesla headlights) have the ligths connected via ethernet cabling.



Question : Explain a single low voltage network cable running it to a light , where it provides complete control over the light in addition to providing power. PoE has been around for 15-20 years. 

We spoke about AAA authentication which prevents tampering with a PoE device. An intruder's device would get blocked. We can tell the switch to provide PoE only (power) but no way to control the lights. 
#### Next Assignment : 

we will connect to a remote network
We will set up a wireless network, set up a vpn 


What is happening is : 


1. Networks : 

	When we set up a network, we would have name , ip address, subnet mask , gateway , DNS , .... you create the network, save the network, and the settings get pushed out to ALL the connected devices. The Unifi can sync settings in 30 seconds. When we set up the VPN clients and servers, the same thing would happen. 


	Underneath it all, it is using the same industry standard protocols (such as IpSEC), and it is not using its proprietary protocol. We can connect devices from different manufacturers this way because they would both use teh same protocols. 


	The Unifi or any SDM network : Site=-toSite
	Client to Server: We connect to a building
	Server to server : The VPN client we see on Unifi , we will do that ourselves. We have an application now which detects with the range/ geolocation of the wireless netowrk, it would authenticate the client (multi factor) into the network ( like a liternal fingerprint)


UnifiProtect : Cameras
UnifiAccess : keyfobs
Unifi Talk : Voip
UnifiCOnnect: connecting all the clients together


Cisco and Miraki do not have the integrations yet ( they charge too much for things)


Project : 

We have to go in , set up Unifi, we log in to the device, set up a wireless network. Everything takes place in software, but we would have physical access points that we connect to ourselves. 








