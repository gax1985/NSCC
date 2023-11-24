



Today , we are working on improving the scanning speed of **NMAP**




Refer to the following link for the **NMAP's Online Documentation** :


https://nmap.org/book/reduce-scantime.html#reduce-scantime-omit-tests



# Basics of Cybersecurity Planning



#### Assets 


We have to categorize the following assets :


##### People

There are risks involving disgruntled individuals for example, negligence or lack of knowledge in regards to cyber security hygiene


##### Equipment

There is a concern of *vulnerabilties*. If the vulnerability exists, we have to fix it. 

##### Information


##### Physical Assets 



##### Reputation 


If our router costs $10000, and the damages of not having this asset is 1 million, then it would tell you something about its inherit value. 


We are trying to figure out how much money it takes to protect the asset  

We *value* them 

We *categorize* them

We figure out the *threats* to the assets 





We are trying to discover ports involving the following categories : 


- Allowing **Communications** 

- Allowing **Connection and Control**

- Allowing **File Transfers**



Most common causes : 


- Programs being uninstalled, but ports being left open 

- Malicious intent, where someone could have installed a backdoor into the infrastructure

- Silly individuals, who either through negligence or due to lack of knowledge or with a malicious intent leaving a door open


> [!question] 
>  How long would it take for Chinese actors to know about vulnerabilities on a system? 


> [!tip] 
> It would take them 5-6 minutes 





> [!tip] 
> When doing the **NMAP** Assignment, it would help to know what is the *Process ID* is (aka. *PID*). We can use **NETSTAT**, where it would show the *Process ID*. 
> 

> [!tip] 
> There is a tool called **VOLATILITY**, where it has a library called *pslist* which will help in showing us the *Process ID*. There is another tool called **SVCHost**. Windows does many functions, and each function is contained in **.DLL** files, which refer to *Dynamically Linked Libraries* ; There are snippets of code that does one function, rather known as a *Windows Process*. They do not have the startup and closing portions of a program. All the startup and shutdown commands are all contained in **SVCHost**, which starts the services associated with the .DLL files. It has an empty spot in the middle, so **SVCHost** will grab the code from the *.DLL* file, and place it in the empty spot. 
> 
>- services PID 1
>- SVCHOST PID 5 PPID 1 (if PPID is not 1, or the service is launched from a user-created folder, then it is malicious)




The **Volatility** tool will figure out which of the vulnerability versions is in place. Microsoft changes how memory is processed frequently, so it is problematic. 



Forensics : Where the process is from, where it is based, what is it doing ?
Hashing information 
Chain of Custody 

We would start with *Disk Forensics*, Ron would hand us a Forensics tool, watch a video on it, then create a file on the USB file, delete the file, and then pass the USB to see if one can retrieve the deleted data

The **Volatility** tool is for *Memory Forensics*
The **FTKImager** tool is for *Disk Forensics*



When we are scanning for an organization's network infrastructure, we are looking for anomolies (differences). Organizations would typically set up things in a consistent way usually, so differences stick out!











