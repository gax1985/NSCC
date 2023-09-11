




We will start with the basics 


We will discuss components


He used AI to generate the presentations


check out Tome AI presentation generator




We will talk about **terminals, thick clients, smart clients** , etc...





#### Introduction



He uses AI, and he would like us to let him know when using AI for documents etc ... 


There are many types of workstations, so there are **thick clients**, **smart clients**, **thin clients**



There were not many workstations back in the day. If we see any old shows, we see CRT monitors with no graphics (**Terminal**). Multiple individuals can work on **Workstations**. The most common type of terminal was **IBM 3270**, which had a green monochrome display and a keyboard. They are nice and efficient, and start up instantly. They are connected to the main frame server. If the main frame went down, all the terminals go down too.


##### Thin Client


	A client with a stripped-down operating system. 


They do not have much processing power or storage capacity. A thin client is not used alone; they connect to the server. You would have dozens of people using them, and they are good for single use, as they prevent workers from browsing the internet. Last year, he saw thin clients at nurseing stations, where they were used for charting. They were replaced during COVID-19 times, as everyone needed Microsoft Teams. Alot of kiosks use thin client, where it is a single purpose application being run on it. These thin clients were pulled out at nursing stations, where they are mounted on the back of the monitor. You would log in, and it would automatically launch the application. They got for 150 CAD. Not great for everyone though!

He worked at a construction place, where the mechanics logged their work time. 

In the virtualization course, he has Azure labs, so he would remotely access an Azure Windows desktop. Since it is in the cloud, you can run multiple applications. 


He looked at comparison between desktop and thin clients involving cloud computing and virtualization. The cost of the service for the VMs vs buying a computer was the same. 


Each scenatrio is different, you would select the ideal system according to your budget.



### Thick Clients


It is a desktop/laptop!


They are a computer woprkstation that has more processing power and storage than thin clients. They run applications locally, and use their own processing power. They do not rely on a central server. 


There are **Thick apps** and **Thin apps**. 


Desktops are not portable but laptops are!

ex. AutoCAD, it needs a lot of resources, so typically desktops are better for the tasks


Desktops are expandable, while laptops are limited in their capacity. 


There are those who favored giant towers, and Macs were more popular as desktops.


Laptops have less RAM space. 


Laptops are more convenient and portable. They may not have the same performance though. both types of **thick clients** have their pros and cons



##### Desktops


They tend to be cheaper, but as compared to laptops, this is changing (they are rising in price, and laptops are getting cheaper)


Once you get a laptop, you would tend to continue using laptops if you prefer them. 


Desktops are good for video editing and gaming due to their upgrade potential as needed.


Alot of video editing is done on Macs as compared to Windows and Linux. 





### Laptops 



Smaller screens with more portability. 


They are thick clients designed for portability. They are used for a variety of tasks 



### Smart Clients



They combine benefits of thin and thick clients. 


There are more security benefits to them


They are more customizable in terms of the device. 


Thehy have better encryption, but they are more costly to set up.


Google has an administration tool for **smart clients**


They are good for hosting apps on the cloud, but still be able to do processing locally. 





### Client/Server VS Mainframe



###### Mainframe 


They were used at the beginning

Cloud applications are client/server based 




Thick client : complete applications | Thin clients : minimalistic software | Smart clients: a combination of thick and thin client features 


Applications : thick clients : local | thin clients : on server | smart clients : hybrid deployment

Processing : Tick clients : performs most processing locally | thin clients : limited processing | smart clients: partial processing on the client 


Resources : Thick client : requires a lot ! | thin client : minimal resources | smart client : moderate 


Network : thick client : less dependant | thin client : highly dependant | smart client : moderately dependant 


Customization : thick client : highly customizable | thin client : limited | smart client : customizable to some extent


Security : thick client : lower security | thin client : higher security | smart client : moderate security 


Maintainance : Thick client : required individual maintainance | thin client centralzized maintainance | smart client : combination of individual and centralized


Recovery : thick client : high recovery times | thin client : low recovery time | smart client : moderate recovery time


Scalability : thick client : limited scalability | thin client : low recovery (images dispatched rapidly) | smart client : to some extent


Data storage : thick client : local stoage | thin client : centralized storage |  smart client : a combination of local and server storage 



Notes :

	Smart client aka Chromebook (you can install some apps on them, but alot are Google-based)
	HD thin clients : size of a notebook, they tend to get mounted on the back of monitors , no mechanical drives
	Digital signage : controlled from a website 
	When thin clients boot up : they automatically log in and are pre-configured. You can interrupt the boot process and change its address on its network. 
	A smart device has an IP address. He mentioned IPV4 and IPV6. IPV4 is typically used : 4 sets of numbers from 1-255. Due to so many devices, there are public and private ip addresses. at the school, 172 ip addresses are internal. we would have a publically facing IP address and a private IP address. DHCP is for figuring out the ip address according to the server. 
	If we watch a show involving computer forensics, numbers higher than 255 in ip addresses are not real. 

	Android Box : more of a smart client, as it has its own applications, but it could be a thin client if it boots to a website. 

	IOT : simpler than a thin client, they can be dangerous. a casino in Las Vegas got hacked through the temperature monitor for the fish tank. It was a network-connected device, and not on a segregated IoT network, they were able to steal funds and data. 

	We have ransomware, where the data is encrypted and the decryption key is available for a ransom. 

	Others simply steal the data

	Companies are obliged to inform their clients in the occurance of a hack. Thus, this plays an important factor from the hackers' end, as it would cause terrible damage to the organization. 

	Thin clients would not have too much information


	Digital signs are seen everywhere. They do log in automatically, but they would log in on the backend to the administration system. 

	Self checkout : most likely thin clients. 

	Kiosk mode in the browser : hit F11 to launch kiosk mode  thin clients log in, boot a browser, and automatically launch them in kiosk mode. 

	If using a thin client in a workspace, alot of the apps are served through the browser. There are systems on the backend that publish these applications. You would log in to Citrix Connector. They used to do this through desktop icons to launch it remotely. Thin client powers up and launches Citrix Connector. Used for nursing and finance applications. They are controlled by user rights

	Thick client : you can have a group opf people using the same Citrix connector

	Would all the components be thin clients ? components in a desktop on a thin client is a slimmed down version of the app. 

	We will talk about components later

	Thin clients tend to not be a target. Thick clients are most likely as compared to thin clients. 

	Thin clients are cheap and easy to service. If someone's digital signage went down, replacements and modifications are quick. Thick clients are more work to get them back up and running.


Questions : 

Provide examples of a smart client, and please indicate the type of local storage it would have (if any)


Provide examples of a thin client , and what kind of specifications


Provide examples of a thick client, and what kind of specifications they would have 




### Server 


Any desktop can be turned into a server 


Windows vs Windows Server : Server handles configurations for networking space management, processing etc. 


The OS are much more different 


Servers would have redundancy in mind. example : two power supplies etc 


You would not necessarily want to run server applications at our workstations, but they can be useful for virtualization. The limitations are space and RAM. at the end of the day, it would have the same components. VMs will run slower on HDDs. 




### Virtual Machines 


Windows : VMWare Workstation Pro | Oracle Virtualbox


They create a virtual computer, and you would allocate RAM , hard drive space etc


If we have 32GB RAM, we can create 4 VMs for example each having 4GBs of RAM


Servers are expensive!


		Question : Recommendations for Virtualization Software ? he uses VMware, some use Virtualbox because of better compatibility with some applications


If we run Task Manager , 



Servers : CPU might sit on 1-2% memory if the server is serving one application. Virtualization allows you to put more servers on the same system. You would cut down on cooling, power consumption. It has gradually increased in popularity due to this reason.


If a VM freezes, it can be shut down 


We will be looking at the individual components in the next class 

	Qualication : you own a physical server in another datacenter and other people are using it. He can have a huge server and rent a VM to one company, and another VM to another company. 

Persistent virtual machine : you would get the same virtual machine all the time . If I save a file, after rebooting the file would still be there

Non-persistent virtual machine : the file would be gone.



We are likely quized on thick clients, thin clients 

The slides will be placed on Brightspace

Quizes are done in Brightspace, and we are on our computer. Quizes are tending to be open book, but he wants us to remember the information without having to resort to older information. 


### Assignments

We will have a walkthrough for the steps needed for assignments

It is a good habit to know the steps

Alot of steps are done virtually. 


Microsoft Office came in a box back in the day (floppies). The fees are paid once. Now, it is subscription based for a lot of software


We will be looking at CPUs, RAM, GPUs (it can do a lot more chores than a central processor, it can do parallel work)


Type 1 virtualization : the system runs VM software only directly


Type 2 : OS running virtualization server, so it can run other applications beside the virtualization application 


There is a baremetal Hyper-V from 2018-2019


We get an account in Azure for eduction :D 

Azure Dev Tools for Teaching - Azureforeducation.microsoft.com --> sign in with our W#

On the desktop in the laptop, we have vizeo. 


If we have azzure for education, we can grab applications from azure such as Vizio. It tends to provide an ISO image, and we get the key to install the application. There is a Microsoft Hyper-V bare metal installation available 
### 1st Assignment

Lab

Install Windows on VMWare Workstation. He does not expect us to be experts in VMWare, and the lab will guide us on the steps to get things done.


Passthrough : when creating the vm, we can assign resources to it, and decide to make resources not available. 




