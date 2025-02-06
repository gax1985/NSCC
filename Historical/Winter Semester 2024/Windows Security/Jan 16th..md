







 Next Thursday is off all the way unto Monday



Tuesday's lecture will be in **Teams**





# The Server we Set Up 



## Domain Controller



We talked about **objects** in the last class. The assignment we had was an installation and a basic setup. 


Some servcies are not requirewd to run. In order to initiate a faster startup, they are set to *delayed start*, as sometimes they have a required service to be in place before they start. You can manually start them if you wish. It does not matter. 



#### ""Local Server""



Computer name, Domain Name, Remote Management/Desktop in place/or not, NIC TEAMING. IPV4 settings, the version of Windows, hardware information, When the last updates were installed. Almost every vulnerability the way to resolve it is to run the latest update. Sometimes updates break things while fixing other things. Keep an eye on the "Logs". 


Windows' Security updates are separate from every other update. Instead of doinbg a handful of updates, it does **Cumulative Update**, which it will load all the updates you have missed, and continue to install the next patch. It used to be *Update Tuesday*, but nowadays that is no longer the case. It will tell us when iut was udpated, when it was last checked for updates. As soon as she logged in, it was looking for updates. Due to it being a server, it will be up to Marie to install the updates or not. The reason why it does that with a server is a server can not have any downtime! In the case of the server, we can look at all the updates ad check them if they have a new issue involved. Reboots on servers are scheduled on Saturday nights. Any workstation is not an issue. 


## Real-Time Protection 



It is looking at real time data. It is looking at the memory, emails, etc. It slows things down, its about reliability and security. 


In a database server, you can not have two live versions of the same database. Blocks are scheduled for updating purposes. This is especially while doing large updates



## Diagnostics


Configrued during the install 



## I-Enhanced Security 

For the administrator and it is to be left on!

For other users, it should be left on.

Internet Explorer was the default on Windows Server. 

You are not going to add software to a server. The core security configurations are designed to work with the server the way it is. 


What I-Enhanced Security does is to prevent browsing to any page at all. Every single page needs to be manually added to the *Acceptable Viewing List*





## Logging System 


#### Services


If a service was stopped by someone, that tells us that someone has hacked into this machine, or a piece of malware hiding as a service. 


Services are a second-thought usually


It sorts services by *status*


We can run *Filters* against the logs, so we can have a glance specifically at something we suspect


#### Performance Monitoring


As a rule, the CPU spikes up in the morning, and when someone gets back from lunch. If someone has accessed the machine maliciously at 7 PM, we would see a spike in the CPU performance. Watching subtle changes is very important. 


When a car is acting up, like a car not starting, then we know it is down. 

If the car is running, but something is not right with the car, we would know by watching for the subtle changes


#### Roles and Features 


We will talk more about them. If someone suddenly adds a role or a feature, that should set a flag. If it is a new machine, there should not be any new roles at all or any extra features






# DNS



We should set up DS in the DNS Manager. You would set "what you are listening on", and we are only listening on IPV4. Normally it would support both IPV4 and IPV6. 


We set up **Forwarders**. It will say "Unable to resolve", which is due to the DNS server forwarding to the next DNS server, VMWare does not forard the address. If we are doing a bridged network, it would use NSCC's DNS and the next is ISP. 



# Active Directory Users and Controllers


It is a database where we can see everything. We would see the users created , groups.


#### Active Directory's **Administrative Centre**



There are certain things that appear different, due to "Users and Computers" being looked at from the Basic View. We can go to Advanced Features and see the Keys tab. Working in Users and Computers provides a concise format for basic management. Active Directory's Users and Computers come from Windows NT 1.0. It was made with the intention of being easy to use, where wizards will populate properties, and do actions behind the scenes. 


There is a feature called *Atribute Editor***. Attributes are stored in **schemas**. Scripting in Windows involves the **Distinguished Name**. It would take some of the data and fill in pieces for the user via the wizard. Attribute Editor will not fill in ALL the pieces. Use **Administrative Center** is useful for quick information. 




## Group Policy Management


We have talked about Password Policies, etc.. We are setting uyp a generic policy, where we would modify a policy, we would decide whether ti was a compuer configuration or a user configuration. Set up a Lockout policy


Group polcy : 


Anyone who automatically logs in the Domain will inherit the policy 


Once a policy is issued to a machine, it stays on that machine. 


When a Group Policy is set and sent to her laptop, the laptop is a member of the domain. If she goes to vacation, and brings her laptop, the policy is set. 







Next Lecture : Tuesday, In class marking
Thursday is a Video/Reading Day!


Following Tuesday : On the 28th/29th , we would have the next lecture. 








