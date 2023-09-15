

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




