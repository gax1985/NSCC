


We will cover **components of an OS



## Components of an OS


#### OS 

	It is the base layer software that manages computer hardware andf software resources, and provides common services for computer programs. 


##### Components of an Operating System :


1. Process Management
2. Memory Management
3. Storage Management
4. I/O Managfement
5. File Management
6. Security Management
7. Networking
8. Command-Interpreter System 



#### Process Management


When the OS is running, it is running a number of processes


In Task Manager, we see all the processes that are running (CTRL + SHIFT + ESC)


The **Process Manager** creates , schedules and terminates processes. It also allocates resources, and allows for the execution of multiple processes simultaneously. It insures fair usage. The **kernel** is responsible for the management of processes. 



#### Memory Management Unit


MMU, controls the allocation and deallocation of memory for processes. It insures efficient memory utilization, handles memory protection, and enables virtual memory management. 


#### I/O System Management


Interface between the person and the system. It controls communication between the computer and external devices. It handles device drivers , I/O requests. 



#### File Management


Creates a hirarchial structure, handles the creation, deletion and relocation of files.  



#### Security Management 


Manages the security of resources, data and user privacy. It includes **authentication, access control, encryption and other security features**. Root kits stand in the way between the kernel and the user. They would be at the root of the computer


#### Network Management


Handles the network interface configuration, IP addresses and routing. 

### Command-Interpreter 


aka Shell. It can be GUI, and it provides a user interface to issue commands for the system.  It executes commands issued by users. 



#### Kernel 


The core of the OS, and has complete control over everything. It is between the hardware and the applications. It is the porition of the OS that is always resident in memory and facilitates interactions. 



There is a tool called Device Manager in Windows. It shows all the hardware, and the corresponding device drivers. You would see virtual and physical devices both with their own drivers. The application facilitates the installation of the driver 


A lot of cybersecurity threats are at the kernel level. They have been on the increase lately. Based on ovservations in TrendMicro,  the number of threats and other events. 



If attacking at kernel level, 

pros : 

1. gaining high priviledged access to the system 
2. Hiding malicious activities on devices, and making detection and response more difficult
3. Protectiong malicious artifacts from normal system filtering processes
4. Execurting stealth operations that bypass detection

cons :
1. Development is expensive
2. Sensitive to errors : If someone came up with a similar OS to Windows, and it could reveal its presence with error messages 
3. Involves highly qualified kernel-mode developers who understand the OS' internal componenets and sufficient lvelel of competence with reveseve engineering. 
4. Since rootkits atre more sensive to errors, they may reveal the whole operation if they crashed to a Blue screen 


### Most common OSes


Windows : Introduced in 1985
Unix: Introduced in 1969
macOS : Introduced in 2001. You do not see them too much in the corporate environment. Microsoft took the lead. You can get Microsoft products for Macs. If concerned about cost and usability, you would use Windows machines. It would be different in graphical design, video production, music production, publishing etc. 

Linux is more common for IT personnel. If someone wanted Linux on their work machine, they would not have any assistance, and would have to rely on themselves. 


Servers : Linux is king in that domain. One of the reasons is Windows servers are not as reliable as 

Linux servers, especially memory management and memory leaks, some obscure issues , etc. Linux servers can run for years. Since it is open-source, a whole community would work on this issue. 

Chromebooks : not used as workstations often. They can be used as a thin client, since they are mostly for web applications 



### Microsoft Windows 


Before Windows, there was MS-DOS

Windows 1.0 1985 - 1st Graphical Interface to MS-DOS with limited functionality 

Windows 3.0 1990 : More refinded GUI, better mulltitasking, and support for a wide array of applications. Made Mictrosofft a leading provider of OSes. 

Windows 3.1 1992: improved performance and introduced new features like TrueType and multimedia support. 


Windows 95 1995 : Introduced a more modern and user friendly interface with a Start button and taskbar. Also, it came with long file names.


Windows 98 1998 : improved stability and support for USB

Windows Me 2000 : enhancements for media

Windows XP 2001 : targheted at businesses and greater stability security and networking 

Windows VISTA 2007 : more visually appealing , but suffered from peerformance and compatibility issues


Windows 7 2009 : addressed tghe many issues of Vista and became highly regarded

Windows 8 2012 : touch centric interface for tablets and touch devices 

Windows 10 2015 : More streamlined and modern interface, Cortana's voice assistance, and introduced Windows as a Service with regular updates and new features over time 

	(Nowadays, it is better to use Windows 11. One has to plan it well when it comes to the applications' requirements)

LTSC version would be good for embedded systems, or systems that you would not like to keep updating regularly. A Long-Support version


Windows 11 2021 : Windows 10 is easily upgradeable to Windows 11. It refreshed visual design,  enhanced productivity features 



#### Windows Workstations 


They are designed for a single-user, multitasking system. 

Windows server in comparison is designed for multiple simultaneous users in mind. 

if we press CTRL + ALT + DELETE, we will see the option to switch user. 



### Kernel 


HAL ( Hardware Abstraction later )

then 

Kernel 




Hardware-Abstraction Layer : 


It is a software component translates communications between hardware devices and applications


Graphics Drivers :

Handles the GUI. 

I/O Manager :

Infornces security, and handles I/O regulation


Cache : 

Places things  used often in memory for a short period of time


Object Manager :


Manages executive objects


When plugging a device in, we get a notification about it at the botton right cotner



Power Manager :

Designed to reduce power consumption when idle. It is trying to save energy. 



Task Manager :


We can right click on a process and choose to end the process. We can also kill the process with the process ID. 


Process Configuration Manager : 


Handles all the configuration for the system



Environmental subsystems : 


He is running the Explorer command. There are environmental settings. There are paths set up in the environment, where it governs where system applications are loaded 




### Unix OS 



Powerful and versatile OS. It was originally developed in the 1970s. It offers a hierarchical file system and a CLI for interacting with the system 


Unix introduced many fundamental concepts and features used in modern computers. 


Shells in Linux like BASH or zsh are similar to PowerShell 



### Linux OS 



It is a family of OSes based on the Linux kernel. 


Linux was developed initially by Linux Torvalds in 1991 and released as free and open-source software. 


They are multiple user interfaces such as Gnome or KDE Plasma. 




### MacOS


Made by Apple. They integrate well with other Apple devices and services. Features lioke Continuity allows users to ask a task on one device and continue on another. 


It is closed source, and locked down. It places a strong emphasis on security and privacy. Apple watches all...





We covered types of hardware, OSes , 


We will do a deeper dive in Windows like file manipulation, process manipulation, VM install in VMWare for Windows , later the same thing in Linux. We will do POwershell in Windows and BASH scripting in Linux. 





