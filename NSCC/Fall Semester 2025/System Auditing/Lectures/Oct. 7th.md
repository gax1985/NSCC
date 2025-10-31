

You have to collect network traffic, as it is the last line of defense that is untouchable by attackers. 


if you have IPS/IDS set up, the biggest mistake is to assume that all these things are working. It is an assumption of protection. 

You MUST testing it. You must review what is actually happening in the network. 

There is a big difference between what you expect to happen on your network, and what is actually happening on the network. This exists due to lack of testing .



## Things to watch out for 


### Red flags 

#### Unfamiliar IP addresses

Writing a program that would routinely write and display all the IP addresses that are making connections.

Central Ops would help in case we do not want to write the program. 

Collect netflow from Monday to Friday. 

Central Ops + Data Logging applications would help considerably!


>[!question]
>
>How would I script that? which commands need to happen in order to perform the activities ?


#### Number of Connections

A few weeks ago, the secret is *Unique-Values-per-Unit-Time*. We are looking for **behavior**. What are those things doing? 

Which question would you ask of the data ? --> "How many unique IPs is each computer talking to today? per day ? per week ? per hour ?"

Unique Value --> IPs 
Unique Unit Value --> Per Day (ordinary number : 2000 +- 500) on a Typical Windows Workstation 


We can write the query in , scroll the screen , and suddenly one is 10000 connections or 35000 connections , then this host gets added to the investigation's TODO list. 

We are looking for the unusual. Consider this data, and if you are a hacker or malware, you cannot help but leave this data behind. You must communicate to an entity outside this machine in order to function. You are either exfiltrating data, adding a machine to a botnet, running a Bitcoin Miner, and when you communicate outside, you leave data about your network traffic. Online gaming is a non-malicious cause of this, due to their peer-to-peer nature. Peer-to-peer systems would leave evidence like that, due to it being a security risk. 

#### Protocols-per-Day

You will see a maximum of *five* protocols.

A machine might talk to an IP address 10000 times that day through *one* protocol. 

Typically, we only see *three* : (Remember these numbers!)

	1. UDP --> Protocol 17
	2. TCP --> Protocol 6
	3. ICMP -> Protocol 1

The other two : 

Depending on complexity of the network : 

	4. BGP

Database Query --> "Count the Protocols!"

If we see ten protocols , what are those protocols ? Protocols are stored in a 8-bit number. Not all of them are used, but what are some specialized protocols that may show up in network traffic? Operational Technology, SCADA, Water Distribution Systems , and so on. If your organization , like a municipality, they may have certain protocols like this. If it is an ordinary organization, then you can tell that they are being scanned, potentially methodically, in a manner that indicates active reconnaissance attempts. Someone is in the network doing enumeration (what is available to me?), which basically maps out what is there in the network. If they are caught at that time, then you can stop the attack (when considering an **Attack Killchain**). 

#### Destination Ports

Destination ports are tied to **Services**. If they are trying to find the database server (3306) for example, seeing this in data would trigger alarm bells. There are as many ports as there are destination IP addresses. Port Scanners would evidently leave behind such evidence. 

In the list of Unique Destination IPs for computers on your network, 2000 is not suspicious, consider how many are currently in the lab network? not that many : Mail Server, Database Server and so on. What if it is talking to every IP address in the network? this is evidence of reconnaissance. It is talking to all of them. 

Within the ports we are looking for, what are ports of immediate interest to us ? If we are looking at network traffic for a week, let us list some important ports :

##### Destination ports that allow Remote Access to machine

65535 Application Protocols 

1. SSH  
2. RDP
3. TELNET --> still active in many networks, but many network administrators do not know it is there. 
   
If there is an application protocol that leads to remote access, which of these computers are trying to access these ports? 

This is evidence of **Lateral Movement**. Someone entered the receptionist's computer, and is trying to remotely connect to other computers/nodes on the network. They are inside, and they could often lurk in the network, and take their time trying different ports on other systems. 

##### Destination ports that Transmit Data

We can separate, not now, web traffic. There could be terrible things in it, but it would obscure our view. We are looking at : 

1. FTP
2. NFS
3. SMB
   
If we have the database, we can program our way into delivering data into it, and building an understanding of the network in which the owners of the networks do not know about. We would have to find out sources of unusual ports, protocols, different purpose identification and figuring out if the activity belongs there in the network. 

You would not spend much time looking at reports, because *the Flow data has all kinds of information to tell you, and it is waiting for you to ask the Right Question*. They have limited the number of vocabulary words you can use. Thus, it is liberating to output the data to a database, and compose the right questions and the right queries. 

Every time you are thinking about a query or a question, you would ask yourself :

**"How do I script that into reality?"**

If you start seeing FTPs and SSHs , then you would set up *Alerts*! If you are in a high-security environment, program in steps to isolate that node. 


#### Packet Flags


It is lower on the list.

You can take the data from the flow report, and output the data into a table field in a database dedicated to packet headers. 




# Steps :


1. Take the flow
2. Separate them into a flow file
3. Create a SQL database
4. Query the Database!



>[!note]
>
>The next section is **Windows**. Next Tuesday is our *Comprehension Quiz* :
>
Consider the steps you have done to set up the router. Brightspace Quiz. You will type your answer :
>
>1. Components you set up on the router : sub-interfaces, exporters, monitors (what settings you have chosen? Time-Outs -> benefits of short-time-out to long time outs, it is the number of seconds the router will wait until it sends its data. Quick timeout --> live monitoring, testing routing. It may make sense of a longer time out --> if you are sending certain types of traffic across the network, you have to do certain things. A lot of communications might impact network performance. Typically, the channel you use to get from the router to the collector, if done properly, does not go over the network. it would go through a side-channel network, in order to avoid impacting production communications. Cache Size --> how much data do you want in a single shipment. "How you use the Flow Data?" , "what are the problems with a microsegmented/NATed network when it comes to flow collection?" --> if we are inside a NATed network, and the collector is on the router, we could never see the traffic between the two machines due to them not having to communicate through the router. Unless the taps are properly located, you can either not see the traffic if it is just passing through a switch, or you will see only the publically facing IP of the NAT Box instead of the IP address pertaining to the relavent machine). These are the concepts we need to know in order to do Network Security on our networks. 



We have :

Router

Three Segments 

Swicthes for each segment

If we collect traffic in the network, we can see traffic going in and our of the segment, but we can not see the traffic between the two pcs

Take a switch port, attach a PC to it with promiscuous mode (seeing all traffic across the switch ) or , instead of having a PC with promiscuous host, you can make the port a **Mirror Port** on the managed switch, thus making the switch port itself Promiscuous.

We have to put the taps inside the segments, and inside the NAT boxes. 

We must have the identifiers of both ends of the conversations : 

1. IPs of machines
2. IPs of Destinations 

In a NATed network, we see the IP of the NAT Box. 


## Visibility within Segments


We have a person who attaches to one segment, first thing they we do is enumerate the segment ( first activity ). If segmentation is done properly and proper network security is done, they would not be able to access the remainder of the network. Old timers made the mistake of not monitoring *Lateral Movement*. It is the first evidence of intrusion! It did not exist during that time. Most of the attacks came from the outside world. Two things increased Lateral Movement : 

1. Deployment of Mobile Computers ( Laptops, Phones,  etc ) 

	If the PC is well guarded, it stays there. If they take it home, it opens the door to unwanted behavior. 

2. Internet Pre-2000s and how we use it after 2000s 

	Prior to 1990s , Internet is for technical individuals, and after 2000, everyone is on it. Social Media use started in post-2006 era. 





