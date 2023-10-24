




We have plenty of network traffic-related applications. The network card has many subroutines to control the type of networking you are doing. 


Instead of typing the subroutines manually, we would have a driver that talks to the network card. The computer talks to the driver, and the driver speaks to the NIC. The NIC talks to the driver, and the driver speaks to the computer. 


#### PCAP


Standard File Protocol Format 

aka **Packet Capture**.


There were two versions of PCAP : 


1. For Windows : 

		WIN-PCAP    ---> This is deprecated. You will need to get rid of it through a multitude of steps. 

There is a replacement for Windows, and it is called **LibPCAP**. 



2. For Linux : 
   
		LIBPCAP



PCAP is required first on the machine. If choosing **nmap** to install Windows, please make sure to install **NPCAP**. When Ron wanted to install *nmap*, he did not use NPCAP. NPCAP is present on newer laptops. 



## NMAP


#### Options : 


-p          Port
-A          When Nmap scans a computer on the network, it will try to figure out with OS is on the machine. It is a guess, but it is often wrong. It slows down the scan a bit.
-T4         Speed of the Scan (1-5)
-v           Verbose Mode



> [!faq] 
> What is **Local Loopback**? 
> 
> Answer : if a program like MySQL is looking for a server, the server will be on the network, so when MySQL starts, it finds it. MySQL's daemon is installed on the computer. We need some way of telling the program to go look at this ip address, but this ip address is a sign to our computer. 
>
> Example : 
> 
> 	192.168.2.3 (IP Address of the Computer )  
> 	Loopback Address : 127.0.0.1   (It is called loopback because it loops back on itself)
> 	aka HOME 
> 	It is used for testing programs that need access to our network.



If we are scanning 127.0.0.1 , we would be scanning outselves.

#### Ports


Ports are akin to radio stations, so only leave open ports that you need only!



When we have a  result, we look up the port that NMAP reports, so in Ron's case, 3306 is MySQL Daemon. 


Port 445 is the port used by EternalBlue


Port 80 can be used by an Anti-Virus fore update purposes. 

Port 8834 is used by Nessus.

Port 913 is VMWare's Authentication Daemon

Since there are so many ports, it is a good idea to have a port list ready and open when scanning ports :


## Port List : 



[[NSCC/NSCC/Network Security/Untitled]]



> [!faq] 
> Filtered Port : Means that the port is blocked
> Unfiltered : The port is open
> 

> [!info] 
>  192.168.0.0/8 (Everything in that network range )


> [!info] 
> nmap -p 1-65535 -T4 -A -v 172.16. * . *   ---> This scans all the IP addresses in that range
> nmap -p 1-65535 -T4 -A 172.0.0.1-255    ---> This scans all the IP addresses within the last octet



## Scanning a Network Range



A client mentions the following IP addresses : 


		192.168.2.0
		192.168.3.0
		192.168.50.0/24

The aim is to find all the machines in that range. We have to be on that network segment. We would use a PING Scan or a SYN scan.  

		-sn     Ping Scan
		-Pn     Bypasses the Ping Scan
		-sS     SYN Scan (SYN/ACK)
		-sF     FIN flag (The way the target responds tells us a bit about the target)
		-sN     NULL Flag(Sends a TCP packet, where if we have an application, the machine gets a TCP packet, and none of the flags are set on it. The PC gets confused. While it is trying to work out this scan, we get to know more about it)
		-sX     Christmas Scan 
		-sM     Maimon Scan


The first thing Ron would do is request the **Network Ranges**. They can be VLANs. He would get on each of these networks, and he would scan just 192.168.50.0/24 or 192.168.50.1-255, where it would scan all possible nodes. It would do a PING scan (-sn). He would get a list of all active nodes , and their IP addresses. If there is a machine that is on the network that no one knows about, and they would go looking for it. Ron would be trying to **Enumerate** the network. Then all the IP addresses would be added to a *Target List*, where he would do a -sS scan and others. We can do this on our home network. Figure out the netmask and your IP address. 

Open ports are concerning. If we find open ports on the machine with no explanation on why they are open. They may be associated with a game for example , but if it is not documented, we would close the port (the Firewall Course is in January). It is possible that someone in the past installed a software on the machine, and the port was left open. It is exactly the same as walking out of the building and leaving the door open. If someone is in the network, scan the network, find open ports, and then they would find vulnerabilities for it. The example we have is port 3306.


We can disable the PING scan on our machines. 



> [!danger] 
> Do NOT scan any machines outside of this lab. Later, we will have an assignment where we would scan all the machines by putting all the IP addresses in a Text File, where we call it a **Target List**. We never want to do a scan where we would type an IP address in the command line. Instead, we would use the **Target List**.  



If a Chinese attacker, they would do a Remote Desktop protocol, a Database Protocol, and they would do a low-frequency scan, with a low port scan. They would go after the valuable targets. They would have vulnerabilities involving these special ports. 


> [!note] 
> **Reconnaissance**: 
> 
>		Do a TCP Port Scan of 1-65535  
>		Do a UDP Port Scan of  1-65535  


Ron mentioned his conversation with network administrators where they mentioned that the attackers would not have the IP address range. The aim is to detect all the open ports, detect vulnerabilities, and deal with them. Today's tidbit of news about the CISCO vulnerabilities, so it would help to remember that. 

When we did encryption, Ron mentioned that the password itself is not stored on the computer, but the Hash is. If they would like to move laterally throughout the network, the password will not do that. They would like to have a Network Administrator's password. 

Terrorists would set off a little bomb in the street, where a number of people would get killed. They would observe the first responders, and then set off a bigger bomb. The attacker might get the network administrator to show up by messing with something on the machine, such as deleting the printers from the network, where one would normally call for IT support. The network administrator would then log in to the user's machine. If the password is the same everywhere for the network administrator, the Hash is stored on the machine. The attacker captures the password hash, and then the attacker could move laterally through the network, which is known as **Pass-the-Hash**. A network administrator would not log in with the administrator. If you are a regular user, and they can not get anywhere with the user's machine, they want to trigger mild alarm bells. 

In reference to today's OS Security class involving the /etc/shadow file, the file would have the hash. 

## Homework : 


Produce a list of 172.16 IP addresses in this room. Look in the NMAP Options List for a command that specifies a Target List


> [!todo] 
> Visit the NMAP Reference Guide in the 3rd section
> Produce a **Target List** of all the IP addresses for the computers in the lab
> Look up a 255.255.252.0/22 network, and how to figure out the equivalent network.  
> Read up on **Host Discovery**, where we would get a list of IPs that exist in the network (Target List)
> Do a *TCP Port Scan* of 1-65535
> Do a *UDP Port Scan* of 1-65535 
> Try some creative scans, where the -V , -O and other options would be most useful. 
> The attacker may try to hide their location, backup the malware, and "Setting Up Camp". They would know all the active devices, open ports, exploits, and vulnerabilities. 
> They would move laterally throughout the network. This is known as **Lateral Movement**. 
> 



> [!caution] 
> The attacker would do the mentioned steps above, but if they do, it is very noisy. 
> They would do a Gentle PING Scan, where the different segments of the network are scanned periodically. They would adjust the **Frequency of the Scans**, where BASH scripting would be useful. The aim is to NOT appear in any *Intrusion Prevention System/Intrusion Detection System*, where the network administrator could miss the infrequent PING scan. 
> 



