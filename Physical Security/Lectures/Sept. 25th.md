


#### Hezbollah Pagers


It could be utilized to maim the target to identify who is a hezbollah member as a part of a greater ground invasion strategy. 

Iran's response is mysterious. 

There was a report given to congress last week pertaining to Iranian hackers being detected in the networks of Infrastructure assets in the US. The threats accordingly have been mentioned to be stopped.



#### Vulnerability Audits


New admin accounts may be required, or there was an issue causing the ADMIN accounts not being available remotely. 

There were attempts to attempt to run Nessus' Vulnerability Assessment on a virtual machine having a *Local Administrator Account*. 

In the previous 7 years, the assignment went through without a hitch. This year is the first time it happened. 

Try a successful attempt against our own laptops. 

This looks like something pertaining to remove Local Admin accounts. Make Me Admin is now adopted. It is possible the changes may be the cause of the Local Admin credentials not being available. 


Try to do a Bridged VM on our desktop machines, and do a Privileged Vulnerability Scan with Nessus. 


In the meantime,

>[!todo]
>We should try the following steps : 
>
>- [ ] build the **Uncredentialed Report**.
>- [ ] Login with the Administrator account, Start the Nessus Service, try scanning with Nessus against 127.0.0.1 with a login to the Local Admin account. The **Loopback Login is working**! If we take the credentialed scan and change the target to manually start *Remote Registry*, make sure that we have the **Remote Registry Configuration Options** ready first before the scan!

>[!note]
>The difference between System account and a Service account is the System Account applies to everyone who is logged-in. The Service account applies to the entity running the service.


