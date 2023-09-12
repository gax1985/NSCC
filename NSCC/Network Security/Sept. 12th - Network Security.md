




Reminder : If we are not here when taking attendance, we would be marked as *absent*. Please let her know if we are late, and we would like to be marked as attending the class. 





As of 4 O'clock, a lot of last-minute changes took place in regards to the course.



How many of us know what networking means ? 


We will learn **OSI model and  TCIP model**. They are meant to clarify how communications happen between one device and another device. Before we look at security, we need to know how the communications happen. We will start at the very basic level. 


We will look at the introduction for Networking. We have a simple assignment. 


We will start with the network itself, what the network is, the network's basics, etc...

Brightspace - Contents - Welcome | Course Resources (lots of helpful resources for completing work for her and other faculties) | How to create a meeting request in outlook | how to take screenshots | how to install Office + Word on home machines using college-based software | how to submit a ticket to the technical support department | How to create an updatable table of Contents and APA citations. After the lecture, we will look at assignments. 


All of courses are given a set of outcomes, and when we are graded, we will get an overall course grade. We have to achieve 60%, but if we skip one of the outcomes, we will fail the course. 


Check the Course Resources folder. 



We will have 5 assignments per course, and we have a Final Project. 



We will start simple! 



### Chapter 1 : Explore the Network


We will talk about being Globally Connected, LANs/WANs/ and the Internet 



Network has no boundary and supports the way we communicate, work and play. 


What networks looked like 20 years ago is nowhere near today's networks. We have smart cities, smart utilities, cities with WIFI access, etc...There are few places that do not have access. Most of us are connected all the time. 


We all have cellphones. She took a drive and took the ocean side by NB, they had no data or cellular connections, and even power lines were absent. Overall, it is becoming more and more the norm. We do streaming movies and TV-Shows, many work from home, and so on. That is where networks stand today. We have learned to count on it. 

Cars are headed for this direction, as Siri and the Google Assistant are present there via Apple Carplay and Android Auto. She uses networking for timing cooking chores etc... 


We will learn more about what networks look like



There are many sizes of networks :

	Small Home/Office Networks
	Medium to Large Networks
	World Wide Networks


Her son worked in a company in NS, and then the company decided to move to Ireland, and relocated there. Thus, it is the same company with the same resources. He has to change the working hours. We have moved to a global environment where networks exist across the world. In between those sizes, we have NSCC's network. We have a bit of everything. 


20 years ago, we were tied to small offices. In international companies, each division would be separate yet connected with a single line. 


What types of networks we have ? 

###### Client and Server 

Client-Server Environment : Client is any device (computer, phone, tablet, etc) that connects to a server. The server manages all devices from a central location 

##### Peer-to-Peer Network

2-3 devices that share and connect with each other, and computers can be both servers and clients at the same time.




### LANs, WANs and the Internet


They are made up of **End Devices** , which is : 

	The first device that makes the connection, and the last device that makes the connection, and everything else in between is the network. 

Intermediary devices : devices that connect networks together (Switch or Router). Something which directs the traffic. It ensures data flows across the network and provides connectivity


Network Media : type of rows that traffic/communication/data flows on. When considering a 6-lane highway with a divider, traffic flowing in 1 direction has an easier time getting from point A to point B, less chance of collision. If driving on an unkept dirt road, it gets difficult, as you would need to drive slow, there are bumps on the way, etc. Network and media are the same; We have **Copper** which is Ethernet, which can carry a certain amount of data. Copper lines are prone to noise and interference, such as a light. This is kin to the dirt road example

We have been using Wireless for the longest time (Radios!), then we have Televisions. We have improved wireless signals, and we use wireless more often! Most places have wireless. The wireless router is an *Intermediary device*, which uses the *Wireless Network Media*. The wireless device sends a signal in a wide manner. If it sees another wireless device close to it, this causes no friction (except intersecting points with weak signals). If the overlap is too much, what happens is they *tighten* their signal on both ends ( right and left). Thus , if a router is close to another router, it tightens the signal from the right and the left, so devices on either right or left ends are affected. 

Radio signals do NOT travel well through metal, so is wireless. Wireless signals travel through bricks. She mentions at NSCC on the C-Wing, there was an apartment building with a strong WIFI signal. Someone with a laptop/cellphone would have a stronger signal, and the phone tries to connect to the strongest signal it sees, so in the same room, people would have fluctuating signal. Thus, they had to put blockers etc. Because wireless signals do not travel through metal, it creates issues. In Garages, if a router is there, and the door leading to the rest of the house is metal, it would cause issues. Boosters are placed in there, and they are electrical devices. They take the signal and boost it. a Booster is an **Intermediary Device**.

So to put it simply 


**End Devices** ---> **Intermediary Network Devices** --> **Network Media**


We will be working in a program that allows us to simulate networks. They cant show us how to build actual networks as it would be a course in itself. We will start in the virtual world. One thing we need to know is that there are actual *representations* of device(Pictures on the slides show a laptop, a router depicted as a circle with directions, VOIP phone, a printer, a wireless signal shown as a DNA double-helix).


###### Topology Diagrams 

Physical 
Logical : Idea of how we connect things and how everything talks to other things on the network. 




###### LANs, WANs 


###### LAN

	One network that is physically connected to itself. Small geographic areas!


###### WAN 

	Multiple networks/locations connected together 

Example : NSCC has many campuses. Base network is 10.13 network, all campuses share multiple resources. WANs is made up of a series of LANs and  the WAN is connecting them. WANs can transcend countries. 

Question : ISP has a network that covers a large area. With ISPs, they are different.



### Internet, Intranet, and Extranet


###### Internet 


	World-Wide-Web of interconnected networks. Not owned by an individual or group 



###### Intranet 


	A network that is an internal network only. 


###### Extranet 

	An Intranet that connects to other Intranets. NSCC's connection to Office365 is part of the Extranet, but not the internet 



###### ISP


	They give us an Internet Connection, provides an IP address, and physically connecting us to the Internet. 



AI Question: Please compare Internet, Extranet, and Intranet, and please explain how they each work!




There is something that exists called **DNS**


###### Internet Access Technologies


NSCC functions on **Dark Fibre**: when Aliant ran FibreOptic Cables in NS, they set up Fibre lines to sell/lease to organizations in order for them to have fast access. They had extra lines that noone is using, so they give them to colleges etc... It is Dark Fibre because they are not in use. All of the campuses are connected via the Dark Fibre. This campus is connected as a Rain Connection --> Akerly --> other campus --> Dalhousie --> Aliant. 
They had an issue of **Chatter** , which is an excess noise. The problem in the end was from one student plugging in something. 



###### DNS

	Translates our IP address to a readable name! It is easier to remember a word rather than a number. It is a database listing IP addresses, including the IP address for the ISP. The table provides associations between the IP and the server.  As a customer, they add you to their DNS table. They are saying " This individual at this address has this IP address". Any communication from the house goes to the ISP, checks the DNS table for the IP address for the needed resource and then connects to it. Internally, we are given a home router, which holds an internal DNS (not an internal DNS, as the IPs in the house are Private IPs. They do not exist on the Internet. We would know what they belong to by using the table on the router. The router connects that internal table to the ISP's DNS Table/server). If we are in an apartment connected to Aliant, our systems connect to the router and then to the Aliant DNS table/server. Connections go to a Junction Box ( a sqaure box sitting on a pole in the community). They hold a copy of the DNS table and redirect connections from there. They have battery backups. When we have hurricanes, not everyone uses the Internet Connection at the same time. The Junction Box has an internal battery depending on the UPS on the box. When the Junction Box's Internal Battery runs out, we would lose the connection to the Internet. We will go into more detail down the road!


###### Network as a Platform 


Back in the day, all phones had their own phone lines. We had special lines for Printers, Computers etc.


Now, everything flows on the same lines. Telephones can use Ethernet lines... aka... **Converging Network**. 


Phones use one pair of copper, and computers use another line of copper, so we connect the two copper lines together. 


We have networks that are quite flexible. 


### Basic Characterists of a Good Network 


Fault Tolerance

	We have multiple paths. If we take down one server, another will take its place.  We would do Switch-Stacking, so if any one switch dies, the rest continue to work. They all have the same programming, so it carries on the work. We would not lose the entire network. Servers and networks : This campus is the main datacenter, but there is a duplicate in Albany's campus. This is set up through redundency


###### Scalability 


	The ability to grow the network. Macs and Laptops share the difficulty of upgrading the components. It means to build the network, and making it easy to grow that network 


###### Quality of Service


	Insuring as much as possible that the network/system is going to work, and that it has the uptime it needs. Most servers would like a 0% downtime, which is unrealistic. Most companies aim for 99%. For security professionals, we will focus on Quality of Service and Security (make sure that the networks, via checks, are able to deliver securely and reliably). We will dive more into this. 


###### Network Trends 


**BYOD**, aka... **Bring Your Own Device** 

	You go to a hospital, and you can connect to their network , even through a secondary network. How do you protect yourself since you have no control over the outside devices? we would not be able to tell people of what they can or cant do.

**Online Collaboration**

	A group of people working on a task remotely together. OneDrive , Office365 etc...


**Video Communication**

	During COVID-19, people who are not invited to meetings are joining the meetings. Example : a lawyer had turned into a cat during a meeting, and did not know how to disable it. How do we know that the meeting is confidential? how can we protect the organization? A lot of video apps are being banned in Canada due to their security risks. 


**Cloud Computing**

	Servers sit in the cloud where you are not sure where it is at, or how it is working currently. 

(COVID-19 propelled us 15 years into the future! Security was an afterthought at the time, and now we are catching up. Companies were handing out video conferencing apps , and they became so widely available that malicious actors were using it)



##### Smart Technologies in the Home


**Smart Devices**

Security is an afterthought. The world is not thinking of security. There is an IoT course at NSCC. There is a new AI course that also discussed IoT devices. We need to change our mindset to realize this, and how we can secure them. Any connected device to the internet is vulnerable to someone connecting to it. On Google's website, everything involving Google services is recorded (Google Assistant, Alexa), so this is how Google improves their voice assistant, improve their services, etc. 


**Powerline Networking**


**Wireless Broadband**

	Wireless Internet Service Provider (WISP) , and , Wireless Intenet Service using cellular technology



### Networking Security


	We will look at security threats, security solutions (what we can do to protect our networks)


(Everything she showed us today is taken directly from Cisco: They are the primary creator of network routers. Most organizations might use different computers, but the primary source they will use to connect to their ISP is a Cisco router. They are the most high end and the most programmable. Sobeys use it for all their stores. They have their programmers in Cellarton looking after the Cisco network). We will not do everything through Cisco, but a lot of it. Think of it as a Textbook. We should have been invited or via email to Cisco. 


(She sent an announcement on how to create a ticket, if needed for the future)



### Assignment 1 (Due in 2 classes, Next Tuesday)


On Brightspace :


We will be doing a case study on working with Sarah. It involves connecting to NetiCAD, Cisco's Packet Tracer (Download from Neticad--> Student resources)

Must include an Introduction, Table of Contents, Title Page, Clearly-defined sections, Identified Screenshots, Sources (used to complete the assignment, quoted in APA format)


She does NOT accept embedded/ZIP files. Uncompressing files is a security issue. 

Any research must be done in our own words! If copying from the internet, even when cited, would lead to failure of that section. Thus, convert it to our own words. Screenshots must include information, so when capturing the screenshot, she wants to make sure to capture the computer name, who is logged in , etc... this is to make sure WE are doing the work, and that the work is not borrowed or stolen from anyone else. We can mark it with the pen if needed! Make sure to provide the screenshots in the order she needs them to be!




Contents of the Assignment 1 Document from Brightspace :




Page
NETW 1015 – Network Security
Due: As per Brightspace
Assignment 1: Explore the Network.
Use resources and applications such as Packet Tracer to explore the network and connect to
the internet.
Notes:
 Moist weeks, part of the lesson may focus around a developing case study that
follows an entrepreneur named Sarah who is starting up a new business.
 Assignments generally cover the material in several different ways that may include
a network simulation program called Packet Tracer, an environment for running
virtual computer images called VMware, and hands-on work with physical equipment.
 Note: Not all of the steps may be provided (if you’re not sure what to do, try figuring
it out on your own, asking a friend, or asking me).
Required Resources
 Cisco Networking Academy https://www.netacad.com . As part of this course, you have
been setup with a student account. Think of this as your online textbook.
 Packet Tracer
 External hard drive
 Course Resources as posted in BrightSpace
Professional Documentation
All documentation must be done in a professional style. It must include:
1. Title page
2. Updateable Table of Contents
3. Document introduction
4. Section introductions or description, each section must be clearly identified
5. Graphics or screenshots MUST include a title with a short description
6. Any direct or copied quotes or graphics MUST be properly credited in a footnote
7. ALL sources MUST be properly cited (APA format) and placed at the end of your
document in a bibliography.
8. NO embedded, zipped or compressed files. ** All scripts must be converted to text
before including them in your documentation. **
*1 Professional Word Document ONLY.
Research and documentation sections - Please complete all research and question
responses in your own words. Research sections not completed in your own words may
result in a mark of 0 for the section.
NOTE: Please do NOT copy and paste responses from internet, even with a citation. I
expect each section or response to be in your own words. Be prepared to explain your
responses and demonstrate your comprehension during the marking period.
No marks will be given for cited or credited information included in document.
Marking and Assignment Notes:
 Screenshots MUST include user or device identifying information.
 Screenshots MUST be added to your document in the order of creation.
 Documentation must meet Professionalism requirements.
 Automatic mark of 0 - Assignment not submitted or work not original.
http://www.nscc.ca/docs/about-nscc/policies-procedures/policy-studentcodeofconduct.pdf
https://www.nscc.ca/docs/about-nscc/policies-procedures/policy-academicintegrity.pdf
NOTE: This assignment may require some adaption, research and troubleshooting.
NB: Citations – Remember that citations MUST be provided for any code, script, test or image copied from another source or used
as a resource. Not attributing appropriately (Plagiarism) or using illegal or unlicensed copies (copy write breach) are serious
academic offenses. If you have any doubt as to when or how to cite, consult with your instructor and the resources provided by the
college.
Page
NETW 1015 – Network Security
Due: As per Brightspace
1. Create a professional document that includes a title page, updateable table of
contents and will list sources in the APA format. Use your Course Resources content
to support your document creation.
2. Go to https://www.netacad.com/ and log into your Cisco account. You should have
received an email about setting one up.
3. Read through section 1 of Introduction to Networks called Networking Today.
 You should attempt all of the Check Your Understanding quizzes since
many of the same questions will show up on the weekly quiz
 You can always skip activities and labs such as 1.9.3 unless I say otherwise
4. If necessary, install the latest version of Cisco Packet Tracer (steps 1.0.3-1.0.4) and
complete Packet Tracer activity 1.0.5. When you have successfully completed the
activity to 100% click the Check Results button (bottom left) and select
Assessment Items. Use the Windows Snipping Tool to attach a screenshot showing
your activity results to your assignment 1 document. (2 pts)
Page | 2







Notes :

	She will show us how to do the Title Page, Table of Contents, and other aspects