# Linux Scripting 


##### Expectations : 


This course is meant for bringing someone with no idea about Linux scripting up to speed. 

##### Marks : 

Assignments 10%
Assignments 25% (2 of them- Basic and Advanced Scripting)
Final Project (40%)


##### Remember : 


2 hours outside of class for EACH 1 hour in class!


# Three Steps : 


1. You create the script. The script is an interpretive program. This is done on text editors ( such as nano, neovim ). 
2. Make the script executable. If it is not executable, it is just a text file. What makes a program executable? the execution permissions are added (chmod +x filename)
3. Place a script in the system's PATH.



#### What is the difference between an **Interpretive Program** and a **Compiled Program** ? 


By default, a compiled program contains binary instructions, not human-readable instructions. There could be text occasionally seen, but low interest. The compiled propgram written for Mac will not run on a pc. The binaryt instruictions are sepcific to the architecture of the processor (x64 vs ARM64). 

The goal is : 


Write a Program that is Platform-Independent!

It means : 


    Normally , you have your program talking directly to a specific computer with a specific OS. With an interpretive program , you have the program text containing the instructions in Englihs-readable form. This is passed to an interpreter, which understands the OS and the Architecture. Scripting interpreter for Mac will be different than the PC's interpreter. 


25 years ago more or less, this model was in use for a lot of different types of programnmibng. BASIC was an interpretive program. The industry wanteds to do that for all types of programming (text-based programming is limited)..,..



Java was born! it is an interpretive program. JAVA applications will run on any device. The way this works is : you write your Java program in text, this is passed to ... 

**Java Virtual Machine**. 


... aka ... interpreter/compiler



The difference between these two is  ": interpeter executres the script one line at a time
.

JKava virtual machine interpretes the program into binary code. 


What is different is the Java virtual machine. All java virtual machiens speak the language of text, but each speak a different language when compiling the code : 


programming lingo -- binary -- executed into a code. 


Any script is an interpretive program.


If we are collectiving data from different sources , to a SEIM, and the SEIM would have an API to communicatre with routers, and all different devices being able to speak to the SEIM. It is the entry point into something else. It formats the data differently. 



Scripting language wew will be using is *BASH*. 


The original *BASH* shell is the **Bourne Shell**. 


A Shell is a computer environemnt. BASH is the Bourne Again Shell. There are Corn Shell, C Shell. We write BASH scereipts i  text, one line at a time. 


We would take a text command , take it to an interopreter, which trtanslates intop machine code. 




We jhavbe to tell every script which shell top use, and we use a **SHEBANG**, which is the beginningf top line of each script 


#!/usr/bin/bash ---> We are telling the OS to use the BASH interprewter, whic hsi located in the /usr/bin directory. 


To do a comment, add a #


Ron insists on good commenting (Pseudocode),.Good commenting does not involve technical gargon, but jyust your *Intention*. 


Mistakes we often make is we do not type the command that achieves what we are trying to achieve., If we atre trying to debig the code, we read the intention. To write things out on the screem , the very first program in every language is "Hello World!" 


The hashtag for the shebang is NOT a comment.The OS looks at the executable file, it will look for the shebang at the top. 


Ron will get us very soon to write this program : 


#!/usr/bin/bash

# echo "Hello World!" 






ls -l helloworld 

(We see the permissions in the following list of files : 



... .. .. . 


if we have no X, thus : 


chmod +x nameofthescript


ls -l helloworld , 

and we see that we have a new execution permission



Where do we place the script ? 

~/ --home directory

~/bin create this folder for personal scripts, which you would like to run locally. 

/usr/local/bin accessioble to every user in the system

/usr/local/sbin accessible to the root user


When creating the ~/bin directory,if we place the script there, and go elsewhere, the script will not be running unless we specify the path 


$PATH = this is the variable indicating the PATH. The system will look there firstr

#PATH includes a lot of directory names. If we do : 


export $PATH=~/bin:$PATH


it adds the ~/bin folder to the long list of folders. 

We must reopen the terminal . The system when laucnihing the terminal, and it checks its variables. 


If we do :

echo $PATH 


it will show you all the directories that binaries can be executed from. 



Steps " add ~? to $PATH

create .zshenv 

add the following line on top : 

export PATH=~/bin:$PATH


# Stages : 


1. Shebang #!bin/bash
2. Add comments with # 
3. Make the script executable with chmod +x 




Ron would like us to create the "Hello World!" Script. In ytour home user account, create a text file called, "Hello World" , and it is good form to put a .sh at the end. EVERYTHINBG in Linux is case senstive. .sh=traditional ending for scripts 


Filename : helloworld.sh

Place it in ~/bin directory 

export the path to the $PATH variable




# Ron's Steps : 


mkdir ~/bin
nano helloworld.sh 

' enter the text '

then, 


chmod +x helloworld.sh 

export PATH=~/bin:$PATH


cd ~

helloworld.sh





