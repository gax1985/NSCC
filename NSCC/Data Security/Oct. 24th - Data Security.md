


# 0-Day Privilege Escalation on CISCO Devices 





> [!info] 
> There are a lot of hacker groups that exist around the world. They may set up an exploit on a vulnerable system, and another hacker group comes in, and utilizes it. 
>  


> [!note] 
>  Check out the following link : 
>  
>  https://cve.mitre.org/
>https://attack.mitre.org/
>https://www.cyber.gc.ca/en
>
>These  websites will be part of our studies and careers. It would be helpful to arrive to work early, and to check out the mentioned websites to keep up with cybersecurity news


Hacking has a few phases, each with their own special techniques : 


#### Exfiltration : 


[Exfiltration](https://attack.mitre.org/tactics/TA0010)



# Data Security - User Roles and Privileges



If we are setting up a secure database environment, we would have to avoid to set up someone new with their accounts. We do not want the IT individuals miscopnfiguring the new account, where the new employee would have access to things they do not need. 


Ron was hired for a rule, be it executive management or sales for example. They have a role they are hired for. 


An organization would have to define what the various roles are that people can be hired for. 



Imagine an industrial company. They would have a lot of staff, such as clerical staff, drivers etc. 
We would have to do the following:

1. Identify the role 
2. Define the role
3. Define their access
4. Define their privileges



## Privileges


A sales person could have access to teh prodcuts database, but they would *only* be able to read it. 

If their role is not well-defined, it would be up to us to do so. 


A clerical person that works in the inventory department, and they can update the quantites of a product on hand, add a product, remove a product, order the product etc. 


A management person can adjust the pricing, where they would for example adjust the discount. Thety would access certain columns, but they would not be able to add or remove a product. 


In order for the clerk, the inventory person, pricing clerk, all of them can access the same database, but they would have different privileges. 


Privileges can be on the entire database, certain columns. 


If the person needs to change the quantity, they would update the quantity column. 


We do not start with building an account for Ron. If Ron is hired on a sales role, we would **already** define the role of the Sales person. They would inherit the role. They are not assigned individually to the role. 


We are not very good in staying up to date in terms of the information. 


If Ron got promoted to the Sales team, he would still have the ability to change the column, or the privileges from the warehouse. This should be changed. 


There is usually an automated process, but we would have to manually change the person's role. 


Someone would not ask Ron for the key, even though he is not working there. Many places have poor key-management processes. 


If he changed jobs within the organization, he should not have the keys. The same is for leaving the organization. 


In today's world, we would use car keys. The same thing is true. We do not manage this process well. 



Question: Can Ron be removed from the database ?

Answer : Yes! Someone has to be aware that Ron is gone, and they would have to add to the task list to remove Ron from the database. 


If we go on a Coop position, the security guard will walk you out of the building. 


Notice the process :Ron has left the company, someone would have the role of de-activatin8g the entry card. If someone forgot to remove Ron, they could forget to check. 


We would have to do a lot of monitoring to check that Ron's privileges are removed. 


There would have to be reports to indicate that these actions are taken. 



#### HR System 


Ron is the HR database, and somewhere in the database is : 


**Status Column         Status          Job Description**


Ron                         Employed           Warehouse

Change to 


Ron                       Probation 


Change to 

Ron                       Suspended 


Change to 

Ron                        Dismissed

Ron is listed in the HR database. Ron did a great job in the warehouse, and he gets promoted to Sales. The pay will change, and someone in HR will go and change the entry to "Sales"


There should be an automated procedure/program in the database where the change cascades into other parts of the system 


1. There would be a change in the **Role**
2. Ron would get the role of *Sales* and its privileges 


No-one else is making the changes. The role changes, access-privilege changes as well. 


If Ron did poorly, Ron would be on **Probation**, thus leading to less privileges. 


If Ron did worse, Ron is **Suspended**, pending review. The role would be removed. 


If  Ron did even worse, Ron is **Fired**. The keycard should automatically not work anymore. 



There are a lot of versions of this, and when Ron goes into the company, Ron is placed in the database, and Ron would have the correct privileges. 


If we use metal keys to get into the door, this triggers the request that someone *gets Ron's keys*


If the key is not returned, and Ron was fired 7 days ago, the police would be notified. 



How would we accomplish all of this ? 



# User Roles and Privileges



There are security threats that we face in databases. SQL Injection is an attack, where we can prepare for it. 


It is like building the foundation of the house. If someone breaks in, and the foundation is not good, the house would fall down on its own.


**Defining User Rights and Privileges** is the first step. Remember : We are not talking about *people*, but **Roles**. 



If people have inappropriate access for their role, the security audit would not be passed. Everyone would have their own user account and password. The password would have rules like changing it every three months. 


Which access is associated with this account? all this is designed on paper, and implementedo nthe IT system.


This could lead to people doing stupid things. If someone unknowingly deletes something, they could delete something for the whole company. The problem is not the deletion of the data itself, but a mismanagement of the data system. 


If you arrive home, and the house fell down, the foundation is not sufficient. 


We could have someone who is a disgurntled employee, and they do not have the right access, or someone leaves and goes to the competitor, and they still have access because no one shut off their access, this is dangerous. 


Watch out for *stupid mistakes* : if someone is allowed to delete something, it is the security specialist's fault. 


We get the issue of the **Insider Abuse**. There was a nurse at the IWK who had access to patient records. Because of the poor design of the database, she had access to all the patients, regardless if they showed up in her department or not. She had a hobby of looking up medical records of friends and family, and she would daily check her neighbor's information. This is illegal, and invasion of privacy. She was let go. Ron teaches about what you can and can not do. There are years in prison for doing this, but not very often people are charged legally. They are dismissed, and the hospital would be content knowing her career is over. If someone managed to change their name, they could get back into the medical field. IWK had to pay out a lot of money to her friends and family. The average was $10000 per person. The funds depended on how close this person was to her, and the impact that would lead to. 



There was a story in CBC Marketplace of computer technicians downloading the users' photos. 


The problem is not the mentioned nurse; the issue is the *system that allowed her to do so*. Ron worked in the healthcare industry (hospitals and medical school), and he did not build this database. Things are surely different now, but in the 1990s the hospital security was terrible. The IT security individual had a Castle Wall mentality. He focused on hardening the external shell, such as a firewall, Intrusion Prevention/Detection System. Hospitals have an tough *outer shell*, but a very mushy inner core. People were granted access inside the firewall. 


Imagine the situation of **Crypto-Malware**. If you clicked on a link in a malicious email, the attacker would have access to all the data, and encrypt the entire thing. The foundation was terrible. 


Security begins with **Policy(what we allow? show me the policy -> Design(how it is created? show me the. design) -> Implementation (show me the implementation of the design) -> Operation(show me the operation of the system, to make sure people are using it properly)**. We have not even discussed attackers yet. If we build a strong foundation, a clerk with a compromised email would not lead to the attacker getting privileges. 


Never Accept a Resume by Email. This is a standard attack :


Sent a Word Document --> click on it ---> attack is launched!


If you would like to accept online application, set up a *portal*. Never click on a resume sent by email. Never respond to the email. Place "We do NOT accept resumes by email. Resumes sent will be deleted without a response to the sender", and get individuals to enforce this policy. A relative of an employee sending a resume via email would not lead to the employee clicking on the resume. This is simple! 


There is a complex strategy : Malicious individuals join companies all the time. There was a report from CISS , someone from another country apply for a program, get hired with an employer with weak requirements for security levels, and the report spoke of a huge increase in Canadian colleges and universities. A foreign operative will get into an IT program, claim they are 18-years old with no education, but they would be 22 years old with a PHD. If it is a university, and get to graduate levels, they get to a graduate team doing advanced research. This is why they came from the beginning. Ron saw them personally. In the academic world , in a highly-secure subjects, no one pays attention to security. Information gets shared regardless of the security level, and this knowledge may be shared driven by compassion to help the individual. Ron attended meetings that he should not have ever been let in. He was a friend of a friend, and he was exposed to information that could lead to prison times for this person. They get sent home. They get discovered by someone in the intelligence services checking their background, or they get caught exfiltrating data. the most common threat is not a trained individual. This is a common issue with China. Students graduate from high school, and once they get accepted, they get a phone call from phone that their family members could go to a prison camp if they do not do what is asked. They are called *Agents*, who are compromised individuals. Russian citizens have decided to work for Canada , for money or other ideological reasons. They would decide to work for a foreign government. Aldrich Ames(https://en.wikipedia.org/wiki/Aldrich_Ames)s' wife wanted to live a lavish lifestyle, and he became an agent to fulfil her needs. His son was a signals officer in the navy, and handed the Soviets secret codes. 


Ron's friend from CISS did the job of getting foreign individuals to work for Canada as spies. He was an intelligence officer, and quit to work in the private sector. 


The systems are designed badly, where someone with that situation could get access to things they should not have been able to access. 


In all these interactions, there is a *human* making these decisions. Never rely on the **Human Firewall**. We would see individuals who are trained on not clicking malicious links. This should not be relied on. The system should prevent links from being open in emails, or other engineered safety controls. Policies have to be implemented!



> [!tldr] 
> Common Threats :
>  
>User rights and privileges
>SQL Injection (needs to be done from a website)
>Passwords
>require ssl
>Don't use default ports
>Encrypt sensitive data
>Stay up to date on compromises for your database 



When Ron sets up his password on a database for a demonstration, he would use really easy passwords. On Systems he cares about, passwords are 20-characters long. We can set up password policies that requires certain things in terms of passwords. Passwords not being displayed are settings implemented. 


The password-change frequency is another. They are commonly changed once a quarter (every three months). Why do we do so? people's passwords are stolen regularly. They are for sale on the Dark-Web. Compromised credentials' list is sold, and the passwords would not be the same as the stolen passwords 


There is another issue : When you change the password, you have to type in the password where it is not necessarily protected. The password can be discovered. You can put the password in the password vault, but when you change the password, it can be discovered. If we have a password policy where the password changes every 30 days, and a hacker is in the network, they would wait for that time to observe the system . Things like **Certificates, Passkeys, Yubi-Keys** are most helpful!


Ron's systems that he built would have nothing in terms of usernames and passwords, they would have certificates unique to the machine itself, which would restrict access to only this certificate 


**SSL Communications** : 



When setting up a database, and the user communicates with the server hosting the database, we would work on a workstation on our desks. We can stress that all communications between the client and the server happens through SSL. The default is *HTTP*, except the actual information communicated is encrypted by default. You can force SSL communication (TLS now) with a setting in the database. That means you get Encryption on top of Encryption. If we end up using HTTPS over port 443, you get an encrypted channel. 



In our case, the database is stored on our computer, which has a loopback server.



#### Default Ports


NEVER use default ports! Use a non-standard port. Most systems would have a default setup, so change the ports due to the attacker scanning your network and they would see the database on it. 


#### Data within the Database


If it is personally-indeitifiable information, the data should be encrypted. Encrypt the data within the database itself 



#### Stay up to date!


Check the Canadian Center for Cybersecurity. If you are handling MySQL, subscribe to a data feed that lets you know of the latest compromises. Make sure you have Windows Vulnerability Feeds! If using a browser, or some type of reporting software interacting with the database, keep up on the latest compromises. Any software we would use should be kept secure, up to date, and for us to be aware of any new vulnerabilities. 



#### MySQL


If you log in to MySQL, you will see databases that we did not create : 


. 
 

> [!danger] 
>  Information_schema - access to metadata
. mysql-stores information required for the server (e.g. user accounts,
privileges, passwords hash etc)
· performance_schema | SYS- server performance monitor, where you can get info on CPU load, memory usage. Ron hired someone to monitor the performance of the database, so Ron got a console to check the status of the database. sys - interpret data collected to view performance


Databases have a ton of **metadata**.


SHOW TABLES ---> USER table (which holds user account information)




## Tuesday's Quiz 

> [!important] 
>  **Tuesday's Quiz** 
>  12 multiple choice
Database design concepts 
It will be on things that he spoke about in class
Online quiz in Brightspace, where it will go off automatically (55 minutes : he figured out how long it took him to do it. He doubled the time, and thought that the person who has studied, and suffered no stress / anxiety, and he doubled the time. The time is for the average student. He doubled that time too. )
We can use notes(digital or written). We are not allowed to use Google. Most of us will finish the quiz before the time expires. Once the quiz is done, we can leave the class. We can stay in the room if we work quietly. 

> [!note] 
>  We have a Demo after the class. Take questions next Tuesday on all the issues we have. We will then get an assignment on "Defining User Roles and Privileges in a Database"




> [!note] 
> Quiz + Regular Class on Tuesday. No Lectures next week (Lab Class : Spend 4 hours) 


If we had a note from Marie about our scores , and a notice to consider withdrawal from the course, Ron has withdrawn from a lot of courses when it was a situation that if he had difficulties in terms of the workload that is too much. The professional decision is to withdraw from the course, and do it next fall. Students do that every semester. It is a way to manage the workload. Everyone manages time and effort differently. Most individuals will adjust the program as they go forward. 