




We took a *switch*, and hooked up *4 PCs *to it, so they can ping each other. 




We can do a **PING** packet in Packet Tracer. We can see the contents of the PING packet. 


Later on, we will talk about **Network Traffic Monitoring**. 



The **Packet's Outter shell** is called a **Header**. The Header contains information about the source, and the destination :


IP Address we are sending it to

Protocol

Port destination 

IP address from the source



The way it ACTUALLY works is boxes within boxes within boxes. Akin to a *Russian Doll*



On the outmost layer, the **HEADER** ...


The **HEADER** contains a **PAYLOAD**...


Within the **PAYLOAD** is another **HEADER** ...


The another **HEADER** contains a **PAYLOAD** 



On the local segment, we use the MAC ADDRESS. Does the MAC ADDRESS and the HEADER match ? The network card sees every packet that passes through the local segment



If sending a packet top some one else in the world (google facebook etc), it is outside of the network


On the outer layer, MAC ADDRESS
Next level , IP ADDRESS 


Destination : Destination IP address 



The other network : "Which one of my machines has the MAC/IP address that you are trying to find"? 



Strips the IP ADDRESS from the header, and creates a new header... 



PDU : Protocol Data Unit (Packet) .. On the outer version It has an ETHERNET PROTOCOL HEADER , 


Sending a machine from one machine via the switch to the other machine, so it would have the MAC ADDRESS< and other statistical information to help the other computer to process the packet. 


At the bottom, We are look at the inbound details (in Packet Tracer)


Inside the outer layer of the packet, we have an ICMP packet (Ping is ECHO requent, "Are you out there? if so , please repy")


The response packet : in the lower layer, there is ECHO REPLY. This is dictated by TYPE AND CODE. It dictates what this packet is meant to be. Echo Reply could be "Destination Host Unreachable!". It is another type. It could be "YES SOMETHING IS HERE!". The difference is, does the machine allow ICMP? 



Why disallow PINGs ? To make the PC undiscoverable. Attackers will enumerate the network. The attacker starts with a PING at the lowest segment. It is Mapping the Network. All the machines that reply will indicate that there is a machine there. If you get "Destination Host Unreachable", it does not mean the machine is not there, but something is preventing PINGs, or it might be a router or firewall preventing PING packets from passing through. it is a "...Maybe? ". The request timing out means "NOTHING IS HERE!". 




Last week, we had the four computers and the switch with Packet Tracer. It is ALWAYS good to start with the Network Design .



1. Put the PCs on the map
2. Put notes under each PC indicating its purpose, or what we intend to do, and the mapping (which port etc)
3. We can configure each machine, so we keep track of the ports we connect it to on the switch. 
4. These machines are all in the same network. The netmask is /24, which means 2^8 possible network addresses. We loose one to the address of the router, lose another to the broadcast address.

Because they are all in the .10 network, they communicate with each other. 


We have the hallway with all the pcs having doors on this hallway. Someone entering the hallway, they can see everything. 


We aim to make it confusing. Let us launch Packet Tracer. 


We are setting up **Subnets**, 2 computers in one , and 2 in another.



We can create a **VLAN**, which is a *LAN within a LAN*.


We will click on the Switch , Enable , Conf (T) ( Switch - CLI - Enable - Conf T - Show VLAN


We have the Default VLAN - VLAN1. Every machine initially will be on VLAN1. We can not delete VLAN1 or rename it. From the list of VLANs (1002-1005), there are other VLANs, Gigabit Ethernet1 and Gigabit Ethernet 2 are assigned to VLAN1. We want to separate them by creating two new vlans.



COMP T - Give VLAN a name or number  (placed in Notes, for PC1 , place it in VLAN 20, and PC2, VLAN 20. PC3 shall be placed on VLAN 30, and PC4 will be placed on VLAN 30

We need two new VLANS : VLAN 20 and VLAN 30


Comp T - VLAN 20 

He will give it a name (VLAN20), we go from configure prompt to configure VLAN prompt. Let us call the first VLAN 20 (on top) : Sails , and VLAN 30 (on bottom) : ADMIN


conf t  -- If we are in command line, CISCO refers to Fast Ethernet as Fast-A, so type FA and hit tab for autocomplete. 

VLAN 20 - Afterwards: name  Sails
VLAN 30 - Afterwards: name  ADMIN





We go into the Switch , At the Privileged Exec Mode, want to go to "conf t" to configure some interfaces. To get into the interface on the switch "int + tab", it is a good idea to type "?", the interesting thing about the "?" it gives you the options you would type next, and puts you at the command prompt. To configure fast ethernet :

FA + tab + ? 

It is looking for an interface number . Which interface are we configuring ? FA-1

We get in "config-if" interface. These are two commands that there is nothing demonic about them, remember these two commands!


(In the notes, below the PC, we indicated that we connect to FA-01, the port where we plugged the pc into the switch.)


Interface  FastEthernet0/1

COMMIT TO MEMORY : 


switchport mode access 

switchport = switchboard we are working with 

We will adjust the MODE of the switchboard (access : means that the pc will communicate) (There is another mode we will get into later )


Fast Ethernet-01 is now in ACCESS mode. We want to connect first VLAN to it. 

switchboard access ? 

? will show possible options 

switchboard access vlan 20 (which vlan are we attaching to this interface? Answer: 20)


#### Commands 


Conf t 

interface fa0/1


Interface fa 01 : switchboard access VLAN 20


Back in priviledged exec --> exit


Show VLAN


We have 20:Sails vlan, but FA-01 is moved from standard default VLAN to the new VLAN 


We will do the same thing for the other port on the other side. FA-03



Go into the switch : 


conf t 

global config - Fast Ethernet interface


int fa 03/3


(Interface Configuration) : switchboard mode access

switchboard access vlan 20 

(back to priviledged exec mode)


show vlan 




Conf t 


Configure an interface : int FA 02


(We want standard access mode )


switchboard mode access

switchboard access vlan 30 






Last interface  ( FA/04)



conf t


int FA 04

switchboard mode access 


switchboard access vlan 30

(privileged exec mode)

show VLAN



Last result (


vlan 20 
vlan 30 
)




(make sure to type EXIT constantly until we get to the root prompt)


switch #





))


ENABLE first!

conf t


int fa/01
switchport mode access
swithcport access vlan 20
int fa/02
switchport mode access
switchpport access vlan 20 


int fa/03
switchport mode access
switchport access vlan 30



int fa/04
switchport mode access
switchport access vlan 30





Layers of commands : 




USERMODE  - >  "EN"
		Global Config --> conf t 
				Interface Configuration --> int (interfacenumber)


to change VLAN's name : 


vlan 20
name "New Name"



Make subnet number same as the VLAN number : 

Change computers to ;
             (vlan number-to name the new subnet)
192.168. 20.


PC - Desktop - IP configuration - change 10 to 20 in the IP address
PC - Desktop - IP configuration - change 10 to 20 in the IP address

PC - Desktop - IP configuration - change 10 to 30 in the IP Address
PC - Desktop - IP configuration - change 10 to 30 in the IP address





We are bound to have more than 1 switch ...




If we put another switch in this network, 


Crossover cable : cables have Send and Receive |   |  - Crossover cable has   X    send is receive for one side, and receive is send , they are cross-wired


They are for connecting two switches, so the two switches can send traffic back and forth! 


We separated the network into 2 VLANs. How can be make them communicate ? 


Put two cables ? 

It would work, but not ideal 


We may have 50 switches, so its too much to put 100 cables for example 


We change the switchboard to another mode, (switchport mode access is to let machines talk to each other)


Other mode : trunkline 




We have two switches 





			Switch 1                                           Switch 2
	We want multiple vlans across on cable 


We will have a command 

	Switch1                                 Switch 2
     \                                                     \
FA0/5                                 FA0/5 




Command : 

>switchport mode trunk 

We will have to configure the ports to "mode trunk" : 


There has to be an additional step that takes place at the switchport 


we have 2 vlans : 

Switch1 

vlan 20                         vlan 30 




Switch 2 


vlan 20                   vlan 30 



Trunk is like a railway train or a boxcarts , or a package 







When the packet comes in, the packet has a tagh ( bound for vlan 20),   switch receives packet (for vlan 20, remove wrapper) , pass message to node 


Switch ( note : for vlan 30 , wrapper removed ) pass it on 



When the message is received by the switch 2, we need to put a packet on the container (encapsulation), putting the box within a larger box 



Theere is a protocol tyhat dictates the ruyle for encapslulation 


encapsulation protocol 801.Q 


Packet comes in from VLAN 20 , gets containarized (encapsulated, with note for VLAN 20), ships to switch 2 , arrives with the note (for VLAN 20), switch 2 removes8 the note, and passes the packet to the correct VLAN. We will do that next class. It is how we add trunklines and allow VLANs to communicate with eachother. 


If you have PCs that you havbe left on VLAN1 (should  NEVER DO so), the attacker will come in and sear h for VLAN 1. The admin does not know what they are doing. Move the pcs into separate VLANs. 



instead of 


switchport access vlan 20 


We will have to allow a range of vlans 


command : switchport access allow vlan 20-50 


So that when the packet arrives at the switch 1 for encapsulation, the switch will ask where is it from? it will check the configuration to see if it is allowed, it is , it gets sent, if not, it wont get accross. 


Notice that the face that VLAN- 20 and V LAN 20 has nothing to do with how it works. We could have called them VLAN 50 and 20, 


Numbering scheme in VLANs and their numbers has nothing to do with its functionlaity, but it is an accepted standard for the naming to make it easier to understand. 



Ron recommends playing with Packet Tracer. There is a series of 10 \-12 commands which will be used to confdigure switches. If we are working on a netwotrk's design, all these commands will be front of mind 


PRactice them daily! If having trouble memorizing commands, we are all going through this. 


It will help to have cheatnotes . It is just like plumbing. 