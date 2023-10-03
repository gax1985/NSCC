



We are looking at a variety of utilities today. 


We are looking at *configurations* in *Settings*. We will look at the *Microsoft Management Console* , and we will discuss the security around it. We will talk about *Hardware Quality Labs*, *Registry*(Next Class, Thursday) (When doing the assignment , do NOT jump to Registry yet).



## Windows Settings 


One of the admin tools Windows provides us with. Configuration access is separated and organized in groups. Located on the *Start Menu* with the Right-Click. We will deal with *Windows Settings*, and we will get into in-depth pieces by right-clicking on Windows. 


There are a huge variety of admin tools already build in Windows. We will see a folder called "Administrative Tools". In her 25 years, she right clicks on Start Menu, **Microsoft Management Console"** or **MMC**. 


#### Microsoft Management Console


Simply a ...

> A console that we can build, manage and maintain


Other people without our authentication can not access our **MMC**. We set it up for us, and for us to manage our machines, and other machines on the network. 


It is not uncommon to have a MMC for security folks, and another MMC for other groups etc... 


MMCs are *Shareable*! 


If she is working as a security administrator, and she has a new recruit, she may want them to perform certain tasks, but she would to set up an MMC with just the tools she would like them to have. 


If you needed someone to do administrative tasks, they would need admin privileges. With their own MMC, then she can manage their abilities. 



#### Services 


What is a *Service*?


In Linux,

	A daemon, running in the background.


In Windows, 

	A little application, run on certain circumstances. It is run without user interaction (unless ofcourse we set a Startup Type) 


If we choose the following properties : 

- Name 

- Status 

- Startup Types
	(We set them to be triggered until something happens, or when someone clicks on something. A service can be set to be only run when a condition happens).

- Log On As 

- Dependencies
	Something the program needs in order to run



#### Driver Signing


Device drivers :

	In the olden days, in order to add a hardware, we had to have the install disk/CDs in order for it to run. When we look at Apple devices,  Apple is proprietary, so the driver is already in the oeprating system. Apple's approach can be good for hardware optimization within the OS. This was an issue for Microsoft. People built viruses within drivers. When Windows did updates, it updated  just the OS, so you had to go and update every application. Microsoft thought about ways to do this better. 


The Solution : 


###### WHQL

aka ...

	Windows Hardware Quality Labs


>It is a method to make sure that the driver has not been modified in any way since it was signed by the creator. Microsoft vets every driver, and include them in OS updates. Microsoft makes sure that the hardware works to the best of its ability. 


If we get an error message : 

	"This hardware is not signed"

Refers to :

>This driver is not part of WHQL


A lot of small companies that do not want to be involved ,or large companies do not trust Microsoft are two situations of these entities not joining **WHQL**, which means : 


1. The driver is not getting updated by Microsoftr
2. The driver is not verified by Microsoft.
3. You would have to update the drivers manually. 




Two years ago, There was a vulnerability in Adobe's software. Adobe's software was hijacked, and loaded with vulnerabilities. 



## Certificates


Tied to 


#### SSL 

	Between browser andf server. We see it on websites.  Even if we are not leaving the physical space, we are still using the protocol. IIS is tied to so many things in the tech industry. They are used widely across the board. 

SSL sits on top of **HTTP**, which turns it into .....


#### HTTPS


What is a Protocol :? Set of rules on how you act coming through the door, at the door and the other side of the door.


	When you walk through the door in the mall, the way you behave in a mall would be different than when you walk through a church. That IS the protocol. The protocol can change, and every protocol havbe a default port (80 for HTTP). If she is at the mall, she wants multiple doors. If something happens, then she wants closed doors, and some doors that are open (delivery doors). If we consider ports and protocols,  when we add SSL turning HTTP into HTTPS, you are allowed through the side doors if you show an ID (delivery personnel with a special ID). This is why we have certificates 


#### What does a Certificate do ? 


It encrypts the communications. When we see S in the HTTP S : // , then communication is encrypted. A key is shared between individuals or entities. SSL also makes sure that the sender and receiver are clearly identified as who they are (Authentication and Non-repudiatation). It is done through the three-way handshake (SSL Handshake). 

To simplify it , 


###### If she wants to access a web server securely,


1. She will send them a message saying "Hello",
2. She will add all the encryption languages she knows, and the browser has its own encryption langugages' list as well, and they compare them. 
3. The server then examines the list, then they compare it to their list of encryption languages, 
4. Then they choose the most secure encryption language, 
5. then they send you a "Hello Back!" and then provide a certtificate,
6. The client then sends their own certificate to the server in the encryption language, 
7. The server send back a "Got it!" and then starts encrypting
8. All the messages then are encrypted!


What is a port? A doorway that traffic is going through. 



#### Types of Certificates 


###### 1. Signed Certificates :

Process :

	1. Company will ask a Certificate Authority for a certificate (they have to buy it)
	2. Certificate Authority requests information (who the company is , what they sell, the name of their IT personnel, etc...)
	3. The Certificate Authority double-checks the information
	4. If everything is correct, the certificate is created, signed and is sold to the company. Certificates are good for 1-year
	5. Certificates get installed on the servier with a public key
	6. Then there would be a ROOT CERTIFICATE

(Browsers have built-in certificates. Based on the machine and its IP address, )


###### 2. Self-Signed Certificates 


Similar to signed certificates but they are NOT signed by a Certificate Authority, so there is NO PUBLIC KEY on the browser. 
Both certificates will generate a site that cannot be read by a third-party.
The Data being sent is encrypted regardless with self-signed certificates. 




WATCH "SSL CERTIFICATES EXPLAINED ON YOUTUBE".


Designed for moving secure data within the organization. 





#### Activity 


If we left click on the Start, we can scrrolll all the way down to "Windows Administrative Tools", which includes all the tools provided by the Windows environment. 


MMC (**Microsoft Management Console**) : 


Hit " Windows key + R"

Type "MMC"

This is going to open the Microsoft Management Console. It is empty, so we need to place tools inside it. We need to save it. 

File --> Save As --> "Demo1 ( it will pick the default location)"


We are at *Console Root*. If there is a tool we need to use, such as "Task Scheduler", where we can schedule tasks to run under specific circumstances  


File --> Add Snap-in ---> Task Scheduler 

A window will appear " Would you like to ask Task Scheduler on the machine you are on, or you wish to add Task Scheduler to manage another computer ? "


Local computer 


Then it places it in the root (Task Scheduler)


She wants to place Services. So let us select "Services" --> ADD 


Another Window (asking if it is local or remote) ---> local


So, let us save everything! 


File ---> Save



Let us select Services from the main screen 


Services --> (Double Click) --> List of Services (Running + Not Running)


We select "File History Service "


It is set to "Manual-Trigger Start"


Double click on it --> We see "File History Service Properties"


Notice "Manual " (Manual-Trigger means when something happens which is its trigger, it starts automatically)


"Notice the System Account " on the "Log on" tab. Scroll the other tabs


Let us find a Running Service! (DHCP client) --> Double-Click


(If this service stops, it will not receive automatic IP addresses.)


DHCP : Gets an IP address for the machine, and it gets the DNS. It gets all the information the machine needs in order to communicate with other machines. If we stop this service, we wont be able to communicate with anyone. 

If we select Task Scheduler from Console Root, then we see four seervices. Select The 1st one --> See Location / Security Options (see the account?) -->
Let us navigate to Triggers --> See what triggers it ? ---> ACTIONS tab --> Conditions Tab ---> Notice the conditions checked, and conditions greyed-out(someone set them, but she does not have the ability to change it.) We have the means to change Power settings for example (to not check for updates if on battery power) --> Settings -->  (Stop if the task runs longer than 3 days) --> History(Disabled) (She can turn History on if there is something that nbeeds ot be aware of)



Main Screen --> Task Scheduler Library --> Microsoft --> Windows  --> (Tons of folders. Each of these folders may or may not have tasks created by the machine. Select one of these tasks ) --> Application Data  ---> 4 Tasks already created, one is set on a Trigger, and the others are Ready but not set to run. We can examine the custom trigger! --> Double-click on it -> then Triggers -> Custom Trigger





She sets up a Honey Pot for 2nd years, they are challenged to hack each other. She always creates a Tasks that logs her in, enables her to do tasks, and then hide the task in an obscure folder. In our case, we would have to check the Task Scheduler for hidden tasks! She also buries files in the SYSTEM files. 



### We have to create an MMC for our assignment!  
Under File--> Options--> Author Mode (the one she is in) | User Mode | User Mode Single |... 

Click on the description.

## ASSIGNMENT 2 : Systems and Security Utility. Create a custom MMC (MicrosoftManagementCopnsole)
Create one from scratch 

Record the full path of the console 

Add some Snapins --> Grouyp policy object editor

Windows Defender Firewall console 


Set Permissions on the Console
Answeer the question on Console 


Add the Certificate on the console

Answer the certificate on the console


Certificates --> Cuyrrent user ---> Pick a certificate 


Set up --> Performance Tuning! 


Add Performance Monitor to the MMC, and then follow the steps to create a performance monitor. Why pay attention to performance monitor? 


We can detect malicious usage of resources (Setting up tasks and services maliciously ... The performance monitor creates a base for the machine's oridinary performance, and then watches processes, so if something abnormal happens,  she would know. )


Registry ---> What each section contains? what datta? 



You will work in the Registry, take a Gold Copy, Create a Snap shot, and pass the assignment in . 



Next class = Walkthrough Demo. 


### Where is this Console existing? If we go to File, Save AS. ... 
Windows Administrative Tools --> clock on drop down arrow, programs , start windos


If she opens file explorer, she clicks on C:\USERS\MARIETADKE|AppDATA\ROAming\MICROSOFT\Windows\STARTMENU\PROGRAMS\Windows Administrative Tools\ ... "All this in the Save As folder in Task Scheduler. APPDATA IS A HIDDEN FILE"






Remember : Playing with the Registry Editor can lead to catastrophic results for the system. 



Do not go though Part 2 yet. ..