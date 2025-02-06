

## Registry : 


#### Definition :

Database containing all core settings for your machine. 


 
 When you log in to Windows , and someone comes and tries to log in, they would use your username and password. The credentials are stored in the registry. 


Login credentials are stored in the **registry**. Other information includes how a program would launch. 


In MS-DOS days, the fancy letters at the end of the . , those letters had a limit of 15 characters, and did not matter what they were. They did not belong to any kind of application. They had to know which file it was. 


Somewhere around MS-DOS (Windows 3.11), it still allowed you to have a 15-letter extension at the end, but interestingly, it allowed the user to make their own association. If we see .txt , a text editor would open it. 


They are building those associations. One of the jobs she had was to upgrade an office to Windows 3.11. The federal office's workers stored persons' information as nameoftheperson.dateofthecreation. With Windows 3.11, after the upgrade, she had to go through every file to check for the appropriate application. 



The registry **holds all the information about the machine**. The passwords are stored *locally*. Even if someone is at their work, and they have a laptop, and they log in to the network at work, and at home, how would it confirm who that someone is? the registry holds the passwords. So, this is the place it looks at.



The registry is **loaded into memory** *every time the system boots*. Not all the registry gets loaded into the memory, but a lot of it does. Any changes made in the registry is automatically saved. 


We have to be EXTREMELY careful when working with the registry. What happens in Python if you delete a . or a comma? it would not work. 


In the registry, the whole operating system will not boot if there was a spelling error or a missing . for example. 


ALWAYS back up the registry! 


Today, we will cover **Snapshots**. 


The registry = reg.dat


Registry is made up of **keys** or **high-keys**. High keys mean each key holds a collection of information. 



It is very easy to export a key. If she was someone who had access to our machines, she can quickly export the keys, and then she can take her time cracking the passwords. We will learn how to crack passwords. In some cases, it would be difficult, and in other cases, it can be  very easy. 



CHILD/PARENT SUBKEYS : Keys that sit below the HIGH-KEY



regedit, or regedit32, when we used to run 32-bit OSes, regedit32 was the key to administer the system. It became regedit in Windows 2000, and both were available. All of this is stored in **reg.dat** located in SYSTEM32 folder. The reason it stays there because it would inherit the security features of that SYSTEM32 folder. 



#### REGKEYS: 

we have 5 **HIGH-KEYS**


1. CLASSES_ROOT : .doc or .docx is associated with MS WORD. It handles file extensions, and how to handle or access files. 
2. _USERS : implies all the system info about all the users. Anything involving the user or someone else who is logging in; on campus, we are logging in the client machines, and any tech can log in, and anything we see applies to everyone. All this info is stored in _USERS
3. _current_user : info about the current user who is logged in into the machine. If we create a shortcut for VMWARE on the taskbar at the bottom, she adds the shortcut to the task bar. Not all the faculty use virtual machines, so they would not have a need for it. Her choice is preserved because it is stored in _current_user
4. _local_machine : information about system and hardware 
5. _current_config : info about the current hardware DURING the active session 

(Both _local_machine and _current_config apply to the hardware)





1. We open "regedit" or "Registry Editor"
2. There are 5 HKEYS. The first one (**__HKEY_CLASSES_ROOT** )
handles file extensions that are available for the user, which are associated with a particular program. 
3. In HKEY_CURRENT_USER, we have subfolders that hold information pertaining to the current user. 
4. HKEY_LOCAL_MACHINE : anything (settings) about the entire machine we are on. Hardware for the currently logged-in user. (We will talk about SAM which is located in HKEY_LOCAL_MACHINE)
5. HKEY_ALLUSERS : holds information pertaining to all users. every object in Windows gets an ID (SID). These are stored in SAM. Each of those IDs are linked to a particular user. There are three users that are set up by default in any system. There is ana ADMIN, GUEST, and DEFAULT. Then we have our account S-1-5 : These are SIDs, and it shows which version of SAM is run. 5-15-18 , 5-15-19,  first three are default accounts., This folder holds all information pertaining to her and her account. We will not know how to read this information yet, but later down the line.
6. HKEY_CURRENT_CONFIG : Information about the current session. It holds SOFTWARE and SYSTEMS. That one will fluctuate, according to the software that is running. This one is on flux depending on what we do. 



1. Backup our Registry (so we can restore things back):
	1. If any of these HKEYS are selected, we are ONLY backing up these folders. Select COMPUTER to backup the key we highlight it. Right click and select Export,. Save it to Desktop and call it, PracticeBK , and it will save as a .reg file. It will take a moment



What is inside the high keys ? we have sub keys and values 



We have : 

1. String value (REG_SZ'meaning string value') means this is a subkey that holds a string value
2. BINARY value : holds the binary data (REG_BINARY)
3. DWORD (REG_DWORD) : Has a value to it that is written in HEX or decimal and cannot be mroe than 32-bit.'
4. QWORD (REG_QWORD) saome as DWORD but 64-bit
5. Multi String Values (REG_MULTI_SZ) : Multi strings 7created by the systeml just the system listing a variety of strings. we do not create that , but we can change it. It is a system created subkey or string, and we do not need to change it unless we MUST. Hackers and attackers can ofcourse. 
6. Expandable string (REG_EXPAND_SZ) : uses a variable, more specifically an environmental variable. It is a variable that is automatically created by the system itself. Windows has a list of variables that it uses itself and built in the OS. Those are what is used. %systemRoot%\file.exe ( meaning , go to the root folder)




Remeber : some of the registry is loaded into the memory, the regisstry is read out of the memory. The reason ie gets loaded in memory, alot needs to be loaded in order for the machine to start up. How to authenticate, which drivers to use,etc gets loaded into memory. A few things do not load into the memory, and because those do not get loaded into the memory we can access those changes. 
2. Right click on the BackupBD and select Properties. It sshould be a large file , and it could range in size. If it is alot smaller, there is an issue. If she right clicks and selects Edit, she can see the 1st thing she sees " version of regedit, scroll to the bottom, and she can see that she is in HKEY_USERS_". 
3. Right click - Edit - it opens it in Notepad. Whenever she works on a file, she can righht click and select Edit. She likes Notepad++. She wants the default to be Notepad++. We will use the registry to get things done : 
	1. Select HKEYS_CLASSES_ROOT :  click on it , select Edit, then Find . Type ".bat". It finds info about a .bat file. Hit F3 to see the next result. 
	2. Go all the way bback to the top. Hit the HKEY_CLASSES_ROOT , Edit --> Find , look for "regfile". hit F3 to go to the next result.  We want one that we can edit.
	3. Go to HKEY_CLASSES_ROOT, scroll down until REGFILE. When we select REGFILE, expand it, and select SHELL, then expand EDIT, and select COMMAND
		1. We will export this particular command in case we need to change it back. Right click-export-Save it to the desktop. called it "Regfile". Right click on the DEFAULT subkey, and click on Modify. We will modify it using the path to her Notepad++. Notepad++ is located in C:\Program Files \notepad++\notepad++.exe "%1". If we want to know the exact path, we can browse to it and copy the path.  (in my case : C:\Program Files\Notepad++\Notepad++.exe "%1") %1 means this is the default command. 
		2. Go all the way back to the top, at the "Computer" or 5 HKEYS at the very top. 
		3. Start with HKEY_LOCAL_MACHINE, expand it, SOFTWARE, andd expand it, find MICROSOFT, expand it, find WINDOWS, expand it, find CURRENTVERSION, expand it, find POLICIES, expand it , select SYSTEM. 

> HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System

4. We have DWORDS and then STRINGS, select LEHALNOTICECAPTION. Add the following "Warning!". select LEGALNOTICE TEXT, click Modify , type "This Windows 10 Installation was Completed by : Mohammad Al Jokhadar."

>This Windows 10 Installation was Completed by Mohammad Al Jokhadar. Any modifications to this computer must be done by the original installer. No other modifications are allowed.


5. This is one of the changes that requires the system to be loaded into the memory. So we need to restart the virtual machine. 
6. Now, we see the greeting message that we have entered! 
7. Let us customize it! 
8. RegEdit will take you back all the way to the same subkey you were in. So this is not secure. 
9. LEGALNOTICETEXT, right click, and select Edit Binary Data. Now we are in a HEX editor. The editor makes it very simple. if we look at the right-hand side, we see ASCII, Capital letters, lower case  , periods , carriage returns , every character we type is a n ASCII character. Every ASCII character is separated by a dot. If we select the dot between T and H, it highlights the binary character to the left. Between every character there is a dot, and all the dots line up and all the dots are represented by 00. If we remember what we type , " this windows 10 installation was completed by .... our name". Find the period at the end of the name (which is represented in two ees and then a dot dot. Then the next line of text with a carriage return. Infront of 20 I will type 0 D . She has to add 00 at the end of the period . 00 is defining the ASCII on either side.  Period = 2E , 0D= carriage return . We need all the lines to line up. Period = 2E00 , type in 0D00. Put a period at the end of Installer. So , type in "0D00"

	We will have period = 2E00
	Carriage return = 0D00

	We need to see 2E00 0D00, and all the 00 need to line up vertically. 



We have to work on the Assignment, Due date is posted in Brightspace. Take the Snapshot when uploading the assignment 
  
  
  
  >It is typical in Registry that it would have the Path showing. 





		- This is not a change that requires a restart. When clicing on the backup reg file on the desktop, it would be opened in Notepad++
-