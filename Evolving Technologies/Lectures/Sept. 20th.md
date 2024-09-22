


  

of 109

                     Automatic Zoom                     Actual Size                     Page Fit                     Page Width                                          50%                     75%                     100%                     125%                     150%                     200%                     300%                     400%                   

Module 2  
Exploitation

Initial  
Access Execution  
Persistence  
Phase 2: Exploitation  
Defense  
Evasion

Execution

What is it?  
When an adversary is trying to execute code in your environment. This is  
usually connected to another tactic like privilege escalation or collection. We  
will look at it from a basic frame at this point  
● Remote Code Execution (RCE)  
● Portable Executables (PE)  
● In Memory Execution  
● Hiding Malware  
● LolBins  
● Browser Exploitation  
● Mobile Device Malware

Remote Code Execution  
The big bad ugly vulnerability. An attacker can exploit a flaw in a piece of  
technology and execute commands on the server/workstation running the code  
● Command Injection  
● Buffer Overflow  
● Can use to download more malware or launch further attacks  
● Usually fileless (vulnerable tech just runs commands)  
● Can be hard to detect  
○ The tech is expected on the machine, but running unexpected code

CVE-2021-34473 (ProxyShell)  
RCE discovered for Windows Exchange servers allowed attackers to upload  
arbitrary files (crypto miners). This file was put in the netlogon share, which is  
shared with all PCs on the domain.

RCEs  
RCEs can pop up time for time, and its dangerous when the technology is  
running with elevated privileges. You should run several layers of security and  
apply updates ASAP to prevent.

Portable Executables  
Executable files that just click and run  
● EXE  
● DLL  
● ELF (Linux)  
● MSI

Portable Executables  
● Can download other attacks  
● Reverse Shells  
● Ransomware  
● Steal info (keylogger, file exfiltration)  
● Crypto Miner  
● Adware

Portable Executables  
It doesn’t matter how environments change (Cloud, local or whatever the future  
holds) portable executables are likely to be around for a long time.  
The are  
● Easy and portable  
● Used for most programs out there  
● The backbone of Windows operations essentially