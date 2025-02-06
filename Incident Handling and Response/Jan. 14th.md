



>[!warning]
>
>Before **Friday Jan. 17th, 2025**, when the **IC2 Representative** will give a presentation, please visit the link :
>
>>https://www.isc2.org/


>[!todo]
>
>Look at **DFIR Certifications**. We are likely to use the knowledge for Incident Response situations for a private organization.  
>
>>https://www.sans.org/digital-forensics-incident-response/




## Three Stages of Incident Response

#### Preparation

#### Detection


#### Response

Active incidents and post-mortem stages.


----------


>[!important]
>>**Rule 0** . Make sure the army you have is prepared to go to war. Choose the right people for the right job. 
>
>>**Rule 1** . As part of our preparation, it is about building our team. You go to war with the army that you have. When something happens, you rely on those around you to respond. 


After choosing the individuals, focus on training them. The whole team would be cross-trained so they can fill in at times of emergencies. If we have ever been in an emergency situation, the technology/application domains are not the center of the problem. In case of a server loss, we know what to do to respond. We would have a backup server ready to go. 
Ron mentioned that he was dealing with a security incident that affected the organization, and they had to bring everything back up as soon as possible. It took four days! The major problem was that everyone was angry. It would help to be trained in conflict resolution, such as de-escalation techniques. In every emergency situation, it is all about *executing the plan*! If you were on a plane, and you face an emergency, it would help you to know where the life vest, and where the exit doors are. It is a minimal amount of planning, but at least you would know what to do. Obviously, when people are screaming, it is a lot harder to focus. 



Make sure the team is equipped and funded with DFIR tools and knowledge. If you face an obstacle, it would help to know the impact on the organization if the server would be down for the next 24 hours. 



Roles should be clearly defined! Someone with authority in the organization does not mean they have authority in the case of emergencies. 


You have to have effective communication for your team. Imagine the situation if the entire communication infrastructure is compromised or down. New Brunswick had their public sector infrastructure spread out in three cities. You would also need to be able to communicate with the public, and other entities as well. 

During the planning stage, please make sure you have a legal team ready to go. 

The vendors who supply software and tools are a liability. What would you do if you have an expensive piece of software that has a downside of having to fail over to a secondary site, what would you do for the secondary license for the second software when you have to use it only in case of emergency? An example would be the necessity of having a duplicate cloud ready to go. Ron mentioned that you would have to face that you need to spend a large amount of funds to use. Ron knows of organizations that started up with using free and open source solutions for their infrastructure, as it has the bonus of having no financial costs except for support. 


The Service Level Agreements that would be signed should include realistic terms and conditions, as you would know not to agree to face a huge financial penalty or backing themselves into a corner. 


You have to talk to the general public. How would you do so ? " We have faced a security incident. We have the best individuals to counter this incident, and they have been extensively trained". You do not have to mention specifics, but you have to talk to them. 


Ron mentioned an example of Georgia State's DFIR team that is fully prepared and equipped with jump drives, log analysis tools, alternate communication, remote/memory dump tools, and disk imaging tools. Memory Dump Tools and Disk Imaging Tools should be used with **Chain of Evidence**. The tool would not perform any writebacks at all to maintain the integrity of the evidence. Remember the affiliate program, where an intern who gets tempted by a large sum of money could infect your organization. 


-----------------------



## Preparation



Step 2. Figure out the **minimum required continuity**. We do not need *everything* back. We just want to maintain continuity for our clients. Consider hospitals, and the absolute minimum requirements to get back up and running as fast as possible. You are not duplicating everything in the enterprise's servers. What would we need to maintain our responsibilities to our clients? 


#### Data Classification


We think of it when it comes to the security of the data systems. Data records are for the eyes of those who have the privileges. Ron mentioned that to ask which portion of the data is critical to maintain in case of system failure? 


1. No need for historical records 

>[!Important]  
>
>Please be mindful of the following factors :
>>1. Transactional Information : this allows proper restoration. You can take all the recorded transactions, and you take them to the database to make an incremental backup/restore. 
>>2. Customer Information
>>3. Account Information 


We are not talking about classifying data in terms of security access, rather it is classifying data to maintain emergency availability. 

Ordinary individuals may think "I would want it all back!". Imagine a fire : would you carry a refrigerator out? You are most likely to grab whatever is most important for you. 

It is a great idea to have a cloud-based server. Keep in mind natural disasters. 


Be mindful to be adequately prepared when it comes to choices pertaining to the operational personnel. It should be absolutely-essential personnel only, due to a malicious insider collecting intelligence to feed back to the malicious entity behind the scenes, as well as the psychological effects of mass panic!


Hypothetically, we have the right team, funding, and the team is continuously preparing on a regular basis. 


#### Network 


What do we have to do with the network and network attached devices? 


1. Establish **Baseline Behavioral Profiles** for all the machines, people, data and this gives the **enhanced ability to detect attacks**.
2. Establish **Micro-Segmentation**. Between the segments, think of the **Chokepoints** (people cannot get through, including the attackers), **Firewalls**(to govern access), **Jumpbox** ( a system with a lot of network cards enabling instant access to multiple microsegments), Intrusion Detection/Prevention systems, Logs Everywhere ( using custom-made programs. Consider monitoring all Windows logs from all machines pertaining to a trigger of a privilege escalation, this event would likely be an action to be taken by the *Intrusion Prevention System*, as it would disable the account and the Domain Controller. It will no longer be able to communicate at all, and consider the frequency of the checks).
3. Place automated monitoring scripts. 
4. The **Principle of Least Privilege** : In every  bit you hear in ransomware attacks, "someone clicking a link" is mentioned. If a system has access to data, the access would be done in a microsegment between the machine and the server ONLY, sans outside-world communications. In the classification system, you can have non-critical data in another segment, and it could have access to email.
5. Dark Telescopes
6. User Training : It does not always work, but it has to be done. 
7. Lunch'n'Learn : if this is done every month, and in one of those, it would mention "From last month, the following individual hacked the organization. He/She is from this and this". If we do this, we make the threat real to them. Open their eyes!
8. **Malware Beaconing** : malware *always* signals home.
   

## Indicators of Compromise 

It is based on :

 
1. Timing : you can transfer all the timing from all your network infrastructure in **POSIX Time**, which is Jan. 1st 1970. 
2. Unusual endpoint agents : you would detect it with **Endpoint Protection**.
3. Log URLS : this could indicate the usage of a **Web Proxy**.
4. Large number of connections : You can detect it with **Netflow**
5. Malicious Domains : Consider the best source you can find for malicious domains, and check if you can pipe it through your development projects! (Due next class). Detected with **Intrusion Prevention Systems** and **Firewalls**!
6. Windows/SYSLOG events : It can be detected on the **Operating System**'s logs !
7. Signatures : Detected through the **Intrusion Detection/Prevention System**. 

		   
>[!important]
>
>You would get an integer, and if you have another integer (another incident's timing) could be subtracted from the first. Change the time to POSIX time, and you will avoid headaches! 



#### Ron's Network 


1. You need an **Intrusion Prevention System**.
2. You need the **First Firewall**!
3. You need **Log Collection Points** for *Netflow, Firewall, DNS and Intrusion Prevention System logs**
4. You need a **Proxy**, and examine the *proxy log*. 
5. You need a **De-Militarized Zone**! 
6. The *De-Militarized Zone* needs its on **Intrusion Detection System**!
7. Then, you need a second **Intrusion Prevention System**
8. Then, you need a **Firewall** from a **different manufacturer** as the other firewall!
9. You need an **Intrusion Detection System** on every segment!
10. On every machine, we have an **Host-based Intrusion Detection System**, **Intrusion Prevention System**, and **Firewall**. 




Dark Telescope : You need to have a few ip addresses designated within a microsegment, where if an attacker attempts to contact them, or worms, or scanners, noone else in the organization would have any reason to contact them, and then they act as a Indicator of Compromise. 



Honey pots : 

It would have a server with fake data. It would be used to detect and study malicious actors. Ron has built a Honeypot system for Dalhousie University, and they were not legally allowed to have it connected to their infrastructure. Ron set up a range of Honeypots. It is very dangerous, because you are putting up honey for bees. If you have an Intrusion Detection System within the microsegment, then you can see it, but no one else. 



   
   
   Remember : Ron can suggest a workaround for every factor in this plan!


Even if we are not going to manage an Incident Response Center, the IC2 certification gives you enough knowledge to know what to do on the fly. 




#### Deceiving your Attackers


One of the things we should look at is **Honey Tokens** :


There is a problem with administrators logging in to a local Windows machine, as the *credentials will be saved*. If Ron was an attacker, and he wanted to find the identity of someone with Administrator privileges, Ron would leave credentials intentionally for an attacker to get attracted to the token, and then they would crack the hash or pass the hash, and use it. The attacker using the token would be akin to a *tripwire*. The account would not exist, or it could, but it would be created intentionally as a means of detection It would raise alarm bells.


Honey Tokens are any piece of data that you place on your system intentionally in order to detect attackers. 



##### Deceptive API/Documentation 


You can leave fake or deceptive API Documentation where you would leave the **Honey Token** in the documentation, so the attacker would get tempted and grab it. There are PowerShell scripts online that would fill your system full of Honey Tokens. There has been instances of an employee leaving the company, and the general consensus is to leave the former employee's account active as it would have four years of history. 


If we have a publically-facing API, it is possible that you can create a phony application and leave Honey Tokens as default passwords. 



All this was a part of our preparation phase. 



>[!important]
>
>The Legislation assignment is due at the **end of the month**!


Ron has placed links on the course shell, and at the end of one of those links, there is a clue left there to help us answer one of the assignment's questions. 


>[!important]
>
>When we get to the **Detection phase**, it would rest on **Security Onion**, which is the *blueteam equivalent of **Metasploit***. One of the things we will do is to do a micro-lecture covering one aspect of the **Security Onion** and it should be detailed enough for other individuals in our class to follow along and set it up successfully! It is a concrete way to show we have understood the material.



