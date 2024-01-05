






Net Academy is not running well for Ron. He is probably not using Net Academy Lessons.



1. Why are networks important to cyber security ? 


Answer :

Networks are vital to the attacker, and they are the first line of defence. It is vital for the attacker because the attacker must use your network to complete the attack. It is as if someone is going through Halifax would have to use the city's roads. The attacker has to use our networks to do what they need to do. Consider a road we normally drive on every morning, and you could be the only car on the road. If you suddenly drive on this road, and there is traffic, this would be evidence that something is happening ahead. Obviously, yuou are aware of the change. The traffic patterns changed, but you do not know why. You know something is happening. The malicious actors change the behaviour of the network. You have clients, users, etc, and the attacker changes the behaviour of the network ; speed, communications, etc... you know it is different, but you do not know why it is different. Just like the traffic pattern, there are explanations, but it might be evident that someone is inside doing something they should not do. We keep the information on the network in a place they do not have access to. They would leave a footprint. Anything they do, they leave some evidence behind. If the attacker gets inside our pcs, we have logs keeping track on what is going on. We have firewall logs, import protection logs, windows logs , etc ... They leave evidence everywhere. A common technique is to remove all evidence. They can not do that with our networks, as they do not know where everything is, and they do not know how to get to it. They found workarounds for everything, but they are akin to walking in mud, and leaving muddy footprints. We may ask "What does this have to do with security? ". Data analytics can be the thing that we fall back on. If we gather data about opur networks correctly, we can always find them. We have to understand our network to find the evidence. When we are comparing secure organizations to keep it from getting attacked, we can do locks on the doors, cameras , key fobs, security guards on the front door etc. If someone gets inside, peolple uised to do things that they stopped doing unfornaturaly ; signage on the building "Data centrer : Ground floor." ATttackers would know where to go. Imagine if we turn our buildinig into a garden maze. No signs! Ron got contacted by someone in Scotland, where they have cities and a national government. Aberdeen is rich, and for years, the city was cash-rich from oil money. North sea oil reserves are declining ; they do not pull out when the oil is gone, they pull out when the oil supply is dropping. They know Ron does rebuilding involving the economies of IT companies. They invited Ron to Scotland to come and speak to them to improve their IT economy. He rented a castle to rent a room from, and his wife slept in a castle. As they wandered through the castle, he knew heating was a huge issue. Every room had a door. This is done to trap the heat. You could open a door, and you could get a hallway, a staircase, etc. .. it was like a maze. They were confused... *they could not find their way to the dining room*... Thus ...

Compare this picture to a building that has one hallway, a 1-storey building, and on this hallway, there are signs above the rooms telling you what is inside the room. Imagine if you are a thief going after the jewels. This building, the thief knows exactly where to go. 


Most organizatgions set up a **Flat-Network Topology** :


1. Edge Router
2. Internet 


then ....
               |                       |                       |                       | 
Router ===================================
                          |                        |                        | 
                          
1 long network, and everything is connected to this one network, with computers, servers, cameras, WIFI access points etc... everytyhing is on **One Network Segment**. People did that because networks used to be dependant on the physical cable that connected them, which is the pre-wireless days. 

It made sendse to translate the physical layer of the network to the logical ... NEVER build a network like that. The attacker would be in the 1-storey building with 1 long highway, with signs above the door. ... Instead .... BUILD A CASTLE : every entry point is confusing, and set up like a maze. 



Incident response : Blue team activated when a malicious actor is there. The Blue Team has three modules : 

1. Prepare
2. Detect 
3. Respond to 



#### Preparation : The Enemy is Coming ! 


60 AD. In Israel, there was an uprrising against Rome. They formed a rebel alliance, attacked the Roman army, and took over land. ROme did not have the legions everywhere. Regional armies were responsible for protecting the area. The Syrian army was keeping the peace, and the rebels defeated them. The messager went back to Rome that they won. Rome dispatched the legions. Thousants of soldiers making their way to Israel. Watch "Massada" : they knew the lgions were coming, they wan8ted to make it diffiicult. Rome won : legions killed everyone in the castle of Massada. The Romans laid a siege and everyone in the castle killed themselves. The point is : they knew the enemy was coming. Everytime we get put in charge of security in any installation, whether a software , a network ... please remeber the Massada example. You do not know how long you have. Preparation is key. How can I build this castle so that when the enemy arrives, they would be confused? It is about network architecture? 


How can we prepare the networks so we can defend them? Later , we will talk about **Detection**. We are well-prepared, but we want to know when the enemy arrives... In the 1st lecture, **mean time for detection is 200 day**. Focus is on cybers security today is : They are already here! Ron is a firearms instructor , and the first thing he teaches : assume the firearm is loaded. The rule is cybersecurity is asusme that the malicious actor is already in. You can not find them unless you have sentries in the right place, so they will know when the enemy arrives. 

Thus : design your networks so when the enemy gets in, the enemy will be going against barriers, and the enemy would be thinking we must be missing something. We have to have the ability to stop them! Maybe you can not prevent them from coming in, but you know when they got in! It does not matter how large the organization, we have to take a look at the network, and think about how to make the architecture more confusing, then we put detection everywhere!


Later on, we talk about *responses* ....



###### How can we make the network more confusing ? 


When people first started to do this, they might have placed a second router, a third router , etc


										Segments ---------------------Accounting 
|
ROuter          =          --------------------------------------------------- -

|

										Segments --------Executive management


Let us say the executive in the company connected to the network with an infected device, thus the executive is connected to a segment, and thus the malicious actors notice that. 

**Segmentation** was the first attempt. Acconting segments involve accounting servers, the sales server is on the other segment, so it is easier to monitor and manage.... It is still not correct. It is still too large. If someone managed to get to the executive branch, they might gety access to tghe information that they will need. There might be reports in the executive section abnout tyhje activities of the accounting department 



We have a change ! 


##### Microsegmentation 


Printers' segment                  Sales' segment
 |                                              | 
-------------------------------------------
| 
IT Support's segment                       HR's segment                                      


(Not a single line, but to demonstrate the point)


This confuses the attacker. They do not knwo the architecture, and they do not know the right segment to go after. Every attack goes through phases. **Kill Chain**



###### Kill Chain 

Attacks happen in phases 

1. Reconnaissance  : See what they can see without raising alarm bells, try the door handle (if unlocked they make a note), look for weaknesses and vulnerabilities, what they can tell about the architecture, let us look through the windows etc .... A professional nation-state actor, organized-crime member, a skilled hacker all go after a big target and they have a reconnaissance  period for **six months** because they do not want to discover anything new while conducting the attack. It is not learning time. Thety would know where everything is. The longer the reconnaissance period, the better their chances are for success and evading capture. We put detection cacpabilites at every point : 
		
  1. Access Control List : who can get in. Are you allowed there? 
  2. (Write this 10 times for memory) Logging : You log EVERYTHING, and never throw the log away. From the network perspective, we are logging network traffic, because it is these logs that are going to make us understand the behaviour of our networks. In the street example, if you drive there everyday, you know the traffic. Any changes to the traffic would be known to you. If it is a small street, it is easier to understand the base-line behaviour. The GROUND TRUTH, which is "This is normal", so when the abnormal happens, it gets spotted immediately. We place other forms of protection there : Firewalls , Endpoint monitors, Packet scanners for code and compromise signatures, addresses of the malicious actors, and we replicate this at every choke point of the network because the segments are so small, they are like a cal-de-sac in a neighbourhood. The attacker would think "where am I? oh no another hallway...". If we connect a wireless router to a switch , add some routers to the network. One thing to remember about **Switches** : Switches have ports in them. Example : Edge router, we try to probe it to let it reveal information about itself, and then we search the dark web to find a way top break into a CISCO 4661, a vulnerability is found, and that is the way in. They break in, they find another router , which they do not know about, and that makes them repeat the process. They are in, but we know they are in. This is a delay tactic. The alarm is already ringing. We are trying to delay them to give us more time to detect them. This is called **Daisy Chaining**....  We have areas in our networks that hold secret information. We have daisy-chained a series of routers, on one end, we have a public-facing web server, but we are watching it. We have an application server for the sales team, and their application server is with the public facing server. The area that is not in the secret files' horizon is called **DMZ** or **demilitarized zone** : it is monitored, the public can use it freely, but they can not pass through the gate. Another thing we put in the **DMZ** is the public guest wireless network. The application server is in the DMZ is the public needs to access it (something involving the sales force, if the organization had an app for example for sales etc...). Recall the example of the customer where Ron found out that going in their DMZ presented an easily-accessible route where it took Ron to their workers' pay-server, and they had left the password blank. Chances are they are using a GUI. This was a government agency and the entity that set this up was contracted to provide networking support.  The contactor threatened Ron with a lawsuit. There is something else we can place within the **DMZ** : 
		We might have an application that we want the outside world to use. We would like our workers to surf the web. It is not a good idea to directly let the workers connect directly to the internet. One employee who is doing something suspicious or innocent (there is a malware in their machine without their knowledge), everything is HTTPS and SSL, which means encrypted traffic. If we are watching the network, we can not see what is going on. The encryption keys for SSL and HTTPS are astored on the worker's machine. He would like to atch 8the traffic, decrypt it, look at it, check if it is ok, re-encrypt it, and send it on its way. The device to do that is called a **Proxy** : we are talking in this example about a web proxy. When our employees on the inside think they are contacting the internet, they are contacting a web proxy. We have the encryption key for encrypting/decrypting the traffic. The employee does not know this is happening. We do NOT let anything in or out of the network without examining it! A sophisticated web proxy would be able to execute code, the email proxy has the intelligence to d8etect malware/malicious content in an email. We do not live in a time where people can have complete privacy. If we say "I have nothing to hide", it is not right as people "expect" privacy. What we do is : everything and anything you do on our systems is ours! expect that we are monitoring everything! if we look at NSCC's policies, we find an item saying : we reserve the right to monitor your activities! From a firewall perspective, we can get control over that, because we do not want alot of noise in our system. If we are part of the fire crew in a community, and there is a heavy drought, you become vigilant to the smell of smoke. If someone has a backyard fire without knowing there is a fire ban. Ron's neighbour started a fire 20 minutes before the fires were allowed. The fine was 26000 CAD. They luckily did not have to pay the fine. The fire was on the beach behind the house (cant start fires until 7 PM). If we have people playing video games, it creates a lot of smoke in the network, and it makes it difficult to find a real fire. Videogames fills the network traffic with a ton of smoke, where you have to investigate itr, and amongst the smoke, there could be a real attacker. Firewalls and proxies prevent access to online gaming, facebook, plenty of fish etc ... this is so because it makes it a lot harder. External proxies : they would allow you to connect to WoW, so it hides the traffic from the NSCC proxy. **IP Tunneling** : Ron was the first to set it up in this province, we will cover it later. compare this model kwith the model we started with (the straight line vs DMZ infested network). Remember this picture because that is our goal.  






## Friday : We are tasked with a *noble* mission : Power-up a switch + take two computers + patch them into the switch board + do all cofigurations necessary for these two computers to be able to ping eachother. You are free to use Packet Tracer to do so. 


## Next week : We place two more computers there. Computer A has to be able to ping Computer A (located on another segment), but not the other two computers. We alternate the computers. Then we add an extra switch : Same concept : make them talk to A but not B, make them talk to B and not A... then we add a router, another switch etc ... we are building *microsegments* and a more confusing architecture for attackers


Next week : **Trunk** (encapsulation protocol) , VLANs, ACLs on the router, DHCP, maybe a VOIP, etc... 


Between now and next week, google "configuring VLANS" "mconfiguring Trunks " "configuring DHCP on a router", "Configuring ACLs". In two weeks, we will be able to teach it. Trust in RON!



What he wants to do : put networking in perspective for you! There is no global idea, but lets fix that. He wants to start the class with a few minutes of lecture on how networking works. We will be going though the **OSI Model**. In Ron's last company, he went into a Masters of Networking program where you had to have a bachelors of computer science. He interviewed graduates from the program, and asked the graduates on a whiteboard to draw the OSI model and explain it! At the end, we will be better than the average graduate. Trust the path!