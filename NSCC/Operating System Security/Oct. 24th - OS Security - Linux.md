



We have an assignment released later today. 


Today will be a day where we go in depth into Linux. 


# Files, Users and Groups



## Linux Mint


It is a derivative of **Ubuntu Linux**


It is not server based ; it is **Workstation-Based**


Because it is a *workstation base*, it automatically installs with a **Graphical User Interface**


It gives us a way to look at things from a different perspective. 


Everything we will do we will do in the **terminal**. 


Servers do not have a Graphical User Interface


We will talk about **Basic Security**, **Basic Permissions**, **Users**, **Groups** , **SUDO**, **Passwords**, and **Commands**



## Linux File System 


Everything in Linux is either a **file** or a **process** (which is like a **Service** in Windows)


Because Linux exists around directories to organize files, it works differently than Windows. They assume we do not want to do all the work involved in a task. 

When you complete a task in Microsoft Windows, such as copying a file, Windows finds every place in the operating system that is related to that file location, and changes it for you. It looks at permissions, and adjusts them. Linux does not do so. 


Linux is independant, and we have to do the work. 


When you run the process, as a part pf the intial setup, it will automatically write to a file. Any changes done afterwards has to be done on a one-by-one basis. You would have to change everything manually. We will learn BASH scripting next semester. It makes Linux fun but challenging. 


It is easier to uninstall the process and to install it again, or in VMWare, we can roll back and try again. 

Everything in Linux starts with the ROOT or top directory **/**


If we are looking at our hard drive in the system :


Hard Drive ---> / (Root)

Folder 1
	File ---------> /home/user/Directory/File

		We do not understand what home is. The / is to go to the root of the drive


In Windows, we use the backslash to define the root  \


Folder 1 
	File 1 ----> C:\Folder\File1



/usr/share


#### Configuration Folder

/etc 

A lot of things live there. Most of our configuration files stay there. 
#### Home Directory 


/home/user


This is the home for the user. The home folder exists by default in Linux. What is in the Home folder can be different. Not every user has to have a home folder. For every user with a Home folder, the folder will exist in the /home/ directory in the Linux filesystem. It would have **Documents, Downloads, Pictures** , etc... 


#### /USR


Contains the program files (Program is a process, not an executable)

It stores the files necessary for the processes running in the background. 


#### /dev


This stores the hardware files


#### /mnt



This stores the mounted removable storage 


/var


Contains temporary Data Files. Things that get modified on an ongoing basis, or things that get updated when you use a process. We will look at it often. 



The main focus is /etc /var/ and /home 



/opt


Third party software


/boot


This contains the boot files



/bin 


contains the programs and commands shared by the system and users. 


/sbin 


almost the same as /bin, buit designed for the ROOT or Super-user on that machine. 


/lost+found 


This is the home of deleted files. 


When we see a . infront of a fdile name, it is a **hidden file**. 



/home/user


This contains a folder for every user account on that machine. We will see a directory with a . , and a directory with .. . They are hidden directories, and they contain details about the configuration of the home directory. 




> [!info] 
> What is the difference between a process 
> POrocess is compiled, and the information is placed in a big file or a variety of files that can do different things. LibreOffice is listed as an *Application*, but if we look at it, it is a bunch of files and processes that do different things. A *Program* takes all that and combines it in one entity. In LibreOffice, we will see files and processes that are scripts. In Windows, we just have Word.exe. Executables are linked to library files and dependencies. One is turned into an executable, and the other is compiled into different processes. 
> 


> [!info] 
> A **Daemon** is a process. She likes using daemons because back in the day with older versions of Linux, they used to identify the process part with a *d* , such as *sshd*. *Crone* is a great example, due to it having a variety of ways that can run a process of a series of processes. 
> 




# Linux Security 



We will discuss *Basic Security*


There are three permissions that exist in Linux's Basic Security : 


#### Read


4

#### Write

2

#### Executre 

1


We have the ability to apply that based on three areas : 

#### User (U) / Owner


Whoever installs Linux becomes the **Default User**
R - X (Read + Execute)



	Whoever created this file/directory

R  W  X   (Read - Write - Execute)

#### Group  --> G
R   X  (Read/Execute privileges), and we add a **-** to indicate they have no **RUN permission**.

	Whichever group is assigned to the file/folder, based on permissions, or the group that the owner belongs to.


#### Others -> O 


R  X  (Read / Execute)


#### File Type (d)



![[Pasted image 20231024110537.png]]




### chmod Command



This is the command to **Set File Permissions**



If we would like to change permissions for the group : 


>chmod g=rwx  (Read/Write/Execute)

(This is the common way)
or 


>chmod g=+w ( add Write privileges to their permissions)


or 


>chmod +w (give everyone Write Permissions)



or 


>chmod rwx rwx rwx 



##### Another Way : 


	4 Read
	2 Write
	1 Execute
	7 All-Permissions


A demonstation : 


>chmod 777 (all permissions for everyone)

>chmod 775 (Users have Read/Write/Execute , Group has Read/Write/Execute, Others have Read, Execute)

>chmod 664 ( Users have Read/Write, Group has Read/Write, and Others have Read)


Sticky bit: 


	chmod 7775 



Example : 

>chmod 600 (Owner has Read/Write, Group and Others have no permissions)



The group that has permissions is the **Primary Group**. There is also a **Secondary Group**. 


To change the group :


>chgrp


Question: Is there a difference between the Superuser and the Owner? 
Answer : if you are the Default User, you have elevated permissions on that system. If you have another user, they do not have elevated permissions. They would not be in the *sudoers* group. 



## Users


The **Default User** is whoever installed the operating system. They are not root, but they are the default user, who has the ability to run something as administrator, which is if they have elevated permissions. The root user in Linux is the equivalent to Admin in Windows. 

**Root** does not always have a password, where you would not be able to log in as root. Root without a password is done on Server operating systems. 

**User** is the basic user, which have abilities based on permissions and groups . 


**System-User** is equivalent to the SYSTEM user in Windows : they have special abilities on Windows, they can perform tasks before anyone logs in. When starting Windows, SYSTEM is the user in the background doing tasks before the system is fully loaded. In Linux, they have a large variety of users where they are created by the distribution. They are less than 100. We can create a system user in Windows that run in the background. In Linux, we can create a user who is a *System* user, or part of a special group, and we give them a USERID below **1000**. 


When creating a regular user, every user that is created gets a **UID**, and it starts at **1000** and up. They automatically get a **Group** created for themselves. When looking at permissions, we would want to be in the **Primary Group** as well. The group is given an UID of 1000. Any user afterwards would get a UID of 1001 and a **Group ID**, which does not always match. 


If we created a *user* , and created a *sample group*, where the *sample group* has a GUID of a 1002. The user may get a UID of a 1001 because they are the first user to be created. The group becomes the Primary Group. You can belong to other groups, where the most common group is a group called **WHEEL**, where it is the administrator group in some distributions such as Ubuntu. The default user will belong to their own group, and possible other groups such as a SUDOERS group or ADM group. Any groups they belong to after the PRIMARY GROUP , and the groups they are added to are called **Secondary Group**.


Any **System Groups** would have its users, either default or secondary users are automatically generated. We can pick the UID that is less than 1000 , and they become like a **SYSTEM** account, and you owuld not be able to log in to the Linux Operating System. An example is 999. 


If we create a user, all of the user accounts are stored in a file called **passwd**, which does NOT hold passwords. The file that holds the passwords is called **Shadow**. 


nobody:x:65534:65533:nobody:/var/lib/nobody:/bin/bash
root:x:0:0:root:/root:/bin/bash
User:/var/lib/YaST2/suse-ncc-fakehome:/bin/bash
halo:x:1000:100:/home/halo:/bin/bash
. Username
" Password (encrypted)
· User ID (UID)
" Group ID (GID)
. Home Directory
. Shell
" Misc = /usr/bin/nologin = means that use cannot log in directly, where they only exist internally 


![[Pasted image 20231024112759.png]]


## Groups 


The /etc/passwd shows us the general information about the user. If we wish to check out the Group Information, there is a file called /etc/group. 


In the /etc/passwd file , the password is repressented with ,s, , which means the password is encrypted. /etc/shadow holds information about the password: 

Column1                Column2                               Column 3
the username         hashed passwords,           Number of days since password change (EPOC                                                                              date/first official day in Linux's life in general 1/1/1970) 

disabled.
"Column 1 = Username
"Column 2 = Hashed password
"Column 3 = Number of days since password was last changed
* since Linux EPOCH (Jan 1, 1970).
"Column 4 = How many days before user can change password again.
"Column 5 = How many days until password change is required.
"Column 6 = How many days before password expiry will the user be notified that they need to
change their password.
"Uncompleted columns are How many days account will be locked, how many days until account is
nsc


> [!info] 
> - Username: The username associated with this account.
>
>- Uid: The user ID number assigned to this account. This is used by system processes and programs when accessing files owned by this user.
>
>- Gid: The group ID number assigned to this account. This determines which groups the user belongs to, and can be used for access control purposes.
>
>- Creation time: The date and time that this entry was created in UTC format (Coordinated Universal Time).
>
>- Last login time: The last time this account logged into the system in UTC format.
>
>- Password expiry: The number of days until the password expires, or 0 if there is no password expiration policy set for this user. 

![[Pasted image 20231024113230.png]]


The /etc/oshadow shows all the passwords that were previously used. 



## SUDO 


aka .. **Superuser DO**


. Sudo (SuperUser Do) command
	It means : Run as Administrator. If you are logged in as ROOT, you do not need to use a sudo command. 
	There are a variety of sudo command; she can change the permissions of the sudo command. A user with sudo can update the system. Someone with sudo have the ability for example to see the shadow file, but restricted from editing other files.

* Temporarily elevates privileges for the user to root
"You must be the sudo group in order to use the sudo command
* Wheel (RedHat/CentOS)
* Sudo (Debian/Ubuntu)
Sudo visudo
"Command required to access the sudoers group
"Allows you to make modification to group
"Can limit or manage permissions


![[Pasted image 20231024113418.png]]

The sudoers file governs which user has the ability to perform commands with "sudo"



An example command that is the top-level command : 

>sudo su

This means : 


		The user can log in as ROOT. Noone is allowed to do so, except for a designated administrator. If she had to go away for six months, she can provide them with the credentials of a generic account, and change the permissions when she gets back. As a rule, this is not a command she would give them permission to run. They can be permitted to run :

>sudo update && sudo upgrade


It might be alright for some users to do certain tasks. In Linux, the sudoers file governs who can use sudo. Make sure the user is in the right group with the right permissions. 



#### chmod 


	Modifies permissions on any file or directory 



#### chown 


	Change the owner of a file directory 


#### chgrp 


	Change group for a file or directory



#### sudo visudo 


	Edit the sudoers group


#### man

	Retrieves the manual of a command


#### ls -al  or ll


	gives all the additional details 


### pwd


	Displays current working directory 


#### touch 


	Creates an empty file



#### grep 


	filters text in a command's output or the contents of a file for a specific term 



#### wc


	Checks the lines, word count and characters in a file (lists the number of lines, word count and characters)



#### mkdir


	Creates a new directory



#### cd .. 


	Goes up one level in  the file system 


#### cat


	Shows the contents of a file



#### echo


	Displays a string 



#### find


	Finds a file or a directory



#### groups


	Lists all the groups a user is a member part of


#### chsh


	Allows change or modifications to a shell




## Next Class : 


> [!abstract] 
>  We will : Create Users, Create Groups , Change Shells , etc ...



