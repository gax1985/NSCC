



We will talk today about some new *Attack Vectors* and discuss *Risk Management*






#### Review :





Larger circle (including any smaller circles )




small Circle - Treasure







Ve ctor : Direction the entity is going into 

Attack Vectors :

	Directions or Strengths or Force the adversaries are using to go after the mentioned treasure




###### Simple Ones : 


Go after the **Network** (Larger Circle )



It is more about **Lateral Movement**, people think that the attacks are coming from the outside world, which is old and does not happen much anymore. 


Attack Vectors are focused on *people* so focusing on endpoints : phones, laptops, computers, etc ...


The goal is to go after the **End Point**



Hyppothetically, a work *laptop*, through improper cyber hygiene online, is compromised. The attackers go *laterally* through the network. 


Equifax hack :


Broke in March of the year. They did NOT steal data until June. One of the reasons why is because Equifax is one of their biggest prices in history. They have knowledge of your income, your spending, etc... thus, they figure out your financial profile from this information (net worth etc...).Equifax takes data feeds from employers, payroll companies, and then get feeds from point of sales systems (AirMiles, Loan, Credit card ...). China did it. WHen they broke in, they were giddy. They found the motherload. They wanted to take EVERYTHING, including senior government officials , military personnel with financian problems to blackmail, spending habits so they can be blackmailed. Gambling expenses are tracked with *Loyalty Cards*, so your activities' information is being sold. They wanted it all, so shipping it all at once is suspicious. 

1. They did inventory (It took them a month ...)
	-They roamed the network 
1. How to get it out (...it took them two months. Off peak hours transfers etc...)




network attack vectors changed!

Someone going after the firewall 


Easier way is to compromise the *End Points*. How many social media pages they have? to they have TikTok? to what degree are they engaged? it creates a lot of mini attack vectors on the actual point. 



The *End Points* are **THE MAIN TARGET**...



It does not have to be a wireless network, or ethernet cable network, but it could be Bluetooth. 


There are worms where when you walk around the room and there is an infected Bluetooth point, it can hop from your phone unto your computer etc via Bluetooth. 



**People** are MASSIVE attack vectors, with blackmail, bribes etc ...


If a **person** is in deep financial trouble, they can be compromised. 


Sextortion is very prevalent. Cyber specialists are typically introverted for that reason. They try to compromise you online. If you are doing something that they can compromise, they will go after it. You are 100% their focus. 



There are many *subsets* ... **Databases**


2nd year students are learning to look out for *scanners*. In Ron's experience, China goes after 2-3 ports. They like databases. Most databases have a standard port by default. If you install MySQL, the admin page is being accessed through the LoopBack address. Oracle have predefined standard ports and protocols. Most people accept the default. China knows which port to look for. Easy way to shut it down is to *change the port number*. **SQL Injection** is a huge one. Going to a website and entering a command in a box (if not properly configured by the developer), the server executes the code.  This way, his SQL statement gets inserted into THEIR SQL statements. 

How do you stop **SQL Injections**? We will cover it in the Data Security class
We can do input filters that look for SQL code
Regular Expressions are used to hide SQL code (you would have to go through the code, to see the result. Not many are doing that)

There was a competition to write a SQL command that is really complicated, and the challenge is to automate the understanding of this line of code. 


This is an ARMS RACE! "Fixed Fortifications are Monuments to the Stupidity of Man". Attackers ALWAYS win! 





#### **Web-based Attack Vectors** 

**Form-Jacking**

	You think you are typing your password on your bank's website, but in truth, it is going somewhere else


iFrame 

	Have someone logged in to the bank, and the ratemymovie.com, you can transition with their credentials from ratemysite, and their bank, because both are open



###### Click-Jacking 

	Would you like to see this movie? YES or NO. YES downloads malware. 




#### Physical Attack Vectors


Power-Over-Ethernet: 

	Use electrical cabling as a networking medium

He can go to an office tower in Downtown Halifax, and as long as he can go into a room with an electrical jack and an ethernet jack, he can go to the food court in the bottom, and plug the electrican to ethernet box, he is inside their network. 


Subset of networking, we can install *devices*. How many have ever checked their keyboard cable to see where it is plugged into ? You can buy a tiny device that plugs into the keyboard port, and he can monitor everything we type, as it is not encrypted. He can use my internet to ship this information to him. He can give my computer instructions. He does not need a  cable connection to do this, as he can become a Bluetooth keyboard for his phone or the desktop. To prevent this, do NOT allow physical access to the computers. Computers should be in a cage in a lockbox, with ventilation. It keeps people from installing these gadgets. It can be from a wireless device that detects what we type in. 


Question: Is that why DeepFreeze is used? 
Answer : DeepFreeze : if he can break into a computer at work, he compromises it, so every time we delete the malware, it would re-install it . This is the **Integrity** problem. If we have a computer we think it is compromised, we have no integrity or faith in this computer. Needs to be wiped completely and zeros overwritten on the hard drive etc ... With Deepfreeze, any unwanted changes are gone. 


Ron designed systems without disks. Everything boots from EEPROM. This way, nothing can be compromised. The web is full of compromises. 

If we have a power outlet on the outside of the building, 


Next time in a coference room . look for an ethernet kack, find an AC jack in the room (usually next to eachother). Find the outside plug in the building, and then plug into that with Ethernet-over-Electrical. 



#### Wireless 


Where is the Voyager 1 now? outside of our solar system. It has a 5V battery. It sends signals to earth, and responds. Radio signals go forever. You just need a really good antenna. If we think the WIFI at home is reaching from the router to the bedroom. There is a wireless cloud around your device that can be broken into. It is very easy to break their security. The cloud goes on forever. If we have the right antenna, and we are broadcasting something wirelessly, he can be miles away and pick up the signal. The wireless signal does not stop on the walls of my building. It is a question of how good the antenna is on the hacking device. 



#### Physical Security


Anyone who has been in this business for a long time have many war stories. He does not have to be technically proficient to break into teh system. He can break into the building. In many circumstances, you can simply walk in. Pretend to be someone else. We will learn **Social Engineering** to break into places. There is a challenge : from being on the sidewalk Infront of the building he was not permitted to, to go to their secure room , and plugging a jack into it in 90 seconds. A lot of things went right for him, and a lot of understanding. He had to look pathetic.  Most war stories : 


"I walked in. Grabbed the server, and walked out"



His friend did a penetration test, where their 1st attack vector was to go agfter wireless. Tehy sat in a van at night to see if they can hack the wireless. One of the guys stepped out of the van, found an open door inside, grabbed a cart, loaded it with systems, and walkeed out. Social engineering is wonderful!



SMU : 


Rice Residence : every floor there is a common room, and every common room had a tv. Someone showed up in overalls and a tv-repair truck. The security/residence manager were told "All the tvs we shipped were faulty. We have to swap them out. Can you pinpoint a date we can replace them all?" "Tuesday 11 AM", then they came back, stole every tv and left. 

ANother is to go to a company's website, grab their logo, print a bandge with their logo with "Security Supervisor", it worked for him in NB. He walked into every office for that company. There are ways to do this where you do not get challenged. 



Golf Course story : 


Hypothetically, there was a countryclub near to his home for the ultrarich. It had a big golf course. He wanted to play golf. He would not be admitted at all. His partner in crime had a car (Spitfire, with a lot of bodywork). It was a sports car, so you had the right appearance, along with clothes and golf clubs. People started golfing at sunrise. The 1st hole is far from the ProShop, and the 2nd hole came back by the ProShop, and then went off to a distance. The Pro did not show up until 7 AM. You were expected to go back when he comes in and tell him the score. They had to be there before the Pro shows up. If you were to climb the fence you would get caught. He drove in the sports car, chitchated with the guests inside, made them laugh, they grabbed the balls quickly, then went off to the next stop (2nd hole, 3rd hole etc...). They played for free for a very long time. They were 16 years old. One day, they were playing their 13th hole, and the groundskeeper comes to them in the cart, started to speak to them, and Ron interrupted him that they were playing and to not interrupt. The keeper asked them if they were members. They deflected this question, and accused them of ignoring kids who were doing donuts in the 30th hole. .


Anger and threats in social engineering is the last resort. It will NOT work against Security Officers. Groundskeeper, receptionist or network tech it would work great as a last resort. Intimidation works as a last resort if you are caught. You need to scare them off enough so they can go check something else, and then you ESCAPE. 


We will learn how to pick locks and do surveillance, and how to detect vulnerabilities in buildings. He wants us to be able to immediately spot weaknesses that noone else can see. When we are doing Risk assessments, we are called upon to do Physical assessments. It is easier to steal the server itself, as compared to hacking into it. Every penetration tester will try it first! People do not expect you to be a liar. 


There are tricks to being a good liar. Lie about being a good liar. There are ways to do it. Humor works well! When you greet someone with a smile with soft eyes (the same look you give to someone you like), and people soften immediately. You can be an old lady with a 5-year old granddaughter who needs to use the washroom. All you have to do is be left alone. You can drop 100 usb drives, where you toss them on desks, in the lunch room, and everywhere else. It will get plugged in guaranteed every time. 

Treat the USB drive like a sandwich on the ground. 


He went to the Beer garden and there was a rail where everyone left the beers, and someone came along and drank all the leftovers. You do not have to put anything on the USB drive. IThere is a code that pings your system that someone plugged in the device. 


When targeting the same person, how many people parlk in the same spot every day? it would take him 2 days to find out the regular spot. If he wants the particular person, he would leave a USB drive right ne8xt to their spot. They will plug it in. Penetration testers will throw them everywhere. 


In 7trainingm, if you find a USB drive around, take it to IT, and mention that someone is trying to use the USB to hack into the network. If we wish to put malware on it, it would have to be a binary file that they will have to open. It should be named something that attracts their attention ("Vacation Pictures", etc... Consider names that would be likely to attract). People will click on things they know they should not. 


USB DRops are part of the physical attack vector. A good hiding place is behind the toilet on the floor. 



Network --- used to be strong, not so strong anymore

Endpoints ---> super focused attacks  (SQL injections , ports , etc ... each attack vector is strong and targeted directlyt at you)




If you put all these vectors together, and you end up with a **surface** that surrounds your treasure. it is not the WALLS of the building. It is the ways to get in. It is called ... **Attack Surface**. 


The key to security is to make the **Attack Surface** *incredibly* **smaller**...


Next September, we will see how easy it is to enter places, hwo to get people to do things for you because they do not believe you are a bad person who showed up at their work. If we play it properly in NS, people here are friendly and chatty. 


Physical access

Social engineering 


Both work excellent


With training, the **attack surface** will get a lot smaller. We are learning how to protect our networks. We are learnin g about Endpoints. We will have an assignment where we will play with the Endpoint Protection software that he has developed. 


Be cautious of people you meet online or in person may have ill intentions. DO NOT DO THINGS THAT EXPOSE YOU TO BE COMPROMISED. 


Saying something to an alcoholic not to be an alcoholic is difficult. But it is very doable to follow common sense information. Be aware of Sextortion, as the deeper we go (in terms of a position in life), the more we would be targeted. 


DO NOT RELY ON THE HUMAN FIREWALL  (where you train people enough not to do silly things, and rely on them to be the walls of your castle)


Aristotle : "We are weak willed , well intentioned creatures"


If your boss is refusing to do something in terms of security, and it is something fixable, it is best to get out of that company ASAP because the responsibility will not be on him. 



Create a Neighbourhood watch for IT, but do not rely on it for everything. 


Make it difficult for your people to do the wrong thing. 


You should not be able to access something that is not critical for your job, or at least to be able to read it but not edit it. Make it hard for threat actors to do something wrong. 



POut a safety net in a way that does not interfer with their job 



Confidentiality : We keep secrets, we have systems to allow us to keep secrets 
Integrity : if we can vouch for the integrity of the system/data, we do! if we can not , we do not! We can not say everything is ok. WE have to personally vouch that something is secure and correcty. 


If wondering if a database is compromised, and they have happened to be on a outward-facing MySQL with a vulnerability, I would not trust it. 


Availability : People want to work everywhere at home or on the bus or on vacation on their phones, tablets, their kids' phones, and want to have access to EVERYTHING, even though they do not need it. They do not Want to sign in to a building. They do not want to be rude to people, where a social engineer is most likely to succeed. People should not be fired for doing this, but there needs to be consequences suych as training lots of support, and a letter of discipline on their file. Approach them with compassion. Find a way to help them if they are not doing their job. 



Databases : What we should have, we do not need ALL The information. Just have the information you actually need. If we have a database that is publically fa ing, make sure it is not suspectable ot SQL injections. 



How many installed a video game at home, and part of the installation, it mentions that it is going to open a particular port (change that port!)

Have a non-standard port they cant scan for. 


Web : You have to have well-tested systems. You need a professional to create your website. If something is not sensitive , go for it. If for an organization, this is facing the outside world. We have to test it, and we have to try to break it. We do not have to be web designers, but we will know the individual components to break them. 



All of the attack vectors we will learn in this program. He asked earlier "why do we teach you these? it is just so we can spot weaknesses where others cant"



When we are on a job, and we find an employee leaving their station open, they should be punished. 


If someone violates policies according to security, and they are fired, it would dissuade others from reporting. We need to have a safe reporting environment. Every person in the organization have to be a valued member of the security team. If the penetration tester comes along, there might be a letter on your file, but they do not name specific individuals in their reports. 







#### Small Assignment : 


ATV Model of Risk :


In order to have risk, you must have **assets** , **threats**, and **vulnerabilities**.


If we can remove *one*, we eliminate risk


If we store credit card info, and attackers are after the records, if we do not store credit cards , we have NO risk. 


Asset                       Threat                                     Vulnerabilites

My life                     Falling+Dying                        Broken board                        
(it is what it is)                                                        (Repair the board = no risk!)
--------------- Bridge ------------------


If there is no vulnerability, there is no risk



If we have a software that has an uppatched vulnerability, we have risk, so we patch software to eliminitate risk 



If we have assets (data), hackers and vulnerabilities (attack surfaces), we have risks1

Key : It is our duty to manage risk.  


There is risk in everything we do. We can not live in a cocoon. 



If we can avoid the risk, it is good  (if we do not have to cross the bridge, store credit card info , ... we can avoid the risk)

- Not having the treasure that someone else wants --> eliminates risk. 

He found bottles of mixology liquors, and stacked them outside, would there be a risk ? 


How important are those mixing bottles? 


We can take all these actions to reduce the *probability* of risk. It is not difficult probability math .


We give things a **Risk score**


Risk Formula = Probability of Event X Impact of the Event


                       =   (0-1 , if 10% 0.1, if 50% . 0.5, max. is 1) X (Consequences)   (Hurricane with a force 5 warning label hits Halifax's harbour , it is terrible)


We can use **Qualitative** methods : Really terrible damage (meh -  really bad)


Or we can do **Quantitative** method : We can measure the risk from 0-10. 

What is the probability of a force-5 hurricane hitting Halifax's Harbour ? never 0, as it could happen. It might be 0.000000000000000001 but not a 0. Tropical storms hitting this weekend, some hurricanes , we can say "0.1 or 10%". Impact 


So : 
Risk   = Probability X Damages

> Risk = (probability being 0.1 ) X (rate the impact from 0-10 = 10)
>          =   1 (Low risk score)



How do we get the probability of a Force-5 Hurricane? we made it up! From knowledge and experience, collectively we could agree that it is 10% or lower. We do not have experiments, but we have our knowledge of the climate of this area. We came up with a guess, and in risk management, qualitative risk management is acceptable. 



Based on what we know, if we are running a hospital, what is the probability of getting a ransomware attack? 1 ( it is bound to happen). If a hospital needlessly stores extra information, it is devastating. 



How many hospitals are paying attention to ransomware attacks ? not many. 


We should have good offline backups, not mapped to a network drive. We should have encryption. We would have no emails for the employees. E-Mails are huge attack vectors. Not everyone needs emails to do their jobs, but they are given to each employee. The threat actors come down this road, and subconsciously, everyone is putting their most important assets on this road. 


How do we know the probability is 1%? Based on the knowledge each of us have currently about cybersecurity, we base this on our expert opinion for a qualitative assessment


If we buy a hard drive, we would have stamped on the surface of the hard drive (MTBF : Mean time to core failure. This was a quantitative measure, which means there is math behind it. They take hard drives , they run them continuously until they fail, They do this for thousands of drives, they take the average from all these drives, and they reach this number ... Quantitative Risk. )



If we are comparing drives, we should decide on the drive with the lowest MTBF if the information that will be stored on it will be critical. 


The probability of the event of having the hurricanes based on 100 years of Halifax data = 0.4 (quantitative , based on history )

or : REALLY BAD …. (qualitative)


Actual risk score = 0.4 X 100 (terrible damage) = 40% (Bigger storm drains, better bridges)


Ron has a friend who is an electrician, where he would pay extra fees to bury the powerlines that lead to his house. Hurricanes can rip off the electrical cabling, in his case, he would still have power, but others would not. Ron had a tree tangled on his powerline. The power company mentioned that this is the home owner's problem not theirs. 


R  =   P   X   I



Spread the risk around ! Do not have all the critical data on one machine! 


Possibility of staying up and running : %99.99999 ( phone companies have to have 5 9s reliability. Why? If a natural disaster happens , such as a tsunami, we have to be able to recover from an area that was not affected). We need a **Live Mirror** of a critical system 


At TONS, they did a NS Power Redistribution Center.  There are a series of monitors, and the room is dark. It is a curved little building ( built to survive a bomb blast) : a movie screen showing live information of electricity in the city. They had a massive machine, and they had an identical machine that mirrored live whatever was happening on their main machine. The other machine was right next to it. This is not smart. 

Risk assessment is ALL about prioritizing your time. 

Next class : avoidance , reduction , spreading , transfer, elimination  and acceptance. 
