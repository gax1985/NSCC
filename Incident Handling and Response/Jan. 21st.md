


Ron wanted to talk to us about using **Equifax** as an example. He goes into greater detail into the **Equifax Hack** in his Law class. It is an example of everything you can do wrong in the event of an incident. 


#### Example of What Not to Do ...

**Equifax** is a **Credit Reporting Agency**. It is used to check an individual's *credit rating* when purchasing a car or a house for example. 

#### How do they do that ? 


The credit rating depends on a few factors : 

1. Where does your money come from ?
2. How do you spend it? 
3. How do you deal with your credit health? 
4. Do you have any loyalty cards? 
   
   
They have the ability to know how much you are spending to a fairly accurate degree. They track purchases and loyalty points. Because it is personal files, they have a lot of data as well. They contract with Payroll companies, just so they would know your income. Payroll is frequently out-sourced to a third party. Equifax keeps track of everything you are making, how much you are spending on your credit cards , your payment history , etc. They are in an excellent position to report on your financial health. They come up with a **Risk Score** connected to you, and they should be concerned with the manner of how you handle your finances. 


##### Timeline 


###### Nov. 2016 


White Hat Hackers often do their work to analyze organizations' servers for a reward. They set up a server that bug bounty hunters can investigate their systems. One White Hat Hacker discovered a **Forced Browsing Vulnerability**, where a sub-folder on the server could be accessible by typing its name in the address bar of the browser. You would enter common names of folders. He is anonymous, and sent a message to Equifax about the vulnerability, and provided instructions on how to fix it. The hacker mentioned public information is accessible. Equifax chose to <u>ignore it</u>!


###### March 2017 

**The Apache Struts Vulnerability**


This vulnerability opens up your servers to the world. You would have to upgrade your Apache installation after taking the server offline to remedy the issue. The reincarnation of US-CERT, which manages and monitors servers in the US, they indicated the vulnerability is currently present in all publicly-facing servers. They indicated that they should fix this issue right away. The person who handles the IT division was tasked with doing testing for the **Apache Struts Vulnerability**. They asked him to scan the network with Nessus to detect if the vulnerability is present. He did not update Nessus, or updated his patches, and he has not used Nessus for a long time. His version of Nessus was incapable of detecting this particular vulnerability. He was not familiar with the micro-segmentation of Equifax's network. He left out the segment where the vulnerability was present on many of its systems. He then thought the vulnerability did not exist. Equifax decided not to do anything. 

Few days after this vulnerability was launched, a massive hacking group penetrated Equifax's systems. As they usually do, after getting inside the network, they did Enumeration and Reconnaissance. They hit a gold mine. They had the records of a 160 million people, containing everything you would need to become this person. The hacking group decided to take it all, but do it in a way that they would not notice. They decided to take their time, and decided to sneak bits of information out of the network on busy times, weekend times , and other times. They did that between March and the end of June. One of the places they were uploading the information to was based in China. A security technician started asking the question " What businesses do we have in China?  Traffic is going to China". Equifax looked at their systems in early June, and thought if they have received any information regarding themselves being vulnerable. Noone mentioned Apache Struts, but remembered the email from November. They also started digging into the Chinese traffic. 


Somewhere in the middle of June, one of the individuals investigating this case. If we are doing an assignment about breach responses in the public and private sectors, we have not covered the laws about a publically-traded company. If you discover something that would affect the trading value of the company, you have to stop share trading for the company's share, and the share holders have to decide on the appropriate action to take. An employee thought they should short Equifax stock. This employee was an Incident Response Investigator. Shorting a stock is the individual agreeing to sell a bunch of stocks at some future time, and you do not have to buy them yet. You are selling at today's price, but you may have 60-90 days for you to purchase them. You are hoping the value of the stock will go down drastically. 

After they fixed the vulnerability in June, they went deeper into the investigation. The Chinese traffic was very suspicious. 


###### July 28th 


The senior CTO went to the CEO and mentioned that they have been hacked, and someone stole a lot of private information. We fixed it, but we need to do something. The CEO called in the FBI, asked the FBI's Cyber Incident Investigation Team to investigate their systems. They had a massive legal department specializing in contracts, they contracted a legal firm geared towards assisting clients to help with breach response. 



###### August 1st 


Most of the C-Suite (CFO, CTO, CEO), dumped as much of the Equifax shares they had as they could. They had limits on the shares they could sell, and maxed it out. All the sales had to be approved by the Chief Legal Officer. Within 24 hours, the legal team signed off on all the trades. He was wise. The company had their quarter start in August, and there was a rule that said "  if you are going to sell shares in our company, you are not allowed to sell them for a while". They had a maximum amount of shares to sell. They were advised to sell the shares they wanted to at the beginning of the quarter. The legal category where they had inside knowledge is "Identity Theft".


###### August 15th


The CEO made a presentation to shareholders. The meeting was established with the CEO as the guest of honor. He made a speech, and did a couple of things in the speech. Any type of material change you know in the company would cause few actions : Stop the sell, tell the public, and start trading again. The speech was aimed to comforting the public about the health of the organization. He mentioned that they sell services protecting against identity theft. If you happen to be breached, you pay a monthly fee and they would monitor transactions on the credit card. Also, he mentioned that they expected this market to explode. 


###### September 6th 


They stopped trading and reported to the SEC that they lost all this data. The CEO accepted the responsibility and resigned. Because he resigned, he kept his executive bonuses that he would get. If he was fired, he would not get that. He volunteered his assistance to help out with the crisis. The interesting event that happened is that there is a particular US senator whose biggest campaign contributor is Equifax. He introduces a bill in congress to make it impossible for a victim of  a data breach to sue the company. If the personal information was lost, the most they would get is $200, and you would not be able to sue them. A reporter thought this would be applicable to the Equifax hack, and investigated the senator. They realized the senator was deeply connected, and the senator withdrew the bill. Any investigative entity started opening investigations about what happened. Congress was receiving testimonies about the hack. This was during Trump's reign. His Attorney General shut down the investigation pertaining to Equifax. The latter said they are very concious to the threat posed to their customers, and that they were going to offer their clients identity protection for a year for free, dependent on the client signing a contract agreeing not to sue the company, and after the year, it would be $20 per month. Clients brought this clause to the media, and Equifax said this was a cut-and-paste error. They reproduced the agreement to remove this clause. 160 million individuals lost faith in Equifax, and they decided to go to another company to get Identity Theft Protection. The other companies were re-selling Equifax's protection services, and most of the money went back to Equifax's pocket. The SEC noticed that in June individuals shorted the stock, the CEO receiving the report of them being hacked, and the C-Suite individuals capitulated on it. They interviewed the executives in the C-Suite, and they claimed ignorance. They denied having any conversations about Equifax being hacked. They brought in the chief legal officer of the company who signed off on the sales, and they also claimed ignorance. The investigators mentioned the CEO hired an external law firm specializing in data breaches, and the chief legal officer again mentioned that they were not aware about the breach. They just mentioned they just discovered there was an investigation. They claimed they did not know the right information about who exactly got hacked, and other information. They did not want to report incorrect information to the public. They mentioned that they were not aware of the crime in regards to this incident, and that they resigned protecting them. They went against the Sarbanes–Oxley Act. If you have an organization with multiple branches. If the accountant embezzles funds, and the CFO signed the report agreeing to the embezzlement, they would face possible jail time and 10-million-dollar-fine. This law came into effect due to IMRON's incident. Anderson Consulting was one of the biggest five consulting companies in the world. They did their auditing of annual financial statements, business development in other companies. Anderson was completely complicit in every aspect of fraud IMRON did. Anderson called the staff, and they started shredding and burning documents. The Sarbanes–Oxley Act says that if you knew about someone embezzling , you would face a 20-million-dollar-fine. The IT person who shorted the stock in June went to jail. Someone had to be the sacrificial lambs. If you were concerned if your information was breached, they set up **Equifax Security**, which would produce a report mentioning you were breached. a White Hat Hacker set up another page called **Security Equifax**, and they would enter their information on the page. Equifax's communications communique mentioned in error the white hacker's page was the site to go to. Since the time Trump's people got out of office, there were more investigations afterwards. 

>[!question]
>
>If the C-Suite person who was responsible found out and advised everyone to keep quiet, would that absolve him of responsibility because he quit? 
>
>>[!answer]
>>
>>No!



#### Testimony


Elizabeth tried to run for Democratic Presidential Nominee. She is an awesome senator. Every committee and investigation she gets involved in had her be the most knowledgeable person about the subject matter. If the senator is facing a horrible question, the response was always a sales pitch (security services). The clip from YouTube is Elizabeth Warren's questioning of the senator. Recall the ethical frameworks from the other class, and the bubble surrounding the senator pertaining to the effects of their actions. 

Mr. Perdue : Under Anti-Trust laws, you are required to talk to eachother following a cyber breach. 

Senator : We talk about issues and trends in Cybersecurity 

Mr. Perdue : Did you talk about the incident in March ? 

Senator : We did not know enough about the incident. 

Mr. Perdue : Senator Cardon and Senator Blanc are working on a Cyber breach law. 

--

Credit Report Freezes 

Mr. Perdue : What methods would the consumer go through to discover evidence of their information's theft? 

Senator : 'Sales Pitch'

Mr. Perdue : What would you advise your successor to deal with this issue ? 

Senator : We need to regain the trust of the consumer with this 'sales pitch'. 

--

Elizabeth Warren : The whole thing is staggering because you knew about it months ago. It has the worst data security, when it should have the best data security due to the sensitivity of the data. "Fraud is a big opportunity for us". Is fraud more likely now before the hack ?

Senator : Yes it is !

Elizabeth Warren : Then this is a big business for you. You are gaining profits based on it. 

Senator : Sales pitch 

Elizabeth : ... they have to pay 17 dollars a month after the year? That is 200 million dollars of revenue for you based on your breach. Lifelot is selling Equifax's services, and funneling the profits back to you. Equifax is selling products to businesses and government agencies centered about protection against identity theft. 

Senator : We are no longer selling consumer products directly .

Elizabeth : You are making money off this. Equifax sells products to business and government agencies to prevent fraud ? 

Senator : We do not sell to businesses, and if we do, the services is not about fraud. 

Elizabeth : The potential cost for Equifax is shockingly low. Equifax's insurance should cover a large amount of the payments needing to be made to consumers. Equifax through four years had a number of hacks. Has the profits gone up during these four years? 

Senator : Yes. 


Elizabeth : Incentives are out of whack. Consumers now have to worry for the rest of their lives about credit theft. Consumers are trapped. Equifax did a lousy job of protecting the data. The industry should be completely transformed. Consumers should direct who has access to their data. The company should pay mandatory fines on every bit of consumer data stolen. 




We assume when dealing with large companies that they are taking care of the data, and they have smart ethical people who do the right thing to prevent incidents from taking place, and report breaches when they do happen. This is a *fantasy*...


This is one of the reasons why Ron wanted Ethics to be added to the program. There is a bigger picture. You do not want to find yourself standing infront of a provincial or federal committee trying to crucify you. 


#### The Sarbanes–Oxley Act


The law itself is fine, and everything you need is in place. There was a "We do not care which political party is in power" attitude. The Republican Party was in power, and shut down investigations pertaining to them. 

Ron mentioned an example where the president and key executives have done something *terrible*. Ron followed the bylaws for the company, put the actions in place to correct the situation, and the term of the Board of Directors was coming to an end, and they would all be replaced. In order to facilitate the communications and changes to correct the situation, the C-Suite had to take certain actions. They refused to do it. The time of the board expired. The people in power chose not to follow the rules. They can be sued, but law courts are tedious. It is uncomfortable to go through. It is wise to walk away from a corrupt institution. 



1. Build your team, equip them, and train them!
2. Know your responsibilities when it comes to the laws in question, and make sure you read the legislation. 
3. Test your systems! Have some real hands-on experience with that aspect! 
4. Start becoming familiar with **Security Onion**. 
5. Prepare your systems and your team.
6. Respond and Post-Mortem : Forensics.
    
>> [!important] 
> There has **not** been any evidence of Identity Theft being conducted based on the Equifax data. It was done by Chinese Intelligence for intelligence gathering.  

>[!todo]
>
>#### Lessons 🧑‍🎓:
>
>>1. Do not ignore your responsibilities in front of evidence of a breach, regardless of how slim the evidence seems to be. You need to be a better detective. We have seen shows where the detective gives up, but the hero of the story *keeps going*. 
>>2. You have a personal responsibility in protecting the data. 
>>3. You have an ethical fiduciary responsibility to the people you are protecting.
>>4. If you end up in the *sacrificial lamb* seat, you should do due diligence in knowing what you are facing, and present well-documented evidence to support your case. 
>>5. Copy your interactions to a safe place!

>[!warning]
>
> ... If you are getting an email that sounds like someone is phishing for information that would implicate you ... 
> 
>>	Document your communications!
>>	Document your evidence!
>    

>[!danger]
>
>We have **two outstanding assignments**!


