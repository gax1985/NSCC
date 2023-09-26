


There has been major changes for the course. 


The link to Brightspace is : 

[https://nscconline.brightspace.com/d2l/le/content/280898/viewContent/4268979/View]

The course plan in a nice Markdown note is available 🗒 : [Course Plan]

The majority of the systems we will encounter will be **Windows-based**, but we can guarantee that the organization will have at least a few **Linux-based servers**.



#### Assignment 1 


We will be working in virtual machines a lot. 


Included is the **link** :[https://nscconline.brightspace.com/d2l/le/content/280898/viewContent/4268985/View] 

and the **Assignment 1 Description** :


Page

**OSYS 1200 – Intro to Windows Administration**

**Due: As per Brightspace**

**Assignment 1: Windows Installation and Installation Types.**

Install Windows 10 into a virtual machine, stored on your external hard disk drive. Install various software. Create a snapshot, install log and “Gold” copy.

  

**Purpose:**

For a variety of reasons, we cannot be administrators and do administrative work on college computers. So, we will emulate a physical Windows 10 computer using a virtual machine and we will do our administrative work on that instead. This will give us the ability to modify the operating system and make changes - and sometimes mistakes - without affecting the other students who use these lab computers.

  

**Required Resources**

- VMWare Workstation from https://nsccvm.onthehub.com/
    
- Windows 10 Educational Edition 22H2.iso from Azure for Education
    
- NSCC Lab KMS Key - As per [Key Management Services (KMS) client activation and product keys for Windows Server and Windows | Microsoft Docs](https://docs.microsoft.com/en-us/windows-server/get-started/kms-client-activation-keys)
    
- External hard disk drive
    
- Course Resources as posted in BrightSpace
    

  

**Professional Documentation**

All documentation must be done in a **professional style**. It must include:

1. Title page
    
2. **Updateable** Table of Contents
    
3. Document introduction
    
4. Section introductions or description, each section must be clearly identified
    
5. Graphics or screenshots MUST include a title with a short description
    
6. Any direct or copied quotes or graphics MUST be properly credited in a footnote
    
7. ALL sources MUST be properly cited (APA format) and placed at the end of your document in a bibliography.
    
8. **NO** embedded, zipped or compressed files. ** All scripts must be converted to text before including them in your documentation. **
    

***1 Professional** **Word** **Document ONLY.**

  

**Research and documentation sections** - Please complete all research and question responses in your own words. Research sections not completed in your own words may result in a mark of 0 for the section.

**NOTE:** Please do NOT copy and paste responses from internet, **even with a citation**. I expect each section or response to be in your own words. Be prepared to explain your responses and demonstrate your comprehension during the marking period.

**No marks** will be given for cited or credited information included in document.

  

**Marking and Assignment Notes:**

- Screenshots MUST include user or device identifying information.
    
- Screenshots MUST be added to your document in the order of creation.
    
- Documentation must meet Professionalism requirements.
    
- **Automatic mark of 0 - Assignment not submitted or work not original.**
    

[http://www.nscc.ca/docs/about-nscc/policies-procedures/policy-studentcodeofconduct.pdf](http://www.nscc.ca/docs/about-nscc/policies-procedures/policy-studentcodeofconduct.pdf)

[https://www.nscc.ca/docs/about-nscc/policies-procedures/policy-academicintegrity.pdf](https://www.nscc.ca/docs/about-nscc/policies-procedures/policy-academicintegrity.pdf)

  

**NOTE: This assignment may require some adaption, research and troubleshooting.**

  

  

**Task 1: Support Documents and Presentations**

  

Review the following presentations, walkthroughs and/or videos in BrightSpace:

**Module 1 Resources**:

1. Azure for Education at NSCC
    
2. Intro to VMWare
    
3. Capturing and Documenting Screenshots
    
4. Table of Contents and APA Citations (Creating an Automatic Updateable Table of Contents and Citations in APA Format)
    
5. Academic Integrity and research resources (how to use and recognize acceptable resources such as **ChatGPT**)
    
6. Create a Meeting Request with Outlook
    

  

  

_Note:_ _Throughout this assignment you may be asked to produce a series of screenshots. Please make sure to include a_ _**label and brief description**_ _of each screenshot added to your professional document in the_ _**order requested**_ _in assignment._

  

example. Task 2 - Virtual Machine settings

  

  

**Task 2: Creating your first virtual machine**

  

_**ATTENTION**_**:**

- _Indicates steps and activities that we will complete in class. If you are NOT present during the walkthrough class you will be expected to complete these steps and activities on your own as part of your assignment._
    

  

Create a new virtual machine following these specifications:

- Do a Typical configuration.
    
- Select “I will install the operating system later” option.
    
- Select Windows 10 x64 for your Guest Operating
    
- Follow your **Naming Convention** for **Virtual Machines**. (hint: **CL** stands for *Client*, or "member of this network")
    
- Set your location to your portable drive.
    
- Maximum Disk Size should be 150G (split) (hint: What will happen is that it will start with the disk space that it requires, and then balloon it up as needed)
    
- Customize your hardware to meet these specifications.
    

- 8192 MB of RAM (_4096 if required / 16384 if available_) (hint: some of us like to work on our pcs at home, it should be a good idea to dedicate half of the total RAM available or a bit less as the situation requires. For the sake of this assignment, it is 1024 X 8 = 8192)
    
- Number of processors: 1
    
- Number of cores per processors:1
    

- Modify your new Virtual Machine to add these specifications:
    

- Add additional: 10g Disk
    
- Add additional: 20g Disk
    
- CD/DVD “Use ISO image file: Select your **Windows 10 Educational Edition 22H2** ISO.
    

- Modify the Virtual Machine Description to list (_you will need to read ahead for some of the information required_):
    

- Operating System: Microsoft Windows 10 22H2
    
- Creation Date: Sept. 26th
    
- Hostname: CLMA01  (According to the naming convention, CL , then first initial M , last initial A, then 01)
    
- Default User Name: MAljokhadar (max 15 characters. No special characters )
    
- Default User Password: Passw0rd
    

Keyboard and mouse is being used by the host machine. So, when we launch a virtual machine, we have to passthrough the keyboard and mouse to the virtual machine.  We do this by launching the virtual machine, and then click repeatedly on the virtual machine's display (the black box) and when the mouse disappears, it has been passed through successfully. 


**Task 3: Install our first Windows Operating System**

 Double click on "CD/DVA (SATA)" in the Virtual Machine Settings. , then select "Use ISO image file", followed by Browse
 

Create a new Windows 10 Professional Workstation following these specifications.

  

Specifications (Windows 10 custom “attended” installation)

- Specify Language preferences as:
    
    - Language to install = English (United States) (Industry-Standard)
        
    - Time and currency format = English (Canadian)
        
    - Keyboard or input method =US (Industry-Standard)
        
- Specify “**Windows 10** **Pro** **Education**” as the version to install
    
- Use your NSCC KMS key ( or I do not have a product key)
    
- Do a Custom installation (Advanced) (**NEVER** select *Upgrade*)
    
- Select your Drive 0 for your installation ( It is looking at Drive0 , and it should be the OS drive)
    
- Specify Canada as your region
    
- Keep your Keyboard set to US, SKIP your second keyboard layout (if required)
    
- Set up for an organization
    
- **** Select** **Domain join instead** **of signing into a Microsoft account**.
    
- Create an account for this PC
    
    - Follow the **Naming Convention** to create your “Default User” username based on your name. example. Marie Dutka = MDutka
        
    - Set the password for your default user to “**Passw0rd**”
        
    - Select the first three security questions and answer all questions with ‘nscc’
        
- Do **NOT** make Cortana your personal Assistant.
    
- Select **NO** for all remaining optional features (select **Basic** for diagnostic info)
    
- Do NOT update your new workstation at this time. There will be some updates that will happen automatically in the background. They can be viewed in your Task Manager.
    
- Follow the **Naming Convention** to rename your new workstation
    

(Workstations and Laptops (**OS Computer Name or Host Name**)), select for first year students. _Ex. Marie A Dutka = CLMAD01_

- Modify your Workgroup name to “OSYS”
    
- Add lines to the end of your VMX (See Course Resources).
    
    - NOTE: _Your VMX is a live file and can only be edited when your VM is in the OFF state._
        
    
- Adjust Date and Time to the set the correct Time zone.
    
- Confirm your workstation is activated:
    

- Open the command prompt as an administrator (elevated command prompt)
    
- Type the following to check activation
    

slmgr /xpr

- If your workstation is not activated run the following commands to set the KMS Key and point your workstation to the KMS Server.
    

slmgr.vbs -ipk KMSKeyHere

slmgr.vbs -skms 10.82.40.52

- Then type the following to force the activation request
    
    - slmgr.vbs -ato
        
- Now recheck activation to confirm our workstation has been activated, by running the command we used earlier.
    

  

  

  

  

  

  

Now that we have successfully installed our Windows 10 workstation, we will continue by making some additional configuration modifications and adding some additional software.

  

- Do a typical install of VMWare Tools.
    
- Modify your File Explorer View:  
    File Explorer – View - Options – Folder Options – View - Advanced Settings to:
    
    - “Show hidden files, folders or drives”
        
    - Uncheck “Hide extensions for known file types”
        
- Install Notepad++ from [https://notepad-plus-plus.org/download/](https://notepad-plus-plus.org/download/)
    

- Install Speccy from [https://www.ccleaner.com/speccy/download/standard](https://www.ccleaner.com/speccy/download/standard)
    
- Install Recommended and Critical Updates but be aware that updating at NSCC will take a significant amount of time. You may want to complete this step off site.
    
- Run Speccy to generate a summary of the final system configuration. Save a copy of your Summary report “**as a** **text** **file”** to your desktop, rename your report ‘Assign1_your initials’ to the file name. example. Assign1_MAD.txt
    
- **Stop.** Upload a copy of your Speccy report text file directly to your BrightSpace drop box. NOTE: This report will be used to confirm you have the correct naming convention and configuration settings for your workstation.
    

  

- **Question 1**. There are 3 different activation types for volume licensing. Please list each method and give a brief description on how it works.
    

  

  

- **Question 2**. Throughout this course and others you will be asked to create a “GOLD” copy of your virtual machine. Review the slide on Gold Copies and answer the following questions:
    
    - How often should you make a Gold Copy?
        
    - Where should your Gold copy be stored?
        
    - What should you NEVER do with a Gold copy?
        

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  Set as an Organization when prompted ! 


Then select "Domain Join Instead"

Who will use this pc ? 

VIew - - Console View -- check the username in the notes !

No to everything, then "Send required diagnostic data"



  

  ## Core Questions : 




  

**Task 3 – Backup and document professionalism**

  

- Since we have created a new workstation and configured it is important to have a good backup.
    
- Create a new snapshot called PostA1
    
- Create a Gold copy of your new virtual machine and store it somewhere OTHER then your portable drive.
	- If she would like to create a backup copy, there are two methods :
		1. Cloning :
			1. Creates an exact duplicate of the virtual machine (Con: It is very slow!). It is essential to make sure the virtual machine is shut down. We go to the virtual machine's folder, and then copy the folder , and add "- Gold" to the folder's name
	
		2. Snapshot:
			1. It creates a roll-back for any changes that happened to the virtual machine. For ESXi , they are called *Snapshots* and Hyper-V calls them *Checkpoints*
			2. Steps : 
				1. Shut the virtual machine down.
				2. Click on the Blue Wrench icon with the wheel on it
				3. CLick on "Take Snapshot"
    
- **Stop.** Take a screenshot of the properties of the folder that contains your “Gold” copy, make sure your screenshot includes **name, location, contents** and **creation date**. Do **NOT** just take a screenshot of a folder.
    

  

Example:

  

![Picture 10](https://d2l-docbuilder-prod-ca-central-1-converted.s3.ca-central-1.amazonaws.com/8208e7eb-8a6a-4371-8e23-d4de75bf2487/06718d57b98cbac19555a59ae1767719_html_ac25c9cd4c494950.gif) ![Shape5](https://d2l-docbuilder-prod-ca-central-1-converted.s3.ca-central-1.amazonaws.com/8208e7eb-8a6a-4371-8e23-d4de75bf2487/06718d57b98cbac19555a59ae1767719_html_be22c4f0e0652029.gif) ![Shape2](https://d2l-docbuilder-prod-ca-central-1-converted.s3.ca-central-1.amazonaws.com/8208e7eb-8a6a-4371-8e23-d4de75bf2487/06718d57b98cbac19555a59ae1767719_html_be22c4f0e0652029.gif) ![Shape3](https://d2l-docbuilder-prod-ca-central-1-converted.s3.ca-central-1.amazonaws.com/8208e7eb-8a6a-4371-8e23-d4de75bf2487/06718d57b98cbac19555a59ae1767719_html_be22c4f0e0652029.gif) ![Shape4](https://d2l-docbuilder-prod-ca-central-1-converted.s3.ca-central-1.amazonaws.com/8208e7eb-8a6a-4371-8e23-d4de75bf2487/06718d57b98cbac19555a59ae1767719_html_be22c4f0e0652029.gif)

  

- Add all required information, reports, screenshots, etc to your professional documentation. Remember to make sure any scripts or reports are converted to text and submitted IN your professional document unless requested otherwise, such as your Speccy Report.
    
    - You should have **two separate items** uploaded to your drop box.
        

- Upload your Professional Document to BrightSpace.
    

  

  
#### HINT : Make a Gold Copy at the end of every assignment!
  

  

  

  

  

  

  

  

  

  

  

  

  Note : VMWare Tools - Assignment asks us to install VMWare-Tools, so we select Install VMWare-Tools. Then We open the Virtual Disk and launch the installation application. It enables window resizing, drag-and-drop between the virtual machine and the host.

  

### NEXT CLASS : Review what we need . Next 2 classes are Lab Class so we can finish this assignment


Assignment due next week! Monday is a holiday!

  

  

Rubric

  

|   |   |
|---|---|
 
|**Value**|**Task**|
||**Activity results**|
|5|Virtual Machine has correct system settings.<br><br>- 3 Disks (150g, 10G x20G)<br>    <br>- 8G RAM<br>    <br>- 1 core /2 Processor<br>    <br>- VM Name = “FirstIinitialLastName-CL01”<br>    <br>- Completed VM Description|
|1|Correct Lines added to .VMX|
|6|Windows 10 workstation has correct settings and software.<br><br>- Correct OS version<br>    <br>- Hostname = CL”Initials”01<br>    <br>- Workgroup = OSYS<br>    <br>- VMWare Tools installed<br>    <br>- Speccy and Notpad++ installed<br>    <br>- Lines added to .VMX|
|2|Folder Options set.|
|2|C:\Users\Default User = FirstIinitialLastName|
|2|“PostA1” Snapshot created.|
||**Documentation Submitted to Brightspace**|
|3|“Gold” copy properties (documentation)|
|3|Speccy report (separate document submission) with correct specifications.|
|3|**Question 1**. There are 3 different methods for volume licensing. Please list each method and give a brief description on how it works.|
|4|**Question 2**. Throughout this course and others you will be asked to create a “GOLD” copy of your virtual machine. Review the slide on Gold Copies and answer the following questions:<br><br>- How often should you make a Gold Copy?<br>    <br>- Where should your Gold copy be stored?<br>    <br>- What should you NEVER do with a Gold copy?|
|4|Document meets professionalism requirements as per page 1 of assignment.|
|**35**|**Total Marks possible**|
|||

  

  

  

  

  

_**NB: Citations – Remember that citations MUST be provided for any code, script, test or image copied from another source or used as a resource. Not attributing appropriately (Plagiarism) or using illegal or unlicensed copies (copy write breach) are serious academic offenses. If you have any doubt as to when or how to cite, consult with your instructor and the resources provided by the college.**_









