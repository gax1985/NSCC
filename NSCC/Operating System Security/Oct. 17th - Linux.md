


We start the **Linux Assignment** today. We will be installing Linux, and checking it out



Thursday is an open-house day, so she will drop in to support those who need it. 



## Linux



We will starting very gently with Linux. 


We will learn the *concepts* and the *basics*. From a Systems end, we will be working ALOT in Linux. 


Running Linux is like driving a Standard-Transmission car. It takes a bit to get started, but it will be really fun!




## Unix


This is the birthplace of **Linux**. It has been used a lot in : 

1. Mainframes/Super-Computers : It was made for that kind of design. 

2. Dedicated Servers/Workstations : We see Linux workstations sometimes, but rarely. You see it most often in servers: 
   
   
> [!note] 
> What is a **DMZ**? 
> 
> If this is our network :
> 
> 
> Network -------- servers 
>               ---------- clients 
>               
>               
>               
> Outside of a network, we have things that the *public* need to connect to; Email Servers , Website , etc...
> 
> 
> If someone is sending us an email from outside the organization, we do not want them coming inside of the internal network. If you have an actual letter sent to you, it gets delivered to your mailbox instead of inside your home.
> 
> 
> DMZ :                          Internal Network : 
> 
> Web servers   |                      Database
> E-Mail             |                     File Server
> 
> 
> We have administration privileges over both. a DMZ is a place where one can watch the traffic getting inside the machine, and the network. 


Unix/Linux is seen in **Web Servers** , **E-Mail Servers** , **Streaming Servers** , ...


There is not much we can do in *Windows* that we can not do in Linux.


Unix/Linux is a **multi-user** operating system, it allows more than one individual to log in. 

Unix/Linux is a **multitasking** operating system; they do one task, stop, do the next task, etc.. with people, they are doing the same, but they are good at moving from one task to another. 

> [!note] 
> Unix/Linux : Unix came into reality in the 1960s. It was a collaboration between universities, which was way before the Internet, and before computers became part of our lives. It was for the old mainframe computers. Programs used to be printed on punchcards, and the computer read the punchcard to understand the program's instructions. This was NOT **Linux**.  


## Unix


Similar to DOS, but different in the sense it uses a **shell**. The **shell environment** provided flexibiltiy. It had a **Unique Design**, which is a bunch of files and folders. Programs than run in Unix/Linux are programs that have been compiled ; a bunch of documents linked together to create a program. This is NOT like *Windows* programs. Most of Linux is a collection of documents and files and folders. That is all. 


What makes **Unix** unique as compared to Windows, is that Windows has a lot of the task you are trying to do already done for you. If you change something in Windows, it changes everytthing along the way. In Windows, if you copy the file from one location to another, the registry recorded the original location, and it does not get updated right away, but it gets updated. In Linux, if you change the file, or move a file, it does not automatically record the change. You would have to do so yourself. In Linux, we need to a lot of things manually. 



Unix was **proprietary**; it was sold between companies. Unix itself is not a free environment, so you had to pay for it. 

**Linus Trovalds** came up with the idea of Linux. He made enough changes in the Unix code, and made it follow the original premise of Unix, but made it slightly different in its design to fit his vision : a free verision of Unix .


He made it so that the **code itself** is **available** to anyone ; he made it **open-source**. Anyone can add, build, improve and make modifications as they see fit. Anyone can see the source code. 


There is some control, but almost everyone can make changes. This is a **positive** and a **negative** as well, as we have NO CONTROL over changes that could hinder its operation. 


If anyone is running Dell through the campus, the version of the distribution will not run the version she is asking for. 



Linux can exist with other operating systems. One of the things we can do with Linux is **dual-booting**, which means that when the system boots up, we can choose which operating system we would like to use. 


Linux is truly open-source. It is free operating system/software. Every distribution of Linux is not necessarily free; some distributions get sold to coorporations. 


Programmers have full-access to the source code ; they can add features, make improvements , fix bugs, or they can copy the entire system and make their own version. They can test and write any vulnerability for it. It is not necessarily safe, as others have hacked into it, and produced malware for it. It is not common to hear of Linux-based attacks, but it does happen. Linux gets viruses as well. 



Linux has **multiple distributions**, which is unlike Windows. Linux has a lot of distributions. They are built on a core (based on). The differences would be in the language you would use to administer it. We will work in one distribution, and at the end of the project we will switch to a different distribution. 



Linux is managed by volunteers in the community. There was an issue earlier of people copying it and making their own distribution. They made communities where they vetted the requested changes, and then would implement all the requests in one-go. 



Linux started in 1991 with a handful of core linux distributions. Each distribution broke off, and started creating their own version or distribution. Such names are Suse, Slackware, Redhat (the distribution is based on Unix, then produced a Linux version that is free, but currently you needed a license for it later), Mandrake, CentOS (extremely popular, due to it looking a lot like working on Apple computers. CentOS is now cloud-based. CentOS 8.0 is the last local version. ) Ubuntu is probably the one we will see the most in the industry. She used to teach Fedora, she switched many years ago to Ubuntu when IBM switched to Ubuntu. There is a huge variety of distributions.  Rocky Linux was built from CentOS, which is designed to be CentOS, and completely self-hosted without resorting to the Cloud. Some are built for niche purposes, but most were built for their uniqueness.  Linux is getting more popular. She wanted to point to the vast variety. A lot of them are built off a similar core : Debian, RedHat, Ubuntu, Arch Linux, etc ... 

Anything that stems from Debian would use the Debian language. There are only a handful of languages. Some of these offshoots or forks are designed with different packages or applications that come with it. Mandrake came with a lot of database applications. Fedora has great web applications. 


Some of them are about the **purpose** or **use**.


They decide to teach us about Linux Distributions that the students are most likely to encounter them in the industry. 


She spent a summer building different linux distributions to see what they can do. We will work a lot in Linux. 


## Shells 


Shells : She used to teach the students how to write their own shells. Linux's flexibility of having it modified to comform with a purpose made it very popular to use in cyber security. 

This is what makes Linux unique. Linux exists with a number of different shells either *built-in* or can be *installed* to the system 


We have a number of different shells : 

1. BASH : default shell in Linux 
2. Bourne
3. Korm
4. C-Shell
5. ZSH


They are written by others so to enable the user to find the most comfortable home for their work. We can switch between shells if we like. You can install any number of shells. 


In cybersecurity, we would need a shell that is effecient, so we may use *bourne* shell or *C-Shell*.


We can connect to a Linux system remotely via **SSH**


We are logging in to a secure shell. It was born in Linux. It encrypts our data. It is open-source, but all of that backend sourcecode is available for anyone to look at, so this is a security issue. 



Linux is a **text-based** environment. To navigate in Linux, we need to be comfortable with an all-text environment, which is the direction we are heading to. 


**The biggest difference between Linux and Windows : Linux is case-sensitive 100%. Windows is not.**


If we have a file that we create called *file1* , and another file we created called FILE1, and a third named *File1*, in Linux's eyes, these are three different files. Linux is case-sensitive. If she asked us to open File1 :

>cat FILE1 

This will open the wrong file, as Linux is case-sensitive. Most distributions now require host names to be lower-case. In Linux, **keep everything lower-case unless it is requested to make it UPPER CASE**. 


> [!attention] 
> Everything is **Case-Sensitive** in Linux. Make everything lower-case unless instructed otherwise. 



## Commands 


> date 

	Displays the system's date


>cal 


	Shows the calender for the system


>who


	to get information about the user who is logged in


>clear


	Clears the screen


>whatis clear


	Shows information about a command


>sudo shutdown -r  

>sudo reboot



	Reboots the system


>sudo shutdown


	shuts down the system 


>ls



	Displays information about the current directory


>cd 


	Change directory


>cat



	Displays the contents of the file on the screen




Question : Which editor ? 

Answer : In the Advanced Linux class, we will learn *vim*. *nano* now comes with most distributions, as it is the most popular. She will use it.




## Assignment 



This assignment is designed to get us the kind of environment that we need. We are going to set up a current version of Linux. We will install **Linux Mint Workstation - Victoria - Cinnamon Edition ISO**. 


> [!error] 
> If you are using a Dell computer, you will have to do this assignment on the Workstation that we have in class. It is a conflict with the current processor on Dell systems.  If you can get it working on Dell, that is wonderful, although there has been a multitude of glitches and errors. 



**Linux Mint** is based on **Ubuntu**. It is a distribution that is used in teaching Linux. *Cinnamon* the Desktop Environment. 



Note that instructions on how to create a virtual machine from the previous assignment : 


If you get prompted with a message pertaining to the iso, select NO.



After it is installed, navigate your way through the *Welcome* window. Select the theme you like, switch the local mirror, which is a site where you can download additional resources. We do not want the default mirror, so we will switch to Dalhousie or the University of Waterloo. Victoria is the version of Linux Mint, Jammy is Ubuntu version(which is the base). 


Do NOT reboot the workstation. Go through the welcome window. Modify the network, give it a static IP. Take a screenshot so she can see if the changes are correct. 


We will install LibreOffice Full Office Productivity Suite. We will finish with the *Welcome* screen. We will restart, and then test LibreOffice by creating a new document. 


Then, we log back in, create a follder on the desktop, take a screenshot of the folder, change the background, when taking the picture of the desktop, make it large enough for her to see that we changed the background 

Run the following commands : 

>hostname
>whoamI
>timedatectl


Go through *LinkedIn Learning*, which teaches the Linux Command-Line. Watch the Introduction, download the exercise files into the documents folder. 





# Assignment 3 : Instructions 



  

  

**Task 1** **- Install a Linux Mint Workstation.**

  

_Client Specifications and guidelines:_

- Create a virtual machine with the following specifications:
    
- Guest operating System = Linux / Ubuntu 64-bit
    
- Virtual Machine Name = YourInitialLastName+-CL02
    

(Example = MDutka-CL02)

- Drive = 1x 60g (split virtual disk)
    
- Memory = 8G
    
- Processors = Processors x2, Core per processor x1 (Total processor cores = 2)
    
- NIC x1 (NAT)
    
- Modify the Virtual Machine Description to list (_you will need to read ahead for some of the information required_):
    

- Operating System:
    
- Creation Date:
    
- Hostname:
    
- Default User Name:
    
- Default User Password:
    

- **Stop**. Take a screenshot of your VM settings and description.
    

  

- *Start Linux Mint 21.2 Cinnamon 64-bit
    
- **Install** **Linux Mint**
    

Hint: run the cd on the desktop.

- Select the following:
    
    - Language = English
        
    - Keyboard = English (US)
        
    - Do not install multimedia codecs
        
    - Erase disk and install Linux Mint (Install Now)
        
        - Write the change to disks? Continue
            
    - Location = Halifax
        
    - Your Name = YourFirstName LastName
        

(Example = Marie Dutka)

- Your computer’s name = cl+yourinitials(x3)+02 ****all lower case**
    

(Example = CLMAD02)

- Pick a username = YourFirstInitialLastName ****all lower case**
    

(Example = mdutka)

- Default user password = Passw0rd
    
- **REQUIRE** a password at log in
    
- Do not select any optional music, video, etc. apps. **SKIP** them.
    
- Restart or Shutdown your VM
    
    - If prompted to Remover your CD and hit Enter, shutdown your VM and remove your ISO from your CD/DVD but setting it to use the physical drive:
        
    - Select No for the following prompt.
        

![](https://d2l-docbuilder-prod-ca-central-1-converted.s3.ca-central-1.amazonaws.com/8208e7eb-8a6a-4371-8e23-d4de75bf2487/b7c9ee4430e05a151a505fe5c88cb1ef_html_b5d5133a92540b29.png)

- Log into your new Linux workstation.
    
- On your Welcome to Linux Mint screen select Let’s go!
    
- Launch your Desktop Colors and select a Theme, feel free to poke around and see what options are available for you to modify. When you have made your selections close your Theme window.
    
- Launch your Update Manager, select OK to update your system, make sure to apply **ALL** updates suggested.
    
- Switch your local mirror to
    
    - Main (victoria) = University of Warterloo
        
    - Base (jammy) = DAL
        
- Do NOT reboot your workstation at this time, we will do that shortly.
    
- Launch your System Settings
    
    - Open your Network
        
    - Modify your Wired settings for **IPv4** as follows:
        
        - Addresses = Manual
            
        - Address = 192.168.208.20
            
        - Netmask = 255.255.255.0
            
        - Gateway = 192.168.208.2
            
        - Add a second DNS and complete in this order:
            
            - DNS = 192.168.208.2
                
            - DNS = 8.8.8.8
                
        - Do not make any other changes. Apply your IPv4 settings.
            
        - Turn your network interface off/on to apply the new settings.
            
- **Stop**. Take a screenshot of your system Settings / Network / Wired Settings, and add it to your documentation. See example in Appendix A.
    
- Launch your Software Manager, under Office install LibreOffice (office productivity suite). After the install just close your window (do not launch Libreoffice).
    
- In your Welcome windows / Documentation, Launch New Features. Review some of the new Features included in this version of Mint.
    
- Now that we are finished with our Welcome window, uncheck the box “Show this dialog at startup”.
    
- Restart your Mint workstation to complete any updates from our previous install.
    
- Test your LibreOffice by opening creating a new document in LibreOffice Document Writer called “YourFirstName LastName” and save it to your documents folder.
    

(Example = Marie Dutka)

  

  

  

  

  

  

  

  

  

  

**Task 2** **- Linux Mint Workstation more modifications.**

  

  

- Log into your Mint workstation
    
- Right click on the desktop and change your Desktop Background. Select any colour or image available.
    
- Right click on the desktop and create a new folder (on the desktop) that is named = YourFirstinitialLastName
    

(Example = mdutka)

  

- **Stop**. Take a screenshot of your new folder on your desktop, include a portion of your desktop to show you change. Add your screenshot to your documentation.
    
- Right click on your desktop and select Open in Terminal
    
- Type the following commands and **capture** the results in a screenshot. See Appendix A for example.
    
    - hostname
        
    - whoami
        
    - timedateclt
        

  

  

**Task 3 – Preparing to work with command line.**

  

- Log into [https://www.linkedinLearning.com/](https://www.linkedinLearning.com/) and find the video called **Learning Linux Command Line** by Scott Simpson and, if necessary, start up your virtual machine to follow along. [Learning Linux command line (linkedin.com)](https://www.linkedin.com/learning/learning-linux-command-line-2018/learning-linux-command-line?autoAdvance=true&autoSkip=false&autoplay=true&resume=true&u=2149225)  
    [https://www.linkedin.com/learning/learning-linux-command-line-2018/learning-linux-command-line?autoAdvance=true&autoSkip=false&autoplay=true&resume=true&u=2149225](https://www.linkedin.com/learning/learning-linux-command-line-2018/learning-linux-command-line?autoAdvance=true&autoSkip=false&autoplay=true&resume=true&u=2149225)
    

  
  

- Watch the **Introduction**, download the exercise files, and move them to your Documents folder. See example in Appendix A.
    

  

- **Stop**. Capture a screenshot similar to the example image to show your Exercise Files folder, LibreOffice document and location.
    

  

  

**Task 4 – System Management and documentation**

  

It is important to keep an up to date copies that include of all changes and modifications made to your workstation so we can have a reliable copy available as backup.

  

- Take a final VMWare snapshot of your workstation called “PostA3” in the **OFF** state.
    
- **Stop**. Take a screenshot of your VM snapshot
    
- Create a new “**Gold**” copy of your workstation.
    
- **Stop**. Take a screenshot of your new “Gold” copy with required details
    
- Add all your screenshots and research responses to your professional document
    
- Confirm all screenshots, questions, summary tables, and sources are included in your documentation.
    
- **Make sure to follow all requirements for Screenshots, research and document professionalism.**
    
- Upload your Professional Document to BrightSpace.
    

  

  

  

## Checklist

  

|   |   |
|---|---|
 
||**Linux install and configuration**|
|5|**Screenshot of correct VMware settings and description.**<br><br>- Drive = 60G<br>    <br>- Nic = NAT<br>    <br>- Memory = 8G<br>    <br>- Processors Total = 2<br>    <br>- VMWare description includes:<br>    <br><br>- Operating System:<br>    <br>- Creation Date:<br>    <br>- Hostname:<br>    <br>- Default User Name:<br>    <br>- Default User Password:|
|5|Wired network settings image contains correct details.<br><br>- Addresses = Manual<br>    <br>- Address = 192.168.208.20<br>    <br>- Netmask = 255.255.255.0<br>    <br>- Gateway = 192.168.208.2<br>    <br>- Add a second DNS and complete in this order:<br>    <br>    - DNS = 192.168.208.2<br>        <br>    - DNS = 8.8.8.8|
|2|Screenshot of desktop folder and partial desktop.|
|3|Screenshot of required commands with correct results.<br><br>- hostname<br>    <br>- whoami<br>    <br>- timedateclt

