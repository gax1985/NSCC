


We are getting deeper into VMWare , then installation of Windows, then Folder Structures, then Networking Shares. Keeping Backup copies and snapshots is going to be critical for this course. 



#### Assignment 1 


We will be using ....


###### **Windows 10 Educational Edition 22H2**

	it refers to version their  Windows by using a number that makes no sense. Then , they decided to version it in a way  based on the year(1st half of 2nd half, thus, 2022 Second Half)*


There is a Windows 11 Issue that is still present. Windows 10 is the most likely to be encountered in the field. 

KMS Key : Industry-standard for licensing Windows. Understanding this industry-standard way of confirming validity of licenses and comparing it to the KMS)

Most medium to large companies use : 


KMS 
	Goes to licensing server. It mentions the key, and the server confirms by confirming version, approved machine (MAC adfdress) , you are on our network., and thus you are approved. Someone can not license a rogue machine as it would need to meetr a whole lot of qualifications. 


Non-KMS
	The key that is ours forever. In order to license KMS, you need to be on the network, and then you can function on your own. 


Azure Key : 
	To be used once. NSCC's licensing with Microsoft is based on the number of members of the organization. It does not matter if NSCC chooses Windows NT , Windows Server, Windows 10 etc ... The key we have used with Azure is done for this year, but they can change it to be licensed with the KMS key. If you are not using it, you can submit a ticket, and they can reissue a new key for you. 


Qestion for AI : 

	Could you please explain KMS licensing with Microsoft, and compare it to the NON-KMS licensing with Microsoft? 



	One key to be used on a set number of machines . Rogue machines would have different license keys that are obvious







In the assignment, it mentions to look at the resources. This is just to give us some resources to glance over as a reference point. 


In the 1st one, the highlighted colors . She would guide us normally in setting up the virtual machine 

2nd part is doing the Windows 10 Education installation

Then we activate Windows with the KMS key




#### Virtual Machines


Beauty of Snapshots! 


VMWare-exclusive feature


Hyper-V has Checkpoints

Virtualbox has a snapshot feature? 


###### Gold Copy

What is it ?

	A nicely-configured copy of a virtual machine that you never run directly, but copies would be made of it. It is stored away from the drive in use. 

**VM Corruption** happens all the time! Thus, make **Golden Copies** of all your virtual machines!

It is a backup! 

### What not to do with a Gold Copy

Everything we do on a machine impacts it. Every time we log in, there are files times and logs we will be looking at. We never do with a gold copy is starting it up. If we want to use it, we make a gold copy.  


Portable drives or laptops are not inheritly-secure environments, so there is a higher risk of corruption and damage. 


Question : How many work on a laptop and you close it and put it in a bag without shutting it down ?

Answer : Never do so. Why ? the battery can die even in hibernation. Also, static electricity, as it is technically still running, and heat from the system. Windows is set usually to automated updates, and the machine would not have an easy time in updating the system, and thus leading to corruption 

Do NOT put it in bags while running 

Do NOT plug it in to charge until you have to 

Unplug it at 80% 

Mac batteries explode


Every battery has a set number of charges, same as a projector, but it does not mean that it provides the service for so long. The battery is designed to have 250 charges. Every time you plug it in, your battery would most likely quit holding a charge, but then you would have to plug it in all the time to have it working. You can buy replacement batteries that are generic. Some phones have a built-in battery preservation settings. With new laptops, they encase everything in one solid piece, so now we are not able to replace batteries now.



### How to make a copy of a Gold Copy


Right click on the folder




### VMWare 


The License key is good for one year!
VMware workstation is already installed on our machines


##### The Slides


Need to know : 

Creating ? 
Opening ? 
Connecting to a Virtual Machine ?


When VMWare creates the machine, the computer does not know it exists in a virtual world. The only entity that knows is VMWare, which is the *Virtualization Host*. 

We have to decide how we will create a virtual machine 


When we do this together, we choose **Typical** it decides some of the options for us

VMware is a Type-II Hypervisor. VMware's Type-I Hypervisor is ESXi. 

Next Option : "Install from a Disk ... or .... Installing from an ISO (what happens is when Windows gets installed, it asks a few questions. We pick and choose what we want, and the choices we make. It will not ask us the same questions, it will look at the host, see what the registry is, and use that. We wish to have full control over decisions involving our machine.  ) I will install the operating system later"  -------> I will install the Operating System later. 


Next : What type of guest are you installing ? 

- [ ] Microsofr Windows
- [ ] Linux
- [ ] VMWare ESX
- [ ] Other

Then a dropdown list with specifics from each OS. It is not overly specific such as "Windows 10 X64 Environment"


Next : Naming the Virtual Machine 

Enter the Virtual Machine's name 

		MordorIsCalling

Decide the location of the Virtual Machine (so we can copy the Golden Copy):

	E:\VMs 

By default it will install UEFI , but one can choose BIOS


Every computer when you install it and turn it off, and replugging it in, it will still load Windows. How do computers remeber what to do when you turn them on? They had : 

#### BIOS 
			A little chip that stores all the basic information about how to start the computer, where the GPU is etc. ..
			BIOS that stores it is powered on 24/7. The machine is getting power from the electrical outlet anyway. 
			There is a battery on the motherboard that powers the BIOS.



#### UEFI
			Orighnated from Macs. Macs are built well to communicate and connect together because it is exclusive. Windows does not have that , so all the parts may not necessarily work well together, so they need different instructions. One of the things Microsoft did was to move into the realms of "Auto-ON"; a special lab environment that we try to build the links and put it on the OS. Sometimes we get "This is not a signed driver". Why start anything from the beginning of the BIOS? why not start what we need?  It is not essentially faster but you access your data faster. Why do printers have to load when the machines are starting up ? UEFI can add the Secure Boot option which adds an extra layer of security. The simplest way to put it : if the user can not log in, do not log me in until I have successfully logged in the machine. There is a lot more to this. 


#### RAM 


1000mb =/ 1GB 

It takes 1024MB to equal 1 GB.

This is important because we will come across a lot of things where you have to recollect the equivalent of 1GB in MBs for example (1024 is a core number)

8GB = 8 X 1024


#### Network Connection 

We will not set up anything in **Bridged**. We need to keep it **Internal**.



#### IO Controller Types 


LSI LOgic 


#### HDDs 

NVMEs
	They are picky


How large would you like the hard drive to be? 

	In the assignment, it is 150GBs.
	
In VMWare, it does not allocate the storage immediately, and it can do a ballooning drive setup, where one chooses the maximum size. 

We should split the hard drives into **separate files**. It is easier to move 50 small files in comparison to moving 1 gigantic file.  


#### CD-ROMs

We will add the drive after the creation of the machine. 



###### Once we have created the machine, we always have the option to *Edit the Virtual Machine*


BIOS vs UEFI 
	If we set up a virtual machine in either BIOS or UEFI, we would not be able to switch it back and forth if the machine has already been started. 


She mentioned an example of going back to a virtual machine to see a tool used in Kali Linux



### VMX

We are 5 lines. 4 of them involving skipping checks and for the machine to start as quickly as possible. 


#### Snapshot

	It is creating a roll-back point.

She will ask us to take a snapshot at the end of every assignment. When we do complicated things in our virtual machines, we should take them more frequently in accordance to the complexity of the task. This way, we would not need to start over again and again. 


Rolling back in Linux is not easy. It is simple with Snapshots, but so simple with actually installing things over again. 


Most likely to get corrupted in virtual machines are the **Virtual Hard Drives**. 







On Tuesday next week, she has a Phone Call with her Doctor. She may have to run and answer the phone