We have a treasure for our organization. Picture a **Circle**, with the treasure inside. The barrier surrounding our organization is referred to as the **Attack Surface**. Ron did a lot of work on Virtual Modelling, and a haptic system that you touch things that are not there. His system was to wear a devide on your hand and touch thhings that are not there.


Imagine poking a hole in modelling clay. in a virtual reality environment, you poke a hole. There is no mention of what happens to the clay. In Ron's system, something has to happen to the clay; the material has to go somewhere so you can model things. 

It was difficult to find the edges of these things in virtual space. In virtual reality, you see them. In Haptic Reality, you touch them, and you feel a vibration of something you can not see. 


How do you define the surface of an object ?


You move in a direction and you encounter something. You have to know whether you : 

1. Hit It
2. Approached It
3. Passed It

If you consider the line of direction and how much force you have exterted. Force , speed and direction would mean a **Vector**.


To determine the surface , you have to test all kinds of vectors. If you get enough of these vectors to the point of having no distance between them, you can then define a **surface** (defined surface). 


The circle is the Attack Surface of an organization. It should NOT be interpreted as a physical surface. The surface and points of contacts of the surface that the attacker can encounter exist wherever your assets are!


It could be a laptop in a coffeeshop, a datacenter, a server in the cloud, a door into something ...


All the points of possible contact define the Attack Surface. Unlike a physical surface where you feel around to find its shape or its definition, the Attack Surface could be anywhere!


The points could contain information, and not necessarily a point you penetrate. Each possible point is an Attack Vector. 


When someone is going after an organization or an individual, you can spend a lot of time in reconnaisance. Anyone who has done this professionally will say reconnaisance takes months and months ... getting to know everything about the target, finding every trace of them on the internet ,...

In DEFCON, you would meet people where they would spend a year on a new Firewall. They would buy it, test it , fire at it, look at all possibilities of failures and mistakes. ... 


Ron has not seen any that can not be compromised. They would discover a chain of events that would create a buffer overflow. When you watch it, you would think that you understand a bit about what is happening, and you get a high-level understanding. It is like watching a Physics demonstration, and 
you skip all the math. 


We have seen it generally in Network Scans, ports and services on a machine, but people who do this for a living spend much more time on these things. Ron told us a story of a client he had who had commercial wireless routers in the organization that wwas produced with firmware which developer
made a mistake of having a backdoor, activated by sending a chain of characters or bits to the router. The client had to rip out the routers and replace them with routers that did not have this attack vector. How did the person discover that ? imagine all the work that went into it. Consider the number
of hours necessary to do this. This is the depth of reconnaisance that Ron is talking about. You usually do not spend that amount of time in Red Teaming ; you are looking for standard physical access , networking access. ... most of what you would do for that router is to research it generally. You 
are not trying to find this vulnerability. This is why it is fun to go to these events!


Ron was chatting with a friend in NYC , and this friend is studying a Masters in Cybersecurity. He mentioned that the best way to meet people in Cybersecurity was to :

1. identifying people/systems that would like to emulate, get to know better, understand them better, and become friends with them 


    for example, one person that Ron met was someone who was doing a PHD in Georgiatech, and he was gifted at combatting Botnets and detecting them. He liked what he was doing, and what his company was doing. He identified a conference where he was speaking. At the end of the session, he spoke to him
    and realized that they both had the same supervisor. He met a lot of people through him. Ron would go to specialized conferences and everyone there had fake names, and they all knew Ron. Finding those skills and meeting these people is one of the best ways that you can expand your knowledge
    and your experience. It is another excellent way of introducing yourself to your industry. You would not graduate with full experience. You are doing two years of basic training. It is just enough knowledge to get you started. The next five years is up to you. Some may choose to do a degree, self directed
    learning, pursue certifications ,.... the most important thing you can do is to get to know the people and the techniques on a personal basis. 

2. Think of the areas you are ineterested in this year. Look for accessible conferences and go there. We are lucky that we are close to Boston NYC, and other parts of the US , Canada and the world. Find events this summer. If you get a job this summer, mention that you are doing serious professional development, 
and I would like a commitment from you to attend this conference that happens every year. They might smile and be happy that you are this sort of person. As we go through these courses, hone in at what you can see yourself doing. Find whichever area of Cybersecurity you are interested in. This is tough to explain,
but the path to go wherever you want to go , in being respected and gifted in the field, is much shorter that you think. 

Ron was interested in politics, and he found a nominee in his area from a particular party. One year later, he was sitting in a luxorious home with the top 5 individuals in that party, as well as key financial backers of the party. All it took was the commitment to do it! Most people do not do *it*. 


"I want to be the Lead Penetration Tester in Mandient". It is about getting off your ass and doing what you want to do!


If you want to do recon, take the vector you are looking at and study it intensly. Figure out what are the vectors we want to consider ? 

1. People : you will focus on an organization you want to get into, 75 percent or better of successful attacks happen through the *people* of the organization. What kind of things we are doing in regards to reconnaisance for people ? understand the people. Phishing emails are the last thing . Find where they work , 
their schedule, where they live, who their friends are, what they do in their free time, what clubs they belong to, what is their religion, what do they like to drink , etc ... everything you can find out about them is helpful. You might decide at the end of this stage that the way to get into this person
is a Phishing email. If they are a runner competing in running events, and they competed two years ago in a race. You create an organization and an identity online "Marathon Organization Team" and you will send them an email saying " Based on your participation last year in the race, you have been granted 
free membership ". It is tailored to them specifically based on who they are , organization they belong to, and it is engineered for them to open it and trust it. 

2. Network : if you consider a network attack, what are sub vectors (hint : public facing)? 

    1. VPN access 
    2. a Website  
    3. Their actual endpoints : home computers, WIFI , IoT devices ( used in sophisticated complicated and successful attack. There was someone at DEFCON of hacking a major energy company through a consulting engineer who had a blog saying about his early adoption of cool technology, including a stove
    that he connected to his home wireless network, and found a way to connect to the stove remotely. He hacked the stove, managed to get through the home network, and then the laptop. The hacker demonstrated hacking the energy company live, and got into trouble). You can start expanding this out. You can
    break it down into separate vectors :

        I. email 
        II. cloud
        III. DNS 
        IV. Physical 
        V. Social Engineering (aka phonecalls) : who can name a hack last year due to a phone call ? MGM Hack. You can find a hundred successful attacks by someone making a phone call. How do you clasify it? in people possibly? Ron mentioned that he went to an event of focusing on a HR office in a company to 
        find out when the new employee is starting work at the office. There is nothing more important than knowing your victims better than they know themselves. If you are going to be a Network Administrator, you will have to Know Your Network, even if it means following teh cables in the ceiling, protocols used 
        by every device that you have, are there any open SSH ports that an employee left open? anyone you hire for an organization for this role is expected to know the network better than you do. Everytime you think about Attack Vectors, think about "How can I understand this vector better?". If you send an phishing email with 
        a malicious attachment, such as PDF containing mnalicious code, office document containing a macro, does their OS is at a level to detect these things, how likely is it to detect it? this takes TESTING. They use Bitdefender for example, you duplicate that on another system, send an email with the malicious attachment, and 
        see if it works. Reverse DNS is part of the email system that assesses whether the domain that the email came from is consistent with the servers that are expected to send the emails from the organization. DNS inquiry goes "Does this sender match your records for an ordinary sender from that organization?"



    ## First Assignment : 
    #####################

    This has danger associated with it. If we do it wrong, we can end up in physical difficulties. He wants us to feel the necessity for Doing Everything Correctly. The details will be provided in handwritten format. He has to add warnings to the assignment because of this. In Penetration Testing, Intelligence work,
    Investigations, and personal safety, you may not want to be using your actual account. You would need to create multiple fake personalities online. There would be nothing in the profile that ties back to you. Ron had a friend well-known internationally, whose social media accounts were a of a rice farmer in Vietnam. 
    Everyone who knew him knew to message this profile to reach him, but there was nothing in the profile that pointed back to him. You need New Identities. You need a basketload of new identities that will be useful to you in your career. You may want to be a 55-year old woman, an 80 year old farmer, you especially need it on the
    Dark Web. If you are going into intelligence, your adversaries will have the greatest capability. Never do something with the expectation that they will not discover it. Your greatest treasure is YOU. If you are going to the Dark Web, it might mean the safety of your lovedones. We are not ready to do this yet. The knowledge
    you gain will be your greatest aid. These fake personas have to have a history and a life. Shortly after you graduate, maintain these personas. Ron had a student that did it really well. He imagined a character who will be used as a lure for his victim. He left the persona online, and on the anniversary of his fake wife's death,
    he ended up getting a lot of creepy and funny emails about loss and love. 

    For this assignment, which will take the month of January, we are going to identify a victim in a real company somewhere in the US. Choose a company based on a role such as Aerospace etc : you will identify an individual who would have access to key information in the company, you will study this individual thoroughly, once you
    understand this person completely, you will build a set of social media profiles to use with him : Facebook, X , LinkedIn , etc ... All these social media companies had put a lot of effort to keep people from doing this. You will have to figure out a way to deal with these limitations. You would most likely need a picture :
    How do you come up with a fake picture? AI , a person who does not exist , ... they are not stupid , they are working on ways to deal with these techniques. Dead people will not complain. You can get online virtual phone numbers that can be generated. You will get so far into the Rabbit Hole, that you may have to back up and research someone else. 

    You do not want to be detected, you do not want to show up yet on a recommended friend , if you do it correctly, your online social media profile WILL be recommended based on the algorithms. Ron was comparing algorithms with friends : call up facebook, go to the reels : see what you get for reels vs what they get for reels. 

    A few of his friends had an identical reel : Family Guy  , etc .. one friend had one where it was about not showing up in the reel. That is difficult. 

    1. Phone Number : Not for this assignment, but this is for your career. (Question : If we use a real number from a business? no, as they will find that out soon). Your adversary on the Dark Web may discover where the phone is sold. If you have any friend in NYC, these states sell burner phones still. 
    You will want to do everything through a VPN. You need a country outside of the Five Eyes with NO LOGIN. It needs to be no logging. You need an email that falls along. ProtonMail triggers alarm bells for social media. You can not tie your home network or school when generating the phone.
    
    2. VPN : You can not establish a social media account via a VPN.


    When establishing a social media account, go to a public WIFI outside of your home. Avoid anything that can be traced back to you, such as Public Airport WIFI. Once you have your account established, everything would have to be done in the anonymous VPN. 

    MintMobile sends a SIM card in the mail. LuckyMobile , swapping out a SIM card , or buying a burner phone are essential. You erase all breadcrumbs back to you, your home , your school or anything associated with you. 


    Possible Mistakes : 

    Next Class, he will release the paper assignment . He will go through much greater detail about the mistakes that you will make. This is practice!


    Example : If you are going after someone who is at a current university, do not create a social media account or be anything associated with their friends or location or school. They could ask you details about something you know nothing about. 


    Example : Someone who works as a scientist, and she offered mentoring for entrepreneurs interested in the cosmetics industry. This fake person graduated from a school.  Problems ? They have no idea about cosmetics. She changed her mind to a business program, but her knowledge was limited in 
    business. She decided to start a small-business about cosmetics at home, and she wanted information about marketing, trends of the industry . It was a perfect match to the person being researched. The profile was believeable with a bit more research, and able to send an email with that person, and send a malicious link to get into this organization, 
    and if that is not possible, to actually meet them. The scientist was researching advanced vaccines. 

    


️️