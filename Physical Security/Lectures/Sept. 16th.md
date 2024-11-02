

# Vulnerability Assessment and Risk Management



We will be talking about Vulnerabilty Assessment objectively. We will focus for our assignment on Standard Digital Network Vulnerability Assessment


We can do the CEPTED assignment discuss everything about it, and most of the points from a Network Vulnerabilty Assessment would be covered.



There is a difference between *Safety* and *Security*. When we are discussing locks, we are focusing on Security, and not Safety. If you notice on something hazardous, there are individuals who take care of it. When discussing Fire, we would ask, do you have anything that mitigates/fights a fire, especially when it comes to the data center? 

Ron used to do so so frequently. He has done this all over the place. This is a really sensitive topic for people, especially if the hiring organization does not welcome us with open arms (which they will do!). If Ron is commenting on the Physical Security, and they have Physical Security people, he will get dismissed on grounds of someone internally who does so. The hiring clients get angry! Managers and employees get scared, especially since they have been doing something wrong on their computers for the longest time. 

The employees usually do not like you. 


There are three fundamental phases : 


## Planning ( 2-3 weeks )


It is super important, because you are going into an environment and interacting with people who do NOT want you there. You should recognize this from the beginning! You start with buy-in from a senior manager, CEO, and get their approval, or *Color of Right*. You will run the risk of doing damage to the organization, either physical damage, information systems' damage, or morale damage. Let us find a way to mitigate that. Mitigation does NOT make the risk go away. What you are afraid of will happen, bnut mitigation will *lessen* its effect. 

Everyone in leadership has to be on board, and it has to come from them and *seen* to have originated from them. 

You do not know if the person who is hiring you has the authority to do so. A Network Manager may not have the authority to hire him. Ron was worried about getting sued. 

1. Buy in process from the senior authority :
2. You negotiate with them in terms of Rules of Engagement. You need in a written agreement what you are hired to do, and what you can do/can not do. "You are allowed to do physical penetration testing. You are not going after employees , etc .". 
3. A timeline has to be established. Make sure that one or more senior executives are available on THAT DAY. If you find a critical vulnerability, they would be the go-to person. When a critical vulnerability is found, Ron would stop what he is doing , report the critical vulnerabilty to the most senior person.  This is to protect them NOW, and from the minute he discovers it until the moment he has told them, Ron is legally responsible for the damages suffered. 
4. When you are working for them , you need to be accompanied by a person in authority for the asset we are assessing. Most people in the organization know the person who will accompany you. They have a comfort level, and they have all the access credentials that we need. 
5. Have a meeting with everyone in the organization (Lunch Time) for 15 minutes. Ron would get introduced by the senior executives, the work will be described, and questions to Ron may be asked. Ron would say " I will be looking at your browsing history. A lot of people go through here. I am not criticizing your work, and I am just an extra set of eyes". Appeal to the Networking crew of the organization
6. Scheduling : 
   Ron has not done a physical assessment that took longer than two weeks. If it is more than two weeks, there would be multiple locations 
## Assessing (2 weeks )

The actual work in Vulnerability Assessment. This takes the *least* amound of time!

## Reporting ( a Month! )


It takes longest because if we look at the output of all his actions, OpenVAS presents a lot of data, and you have to interpret it. You have to present it in such a way the network administrator will know quickly what they need to do, and make it to a non-technical audience. So visually-present the information for the non-technical audience. You start with the raw data , even from Nessus, and find a way to present it in a report to a non-technical person. The graphical side could be complex, and Ron had to hire a programmer to visualize the data. There is a program called SAINT , and it does a great job at the Visualizing part of the report. The difference is Nessus' license is 1200 a year, and SAINT was 7000-8000 dollars. Then , you have to present it, physically present to walk through slideshows, paper content has to be prepared, and include a large-volume media ( like an external drive). Because the list of vulnerabilties that need to be repaired can/will be incredibly extensive ( Ron reported that his reports from Nessus were 10000 pages). And what WILL happen is , people will want to know what he will be doing about it. The report is a Medium-Level vulnerabilty assessment, that lists what is the vulnerability, and the time period to clean up the mess ( 3-6 months of repair/remedy to fix all the vulnerabilities). Offer to patch software for 200CAD / hour, hire a summer student and give them a list of what they need to remedy. It is often what administrators will do is swapping all their desktops for 300 CAD a piece rather than paying someone fulltime salary to patch everything. It is cheaper to buy new, and you get the benefit of having the newest things. Organizations move computers, and more people around computers. What we have left on the computers are artefacts of what the other person did. The crumbs left behind can be detected ( one example is the Mac-based tool ..) ..




# Risk 

### Avoidance :
When it comes to Risk, we want to avoid risk by avoiding the bad things that cause the risk! 

### Reduction/Mitigation: 
Reduce impact of the risk ( better fire extinguishers), installing segments on networks. You make the outcome of the risk affect you much less in terms of impact. It is most common to reduce the impact to various extents. 

### Spreading : 
If you have a data center in Halifax, have a backup server somewhere else. We have multiple backups at different locations ( work, secure facility, offsite third-party site etc. ) 1 = None , 2=1


### Transfer :

You can buy cyber insurance. Cyber insurance covers ransomware attacks, rebuild the infrastructure or pay the ransom. Other types of insurance you can get for natural disasters. You are transferring the risk to an insurance company. 

Publicly traded companies with ISO31 certification will indicate how much they spend on cyber insurance.

### Elimination: 
If you have a risk of something bad happening, you can take precautionary measure to keep it from impacting you at all costs. If you live in a log house, and you are worried about bears, you upgrade it to a cement-based house. 

### Acceptance :
We have a risk, the cost of dealing with the risk is far greater than the value of the asset ( "Who cares if they steal a toaster"). 




NIST Auditing:  Reading paperwork, checking for 1200 security controls (common controls)


-------------------------------


If we ask any customer-facing Risk Specialist, what is the **Risk Formula** ?





## R = P I 

### Risk = Probablity X Impact

If the impact is from 0-1000 , and the

impact is 1000
probability is %10 

The Risk is 100 ( the number is relative to the other numbers). We have a value of Impact that is qualitative. You do not want to convice someone ever that something qualitative is quantitative. There is no underling science/physics behind it, but it is something to give you enough increments to know what you are dealing with 

Impact is better to be 0-100



What is the probability at a Nuclear Missile Site worker triggering the missile   on their own ? 



Richard Fienman was one of the best physicists in the 20th century. He joined the Los Allemos project to build atomic bombs. He knew physics and math. He was 19 years old, and he got sent to a room as big as a school gym. He was looking at blueprints for the design of the enrichment facility. They asked him to look over the blueprints to see if there are any risks vulnerabilities etc. He was concerned about vulnerabilities in a valve.  They considered him to be the expert, even though he did not know what he is looking for. 


Probability changed if every part changes vs if one part fails. 


Mirrored backup infrastructure on a remote site. 


When you get to the solutions, they are done by systems people. Our job is to ask questions about the repercussions of certain eventualities. 



At the Fukhishima Facility everything that they were afraid of happened all together. 



We have to adapt to based on what could happen using evidence of what has happened!



Any Risk Professional talking to a client, they will summarise the formula to : 

Risk = Probability X Impact


How to get Probability? 

You use data that is not qualitative. Use for example Average mean time until failure on the hard drives. They know because the run the hard drive in a lab that repeats the same action. It is real numbers, and if you do not have that, make it a best-guess of expert opinion 

What is the probability of a hospital being hit with ransomware? 

It WILL happen so , its 100%. 

There are things we can do to improve our guesswork, and we would do so alot in Malware Campaigns.

If you get hired by a specialized organization, you have to do a bunch of research. Is there malware that specifically targets that ? it turns that navigation systems on ships do have malware ,and they have been attacked! 


If a pilot plugs in their tablet , and they plug it into a ship, it is possible that the device has been previously infected at home, and now the infection spread to the boat. 


The probability numbers are done with due diligence. 

You have to be open with quanative( 70% ) vs qualatative (best guess) 

Probability is 78% based on a qualative assessment of risk. 


What can go wrong? everything! what is the liklihood of that thing occurring ? 



There are certain risks that the organization may have, where the liklihood is high (10%). If it does happen , the impact will be critical. If we are considering a life-saving machine, the probability will rise to 100% , due to the impact being huge. You do not want to mislead them into ignoring it ...




We have to conduct a series of analysis ( we will see it on Brightspace's Slides) regarding cyberthreats, what are the cyberthreats targetting that industry, we should have an idea about the types of analysis we will do, this is where we stay up to speed on threat intelligence feeds.

Consequence analysis : 

impact of what happens when the bad thing happens. 

Most people do not fully know the true impact. You have to launch collective campaigns and legal consequences .


Richard Fiedmann, Motors , Airplaces : studying impact of failure of one system on other systems!


Documentary "Hunt for the Bismark" : ship could only steer in a circle due to torpedo damage to the rotor


Are we vulnerabile to ___ ? what is the liklihood of our employees clicking on Spear Phishing emails/links ? We hope to do intensive employee training, a way to check emails before they arrive ... not everyone in the organization need external email. Do they need external email to DO THE JOB? 


If we are reducing the attack surface by limiting the number of people who could click on malicious links . 



Risk formula from last year : 
This formula is for us only! 

R = PA X (1-Pe) X C
Risk = Probability of Attack X (1 - Probability of interruption X probability of neutralization) X Consequence 


Consequence = 1 - 100  

Impact = 1 - 100


If any component of the equation is 0 , the risk is 0 


If we can always detect it X if we can always stop it






It has been determined probability of attack is 90 percent, we can detect it 50% , and can stop it 50% , it is bad


Which event should you concentrate on ? 

If you are hospital, you will get ransomwared ! 

Can we interrupt the attack ? 

100% 


Can we neutralize it ? 

100% 



R = PA X (1-Pe) X C

Event 1 --> Pa = 0.9 , Pi = 0.5 , Pn = 0.6 C = 0.9
Event 2 --> Pa = 1 , Pi = 0 , Pn=o , C=0.8




Pa = 1 
Pi = 0.0 
Pn = 0.0
C = 0.1


Pa (1) x (1) X 0.1





# Attack 


### Preattack


### Attack Phase ( In the Middle of an Attack)



### Post Attack ( Fix it for Next Time)



We are using qualitative levels = likely , minimal etc






The worst possible scenario 

Pa = 1
Pe = 0 
C = 1 




If an organization has the resources to pay the wealthiest ransom, the organization will draw very proficient attacks/attackers



Annualized Rate of Occurrence :  ( For Next Class )

This we do on a quiz. The likliheed of an event in a given year = annual rate of occurrence 


This formula is all about what you give to management to justify your budget. This is the math you use to justify high costs 



Annulalized Rate of Occurrence ( liklihood of something bad happening in any given year )

Asset value you are trying to protect 


Exposure Factor ( how much of the asset did we lose ? )


If we have a bunch of data that is encrypted, and puts us in a bad situation ? 


If there is an attack, if it only corrupts today's transactions, we are only at risk of losing 10% of our data . 


If a exposure factor ( 0 -1 ), the value in dollars of the asset value that you lose Exposure factor of 0,5 means that each event we lose half of its value



Single Loss Expectency ( how much value we lose ) = Asset Value X Exposure Factor 


Annualzed loss exptency = how much value in dollars and cents will I lose each year based ona  cyber threat ? 

SLE X ARO

Single Loss Extency ( how much value we lose each time) X Annualized Rate of Occurrence 


SLE = 2000 
ARO = 0.5 


This would yield the number that is our budget ? 


Hypothetically, if we do not lose a whole asset each year, and the person asked for 20000 dollars which is the value of the asset ...


The goal is to build a system that costs 17000 to protect an asset worth 20000 , if it will take 17 years to happen, then we are not doing too badly. 



If you do not ask for a number that will cover 20 years, you will do well , as it would realistically cover the liklihood of it actually happening and thus costing the organization just the amount needed. 



eCommerce website that produces an average of 1000000 a year. If we get a DDoS Attack 100000 dollars a year in damage (exposure factor is 10%, since loss exptency is 10%) .. 0,5 for liklihood of it happening in a year ... Mitigation cost for DDoS for this year = 50000 dollars 



Last Example : 

Kids break windows in a building , 500 dollars to replace ,no bit of window can be saved , 100 dollars in water damages due to it raining after they break, how much would it cost us to prevent the damage . 


You spend 500 bucks every time the window breaks. Every now and again, it rains , we end up with water damage. 

No part of the broken window can be saved = exposure factor of 100% 

Annualized loss expectancy = 

Break 3 times a year 

each window worth 500 

1000 dollars in water damage. 


If they break one window every 3 years 


We will have a quiz , read chapter 2, we will have an assignment based on Nessus vulnerability assessment , we will have a quiz that calculates risk formula 



All our assignments are hands on. 











