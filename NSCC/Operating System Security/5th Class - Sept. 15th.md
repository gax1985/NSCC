

We are taking a closer look at **Windows** today


Next week, in-class lab and quiz


On Monday, if school is not closed, It is on Monday. If the school is closed, then it is on Wednesday.


The quiz is on **Computer Components**



The lab will involve **file manipulation**




## Microsoft Windows 




It features a **user-friendly interface.


A lot of shortcuts in Microsoft Windows stemmed from **MS-DOS**


If you are in MS-DOS, there was no mouse option. You would use CTRL+C to copy and CTRL+V to paste


Each version of Windows is designed to meet the changing needs of computer users


Microsoft Windows 10 and Windows 11 is not very focused on the touchscreen


It features a *Start* button, which shows you the applications

The *taskbar* is at the bottom. You can unlock the taskbar and move it around. 


The *Desktop*  features icons designated for My Computer, Control Panel, Recycle Bin and others (according to the wishes of the user)


If we right-click on a Shortcut, and then select Properties, we can see the file path for the application. 


**Available Physical Memory** is RAM memory that is not used by Microsoft Windows


If we right click on the *Start* button, and select *System Information*, we will see a lot of information on the computer. 


**File Explorer** allows the user to create folders and files, rename them, delete them, move them via *Cut* and *Paste* and other actions. 


**Recycle Bin** is the location for deleted files, which allows the user to return them to their original place, or empty the Recycle Bin


If we right click on C Drive, we will see a *Disk Cleanup* option. 


**Formatting a Hard Drive** involve wiping out the hard drive. If one plugs in an external drive, we would have the *Format* option. Formatting can be quick. 

**High-Level Format** involves resetting the file index that is stored on the drive. If we format the drive, or if the index is corrupt, a file recovery institution can rebuild the files on the drive, as the 1s and 0s are still there.  If we do not do that, and we simply write over the drive, then the old data would be gone.


If we are trying to retire a Hard Drive, it would involve drilling a hole in the Hard Drive and degaussing. If we formatted the drive, the information is still there.  As an example, the hospital got rid of their Xerox printers. Printers have a hard drive inside each one. Someone pulled the hard drives out of the printers, and had access to patient records, as the print queue/information were still there. 


If using **OneDrive**, the files would be synced and updated automatically on the cloud. There is a *Previous Versions* option there, so a file can be restored to an earlier version. If we open a file, we make changes to it, with Office365 syncing the changes. we can revert back to an older version. 


The **Calculator** application is very useful, especially if we select the *Programmer* calculator. It can instantly convert Binary numbers into Decimal numbers. 255 = 1111 1111 (the maximum number in order to keep it in 8-bits). 192, 172 and 10 IP addresses are internal IP addresses. 8.8.8.8 is Google's DNS server. *tracert* is a command for finding out the steps that the system has taken when issuing the following command : 

	ping www.google.com

And if we wish to use *tracert* :

	
	Usage: tracert [-d] [-h maximum_hops] [-j host-list] [-w timeout]
               [-R] [-S srcaddr] [-4] [-6] target_name

	Options:
    -d                 Do not resolve addresses to hostnames.
    -h maximum_hops    Maximum number of hops to search for target.
    -j host-list       Loose source route along host-list (IPv4-only).
    -w timeout         Wait timeout milliseconds for each reply.
    -R                 Trace round-trip path (IPv6-only).
    -S srcaddr         Source address to use (IPv6-only).
    -4                 Force using IPv4.
    -6                 Force using IPv6.


##### Customizing Windows



If we were to *Personalize our Look and Feel*, you can change the background and  display settings (to control font size, resolution, etc...)


Administrators can limit the user's ability to customize it according to the requirements/regulations of the institution


With the **Registry Editor**, we can do our customizations there if we wish.



Back in the day, when starting the computer, earlier viruses would launch on boot. If we look in the **Registry Editor** for the *Startup* option. It is a great option for Kiosks or any other applications. If we were to add the application to the old *Startup folder (ms:startup in the Run Window)*, it would not show up in the **Registry Editor**. If the registry is corrupt, we would have serious issues



Excessive customizations could be a security risk, so naturally there would be limitations on what kind of applications that the user can install. Also, some customizations via the *Registry Editor* would be seriously risky if it was in the hands of users instead of administrators




#### Windows Applications 



Unwanted applications that come installed from the makers of computers and laptops which slow down the system without the user realizing it are called **Bloatware**


**Executables** are some form of applications. The name is connected to their *extension*, which is **.exe**. Applications can run background processes as well without the user knowing. 



#### File Manipulation 




We have a lab coming up which involves modifying files


He did a example of cutting and pasting .dll files, and how he was not able to do so due to these files being in use. If something is not directly in use by the user, they could be still used in the background. If we move .dll files or other important/critical files, then the application using them would cease to work


When working with files and folders , we would have to be aware of the essential files' locations, what it is we are moving, and what type of impact we would have if we did move the files. 




#### Managing User Accounts 



Every time a user logs in into the system, a *USER* directory would be created for that user


We have **Local Users**, who can be ordinary users or administrators. If it is a local user, then the user would only exist on that computer only. 


**Network Users** are users who logged in with network credentials 



if we have a small IT shop, we would need to streamline as much as possible. An example of a bad configuration was to create local users , and making them an administrator for their local machine. There was a phishing attack where the local user's credentials'(who happened to be an administrator on the local machine as well as a domain administrator) were found by the hacker, and was zipping files in order to conduct a ransomware attack (the hacker did not encrypt them yet). The company decided to roll in **Multi-Factor Authentication** over a period of four months. 



When malicious actors conduct a ransomware attack, they would do a lot of research about their targets before hand, in order to decide how much of a ransom they would ask for, and what the organization is most likely to do. There are no guarantees that the ,malicious actors would provide the the decryption key.


(... we will get into **Hardening** Windows later )


User accounts are doing the accounts' management *centrally*. **Active Directory** is a large directory of users, systems, and all connected devices in a network


We switch user accounts all the time. When a user logs out, they exit from the configured Windows environment. When another user logs in, then their pre-configured Windows environment gets loaded for the other user


Intune was mentioned as a way to package applications, so it enables the ordinary users to install applications without themselves being administrators, due to the applications being packaged by the company behind InTune



#### Windows Security 


**BitLocker**  would prevent a ransomware attack, as pre-encrypted files and data would not be able to be used in a ransomware attack


**Windows Defender** is a suite with Microsoft Windows' Security Features. There is a risk of a Windows update breaking applications, so it is common to test all the applications on a test system. 


Microsoft in corporate environments sell security patches for older versions of Microsoft Windows




#### Troubleshooting 



Restarting the system is a valid troubleshooting step. Sometimes rebooting fixes an issue


Patches can be rolled back if needed to attempt to pinpoint the source of the issue 


Troubleshooting would be done step by step!





#### Tips and Tricks




1. Keyboard Shortcuts : CTRL + X (Cut) ,CTRL + C (Copy), CTRL + V(Paste)
2. **PowerShell Scripting** is something we will learn later... it is a most-powerful asset.
3. **Virtual Desktops** to separate workspaces 


(In the 1990s, icons made by one user can not be reused by another user)




#### Virtual Machines



technically, it would be the same operating system that we have on a physical machine, but it is running on virtual hardware


A virtual machine's folder would contain three or four drives. One of these files would be the virtual machine's hard drive.



The file format of the virtual hard drive would be essential in order to mount the virtual hard drive in Microsoft Windows. 


**VMWare Workstation** and **Oracle Virtualbox** are hypervisors. There is a difference between a *virtual machine* and a *virtual desktop*, as *virtual desktops* are set up for organization, and *virtual machines* are complete virtual systems with virtual hardware



##### Non-virtualized

Applications


OS + Drivers

Hardware



vs.





##### Virtualized Computers 


Applications + GuestOS ---> VM


VMM Virtual Mahchine Monitor


Hardware






###### Advantages of  a Virtual Machine :


Supports legacy applications (older versions)
Provides segregation
Provides disaster-recovery
Provides redundency 



###### Disadvantages of a Virtual Machine : 


Not 100% stable
Bare metal is faster than a virtual machine 


VM in a VM ---> Azure Microsoft Labs 

He did a virtualization course, turned on Hyper-V service, Azure labs provided a Hyper-V version which enables the user to run a virtual machine in a virtual machine ---> **Nested Virtualization**






He mentioned doing a comparisonof the costs between setting up thin-client-based workstations connected to a cloud-based virtual machine compared to the costs of thick clients. The results was very close

	Another consideration in this situation : actual systems would be easier to do a redundency plan in terms of an electrical outage as compared to cloud-based systems.
