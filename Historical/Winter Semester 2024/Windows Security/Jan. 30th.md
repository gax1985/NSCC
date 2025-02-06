


We will do things differently today, due to us being online. 



We will cover a bit in the slides, get us on track with an understanding, and Thursday we can work on the assignment in class. Tuesday next week, we will do some hands on demo stuff together. She extended the due date to the Tuesday after that. 


If we did the **LinkedIn Learning** , we would have an idea about it today



# System Utilities & Logs 



We will discuss the tools available to us in the Windows environment, understand the usefulness of these tools, and how we could use them. 


## Security and Maintenance Center



We are aware of the **Control Panel**, **Windows Settings**, instead of going to the cotrol panel, if you right click on the Start Menu, all the admin tools are available to you. If you left-clickl, there is an organized grouping called *Administrative Tools*. We will be navigating them next week. 



## Windows Administrative Tools

###### Definition : 

>it is a place that keeps all the tools we need to manage the machine together. 



We will bve looking at these tools as we go through


#### Microsoft Management Console 

It is not a requirement; it is an *optional* tool that the SYstems Administrator will be working wirth, have access to it, or will give us access to it. 


We can add **Tools and Resources** that we need, such as *Event Viewer*, *Event Logs* for any computer for the organization, *Performance Monitor*, *Local Users and Groups*, etc... 


If we added these tools, we had them before, so what is the benefit ? 
1. We can set security around this Console : We can go to **Options/Console Mode|Set it to "Console Mode - Administrator of this console - > Author | Usermode : Users can use the tools, but can not modify the tools" 
2. These consoles are *flexible*. It is not uncommon to host the tools with implementation of security policies involving these tools. You can remotely view other people's desktop environments securely. It is common that these tools would be available depending on the individual's role. 
   


## Services 


It is a location/environemnt that gets overlooked, mostly because epople know that services exist, but they do not understand with what the Services are doing


Service : Small applications (not necessarily full applications), they run in the background,. oftren run to support a task. Example : When you log in, what authenticates the login is **Kerberos Service**, which runs in the background to authenticate individuals. 

Some run *automatically*, some have a *delayed start*, or *wait upon a condition to happen* to run

A lot of vulnerabilities and viruses hide themsevles by registering/listgening as a service. If they run as a service as compared as a full appliucation, you may not notice anything odd. If it is a virus running as a service, people do not pay attention to running services. If we look in the *Task Manager*, and our PC is slow, we do not pay attention to what services are running. We will identify why we should pay more attention : 


Information pertaining **Services** : 

1. Log On Ask : The service has the ability to run as any user who has access to the machine. We spoke briefly about the **System User**, who is a user who belongs only to that computer. The system user can not log in to the computer, but the account is created by default. The system user has full access to the machine before anyone logs in. When running a startup script when the PC boots, we would need to do it as the System User. When thinking of someone trying to take advantage, it will be very common to do so as a System User. The User is *NOT Linked to a Password Requirement*. They would need an account high enough to run the service, and run the virus quietly in the background. 

How can we manage our **Services** better? 


Answer : Sometimes something has to run before anyone logs in. She rightclicked on the Start menu, She went to *Computer Management*, Clicked on *Services and Applications*, and clicked on *Services*. It gives the description of the service, what is running , startup types (some are manual triggered when something starts, others are automatic, some are just disabled due to nto using the app or application it is associated with). Some of them are *manual* , to be started by the user. 


If we sawihthc to the **Standard View**, we can see which account is used to log in (SYSTEM account). Because the compyter is a member of the Domain, some services log in as a DOMAIN account. The majority of them do not run as a specific user, some are run as a local service ( part of the pc itself) , or being called on by a particular network system 


If we double-clicked the service, We can see more information about the service, Dependencies that it needs, (She picked a running service) , LicenseManager (on her PC, it is manual) , it is logged on as a local service, which means that it is tied to the application which requires it


There are a lot of services. 


What can you do to manage this from a Security Standpoint? 
We can limit who creates services, set up an MMC , We should have a list of what servcies are running in an avergae period on our machine, what services are manually-triggered. There are some *PowerShell* command that grabs a list of services. 


Marie saw a lot of viruses running as Services. Marie may not now what a random service is, but if she does not, and she has a list that specifies this service, she would use this information to diagnose issues. 


We can run the list comparison against any other list you are running with the *Comparison* feature. 


You should be aware of the Services that are common with your machine


You have to discover what is normal for your environment


**Scheduled  Tasks** are something to keep an eye on. She usually set up a *Honeypot Project* with the Systems' Students. They are running a server, which they moniotor, and the idea was to open it to the security students, who try to hack it. They would want data to find, so they perform a lot of attacks against this machine. One of the attacks she does early on is she would create a *Task* in **Task Scheduler**. She looked at *Task Scheduler* and found tasks created by applications on the machine itself. These are set up by default. If you look under Microsoft , there many areas. We did not create any of these. They were created by the Windows environment when it was installed. She does not know what inside each of these tasks, as she does not examine services. Sometimes the viruses/worms link to a particular application. Some that use word, and alot of those actions are build in Task Manager. Doing something in an application can trigger a task. She saw a task set to be triggered by multiple triggers. Both of the ones she found were scheduled to write today. She would build tasks with specific trigger,s and she would bury them down in something the user is not expecting. She can create a simple task "Windows Defender Something", and if you are not keeping an eye on the tasks, you may not know that this trigger or task was running in the background. This is one spot that is hugely overlooked. 

We can run scripts that gets us a list of tasks that were run in the previous 10 hours, and compare the list with tasks that ran in the past 24 hours. Look for links running in activities in new tasks. We have to keep an eye to see what is *normal* and what is *abnormal*. 



## Security and Maintenance Center


One Stop Shop to detect issues. 


## Defender



One virus protection is not *enough* , one type is not *enough* , you should run more than one type of virus protection, and never leave the Firewall off!



## Event Logs 


Microsoft set up the logs to manage the system. We log everything, such as Remote Desktop Connections which makes its own logs. Individual applications will create their own application logs. It may not be presented in the Microsoft Event Logs (It is the key starting place when investigating issues)


**Subscription Node** : Assume you are looking at an environment that has more than one server in the environment. If we make it difficult to manage/keep an eye on these things ( like the logs), if we check the logs on 5-6 servers, it will take a long time.  If we had an intruder log in to a machine, or someone came in and created accounts, and they came in through the back door, we need to be aware of thnese events. One of teh options that we have whcih has more than one services is the ability to do a *Subscription* : if we have a specific purpose PC  that we wish to monitor, we can make a *Subscription*, which makes it possible that all the machines will forward their logs to the *Subscription*. Instead of checking multiple, we check only one place. 


It is very common to have multiple machines into one or more subscriptions, such as subscriptions for high-priority, another for internal machines, etc... When creating a subscription, we do not have to captyure all the evbenets in te logs., as we cana make it for the events we are interested in/. 



How do we identify the specific events? 


EVENET ID : Every event that is captured is alliged with some ID/ There are IDs tyhaty reflect new logins, failed logins, multiple logins, evenets that capture new accoutns being created, new services beingf started, everything has an event ID. There are thousands of them. Other important information is provided " what time was the failed login?" "who is the source of the event?" "which compyter? which user?" If it is not tied to a user, it can be a system user, it could contain any key word that describes this event. 



#### Event Viewer : 
The tool to look at the logs. We can have one subscription, and another for her other systems. It would show up in logs / events. When creating a subscription, we can base it on a specific ID. Windows has determined which event to capture based on IDs. Everything is done based on the ID, and then it is categorized whether it is just information it has captured, successful audits, some failed audits,. Under applications, we saw one error. There was no user involved it was against an Application, it was not categorized. If we want to know more about it, we have a section called "Details", which gives us a bit more details about the event. **The Event ID** : if we go to Microsoft and look up any **Event ID**, you can look up by a specific ID (there are thousands) , each ID would show you the service it is linked to. 


She had a service called 8198. It gave her specific information pertaining to that ID. It is always helpful to search for it via reliable sources. She can check the Windows logs to check, and a variety of places that can give her more information about this particular event. The ID Number is key!






### Application Logs



### System Logs




# Remote Management Tools 




More people are working remotely. Systems need to be accessed and managed remotely 



We spoke about **Remote Desktop**, but it goes beyond that. It is not uncommon to sit in the same physical area, same country as a machine you are managing. Aloto of management happens remotely. This happens a lot when companies expand. As we move more resources into the cloud, it does change our requirements to manage/secure the machines. When a company's domain sits in the cloud, someone has given them the physical resource to hosdt tyheir environment in the cloud, but we are responsible for managing the machines regardless of where they sit. It turns it more into an environment that is hybrid physical to remote. 




## What is Remote Management ?







## What is Remote Desktop? 






## RSAT Tools 







## PowerShell 



Went cros-s-platform. It has started as a Windows tool , but now it is cross-platform ( it runs in Linux too!). Back in the day, SSH was used heavily. Moving into PowerShell is much more secure. 


Remote management wise, there are a vairety of tools/methods that can enable us to do so. We will cover it next week on Tuesday



Some tools : 


RDP

PowerShell

RSAT


We already looked at *8Server Manager* , which is a place where you acna select tools and grab tools from the environment


Remote Server Administrative Tools : It is features that you can add to any Windows environment, all you have to do is turn the features on. It does not matter which version of Windows. They are baked in to every environment, and they essentially give you the same access you are used to on the server. The DNS manager you used before, group policy , all these tools are available as RSAT tools. You can access them directly on the machine you are on. You can use authewntication to authenticate on the swerver, and the nuse the tools locally. SHe would not havde toi weotrkky about any connection set up between the two entities : She is not making a VPN tunnel. You would need the authentication abiltiy to use these tools 


Powershell allows us to work similarly to SSH : PowerShell has imbedded security through it, so we can run scripts on PowerShell remotely; she can connect her con sole if it is logged in , she can connect with a one-way tunnel to run commands directly on the server from her physical machine. The PowerShell Session creates a secure connection betrween these two points 


Remote Desktop : gives the ability to remotely login to a remote desktop. It is a popular way to connect via RDP. There is soem security built in . We are a bit limited in terms of moving files, dropping files on a machine with remote access because she would need special security to do so, and she limits who has access to connect to that machine. In the Industry she would allow specific users to use PowerShell or connect remotely to her server/environment, but it can be a method for managing machines remotely. One way we can do is to create **specific users**.. We would not allow anyone to make changes on a machine based on *themselves*, normally we would have a special account . 



Good account management: If they needed higher level permissions, they should have a second account that gives them only the permuissions they require to accomplish the privileged tasks they need to do. 



Higher level accounts : They have high level administrative abiltiies:  limited to the IT peoplle that require the elevated abilities. 



Using these tools allows us to put the right account at the right plac,e and manage/watch these permissions. 



Using **Server Manager** is the most common way of doing so ; we talked about installing a server with GUI, it is rare to do so. Most machines are commandline-based. But we can manage those machines remotely with Server Manager. to access RSAT and the special tools , you need authentication and the ability to authenticate. You should check if the user has the right abilities. 



Remote Desktop Protocol, it is a way to sign in to a Desktop environment. From a security standpoint, it puts a divider. If we have a machine with a suspected virus, and we manage it remotely, we are directly connecting to the machine: The application can send information one-way only. if we remote desktoped into the machine, we can check the system without getting the virus ourselves. RDP only works in one direction! 


Because RDP uses a particular port, which other applications do, it is a good idea to add a randomized port. By changing the port, it adds another level of security because you need to identify which port to use. You can get RDP software/application, it is never recommended to use a Third-Party product, you do not know what comes with the product. It is always best to stick with the tools that are shipped from Microsoft until the tools were vetted. 


As a rule, do not go to a small company offering you a new remote desktop/system tool.



The big thing with RDP : We have tghe abiulity to manage permissions to have certain individuals with access to our systems. We can add the need for encryption when signing in/out, we can view wwho can copnnect via RDP, watch them, track them, changing the default port, and because RDP goes in initially, there is nothing transferable between the two devices. We do not have the ability to copy and paste between machines, and we can not go backwards. 





RSAT tools : 



windows.capabilies/rsat ONLINE





Connecting a PowerShell Session : Connecting one console to another console : requires a TRUST RELATIONSHIP ( YOU HAVE TO BE IN THE SMAE DOMAIN ON THE TRUSTED NODE : WE CAN GET KICKED OUT  : WE CNA ASK permission, as we would have to create an independent trust relationship, and the authentication/ability to control that trust relationship. We have to have a firewall available This is all logged/tracked., and when running auditing tools , you woudl be alerted when they connect to your environment. 



If we want to start a **Transcript**: which is the way we track of the commands we are using. Being able to create a transcript is very helpful , as you can record your commands, save them as a report for later , or start a task "Anytime anyone opens Powerrshell, start a transcript, and when they close, stop the transcript (it coujld be a text docujment )". There is PowerShell history but it is not as good as creating a full transcript. 



To start the session : We will be doing a PowerShell session in the assignment, but she will give us the commands. 






We will be doing auditing monitioring system management on our machines. We will do security settings, and she has provided links for additional learning. We are going to look at the performance monitor, and create a Data Collection Set. We will see how our machine is doing, and what we can do if we see someone connecting to our system. We will look ayt Security and Maintainance center. You will answer a question about the UAC (user account control) 



































