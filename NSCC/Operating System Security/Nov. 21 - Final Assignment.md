



She might miss a class *Next Week*


*Final Assignment* before the **Final Project**



# System Logging



What is **System Logging**? 


	Monitoring the system via Log Analysis


## SSH Logs


What is so special with **SSH**? 


The connection is *encrypted*. Nowadays, *Remote Work* is common place, the *Cloud Infrastructure is very present*, and in order to ensure the security , we should check the **logs**.


We will look at **Windows Logging** next semestar. We will cover more **Linux Logging**. The priciples of how logs are stored is the same between Windows and Linux, albeit with subtle differences. 

Windows splits it into *five or six areas*


### Linux Logging 


Two types : 

#### Kernel Logging 

	Relating to errors, warning or information enteries for your kernel, such as Startup Information. Sometimes, things are stored in kernel logs and user logs (for authentication for example)

> [!example] 
> Much like a Car's Dashboard's Lights 

#### User Logging 

	Relating to the User Space, user processing and services, user details like authentication. 



> [!warning] 
> Not all the data *captures* data. You need to configure logging and other tracking tools in *Settings*. If you need something specific, you would need to **configure** the logging values in order to capture this information. In Linux, everything is in files. Windows tends to be more *wizard-involved*, so a lot of this stuff is done in a simplified manner. 
> 



##### Location of Logs :


> /var/logs


The majority of the logs are sitting in the *root* of the **/var/logs** directory


*/var/log/lastlog* : captures the last time a user logged in into the system 
*/var/log/wtmp* : details for all the login sessions
*/var/log/btmp* : details about failed logins 
		To get the /var/log/btmp , we can use this command : 
		
				lastb


>	dmesg :
>
>		It will open the Kernel Logs for the administrator to look at


>	journalctl :
>
				It will be used to read User Logs



##### Additional Locations for Logs :


		/var/log/sshd.log :
		
				Contains SSH-specific logs on systems that store the logs in a separate file.


		/var/log/auth
		
				Contains Authentication Information for SSH and other services


		/var/log/security
		
				Contains logs used by Red Hat-based systems



# Policy of Least Privilage



#### What does it mean ? 



The users get the only rights and privileges necessary for their task requirements. That applies to both the **User** and the **Machine**



If, for example, the user does NOT need to use the *ftp* protocol, the user does not need **Port 21** open. The port should be *changed* anyway as it is a bad habit to leave the default port in use. **POLP** means :


	Turn off programs and services not needed, close open ports that are not needed, and check the enabled permissions 



### Permissions in Linux : 


>Owner
>Group
>Others



> [!warning] 
> If they do **NOT** require it, do **NOT** include it!
> 



If the directory is shared, one would have different sets of permissions. She can look at these permissions, and the shared folder permissions, and say "What permissions does the user/group actually need?". If she needed the whole *Sales Department* to edit files in the folder, she might add Read, Write, Execute for that folder. For those *Working at Home*, she can make the permissions **Read-Only**, so they can make the modifications when they get to the office. 


With the *sudoers group*, in terms of the **Policy of Least Privilege**, the *sysop* account was created. Because the sysops group has access, she mentioned that the one thing she can do to make sure it is used responsibly : 


1. Only have the permissions they need (They cant sudo everything)
2. Set up logging, so she can track the user, location of login, and when they did log in. 
3. Restrict their access, where they can login onsite from a specific machine
4. Limiting Access Times : Limiting when they can access.
5. Limiting Usage : " You have a regular account, and you have elevated permissions that you would get only when necessary". She can build policies around it. We can limit which commands that can be run. We did limit the sudo usage in our previous assignments. 
6. Adding Security (Additional step, but not related to POLP)



Hypothetically, if your responsibility is to do periodic audits with a script, the script would need elevated permissions. The user would be logging in via their own user account, and the script itself will request permissions. This course is a lot about policies and interpreting policies. In some cases in *Windows*, the user account could have a **One-Time-Only Password**, where the password would be approved when needed. 


> [!warning] 
> **NO ONE** should be logging in via the *ROOT* user!
> 



Make sure that you have *general accounts*, a *support user*, and a **systems-operator separate account with separate rights and responsibilities**. 




> [!example] 
> The NSCC Book Store has a Search Platform. Books go out of edition, they get new booksm so there are a lot of changes. They need to update their software on a weekly basis, and for them to do so, they need elevated permissions, which is not done. She would give only the files and programs that actually need the permissions (often seen in the Windows directory), and then you can update the employees' permissions for those specific files and folders. 
> 





# System Hardening 


What is **System Hardening**? 


It could be **Putting Password Policies**, or a variety of things.



Every computer comes with a *default installation*. 



The issue is, everyone has the **same default installation**. It does not matter if you install **Linux Mint** and **Windows**, then everyone would know the default users , backend, default ports that are open. This is because they have a duplicate of the machine you are workiing. 



Hardening involves making the machine uniquely secure, look at firewall, privilages, shut down open ports, change settings so it does not comform to the defaults.  There are many ports that are available for use. 


Hardening : 

	Take the default install, and make it nowhere near the default. Make it secure with rules , privileges, and to make it conform to what the user needs to do. 

One thing that can be done is to block USB booting, where data can be exfiltrated. One thing that can be done is to change the drive letter to boot Windows from. 


The aim is : 


	Make it as difficult as possible to gain access into the machine



When installing an application, you should check the verbose information. When doing an update, one would check what the update is changing. 



One of the major issues with **Windows** is that it does *Automated Updates* by default. One of the things to do is to *Turn Off Automatic Updates*. Windows removed the option to turn it off. 



> [!danger] 
> The **Vulnerabilities** we are looking at is different between a *Web Server* and a *File Server*. Anything with an Internet-facing side , like an email for example, would be a public server. You do not know the people who will use it, and those are the machines that need to be focused on the **MOST**, because it is a *doorway*. The attackers could walk in the front door. 
> 


> [!hint] 
>  **Hardening :** 
>
>Finding the Best Way to make your machine different , and the least-vulnerable based on what type of machine it is!





# Assignment 6



In terms of Cyber crime Businesses like *The Village*, if you had a dispute with a competitor that retailers can use, possibly one company may take the market share from the other company, the Cyber crime businesses will kill and kidnap competitors. Traditional mafia organizations could be importing Olive Oil from Italy, and another company starts shipping Olive Oil from Italy as well, the company would disappear. Russian Business Network's leader compromised, cheated and stole from any organization that he joined. There are no moral boundaries at all; they have a single objective (an ethical social domain that surrounds them ONLY). The other really important thing that one has to keep in mind : 

Millions and Millions of Dollars in the child pornography being made. This is the basis of business for Russian Business Network. Everything is invested in supporting this market. One could look down upon them, but North America is the land of consumption (mostly). How many times you have heard once a year or twice a year of someone being arrested for child pornography. Only a tiny portion of consumers of child porn are caught. 

We spoke about having the RCMP visiting, more specifically , the Digital Forensics and the Cyber Crime Divisions are visiting. 

Russian Business Network was the first of the biggest : they were broad-based, with tremendous political support. Flyman may have been a nephew of a member of parliament (well-supported). The members of this organization could have been relatives of the leaders of the former Soviet Union/Russian Federation. 

If they were arrested, it could be due to a rival having connections with a federal judge for example, who would utilize this connection to push aside a competitor. 



When Russia invaded Georgia, there was a massive cyber component affecting all aspects of society. No one knew what was happening. It was the *first example* of **Hybrid War**; it means that Air Force, Army and Navy attacking alongside a *Digital Force* that breaks communication, spreading misinformation, etc. 



#### Two potential strategies for Ransomware : 

Only people to get email : People who must receive emails (absolute necessity for their work ; train them and punish them if they go against the email policy) , or , find a way to replace external email with something else. Not clicking on links is a great idea :

1. limit who has access to email : train and monitor those people
2. Use a dedicated email device (airgapped to the mail server ONLY), and in no way connected to the rest of the infrastructure). This is how it was done previously. If you restrict email to only those who need it, and have a dedicated email device that is separate from the rest of the infrastructure.











