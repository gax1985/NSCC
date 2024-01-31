




# Processes 




On Windows machines when you go to Task Manager you would see a list of processes running on the computer, and they are accompanied by a Process Identifier (PID).




### On Windows 



You might be seeing a process called *sbchost* it is short for *Service Host*, Windows has a lot of services under the hood, you may have a couple of dozens running in the background. Most things are structured as a *service*, something online is a *service*. Imagine the developer who wrote them. Every program has a setup section, defining libraries inputs and outputs , and at the end you may have *Outputs*, it communicates in some way ....



Between these, there is the **Computational Process** ; it is something *specific* to the program. Alot of program begin and end in a comment, what makes them different is the job it is doing : outputs, communicate, but those are all things that programs have in common, but the computational process would do the job that the program intends on doing .,..



If everything is a comment before and after the computational process, we can build a porogram to set up the wholt thing, when we need to do a job we go to the disk and grab the binary object that does the action, and stick it in the shell. The program's shell is empty, and the binary code is called **Dynamically Linked Library**, which is the core piece of the program that does what the program wants to do. That shell that it is plugged in to is called *sbchosts*, and there are many of them with each a unique process ID. It is not always easy to pin them down. 



The process also has **PPID**, or **Parent Process ID** ; it is the process/program that has spawned created or launched the program we are looking atr. Often, the programs running on the OS has been spawnbed by ajnother program to do something . 


*sbchost* is always hosted by a program called **Services**. Services' PID is 1. The *services* program is responsbible for spawning *sbchosts*. Every time the program needs to do something , it launches sbchost, finds the DLL, and then assigns the sbchost its own unique PID. 


If we have an svchost rgar gas a PID = 203. If you examine the PPID for every one of them, the PPID is always equal to the services program. They all have the same parent. Every sbchost will be spawend by the *services* program. 



If you have another svchost with PID of 507, its PPID is = 1. How do we use that? if you have malware on a comproimised machine, maybe during the compromise, or you are investigating this OS on this machine, one of the things you might want to do is **List the running proccesses in memory and look at their PIDs and PPIDs**. If a criminal wants to hide malware, (how many people looked at the task manager and tried to investigate it by shutting things down), in that list you see *svchosts* Ron tends to enumerate them. 



There are a dozen svchosts , and none of them stand out. If we look at the PPIDs and we see a svchost with a PPID not eequal to 1, then we know it is malickous due to it not being spawned by the services app. 



svchost lives in WINDOWS32 Directory. svchost should ALWAYS come from the Windows32 directory. If a svchost process came from elsewhere, it is malicious



If you want to look further into the program, you have the exact command that was issued including parameters being listed, if you find svchost without PPID of 1, you look at the command to see what it is doing. It is important to dig a bit deeper into proccesses. 




# *ps* Command




In Linux, we can see the PIDs in Linux with the *ps* command. 



In WSL, 


![[Pasted image 20240130140908.png]]


Look at the two proccesses that are running, TTY is for communicating the terminal. *ps* was run, so it appears in the output


If we do ....


![[Pasted image 20240130140957.png]]


We see the actual processes of the machine! 



We see PID, % CPU, %MEM, 


/sbin/init  ---> it has a PID of 1. First thing that is run when the OS is booted


There are a series of other processes that are running, if we scroll down .... 




![[Pasted image 20240130141240.png]]




/sbin/init 

/init was the child process of the /sbin/init


All the other processes are children of init. This is very important to understand how the processes relate to each other...



Fior the next 5-10 minutes, in the course sehhll / readings /refrences / there is a man page for the ps command. Look at the manual page, and look at the explanations for some of the options . Try a few, and see what you can see. 



OS is built from processes, it does something. We are digging deeper into udnerstanding the program. AN OS : Program someone wrote, it does things by itself, interacts with you with input/out, and the program does its thing. We get broader insight about how the program does what it does. 


He could ask us, which of the processes are using the most memory? which processes are running right now? which processes are using the most CPU time? 


With options , - is when dealing with a single letter, -- means that we are adding more than one letter.



# *uname* Command


>uname -all 


![[Pasted image 20240130143852.png]]

It is telling him about his machine and the OS running on it. We can ask for the kernel name : 


>uname --kernel-name 


![[Pasted image 20240130143931.png]]


>uname --kernel-release  (When the release was done)


![[Pasted image 20240130144006.png]]


>uname --nodename (Network Node) 


![[Pasted image 20240130144034.png]]

>uname --machine


![[Pasted image 20240130144052.png]]


>uname --kernel-release --kernel-version 



In plumbing , we have T connections so it passes the water in a t shape in both side. In Linux, there is a *tee* command, which displays the content on the screen and inserts it into a file

When you turn in the assingment, make sure the output of the command is in the file as well. If you did the > arrow, you do not have to go if it is actually good. So with the *tee* command, you can check the string that you are inserting and insert the string into a file : 


>ls -l | tee testt2.txt 
>
>![[Pasted image 20240130144642.png]]



if he wanted to see all the processes that are running and save the list into *processlist.txt* : 

>ps -aux | tee process_list.txt 
>
>![[Pasted image 20240130144754.png]]

>[!hint]
>
>The *tee* command will be used in the next assignment!
>



GO to course shell, and check the *man page for the tee command*. You have a link also for explanations for the *cronjob* command. 



# *cronjob* Command


You can have a script run automatically every Sunday morning at 2 AM. For example, you may run a script that does a vulnerability/port scan against the computers on your network every morning at 4 AM. You can write an automatic backup script, and have it go off midnight every night Friday. It is a *timed job* ...


Instead of a *man* page , we have a link to a nice page that describes it. The actual command ( under *basic crontab syntax*), you have A B C D E, and Command - Output (placeholder for the script you write)


In terms of A B C D E , they are explained under **Time Format** : 


A *Minutes*


0  **AND** 7 Sunday 
1 Monday 


Next parameter in the command is the script it is meant to execute. The output of the command can be directed or not. Output is *optional*. You can use the *tee* command if you wish. 


Asterix All values

,    separate individual values


To insert a cronjob command file to your crontab file, you put the command at the VERY **LAST LINE!**



## Next Assignment : 


We will start using Linux from a *Systems Management Perspective*. You will use commands used in administration such as the *ps* command, which is used forensically to investigate processes. 


















