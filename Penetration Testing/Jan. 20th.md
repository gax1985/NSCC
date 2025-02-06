
# Objectives


1. Comprehend the functioning of scanners
2. Trace the development of scanners
3. Identify various types of scanning
4. Identify different scanners


We might be asked to do penetration testing on the Systems Administration's Students' Systems. Brian will give us a lecture involving a scenario he has built, which is a **Buffer Overflow Attack**. He will walk us through it. Stop him and ask him for questions. 



#### Scanners' Roles :

1. Find and fix vulnerabilities in remote machines on a network
2. Software tool that examines and reports about vulnerabilities on local and remote hosts

It is good to automate scans and automate results. Setting up scheduled scans help in making available a lot of information to assess security with. 


#### Scanners Categories:

- Active
    example :  Port scanner - Examines and reports the condition of a port
- Passive
    example :  Network Monitor – Captures packets travelling through the network



In the 1960s , in 1969 specifcally, there were **four nodes**

Scanners appeared before the ARPANET. Legitimate users would dial in with modems to Unix servers. They would write shell scripts to check their networks. 

In the end of 1970, ARPANET has grown to 13 nodes.

- Scanners first appeared even before ARPANET to monitor connections between mainframes and dumb terminals
- The early UNIX-like languages had no security at all
- Legitimate network users would connect to remote UNIX servers
    - Their modem would dial specific telephone numbers
    - Led to the invention of a new tool, the **war dialer**


- War Dialer
    - Script that tells the modem to dial a range of phone numbers defined by the user and then identifies those numbers that connect to remote computers
    - An early form of an automated scanner
- In the early 1980s, the majority of servers ran on UNIX platforms
    - System administrators created shell scripts that let them check on their networks



- Evolution of Scanners (continued)

- 8

- As the Internet increased in availability and popularity, more computers and networks became connected
- Today, scanners are available for several popular platforms

- Scanners automate the process of examining network weaknesses
- Functions
    - Connects to a target host(s)
    - Examines the target host for the services running on it
    - Examines each service for any known vulnerability


Ping scanning

- Demonstrates whether a remote host is active by sending ICMP echo request packets to that host
- Some hosts will actively ignore ping requests

Are you alive or not ?


- TCP Connect Scanning
    - Attempts to make TCP connections with all of the ports on a remote system
    - Target host transmits connection-succeeded messages for active ports
- Half-Open or Stealth Scan (-sS)
    - The default and most popular scan option for good reasons. It can be performed quickly, scanning thousands of ports per second on a fast network not hampered by restrictive firewalls.
      
      - Only the SYN message is sent from the scanner
	- Reply signal may be a SYN/ACK, indicating the port is open
    - Attacker replies with an RST flag to avoid detection
	- Some IDS/IPS can be configured to log all network activities
    - A TCP connection scan does not complete the connection, uses a SYN packet to check on port status

UDP Scanning (-Su)

- Examines the status of UDP ports on a target system
- Scanner sends a 0-byte UDP packet to all the ports on a target host
    - If port is closed, the target host replies with an ICMP unreachable message
- Most operating systems generate UDP messages very slowly
    - Because UDP scanning is generally slower and more difficult than TCP, some security auditors ignore these ports. This is a mistake, as exploitable UDP services are quite common and attackers certainly don't ignore the whole protocol.


IP Protocol Scanning (-sO)

- Examines a target host for supported IP protocols (TCP, ICMP, IGMP, etc.)
- Scanner transmits IP packets to each protocol on the target host
- If target host replies with an ICMP unreachable message to the scanner then the target host does not use that protocol


- Nmap (Zenmap)

- 1

- Unicornscan: An open-source tool designed to identify information related to TCP flags and banners.
- Tends to be faster than nmap, especially in regard to UDP

-- tcpdump: An open-source command-line packet analyzer. It can read packets from a network interface card or from a previously created saved packet file. tcpdump can write packets to standard output or a file.
- WinDump is the Windows equivalent
- The tcpdump command returns the following counts after capturing all the packets:


- Wireshark: Similar to tcpdump but contains a GUI interface allowing for organizing packets to be displayed in a more comprehensive method. Also capable of opening a wide variety of packet captures from other applications.
- Both tcpdump and Wireshark are capable of operating in promiscuous mode, this means it can intercept and read, in its entirety, each network packet that arrives. Not just those packets destined for that interface.

- Vulnerability Identification
- Nessus: A platform developed by Tenable that scans for security vulnerabilities in devices, applications, operating systems, cloud services and other network resources.
- NeXpose: A commercial enterprise vulnerability testing tool.
- OpenVAS: Open-source version of Nessus.
- GreenBone ( part of OpenVAS)
- - Vulnerability Identification
- - QualysGuard (SaaS): vulnerability management tool that offers network discovery and 
mapping, asset prioritization, vulnerability assessment reporting and remediation tracking 
according to business risk.
- - SAINT: Security Administrator’s Integrated Network Tool: Initially developed as a free UNIX tool. Later SAINT became part of a commercial suite of tools for vulnerability detection, exploitation, and more.

  
  **Security Administrator Tool for Analyzing Networks** (**SATAN**) was a free software vulnerability scanner for analyzing networked computers. SATAN captured the attention of a broad technical audience, appearing in _[PC Magazine](https://en.wikipedia.org/wiki/PC_Magazine "PC Magazine")_[[1]](https://en.wikipedia.org/wiki/Security_Administrator_Tool_for_Analyzing_Networks#cite_note-pcmag-96-1) and drawing threats from the [United States Department of Justice](https://en.wikipedia.org/wiki/United_States_Department_of_Justice "United States Department of Justice").[[1]](https://en.wikipedia.org/wiki/Security_Administrator_Tool_for_Analyzing_Networks#cite_note-pcmag-96-1) It featured a web interface, complete with forms to enter targets, tables to display results, and context-sensitive tutorials that appeared when a vulnerability had been found.

- Exploitation
- - CORE Impact: full-service commercial vulnerability testing and penetration tool.
- - MetaSploit: network vulnerability tool that, like CORE Impact, offers a wide range of functions.

Check our **Bettercap** : the Swiss Army knife for [WiFi](https://www.bettercap.org/modules/wifi/), [Bluetooth Low Energy](https://www.bettercap.org/modules/ble/), wireless [HID hijacking](https://www.bettercap.org/modules/hid/), [CAN-bus](https://www.bettercap.org/modules/canbus/) and [IPv4 and IPv6](https://www.bettercap.org/modules/ethernet) networks reconnaissance and MITM attacks.

Read the [project introduction](https://www.bettercap.org/intro/) to get an idea of what bettercap can do for you, [install](https://www.bettercap.org/installation/) it, [RTFM](https://www.bettercap.org/usage/) and start **hacking all the things!!!**

[](https://discord.gg/btZpkp45gQ "Join our community!")


Kali Linux, formerly BackTrack, is maintained and funded by Offensive Security. It contains approximately 600 penetration-testing programs (tools).

- As students and hobbyists started playing with scanning applications, new vulnerabilities were discovered
- Scanners automate the process of examining network weaknesses, and check only for known vulnerabilities and open ports
- Scanning permits hackers to learn the vulnerabilities of the target system
- In the early days of computing, security vulnerabilities, while abundant, were not well known