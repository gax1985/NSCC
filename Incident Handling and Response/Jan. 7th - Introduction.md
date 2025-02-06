


Insider malicious actors are increasing in numbers. It is very tempting for insiders to install a malicious tool on an organization's system, and then collect a huge portion of the ransomware attack's proceeds. There are many incidents that are a direct result of that. Ron was investigating an organization, and when the entity that hired them announced that Ron is on the case, this employee fled the country immediately. Prior to that, every single incident of ransomware in Ron's career was a result of an employee clicking on an email. 


Ron's approach to protect against ransomware is to lock the door, aka protect the endpoints that the malicious actor would install the malicious tool on. 

Ron wishes that he has recorded the source 2018, which took place in SECOM 2018. A British researcher gave a talk about a study she did where the employees would be told not to click on the link in phishing email, and employees that have not been trained. Her results said that it showed no statistical difference between the employees that were trained vs the employees that were not trained. We have to make sure everyone is protected by drastically decreasing their access. Everyone is usually fine with the limitations in protection except the leadership team (CEO) due to them discovering that they can not get a file, and then get angry. It is about good practices. If someone said "Give complete access to the team", run away as fast as possible due to it heading into disaster. Here is a TODO list :

1. reinforce that we are all part of a team
2. Establish a **Sense of Ownership** :
   
   >Take all the workers working with a system, establishing regular guidance sessions, collect statistics and work with them continuously. Establishing a sense of ownership by every member of the team reaffirms the positive reinforcement that would lead to a more secure organization. 

>[!note]
>NSCC works with an organization specializing in Phishing Prevention. They provide multiple choice tests involving Phishing in general, but it does not fulfill this requirement. Time should be spent in establishing positive changes in an organization. 

3. Actively *Listen* :

>[!hint]
>
>Ask them questions ! Tell them about something happening in the Cybersecurity industry. Individuals may react in the required way if they knew an example of a malicious actor instead of an Archetype of a Malicious Cyberactor.


4. Make it *clear* to them! 
   
   
>[!note]
>
>Ron experienced a situation where the employee was not taking this information seriously. This person was most likely to damage the organization due to carelessness.


5. Creating an IT environment that is **very difficult to navigate** *by someone who is not supposed to be there*

>[!note]
>
>Anyone from the outside would have great difficulties in navigating a complex layout of systems without being detected. The concept of **Least Privilege** means that the individual would have just enough privileges to complete their work. It makes it interesting as *Privilege Escalation* can be seen easily through scripting and automation. Study the behavior of an attacker through the logs. 

>[!danger]
>
>Intrusion Prevention Systems are prone to *false positives*. Organizations tend to choose an Intrusion Detection/Prevention Systems to fulfill a requirement such as **PCI-DSS**

6. Start looking at the **Software on the systems!**

>[!note]
>
>If 95% of the attacks are coming through emails, why would employees have access to emails? there was a Dalhousie University professor who would choose the most gifted C/C# programmers, and he would form a group called **Lazer Group**, and would all have privileges such as a special lab just for the Lazer Group. Ron spent a semester in the lab through Social Engineering! If you get elevated to a special level in the organizations (such as email), you can prevent individuals who would be a higher risk due to a questionnaire as a part of a threat risk assessment, and  offer them conditional access on the condition of providing access to emails *only* after completing a counter-phishing training course for example. 

>


>[!warning]
>
>The latter does not work against *really small organizations*!



## Cyber Resiliency


Designed to enable mission objectives. It is the ability to anticipate, withstand, recover from and adapt to adverse conditions , stresses , attacks, or compromises on systems that use or are enabled by cuber resources. 


1. anticipate : 
>[!example]
>
>Ron gets flooded at home in the basement. He had to get generators to provide a solution for power outages. He would test everything to make sure all is functional. He *anticipated*, prepared, and made sure he is able to withstand all conditions. 


Not everything in the organization has to be recoverable. You should decide for example the core requirements that need to be functional and available at all times. We focus first on the *core requirements*, dangers to them, what to do to overcome the loss of these systems ( such as backups for your data. One is none : two is one). Backups have to be accessible to an attacker. The actions to take vary due to multitudes of risk. Aliance Systems in Manitoba have to be 99.999% working all the time. 


If the building burns, and you have a remote backup, you would not nothing to restore the data to. It does not have to support 100 users, but has to be able to support the public facing infrastructure. Cloud based backups transfer the risk to the cloud provider. It does not have to replicate the entire system, but just the core components. 

>[!note]
>
>Research **Haboob** and **Worker Bees**




# Three Phases of Incident Response


Ron has experienced a hard-drive failure at home. The hard-drive was ticking. How do you avoid the complete panic? 
1. Develop a plan 
2. Work the plan 
   
If you are focused on what to do next, you do not have any panic attacks. 

## Prepare

We have to prepare for the eventuality of an attack. It is akin to getting supplies ahead of a storm and possible power cutoffs. It is all about the team, the resources, the environment, and a plan for the next six months

#### Detection

It is akin to setting up water level alarms. It is all about putting in IPSes , monitoring logs ....

A significant portion of programming would have to come from analyzing logs. Early detection is the key! We will go through hell, and we will have an experience. We will have to response to that circumstance. Then, we have an opportunity to learn from it. 

## Prevention ( This wont work )

You take the lessons learned, and we go through the loop ( it is a continuous loop )

## Detection - Our Focus

What went wrong ? In Alien 2 , walls were put up and the aliens got in from the roof!

## Respond - Clean up the Mess!


#### Ask the Following Questions Afterwards ...


1. What went wrong ?
2. What worked ?
3. How do we cut down on this happening again ? 




## Active Cyber Defence Cycle

Asset Identification and Network Security Monitoring

Incident Response 

Threat and Environment Manipulation

Threat Intelligence Consumption


### NIST Incident Handling Guide


1. Preparation
2. Detection and Analysis
3. Containment Eradication and Activity
4. Post Attack Activities



## NIST Security Incident Handling Guide


In the center of the diagram we have the **Incident Response Team**, and it can be internal and external teams : 

1. Software and Support Vendors
2. Consumers, Constituents and Media
3. Other Incident Response Teams
4. Internet Service Providers
5. Incident Reporters 
6. Law Enforcement Agencies 

	Every point should have logs, monitoring all the activity of the components and users, and analyzing the logs on a continuous basis. 



## Incident Response Team : Establishing Roles Responsibilities and Authority


#### Roles 




#### Responsibilities 



### Authority 



We will have an assignment of researching the consequences of a cyber-attack. Think of any model you like. There used to be a **Tiger Team** , which is the top 5 consulting groups, who would have a team of incident responders, who would go to deal with the most serious cyber incidents. Consider the example of a SWAT Team. They would have a double role, where they would do the SWAT part of their life. The Incident Response team is a virtual team. They tend not to do this on a daily basis. They form in response to an incident. Each member would be equiped differently, would have different roles, and would be trained on these roles and this situation. Your role could be to prepare Incident Response. 


First Focus :

1. Build a team !
   
   
   >[!note]
   >
   >We have been a team now for almost two years. Everyone has their own strengths and weaknesses. You would select people from your own IT team, where you would consider the best programmer, user support, etc. You would identiy who is best equiped to do particular roles. You would have to have a Network Engineer who is familiar with routers, switches, IOS CISCO commands etc. You would have an OS person. 
   
2. Receive Extra Training for their role during an Incident :

>[!note]
>
>They would be trained in a higher level understanding of their particular role. One of the worst things that could happen in a crisis is when someone has an emotional breakdown. They are not properly trained in dealing with a crisis. They would experience an uncontrollable physical reaction. It is not emotional but a full-body physical reaction. You have to pick a *temperment*. You need someone who is calm and  stable in a crisis. You need to train them on that eventuality, and if they do not complete the training , they would not be included. You also have to understand that everyone has opinions, anger all around, etc. The best remedy is conflict resolution. You have to know how to talk to them but understand them. You would do deescalation techniques. The team is small. It could be a dozen individuals. 


3. Convince the Managers (individuals in authority) that the Incident Response Team needs the required training.

>[!danger]
>
>Run away if they refuse!


4. Understand that the corporation's systems and infrastructure may not be available!

>[!note]
>
>You need to have a complete Duplication of Infrastructure that gets triggered automatically during a crisis ( think Warm --> Cold). In Georgia, they started a Georgian Cyber Incident Response Team. They would have vans that contain all their gear, and they would arrive at the site. The individuals are highly trained, and most often IT individuals. In the US , IT individuals who would be members of the team would have another job they do, but would be prepared for an incident for the National Guard Cyber Incident Response Team. Ron mentioned that they are an army!



Assignment :


1. As part of our preparation, you would know all the members of the team, their phone numbers and their addresses.
2. The Boss has to agree on the plan! The plan would have a budget , a time-frame, milestone to accomplish, and then get it signed by the highest level of authority possible! Individuals who are not part of the team should be politely asked not to interfere with the operations of team members when an incident happens. Executives and other members of the organization will attempt to exercise their authority, or offer advice. Part of the policy has to be : Everyone will do their roles and *only* their roles during an incident. 
3. IT Team members face *contractual and legal requirements*. 

Service Level Agreements : 

These would be contracts and commitments to perform a certain action as a consequence of the action of the individuals. There are criminal jailtime for this, as well as financial reprecussions. The contracts will name the roles that will be fined and jailed. Insurance companies may have an authority during an incident that will dictate your responses. 


4. Legal consequences :

A cyber incident will cause someone to sue the organization that faces a cyber incident. The Legal team has to participate in the policy planning when completing the Incident Response Plan. Our role is also to let the clients know of other consequences that were not considered before. 



On Call Assignments : 

On-Call assignments often dictate certain actions performed by the individual who is on call. They have to be prepared and ready to go 24 hours a day, 7 days a week. The On-call requirements are a part of the plan. 

Cross Training : 

Everyone in the team will have to be **cross-trained** on the other individual's roles. Everyone should be able to take over another individual's role at any time. 

Inter-Team Communications : 

The team should have an offsite infrastructure to provide the means for them to do their work. During the SARS period, individuals would refuse to go to work. Organizations had to go to malls in Toronto and set up offices there for those who are comfortable to work there. 


Rights and Privileges : 


They could have a regular user identity ,. and another user identity used exclusively in the incident response role , which would have unfeathered access. 


Imagine the Incident Response Team in a command center, and the doors automatically lock to prevent unauthorized individuals from going in and leaving. There would be a role of a Communicator, who is the only person authorized to talk to the team, and is outside the room. Everything is on an absolute **Need to Know** basis. A CEO may ask about the incident, and the team would refuse to talk to the CEO or the press. Sobeys' employees got in trouble due to a cyber incident affecting the pharmacy. Some workers informed the press of everything, while others refused to mention it due to the security requirement. No one should talk to the press. 


Legal Requirement : 

You may not be allowed under legistlation to speak about the incident due to privacy laws, and may get sued. You would say nothing, talk to one, and have one communicator to speak to the outside world. In Frank magazine, Ron was in a meeting with three other individuals. The next day, Frank magazine contacted him to ask about details from the meeting. Thus, there was a leak. 



Treat it like a Penetration Testing Environment : 


All data must be **isolated , stored and encrypted**. You do not want to violate any laws, and you have to remember that the integrity of the data is essential for maintaining evidence used in criminal proceedings. They could be logs , image captures, etc.  You have to consider **Chain of Custody Maintenance**. Is the information hashed? do we maintain the hashes? do we image the collected information, and place it in a locker with logged access? The evident is thrown out if it is not maintained. You can not protect a mess. For example, you would have a multitude of identical tools due to them being lost. You have to have everything documented, understood and monitored and prepared. The system has to be absolutely organized, and maintain it always. You have to establish a **Behavior Profile**



Maintain  a Patch Log, System Images, and Installed Applications : 


Track everything involving patches, updates, addons, libraries, software requirements etc. If there is any change on the IT environment , it does not happen quickly. It would take days to perform the simple task. A Change Request would include information on the task to be performed, the effects of the change and who it would affect. You would have to check if this change will affect any other portion of the organization's data assets. It could take a year to distribute a new version of the software that could change everything for the security stature of the organization.


Identify the Assets and the Actions to be Taken : 

If you keep an accurate inventory of the assets at hand, you would know exactly where everything is. You would recognize what is important to you, and what you could live without. 


In a Sports Context , it is not about being the next Sydney Crosby, or the next Ultra-Human Being, it is about performing the basics flawlessly. If you could pass, shoot, skate, run, and catch exactly how you are supposed to do it, and you do so correctly, each move is done slowly until you can do it flawlessly, over and over again. It would be as granular as learning how to breathe correctly. There is no competition. We have to be the Average Worker who would do all the basics flawlessly. These are not extraordinary actions, yet they are simple things that we have to do correctly. 



Establish a Difficult Micro Segmented Network with : 

1. Difficult to navigate
2. Micro-Segmentation
3. Traffic Monitoring
4. Application-Aware Firewalls
5. Intrusion Detection and Prevention Systems at Chokepoints 
6. Establish a Least Privilege Access Control Policy. 



>[!todo]
>
>Check out the **First Assignment**, which is about Legal Responsibilities in the Event of a Data Breach!