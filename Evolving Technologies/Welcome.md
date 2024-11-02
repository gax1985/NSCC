TTP : 


Tactics Techniques and Procedures



## Tactics :


Execution Reconnnaisance, Privilege escalations
Stays Similar!



## Technique : 

Kernel Exploit , Privilege Escalation

Stays similar! 


## Procedure : 

Specific things that change all the time 










## Indicactor of Compromise

It is a sign that the system has been compromised. such as : 

1. Traffic to IP addresses
2. File Hashes :
   
   Hashing is used for logs/keys, and often used to check encryption of databases
   
3. System Commands

Powershell is very powerful, and alot of attackers would use PowerShell.

You can takke the powershell command, BASE64-it, and then you can execute it as BASE64. If you see Base64, it is a bad sign. 


We will touch on **Forensics**,


BASE64 is a public key. The algorithm is used everywhere! It is encoding and **NOT** encryption. 



Very common on webservers to include special characters , such as "" // etc , you can BASE64 to encode it, and then BASE64 it back to original. It is used to send data. 



Example of indicator of compromise : 


Mazer Ransomware

Virus total is often used to check payloads,so if we have a payload that we like, NEVER upload it to virus total. 

Virus total tells you how many anti-viruses had detected the payload!



## Communities : 


People go away from traditional antivirus ( where it sandboxes the suspicious file, and it does it in a way that is not very apparent. It will check its behaviour.)

Some threat actors will upload it to Virustotal, and then spam communities that the file is fine. 


You can do your own static/dynamic analysis. Watch out for community ratings. 



## Types of Threat Actors :


## 1. Script kiddies :


They watch Youtube videos, take scripts that they find online and run it with little understanding of how they work. They would have very bad configurations. They are opportunistic, and alot of them will bruteforce it. They know how to use metasploit. They do it for the credit online. 


Example : 


According to Imperva (security firm) , 47.4% of all internet traffic is made by bots, with a 5.1% increase every year! Human traffic decreased to 52.6%. It is the lowest in 8 years! 
--> Dead Internet Theory


Something that empowered script kiddies is Ransomware-as-a-Service or Malware-as-a-Service, or selling gained foothold. Example : EMOTET !

Sometimes you find some 0-day attacks as well, and often sold by government agents



Alot of the script kiddies are running bots!

## 2. Inside Actors : 

Initial access is the hard part. Disgrunted employees can do a lot of damage. This is why we do not have ADMIN privileges. If they want, they can sell their credentials to threat actors. 

Example : Disney! Someone sold their credentials for something like $5000.  

Vulnerabilities are not all technical. MGM had someone call to do a password reset, and they had weak procedures, so a procedure can be a vulnerability. 


You can get a job as an IT worker, get all the access you need, and install Ransomware on their systems. Companies have now Ransomware insurance. 

Some individuals provide fake information to get the job.


Phishing and Social Engineering happens often, and is used frequently by inside threat actos. 


Business email compromise happens as well! 


Inside actors can be script kiddies. Trust Noone!

They would know the environment, the people, the security procedures. They will go after : 

1. Data : They would destroy the company's reputation with data leaks


## 3. Hacktivists


Anonymous is an example. Hacking for a Cause. They are often large groups. They would have a good network, and they would have memebers around the world. They would do Targeted Attacks. It takes a lot of time. They target essential services, such as a power company. 

Wikileaks



We will do : 

MFA Bypass
Vishing : Deepfaked Voices, it is using your voice to social engineer your way into the network. 
Long Email Compaigns
DDoSing is common!
Zero Day Attacks




## 4. Nationstate Actors

Every country has a cyberwarfare division. They find and make zero-days . They work with Microsoft (NSA) to spy on every system! There are a lot of nation states that target critical infrastructure. Sometimes they work with cybersecurity companies ( Russians and the Zebersky)


Example : 


If we have malware on a PC, it connects to a C&C system (command and control)
It scans the network and sees new ways of traversing the network . this example : SSH tunnel to OT Network 


explanation : IT vs OT : 

	IT is the technology backbone of any organization. It's necessary for monitoring, managing, and securing core functions such as email, finance, human resources (HR), and other applications in the data center and cloud.

	OT is for connecting, monitoring, managing, and securing an organization's industrial operations. Businesses engaged in activities such as manufacturing, mining, oil and gas, utilities, and transportation, among many others, rely heavily on OT. Robots, industrial control systems (ICS), Supervisory control and data acquisition (SCADA) systems, programmable logic controllers (PLCs), and computer numerical control (CNC) are examples of OT.




Example : Russia attacking Ukraine in 2016 : 


Dragos security condluced that the attack was not merely to do shortterm damage, but long term damage that could last weeks or months. 


If you are a firm that does accounting, they can pivot into your clients' networks. 



Codenames for Nation-State Actors. : 


TODO: Read this year's report ( located in the Brightspace's files)



2. Organized Crime





How the course is split : 


1. Discovery 
	   Reconnaisance : who are the people ? what they do online ? 
	   
	   
	   Example : Bryan had a client that mentioned that they had a whole entire fake email chain, and it was a targeted attach against a VP or someone in a leadership position to gain an invoice. 
	90% of the work is reconnaisance in a Red Teaming Scenario 

Resource Development : Test the payloads, figure out things and how they work 


2. Initial Access : Get through VPN? or how would you get in ? 
3. Execution : Installaing Malware, running malware,
4. Defense Evasion : How to avoid getting caught? What would you do to achieve this? Turn of Microsoft Defender. 
5. Persistance : What happens if the malware stops communicating to the C&C server? How do you maintain a portal ?
6. Privilege Escalation : Would you take advantage of a kernel Exploits? social engineer someone's IT credentials? use MIMIkatz ? 
7. Lateral Movement : WinRM and SMB can be used to traverse the network. Antivirus does not pick up on PowerShell commands to traverse the network. 
8. Collection : Collect as much data as possible
9. Command and Control 
10. Exfilteration : Get data out
11. Impact : cause as much damage as possible!



How do you keep informed? 


Crowdstrike gives a great yearly report. You can sign up on the website. You can put in whatever you want. DEFCON is happening now! Go to Confreneces

FALCON is another crowdstrike events


YouTube can be a good source

RedPacketSecurity divulges who got breached. 



Check out CHECKPOINT"S CYBER Threat Map



TryHackMe does a lot of new boxes based on new attacks


Set up GOOGLE ALERTS :


https://www.google.com/alerts 


Enter your Topic : Breach ? Zero-Day ? Exploit ? Cyberattack

Enter the Settings : Once per week

Create Alert




## Old Techniques : 


EternalBlue :


From 2016. Microsoft put a patch out, but we still see it in action today!

Sometimes the networks are not segmented very well

You should know the old techniques because they are still viable in some situations. 




Reconnaisance :


Active : 

Digging through the dumpster is active

chatting on linkedin is passive


CNAME records : vpn.nscc.ca 
a subdomain might yield an IP address
An IT portal
HR Portal 

You can look at the records and CNAME a few 

 "A "canonical name" (CNAME) record points from an alias domain to a "canonical" domain. A CNAME record is used in lieu of an [A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/), when a [domain](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/) or subdomain is an alias of another domain. All CNAME records must point to a domain, never to an [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/). Imagine a scavenger hunt where each clue points to another clue, and the final clue points to the treasure. A domain with a CNAME record is like a clue that can point you to another clue (another domain with a CNAME record) or to the treasure (a domain with an A record)."
 
We can look at the website itself! You can see the job postings, the directories, ...
The directory for the staff contant information is most useful for phishing 


Active because you are interacting with the target's website directly when searching their employee directories.



Google Dorking : 

"Index of " or "Browsable Directories"

"Ext:PDF"

There is a Google Dorking lab at TryHackMe



Passive : 

You do not interact with the organization
llooking at linkedin is passive
WHOIS is passive , because you are looking at the records of the domain 


![[Pasted image 20240904093753.png]]

In Canada, alot of this information is censored. But you might be able to gather a certain email

When registering a domain, a lot of stuff can be found. It is often one of the first things you can do

You can check if a website is protected by CloudFlare. Instead of going from user to website, you go user --> cloudflare --> website


ARECORD points to the IP address :

"The "A" stands for "address" and this is the most fundamental type of [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) record: it indicates the [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) of a given [domain](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/). For example, if you pull the DNS records of cloudflare.com, the A record currently returns an IP address of: 104.17.210.9."



There are some ways of bypassing CloudFlare



nmap will try to guess which version a software is running -sV
nmap has tons of scripts as well!




TODO :


Google Dorking

Rings of Power