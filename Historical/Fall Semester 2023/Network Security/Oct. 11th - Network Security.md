



Packet tracer is all about connecting things together, making things flow like valves and switches. Ron finds it a bit of a challenge to relate it to real-life. In real life, there are a lot of devices on a rack. 


It helps to imagine the real world. The example we have done is like the computers of this classroom. Wires go from the computers through the wall, gets plugged in to a switchboard, this switch would be connected to another switch, and other computers are connected to this switch. 


Imagine a building with closets in rooms. We can draw the whole thing in a practical sense, as it is all about planning. Ron would like us to get into the lab to work with actual switches. 


2nd year students are working on a lot of assignments, and the switches are configured in a particular way for their assignments. 


If we did this, we would be ahead of a 3rd year Computer Science student


When we show up to work, we can start knowing what we are doing from the start.


Nessus and Nmap are fun and valuable tools. We will have an assignment based on packet tracer


Assignments are hands-on pass or fail. He will get us through the pass line. 


He will give us a network diagram to base the assignment on. He will give us some time, and then ask us to ping from one machine to another, and to get each of us to demonstrate our knowledge. 


Do not be intimidated by the pass or fail. Only way we fail is to not show up and not do the work. 


In database, we have to put ; at the end of the command. 


When we put all these commands into a switch(configuring the VLANs on the switch. If we turn it off, all our work goes away ) 


Switches and routers have configuration files. When we are making all these changes, we are changing the configuration file, we are changing the file into a RAM. Unless we write to a disk, it goes away :

We have 2 configurations :

1. RAM
2. Disk

We do the following command to copy the settings from **RAM** to **Disk** :


>copy run start

it will ask : 

>Do you want to save them to startup config?


Why does it ask? we can have multiple configuration files. If we have a switch that we are testing (hypnotically to a building on Barrington), we copy to a backup file :

>copy barrington run --> copies to the run config (bootup config)
>copy run config  -------> copies the bootup config to current config
>


In this settings ,we had two VLANs (VLAN 20 and VLAN 30), these connections are connected to the switches, and the switches are connected via a **Trunk cable**. 


PING ROUTE --> Shows a graphical example of a packet travelling through the network. 


He is showing us the 0,12 wrapper


He will tell us when to use a straight through cable or a crossover cable


These VLANS cannot talk to each other because they are separated. 


Now, he will configure them to talk to each other via *Routing*


The **Router** will give the ability for the two VLANs to talk to each other 


Grab a router, 4331


Connect it with a **Straightthroough cable**


The router has a gigabit ethernet (faster than switches.)


Connect from a gigabit port on the router . Switches have 28 ports on them. Routers have 2 ports , serial port and a console cable


If we want the two VLANs to talk to the router, we can have 2 cables , one from one switch, and another from the other switch. 


If we have multiple VLANS to go across one cable, 


>conf t
>#Go into interface , normally "fa 0/1"
>gig ? to see options --> it is looking for the interface number. 
>gig fa 0/1
>switchboard trunk
>switchboard trunk allow vlan 0-99
>(go to the commandline on the router)
>exec
>conf t interface gigabit 0/1

He made this difficult for himself as he needed to remember what he did. It is a good idea to add notes : 

	gig 0/1 - it will be a trunk but different than we think 

	gig 
	0/1 allow 
	vlan 0-99 ---?


now go back to the switch to figure out where to place the trunk on : 

He has multiple VLANs that have to reach this router, but we have one cable connecting them. On the switch, we do *trunk*. On the router, it needs a different interface for each VLAN. We have it connected to one interface. We can subdivide the interface. We are connected to Gig 0/1, 


If we are in a 192.178.30.200 , and we would like to go to the network, what is the ip address of the router? 

	192.168.1.1


This is a sub-interface on the router, we will have to sub-interface it, just like the trunk associates VLANS with different destinations :


>encapsulation .1q ?

We want to tell it which VLAN is going across to the sub-interface. We are going to call it "Encapsulation".


Note : 

	gig 0/1
	encapsulation
	allowed vlan 1-99
	int 0/0/1 30 vlan 30


The notes are a reminder of which VLAN it is on, when we set the ip address to 192.168.30.1. By making the subinterface .30 , we still have to tell itu which interface it os going on : 

> encapsulation dot1q 30


Now we told it to put VLAN 30 across this subinterface. Now, I would like it to have an ip address to be router for 192.168.30.1 : 

>ip address 192.168.30.1 255.255.255.0


Prevent it from shutting down (putting NO before it negates the option. so no vlan30 to take out the error if it was set in error)

> no shut





We have a router, and a switch connected to it. We connect a gigaport here to gig ethernet port on the router. 

Megabit = 1 million bits/second 
10 Megabit = 10 million bit/second


That is enough for a network in the house, but we can go to 2 gigabit. 


Ron worked with petabit networks. 


The main connection between NA and Europe comes from Ireland and goes to Sambro,NS. These petabit networks go by the sea. The line spliots before Sambro and goes to NYC. Therew is one hop bnetween Sambro and Ireland. If we look at we are going on Facebook, we are going to Ireland, because it is closer for us. Remember, geography on the internet is the geography of routers. If we have one router in Halifax and another in Thaiwan, it would be shorter distance form Tauiwan to halifax vs halifax to NYC. 


A very inetersting command is traceroute 

> traceroute facebook.comn 

This command will show you all the routers it hops across. Each router monitors the connections, and knows which is fatser at the moment, and sends it on its way .



Back to the switc and router : 


We define a trunk from router to switch, it will do **Encapsulation for us**. We will split it into 3 multiple interfaces :

1. Going to gig ethernet 0/0/1.30 --> Machines on VLAN 30 into sub uinterface. We call it 30 just as a reminder. We have to manually create the encapsulation at the router's end, and tell it to use VLAN 30 (we do not write it down, but Ron does this as a note). It needs an IP address, and the ip address of the .30 network will be 192.168.30.1 and subnet mask , "no shut (prevent shutdown)"
2. Another machine on VLAN 20, will come across the trunk, and goes into another subinterface on the same cable, and we will call  it "0/0/1.20". Again the .20 is a reminder we are sending VLAN 20 aceross. We have to set the encapsulation on the router's end manually on the router's end. Encapsulation adds it in a container, and it tells it to take the packets to VLAN 20. Give it an IP address 192.168.20.1. We have to do a : "no shut" command. 
3. We need to give the switches ip addresses to administer them. When we click on the switch in Packet Tracer, we are pretending that we plugged in our laptop to the switch

	If we are at home, and we see the ip address of our laptop:

>ip config



PuttY is a terminal serial emulator

If the switch is in another city, we do not need to fly to it. We can telnet into it if it has an ip address. If it does not, we need to plug in directly there. 

We will see the ip. If we go to 192.168.20.1 , we go to the router. 

>switchboard mode trunk --> not available, because we want to split one port into many



Back to Packet Tracer : 


1. en
2. conmft 
3. int gig
4. int gigabitEthernet 0/0/1.20
5. encapsulation dot1Q 20 (we tell it it is VLAN 20)
6. ip address 192.168.20.1 255.255.255.0 (why the netmask? which part of the ip address is the network address and which is the node address -- last 8 bits)
7. no shut
8. end --> goes back to priv. exec mode

We have done a lot of changes so we do this : 


>copy run start


Some commands Ron was typing while trying to deal with the Router not communicating with the switch : 

int gig
conf t
int gigabitEthernet 0/0/1
no shut


Router : 

show run  --> shows the interfaces' information 

Hint : make sure the router is turned on


conf t
int 0/0/1.20 (remember .20 is a note for oneself)
no shut
int gig 0/0/1.30
no shut


int gigabit Ethernet 0/1
no shut


switchboard mode trunk
switchboard mode allowed vlan 1-99



What this will do is allow the two VLANs to communicate. The router has access to both VLANs via a sub-interface

Maximum number of VLANS : 1004-1005. You do not want that many, but it can do it. We separate the VLANs to make sure there are lots of hallways and doors. He wiped it all out when placing the router in there. The router gives extra level of control . We do not want the Sales VLAN to talk to ADMIN VLAN. Since we are ADMIN, we need to able to access it all. The router is like a guard with a clipboard. You can separate machiens to any level you want, such as allowing certain nodes to talk to each other. We can control everything in the router, such as one machine on VLAN 20 cannot talk to another machine on VLAN 20, we can let a port number to be restricted. The router provides **ACCESS CONTROL**< which means, only certain entities are allwoed in. This is done via L

**ACCESS CONTROL LIST** ---> on Friday!



The switches allow you to gain distance, and have more machines. The switch has 24 ports , so he can place 23 machines on there. Leave ONE PORT OPEN. We will need to drop in and change things in the network. When getting to 22 machines , drop another switch in. It tells us how many machines, and also it tells us the distance. When connecting a machine to another machine in another building, we need to keep the cable distance to a minimum. The signal loses power from the resistance due to the longer distance. If we run several extension cords to a motor, it catches fire. We want to reduce the load on any computing device. We do not want it to handle 23 active machines, as it can handle 12 comfortably. A cheap switch might crap out with 23 ports. 


We will use *Access Control Lists* to regulate access to our nodes and our network. We will have an assignment to build a small network with switches, and VLANs and some computers. When we all can do this, we proceed to the next assignment. Then , we have to get into *Network Scanning*, wherew we connect to the network, find all the machines, find all open ports, and use Nessus to do more with these machines. When Ron is doing this professionally, he would connect his laptop, and find all the devices on their networks (including devices they did not know). Then they investigate irregularities, and it is almost always people plugging in devices into a network. If the access device has vulnerabilities, we sort it out. We are **Enumerating** the network. We are looking at all the open ports. This is tremendously tough. People use different machines with different software that uses different ports. If noone SSHes into a machine, close the open 22 port. If you are a hacker, you map the networkl, find all the device,s find all open ports, 3306 is open? MySQL is runnning, find which version of MySQL and see its vulnerability. 


Next phase : how we review them and secure them. 

We will use **NMAP**, and then **Nessus** which is critical!

He wants us to do this in our sleep. 

**Nessus** can go into the registry, find all the installed software, which versions they are, and it tells you which exploit is available , and give you a link to the exploit!



![[Pasted image 20231011100632.png]]