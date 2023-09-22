



Today, we are working on **Lab 2**. The Assignment portion is not due until Friday. We should get it done and share what we experienced in Friday's class. 





#### Assignment 2



Page  
OSYS 1200 – Intro to Windows Administration  
Due: As per Brightspace  
NB: Citations – Remember that citations MUST be provided for any code, script, test or image copied from another source or used  
as a resource. Not attributing appropriately (Plagiarism) or using illegal or unlicensed copies (copy write breach) are serious  
academic offenses. If you have any doubt as to when or how to cite, consult with your instructor and the resources provided by the  
college.  
Assignment 1: Windows Installation and Installation Types.  
Install Windows 10 into a virtual machine, stored on your external hard disk drive. Install  
various software. Create a snapshot, install log and “Gold” copy.  
Purpose:  
For a variety of reasons, we cannot be administrators and do administrative work on college  
computers. So, we will emulate a physical Windows 10 computer using a virtual machine  
and we will do our administrative work on that instead. This will give us the ability to modify  
the operating system and make changes - and sometimes mistakes - without affecting the  
other students who use these lab computers.  
Required Resources  
• VMWare Workstation from https://nsccvm.onthehub.com/  
• Windows 10 Educational Edition 22H2.iso from Azure for Education  
• NSCC Lab KMS Key - As per Key Management Services (KMS) client activation and product keys for  
Windows Server and Windows | Microsoft Docs  
• External hard disk drive  
• Course Resources as posted in BrightSpace  
Professional Documentation  
All documentation must be done in a professional style. It must include:  
1. Title page  
2. Updateable Table of Contents  
3. Document introduction  
4. Section introductions or description, each section must be clearly identified  
5. Graphics or screenshots MUST include a title with a short description  
6. Any direct or copied quotes or graphics MUST be properly credited in a footnote  
7. ALL sources MUST be properly cited (APA format) and placed at the end of your  
document in a bibliography.  
8. NO embedded, zipped or compressed files. ** All scripts must be converted to text  
before including them in your documentation. **  
*1 Professional Word Document ONLY.  
Research and documentation sections - Please complete all research and question  
responses in your own words. Research sections not completed in your own words may  
result in a mark of 0 for the section.  
NOTE: Please do NOT copy and paste responses from internet, even with a citation. I  
expect each section or response to be in your own words. Be prepared to explain your  
responses and demonstrate your comprehension during the marking period.  
No marks will be given for cited or credited information included in document.  
Marking and Assignment Notes:  
• Screenshots MUST include user or device identifying information.  
• Screenshots MUST be added to your document in the order of creation.  
• Documentation must meet Professionalism requirements.  
• Automatic mark of 0 - Assignment not submitted or work not original.  
http://www.nscc.ca/docs/about-nscc/policies-procedures/policy-studentcodeofconduct.pdf  
https://www.nscc.ca/docs/about-nscc/policies-procedures/policy-academicintegrity.pdf  
NOTE: This assignment may require some adaption, research and troubleshooting.

[](https://docs.microsoft.com/en-us/windows-server/get-started/kms-client-activation-keys "https://docs.microsoft.com/en-us/windows-server/get-started/kms-client-activation-keys")

[](https://docs.microsoft.com/en-us/windows-server/get-started/kms-client-activation-keys "https://docs.microsoft.com/en-us/windows-server/get-started/kms-client-activation-keys")

[](http://www.nscc.ca/docs/about-nscc/policies-procedures/policy-studentcodeofconduct.pdf "http://www.nscc.ca/docs/about-nscc/policies-procedures/policy-studentcodeofconduct.pdf")

[](https://www.nscc.ca/docs/about-nscc/policies-procedures/policy-academicintegrity.pdf "https://www.nscc.ca/docs/about-nscc/policies-procedures/policy-academicintegrity.pdf")

Page  
OSYS 1200 – Intro to Windows Administration  
Due: As per Brightspace  
Page | 2  
Task 1: Support Documents and Presentations  
Review the following presentations, walkthroughs and/or videos in BrightSpace:  
Module 1 Resources:  
1. Azure for Education at NSCC  
2. Intro to VMWare  
3. Capturing and Documenting Screenshots  
4. Table of Contents and APA Citations (Creating an Automatic Updateable Table of  
Contents and Citations in APA Format)  
5. Academic Integrity and research resources (how to use and recognize acceptable  
resources such as ChatGPT)  
6. Create a Meeting Request with Outlook  
Note: Throughout this assignment you may be asked to produce a series of screenshots.  
Please make sure to include a label and brief description of each screenshot added to your  
professional document in the order requested in assignment.  
example. Task 2 - Virtual Machine settings  
Task 2: Creating your first virtual machine  
ATTENTION:  
Indicates steps and activities that we will complete in class. If you are NOT present during the  
walkthrough class you will be expected to complete these steps and activities on your own as  
part of your assignment.  
Create a new virtual machine following these specifications:  
Do a Typical configuration.  
Select “I will install the operating system later” option.  
Select Windows 10 x64 for your Guest Operating  
Follow your Naming Convention for Virtual Machines.  
Set your location to your portable drive.  
Maximum Disk Size should be 150G (split)  
Customize your hardware to meet these specifications.  
o 8192 MB of RAM (4096 if required / 16384 if available)  
o Number of processors: 1  
o Number of cores per processors:1  
Modify your new Virtual Machine to add these specifications:  
o Add additional: 10g Disk  
o Add additional: 20g Disk  
o CD/DVD “Use ISO image file: Select your Windows 10 Educational Edition  
22H2 ISO.  
Modify the Virtual Machine Description to list (you will need to read ahead for some  
of the information required):  
o Operating System:  
o Creation Date:  
o Hostname:  
o Default User Name:  
o Default User Password:

Page  
OSYS 1200 – Intro to Windows Administration  
Due: As per Brightspace  
Page | 3  
Task 3: Install our first Windows Operating System  
Create a new Windows 10 Professional Workstation following these specifications.  
Specifications (Windows 10 custom “attended” installation)  
Specify Language preferences as:  
o Language to install = English (United States)  
o Time and currency format = English (Canadian)  
o Keyboard or input method =US  
Specify “Windows 10 Pro Education” as the version to install  
Use your NSCC KMS key  
Do a Custom installation (Advanced)  
Select your Drive 0 for your installation  
Specify Canada as your region  
Keep your Keyboard set to US, SKIP your second keyboard layout (if required)  
Set up for an organization  
 Select Domain join instead of signing into a Microsoft account.
Create an account for this PC  
o Follow the Naming Convention to create your “Default User” username  
based on your name. example. Marie Dutka = MDutka  
###### o Set the password for your default user to “Passw0rd”  
o Select the first three security questions and answer all questions with ‘nscc’  
Do NOT make Cortana your personal Assistant.  
Select NO for all remaining optional features (select Basic for diagnostic info)  
Do NOT update your new workstation at this time. There will be some updates that  
will happen automatically in the background. They can be viewed in your Task  
Manager.  
Follow the Naming Convention to rename your new workstation  
(Workstations and Laptops (OS Computer Name or Host Name)), select for first  
year students. Ex. Marie A Dutka = CLMAD01  
Modify your Workgroup name to “OSYS”  
Add lines to the end of your VMX (See Course Resources).  
▪ NOTE: Your VMX is a live file and can only be edited when your VM is  
in the OFF state.  
Adjust Date and Time to the set the correct Time zone.  
Confirm your workstation is activated:  
o Open the command prompt as an administrator (elevated command prompt)  
o Type the following to check activation  
slmgr /xpr  
o If your workstation is not activated run the following commands to set the  
KMS Key and point your workstation to the KMS Server.  
slmgr.vbs -ipk KMSKeyHere  
slmgr.vbs -skms 10.82.40.52  
o Then type the following to force the activation request  
▪ slmgr.vbs -ato  
o Now recheck activation to confirm our workstation has been activated, by  
running the command we used earlier.

Page  
OSYS 1200 – Intro to Windows Administration  
Due: As per Brightspace  
Page | 4  
Now that we have successfully installed our Windows 10 workstation, we will continue by  
making some additional configuration modifications and adding some additional software.  
 Do a typical install of VMWare Tools.  
 Modify your File Explorer View:  
File Explorer – View - Options – Folder Options – View - Advanced Settings to:  
o “Show hidden files, folders or drives”  
o Uncheck “Hide extensions for known file types”  
 Install Notepad++ from https://notepad-plus-plus.org/download/  
 Install Speccy from https://www.ccleaner.com/speccy/download/standard  
 Install Recommended and Critical Updates but be aware that updating at NSCC will  
take a significant amount of time. You may want to complete this step off site.  
 Run Speccy to generate a summary of the final system configuration. Save a copy of  
your Summary report “as a text file” to your desktop, rename your report  
‘Assign1_your initials’ to the file name. example. Assign1_MAD.txt  
 Stop. Upload a copy of your Speccy report text file directly to your BrightSpace drop  
box. NOTE: This report will be used to confirm you have the correct naming  
convention and configuration settings for your workstation.  
 Question 1. There are 3 different activation types for volume licensing. Please list  
each method and give a brief description on how it works.  
 Question 2. Throughout this course and others you will be asked to create a “GOLD”  
copy of your virtual machine. Review the slide on Gold Copies and answer the  
following questions:  
o How often should you make a Gold Copy?  
o Where should your Gold copy be stored?  
o What should you NEVER do with a Gold copy?

[](https://notepad-plus-plus.org/download/ "https://notepad-plus-plus.org/download/")

[](https://www.ccleaner.com/speccy/download/standard "https://www.ccleaner.com/speccy/download/standard")

Page  
OSYS 1200 – Intro to Windows Administration  
Due: As per Brightspace  
Page | 5  
Task 3 – Backup and document professionalism  
 Since we have created a new workstation and configured it is important to have a good  
backup.  
 Create a new snapshot called PostA1  
 Create a Gold copy of your new virtual machine and store it somewhere OTHER then  
your portable drive.  
 Stop. Take a screenshot of the properties of the folder that contains your “Gold” copy,  
make sure your screenshot includes name, location, contents and creation date. Do  
NOT just take a screenshot of a folder.  
Example:  
 Add all required information, reports, screenshots, etc to your professional  
documentation. Remember to make sure any scripts or reports are converted to text  
and submitted IN your professional document unless requested otherwise, such as  
your Speccy Report.  
o You should have two separate items uploaded to your drop box.  
 Upload your Professional Document to BrightSpace.