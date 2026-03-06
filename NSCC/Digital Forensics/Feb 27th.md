

When making a Logical Image of a drive in FTK Imager, the folllowing are not included: 

1. Boot Partition
2. FAT Table
3. INode Table
4. Unallocated Space



We would want to get Logical Images of Physical Drives, which will yield the entire filesystem itself (meaning all the files and folders). 


When looking at unallocated space, the retrieved deleted files' names are not listed, due to the Logical Imaging process being concerned with the files and folders, and it skips the FAT Table. 


When using FTK Imager in a Windows VM : 

1. Plug in the drive.
2. Wait for the message prompting you to select where to connect the drive to (*Guest* or Host).
3. When the drive is plugged in, select "**Add Removable Drive**"
4. You can select ****Physical Image*** (which is bit by bit image), **Logical Drive** (the filesystem). We would see the following : 
   
   ![[Pasted image 20260227112424.png]]
	Unallocated Space 

![[Pasted image 20260227112504.png]]

The **EFI Partition** is the connection betwee the *firmware of the machine* and the *operating system*. This is a potential quiz question on the Disk Forensics Quiz. You do not have to know it to great depth, but you should know its name. 

We have the **Microsoft Reserved Partition**, which is 16mbs in size: 
![[Pasted image 20260227112728.png]]


Microsoft Reserved Partition is for recovery partitions. **MFT** is **Master File Table**

If we go into the root directory (**C**) .We are not looking at the sectors, but we are looking at the tables that the files are a part of : 

![[Pasted image 20260227113028.png]]

This is the methodology for getting a Logical Image.


How many sectors does a block use ? --> 1 or more. 


FTK Imager has to know the byte offset from the beginning of the drive in order to find the partition in the command line. 

We need to figure our how many bytes from the beginning of the drive to find the partition in question. For example, if the partition begins from a particular sector, it still needs the offset. We can use *diskpart*


Sector Number x Block Size = Byte Offset 


Ron will do a **physical image** of the drive, but we can go a **logical image** in Tsurugi. 

File --> Create a Disk Image --> Physical Drive --> Choose file format (E01) -> Enter :

Case number (W01)
Evidence Number 1 
Hard drive from suspect 1 main computer
Examiner : Ron McLeod
Physical Image of that drive
Image File Name : {case number}_1(evidenceitem)_1e01
Image Fragment Size : 1500 MB
Compression (0=None (fastest of all),  1=Fastest actual Compression , 9=... ) he chose **6**
Check "Verify images after they are created" + Precalculate Progress Statistics + Create Directory Listings of all files in the image after they are created. 



---
Create a Word file
Add the Case Number to it
Add Notes identifying the drive, add description and other information 
As you are doing your image, you are recording your steps in the Word document. 

1. Mount the drive
2. Drive name as it shows up
3. Select the Drive
4. Physical Image --> gave it this name, has this mbs for segments, uses this comrpession ratio, saved it to the folder so and so
5. Add date-time-location to every step. 
   
Add as much detail as possible, as others will be poking through any undocumented steps. 

Quiz Question --> which file format do you use ? we use **E01**. Each type comes from the manufacturer, except for *RAW*. The image formats bring abilities such as adding notes and so on. the RAW image format does not. NCase format E01 is the chosen one.   

---
Requirements : 

Make a Physical Image of the drive


Due date : **Next Class** 

In order to get to the data offset of the partition, you would need to go to the **Byte Offset**. 
When FTK Imager names a drive, it will be like this :

**SBC** -> This is our target. 
	SBC1
	SBC2

In Linux, to mount a drive : 

1. Connect the drive.
2. Make sure you see it.
3. mkdir "/media/foldername"
4. Mount SBC to folder. 