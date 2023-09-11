

### Hardware


Before computers, the term was from the early 17th century, which means : *something/one that computes*. 


The basic functions and features of a computer:


###### Input :


Sensors, keyboards, mice, etc (anything that takes in input from the user/machine)



###### Output :


Where the information gets directed to


###### Processing : 


The parts which do the processing 



###### Components of an office :


1. Files kept in cabinets --> The cabinets is for storage of files not in use ---> modern equivalent : Hard drive
2. Pens and pen-holders ---> your input device --> Modern equivalent : keyboard + mouse, touch screen
3. Desktop --> where you put the files that you are working on.  
4. Document stand --> where you keep the files you are working on



### Hard Drives 


###### Hard Disk Drive (HDD)


		It is a mechanical drive made up of magnetic platters and read/write heads


###### Solid State Drives (SSD)


			Like other forms of memory, it uses chips to record data, and it does not have magnetic platters and read/write heads that need to physically move. They are more expensive than HDDs. The SSD is much faster and less prone to failures than HDDs. 


	We can turn on TRIM to improve performance



### Random Access Memory (RAM)


		Temporary memory. The memory gets wiped when the computer is shut down. It is random because any portion of the memoryt can be read without reading the preceding memory (hence, Random!). It requires power, and when the power is removed, the data is removed. The read/write speeds are very fast!


##### Types of RAM : 


**SIMM 

	Single inline Memory Module


##### DIMM

	Dual Inline Memory Module 


Question : compare SIMM and DIMM



### ROM



###### Read-Only Memory


The information is permanent. It can not be written to by users. It contains the start-up instructions/firmware 


### BIOS and Unified Extensivle Firmware Interface


###### Legacy Boot


Window Boot screen
no graphics
Cant recognize Ethernet. WIFI or Bluetooth 
No remote diagnosis and repair
No mouse support
No Secure Boot
Firmware program in 16-bit assembly language
Supports drives up to 2.2 TB


###### UEFI

User friendly
Support Networking (WIFI Bluetooth
Remote diagnosis
Keyboard/mouse
Secure Boot
Firmware program in 64-bit C language
Supports drive sizes up to 0 zettabytes


Question : Thin clients and UEFI vs Legacy Boot.


### SWAP Storage


Let us assume we have our desktop, and we are running out of space. I need to run the cloud, but I am running out of RAM memory. Swap storage is taken from the solid-state hard drive, and it is used to overcome the limited RAM memory. It takes a section of RAM storage from an idle program and frees up memort for other programs. 

Example : at the root of our hard-drive (C Drive), we can right click on it in Windows, and then select Properties. We see the option to optimize the drive. There is an option where we can view all of the files. We would see the SWAP file listed on the drive. The PAGE file is also a SWAP file. System files are mostly hidden. We can enable the viewing of extensions in Explorer as well. 


We will took at the differences between Bits and Bytes. 


In Task Manager, we can see how much memory every application is using. We can sort the applications by CPU use. 




### CPU


			Central Processing Unit


It does logic control, math. It is referring to the central processor. We used to have single-threaded processor, and now we have hyperthreading. The number of cores increased dramatically. The more cores we have, the more parallel work we can do. 



### GPU


			Graphical Processing Unit


It can be build into the motherboard or a separate card. it is a silicon-based microprocessor. The GPU tends to have a lot more cores than a CPU ( it can be thousands). When doing AI work or high-end graphics, the GPUs are champions. The lalrge number of cores can enable more math and geographical chops than CPUs. 


##### CPU vs GPU


Serial vs Parallel : 

	We have a lot of pipes to transfer information from point A to point B . Parallel in comparison is able to handle thousands of tasks and process them at the same time via multiple channels. Serial cables/Universal Serial Bus (from the olden days)

###### CPU : Generalist component, it handles main proicessing functions of a computer. Core count is a max of 64 cores. 

GPU : Specialized component, handles graphics and video. Core count : thousands!



### Ones and Zeros 


On | Off


All the communication is done based on the on-off cycle

It is either zero volts or 5 volts (typically). The language computers speak in is binary \

HEX : 0-16  | 0123456789-ABCDEF

He mentioned that in HEX, since numbers are from 0123456789-ABCDEF, at the end of the cycle (after 15), we just add a 1 and a 0 --> 10, then we keep adding the new cycle next to the 1, so 16 would be ....

Question: Could you explain what happens in HEX after reaching the end of the cycle (0-15 digits, 0123456789-ABCDEF)

He mentioned he did a senior project to program a CPU in HEX. 



### Bits and Bytes


1 byte = 8 bits 

0001 = 1 Bit  |  1000 = 1 Byte

Memory is discussed in Bytes ---> 500MB = 500 MegaBytes
Speed is discussed in Bits ------> 100Mbps = 100 megabits per second
0100 0000 0000  Binary = 400 Hex =1,024 Dec
1KB






Note : Hibernation file is on the root of C:\. Sleep stays powered on and stays in RAM, and consumes battery. The Hibernation file is for saving the currewnt state of the computer. It will dump the RAM memory into the file. The page file is on your drive acting as RAM!



In relation to the office example , we have **Folders** where the files stay, **Shortcuts** are placeholders pointing you to a file. If the icon does not have an arrow, it is either a file or a folder. The **Desktop** is a folder that is representative of what you have on the desktop, usually files are hidden on the desktop if they are system files for example. 



### The Graphical Representation of Computer Components



USB Connectors, RAM, Modem, Motherboard, GPU, cooling (radiator + fans), hard drives + SSDs (In the olden days, if you are trying to shutdown the computer, you had to issue a command to lift the reading head off the internal disk layers in a HDD). Degausing is with a magnet taken next to a HDD or magnetic tape storage. 


###### The Motherboard


Where the CPU sits. It has buses ---> pathways between the different components. The CPUs have CPU coolers. Newer computers have liquid cooling similar to a car's radiator. A lot of the motherboards will have a network adapter/USB adapter. The CPU's yellow dots are CPU pins. The cards slot in different types of slots depending on the card. A sound card is an output device. Network card is an input/output device. 


###### Desktop 

Not recommended as a file storage, but it is usable since the desktop is a file folder in of itself.


In the corporate world, storing files on the desktop is a terrible idea. Files are hosted remotely. With OneDrive, the auto save option is there. If we are working with a Word file, and needed to make some modifications, the auto save will kick in automatically, and that could lead to losing changes. The old days had manual saving since the file itself is local. There is a versioning option now , so we can restore the file to a previous state. The cloud infrastructure is helpful since it provides redundency. The desktop does not get backed up. If we are storing files to the desktop, and the system gets flooded, you would lose all the files you placed into the desktop. The desktop is not a safe place to store the files. If My Documents is local, and there is a conversion process to the cloud infrastructure, they will not be copying files from the Desktop. 


###### Motherboard 

Motherboards can die. Computers running in dusty environments would cause dust to cling to electronics. Chip Keep --->  Computers turn on and off, computers cool off and warm up. 10 years ago, you would tell people to leave the computers running, due to the metals inside expanding and contracting when on and off. If the fans stop spinning, cool air is not reaching the components. Thus, it is a good idea to keep computers away from dusty environments.

##### graphics card


not likely to send a broken GPU to be repaired. Everything is soldered


Back in  the day, computers had a Turbo button, which boosts the CPU's power.


### NVME


Non Volatile Memory Express : faster than regular SSDs. The newer type



Thin clients would not have an HDD. 


### Form Factors 


It is the size of the device. Used for hard drives, floppy drives. If we look at the front of the computer , CD roms is 5.25 form factor. Hard drives would be 5.25 slots, 3.5 inch slots. Floppy drives 5.25. Laptops --> 2.5 inch form factor

Question : Footprint is used for the desktop, but is it used to the parts inside of it. 


Desktops would have full tower , slim desktop.s , etc. 

Form Factor is a measurement. 


In a server rack, what is the typical width of the device ? 19 inches. Server racks have certain heights : 19 inches. The thickness is how many slots it has. It is measured in Us : 1U (server, switch), etc. When planning a server rack, you need to calculate how tall the rack will be. If we are discussing 1U, 19 inches wide and just as deep as they are wide (at least 19 inches)





Next time : We will be looking at Windows' components. No assignments for this week, but next week we will have a quiz on computer components. We will also discuss users and sharing. We have done the hardware, so we will do the software next. There is no book, but we can look up information if we need to. Wednesday next week is the quiz. 
