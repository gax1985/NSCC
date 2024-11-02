

### Risk Acceptance : 

	What is an acceptable level of Risk ? 

	If you accept a risk, it has to be an acceptable level of risk. 

	If the value of the protection is less than the cost of the asset


### Risk Mitigation: 


	Cut down on the **Impact**, **Probability**, increase the ability to interrupt the attack , etc


### Risk Elimination :

	Example : We do not have to hold onto the credit card information. All we need is the "All Clear" Signal from the Bank





Risk Formula = Probability X Impact 

= The chance of something happening x the result of it happening







When we are dealing with **Detection Systems**, like IPSes or something that is so simple as showing your ID card to a guard at the door, a motion detector in the hallway, there are four possibilities : 





####  True Reject (*True Positive*)  

Someone is using a fake ID, detect it , and prevent them from entering 

Motion detector goes off in the hallway, and we chase the intruder 


#### False Reject ( *False Positive* )

The IPS system goes haywire over nothing 

Motion Detector goes off due a Racoon 


#### True Accept 


The traffic goes through your network because they are permitted in , and it is legitimate

#### False Accept --> Our Primary Focus of Attention

A fake ID is utilized successfully due to a guard not noticing it

	It should be as close to zero as we can get!

"We have the lowest level of False Positives" 

	It is a time waster
	It is irritating
	If you get too many false-positives, you will either ignore the genuine signal entirely, or you turn them off!
	
	Example : 
	
		You are getting alerts (100s) that are all false-positives, the response to these alerts will change! You would start looking around for systems that reduce the false positives. This is the worst way to go!
		
		Our focus is False Accept!



Before Doing an Vulnerability Assessment, 

True or False to include : 

1. Engineering Drawings : 
   
   If we are discussing ways to get into the place, we should have as close to possible to the absolute truth. We have to know every door , window or hatch 

2. Number of individuals in the facility :
   
   Chance to blend in is easier between 100 employees as compared to 5 individuals!
      
3. When you Open and When you Close : 
   
   We should know when and who should be there. As partr of the vulnerabiltiy assessment, we should go on both times 

4. Where is the goal? 
   
   Does the villan keep the diamonds in the safe? you must know where the assets are, and in terms of vulnerabilities, where the assets are kept.
   
   Knowing where the asset is stored is essential, because we have to judge whether it is kept in a proper place. 
   
From Ron's previous contract : 

   All the backup tapes are kept on a shelf for the system administrator's office(Ron's office) ( for a government institution). Often, the door would be left unlocked. 


When finishing the vulnerability assessment, and when you have a complete report for the client, we have to do *what the customer wants*. It should be encrypted, and whether we have a copy on file for the customer depends on their wishes. 


Is there a difference between a Risk Assessment and Vulnerability Assessment ? which is done first ? 


We do  the Risk Assessment first to know the risks : 

1. What are you trying to protect? 
2. Why is it important ? 
   
   If someone has an item for sentimental reasons, such as an old phone, there is no threats by losing it. If we are holding on to important tactical information, are there anyone who would be interested? the threats are extreme. Determining the threat tells you something important : we have to base our strategy on the level of threat. The defense system to protect an asset has to be extremely sophisticated, because you have to assume the adversary is better than you in every way!

If you are building a data center on the lowlands by a river, it should tell you to place your assets on the top floor ( the threat is water for example ).



Our houses are designed with low security. There will not be a SPETNAZ team breaking dow your door. We have to reference the threat. 


Ron is concerned right now, as there could be a very serious conflict in the Middle East. If that happens, it can go multiple ways (including attacks on Canadian soil). Halifax used to take security very seriously, and then suddenly people stopped caring. Ron is concerned about the possible threats to Canadians right now.


Physical Protection System (PPT) :

Should the following be components of a Physical Protection System : 


Interior / Exterior Intrusion System

Alarm

Access Control 

Communications 

System like PRTG ( to represent the information  ) : if we monitor network traffic, the data needs to be displayed in a manner people can act upon it, so if it is presented , we can act


	Possibility Of Hurricanes (Part of Risk Assessment = Asset  vs Threats. Then do a vulnerability assessment. Risk assessment becomes before the vulnerability assessment. Do you need to prpare for russian hackers >?

	Physical Protection Systems is not part of *weather*. The *Weather* is part of the Risk Assessment


	Open Close times : Hours of Operation. --> Components of Vulnerability Assessment. The physical protection plan should not have OpenClose Times, as it is part of the **Vulnerability Assessment**


If an alarm goes off, What is the capability of a system? low security -> impede. Medium --> Impede and Detect . What caused the alarm? You look at the area related to the alarm. 


We are putting in some sort of access control system. When entering a building, where you have to swipe a card, talk to a security guard, there is something very important about every security control, the point of avoidance is having a security control being unnecessarily annoying to use by those who use it, avoiding long unnecessary processes involving it. If you are a Systems Administrator, you can live with it, for us though, we have to break it. The security control would be annoying on a daily-use. If we unnecessarily interfere with the user's ability to do their job, they will *find ways around it*, causing **Undocumented Vulnerabilities**, or **Undocumented Access Points**. People would get some access points from walmart, and then adding it to their office without the Systems Administrator knowing about it. The Access Points were common in smoking areas. Ron looked at one faculity, where there was a groundskeeper shed, where he has kept their tools, computer and other necessities. The local administrator for this faculity stuck a Wireless Access Points for the groundskeeper. Ron was able to get into the core network from the groundskeeper shed. The only security was a padlock. People find ways around security measures, and we would have to discover it. 


Any detection systems , one of the most important performance measures of it is not just the *False Acceptance* that concerns us (the weakness) , b but the best feature of an Access Control system is the probabilitty of it detecting what you are trying to prevent. Ron had to tune the area that the motion detector covers in the backyard. He kept aiming the sensors , walking out in the yard , and adjust its ability to do its job. If we have some sort of antivirus system on the end point, we all know that 1990s antivirus' probabilitty of detection is very weak. 

Any type of access control system the mosty important element is its **Ability to Detect**. 


If we do walk straight at a motion sensor, it might be possible to bypass it. 


The ability to detect is one of the most important features. 


As we read through the chapters between now and wednesday, focus on the chapter and the notes. 


One of the biggest problems in organizations implementing security, back in the early 1990s, Ron had a client where he could take video images from security cameras, and in the event of a bank robbery, the cops needed the feed from one camera, capture a still-image and then send the photo to newspapers . Police would come with tapes from the bank, cut the frame from the camera, and provide it to them. The quality is terrible. Ron talked to a bank manager, and mentioned he could do a system that provides a clear image of the thieves. The manager declined. The manager mentioned the cameras are there because of the insurance company's requirements are met, regardless of the camera's ability to capture the image of the theives. 


There is a big difference between a Compliance Audit and a Security Audit. 


#### One Note

When dealing with **Incident Response**, where the Protection System includes a *Response Element*, there are levels to Response : 


1. a Low-paid security guard 
2. Soldiers with assault rifles

The only thing we have to determine with **Response Systems**, from a digital perespective, when the antivirus detects something bad, Intrusion Prevention System would take actions to quarantine the virus , block the network traffic, and **ALLOWS THE HUMANS TO MAKE THE DECISIONS**. 

The main difference in Response Systems is thinking about whether thety are **Immediate** or of they **have a delay**. Do we do something right away ? or do we allow an assessment period? Consider not having a guard on the premises, and having a contract with a security company instead. There would be a difference in terms of time/response.


Chapter 2 is the most important chapter. 


After the quiz on Wednesday, we will get into the next chapter , Chapter 6 : Electronic Elements. At Early November, we will build them! 



