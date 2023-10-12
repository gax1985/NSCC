


Today, we get into **Encryption**



Here is how it works usually : 


Plaintext message text --------> Encryption ------------> *Cyphertext*



Decryption : 


Cyphertext --------------> Decryption with key ----------> Plaintext






There has always been a need to share secrets.



## Hashing


It falls under the domain of encryption, but it does not work this way 


Demostration : 


       Hashing algorithm
File ---------------------->  **Message Digest** 


Message Digest : long string of characters. The size of the string depends on the hashing algorithm. If we have the string, and we have the hashing algorithm, we can never use the string to recover the file itself. It can never be decrypted back to the original state of the file. You know what was used to create the hash, but you can NEVER recreate it. It is **one-way**!



If we have the same algorithm will produce the *same* results. The output is unique. 

Hashing involves the *bits* in the file.


The file can be millions or billions of bits, or a bit to represent one character. 

The string is **ALWAYS** the same size for output



MD5



It is always **the same size** and **unique**.




If we encrypt Don instead of "Ron", we would get a vastly different result. 


#### The rules of hashing : 

	"There cannot be any relationship between the source and the result"


#### Collision

	If we ever get a hashing algorithm, that given 2 different inputs producing the same output, through it out!


Question : Is there a size limit for the output?

Answer : No!



Persons sharing child porn over the internet would have a collection of images that they share, and one individual has one image, and another has another image, an investigator would have a database of images found on these computers, and they have hashed that image. They have a collection of hashes, and they take a disk where it have the stored hashes, and they compare the hashes they have with the hashes that is produced from the files on the offender's computer. 



Warrants would limit what we can look for. If we accidently find a picture of the significant other of the offender, they would not be legally allowed within the scope of the warrant.



This is prevalent, more than one would think. Pornography itself is legal, but unfortunately very prevalent. We might imagine a particular image of the person who produces this. In Canada, in Ontario specifically, there were a couple of neighbor who had a 7-year old son, and another neighbour had a son and daugher (both the same age). The neighbour with the two children asked her neighbour to drive her children home. The neighbor who is driving the children asked them what they plan to do, and the children answered an answer involving child exploitation. The police investigated this, and 70 individuals went to prison. 35 couples who met, got married, had children for the intention of doing this. 



Law inforcement, whenever they are investigating a storage device, they take the device. Defence attorneys would ask if there were any changes made to the device/computer. Usually, when a raid happens, the police officers go inside, secure the scene, and investigators have special devices whom they attach to the offenders computer, where they create a disk image, which is bit-by-bit image, and then they take the drive to evidence. 


Before they probe the image, they *hash* the entire drive. The bit-by-bit image of the drive gets fed into the hashing algorithm, and they get an **output string**. Then, they begin their investigation. 


It is important to mention the **Chain of Custody**. From the time the drive is acquirewd, bagghed sealed, there would be a trail of who had it. 


The defence attorney might argue "The incriminatiing evidence was not actually on the drive. You have planted it there.". The prosecutor would say here is the image of the drive, and then they hash the drive, and then they get the exact same string as the original hash. 


If someone screwed up the chain of custody, it would be evident in a difference in the produced *digest*. 


The arguement by the defence attorney is done to have doubt in the jury's mind. 



#### Non-Repudiation :


	We are guaranteeing that the source is the same, and from the same source 



If you are trading stocks on a phone , and the broker would repeat back the purchase order, this gets recorded, the recording gets hashed, and if the client is arguing that they ordered differently, the trader would produce the hash of the recording and compare it. 


Hashing is **one-way**. We can send anything we want, we get a string as an output. 


Question : Would metadata be included in the hash? 

Answer : images have byte blockers that prevent changes


Ron's trainer had a hobby of creating algorithms. Anything can be fed into the hashing algorithms.


If the hashing algorithm fails (based on mathematical proofs, justified by mathmatreical equations that yild the same result).


There are hashing algorithms that do not have to be unique. 


One of the methods in advanced cybersecurity to check if there was a compromise, all of the files (OS files), once the OS is stable and configured just like you want it, you hash each application, and going through the file allocation table, and then the security system does it again. We spoke persistance with malware, where they would use the startup of the OS. 



The original hash , in the Appender virus, is the original application's code. If the virus code was well-known, and we had a copy of it, and we analyzed it, and we added the signal of instructions to the database. Files in and out of your compyer would scan those files, and see if it can find the signature. It is looking for the file, and for the presence of the signature. 


This is an arms race. 


If we are the attacker, what would we do to make Ron's life difficult ? 


1. Encrypt the virus code :

	If we have a signature of the virus, it would not be detected if the virus code is encrypted, as when you encrypt the file, the encrypted result would have a different digest as a result. So, the malicious actor would have a de-crypter. The decrypter has to run, and the thing that decryopts the file is plain code. The presence of the decryptor code in a file would indicate the possibility of its presence. 

2. **Split Infection :


	Virus code is split up and located in different places, and it has **salt** added : random group of characters added to defeat the signature detectors. Since they randomize the salt, it would look different. The instruction pointer starts at the top of the program. It hits the jump code, the jump code executes the first section of the virus, ontop the next secitio n ,and then the last section . Then the virus code boots the original application ( to the jump code right below the original) ,and then jumps over the virus code. 




#### Changing Viruses 


1. Oligomorphic virus : comes with different versions of itself, and it would choose the appropriate version. If you are hunting for a version, it would launch the version that is not wanted. 
2. Polymorphic : creates a new version of itself most of the time , always! How do you have a program that does the same thing every time, but changes the code? 

		If we want the result of this math equation to equal 10 : 


		9 + 1 = 10 
		10 + 0 = 10
		11 - 1 = 10

		We can have a series of instructions that are different from each other, but achieves the same result
		
3. Metamorphic virus : it would have its own compiler, and when its run, it rewrites its own code, possibly based on where it is and its target --> MySQL? I will change to the appropriate code. 



###### Statistics: 

1. 70% of breaches originate at the end-point, yet spending on end-point security is at 24%. 
2. 60% of breaches stem from unpatched software. How many of us are unaware of any unpatched software currently on our computers? Abobe Acrobat have a huge number of problems.
3. 78% of enterprises are using WIndows 10. 22% of enterprises are using something older. If we are running a Windows environment, we should be at least on Windows 10. Windows 10 is one of the most complex OSes, due to Windows 8 being a disaster. Microsoft fired every single person who made it. 
4. 90% of Windows devices are out of date on patching, on average for a period of 90 days. As security individuals , we need a **patch policy**. We will lose eventually, but we are tying to reduce the number of times we lose. There are a lot of businesses, including critical government oipoerations, that still use Windows XP, the reason being that there are a lot of proprietary software. There is a small company in NFLD who developed a program that was purchased by a lot of government departments that would be used on critical infrastructure. They never updated the program. If we patch the vulnerable Windows XP, 8the program would not work anymore. We would make a new program , which has to be updated and made to go with the times. They did NOTHING! This is due to the costs, which would mean raising taxes. Has there been any damage made to the Windows 10 infrastructure pc? not yet! Threat actors are still using Windows XP waiting to get in. There has been no pressures at all to get the new software. 
5. During COVID-10's start , March 2021, people were not expecting to remain at home, so many of them took their endpoints home with them. They noticed that at that time, there has been an influx of hacking attempts. There was a lot of sensitive data (40-60%). For those with sensitive positions, they would lay cables at home. Wireless networks was used extensively. 



#### Patch Policies :


	We tell the user that we will set up the pc so that when the pc boots, it checks for updates. If there are patches, they have to be installed!

1. Patch everything right away! 
2. Patching it may cause one of the systems to fail, so , test it in a sandbox with a mockup environment! if you have any issues, patch it! If the software is bad, fix the problem, if not, patch it! It has to be part of the security operations protocol every week!
3. You would have to decide on the method : the users ? network techs?





## Windows Security 


Windows has done some things to make itself more secure. It has tried to isolate applications. Basically ,what it means is when you isolate apps, you would use **Microsoft App Isolation**. You woudl have the main Windows environment at your home, and when you have an app that is isolated, you create a VM on the fly, which is a copy of the host operating system.  The application is run inside the virtual machine. It has no ability to infect your host machikne or your network. If you are considering a new software, or going to a new website , if you were to do so within Windows App Isolation, you would use the browser inside the VM or the application. This is called **Windows Sandbox**. 


When the app spins up, it is in a **Dynamic Container**, so the app itself is run inside the container. These features are not enabled by default. You would make certain changes. You need :


	1. Windows 10 (11) May 2019 and afterwards
	2. Hardware virutalization
	3. Windows 10 or 11 Pro or Enterprise
	4. Run "Turn Windows features on and off"
	5. Run Windows Sandbox.


Windows Defender has gotten quite good lately.



###### Encryption 


Bitlocker Encryption encrypts files and disks




###### HP Sure Click Enterprise (used to be Bromium)

Creates a microvisor, or a micro hypervisor, and it is launched every time the process is launched on the computer. The process is placed inside a virtual machine that is inside the microvisor. This is IMPOSSIBLE for a virus or malware to escape it. Ron argued with the makers of this software, as they were advertising that you do not need anti-virus anymore. If a virus infects the computer with Bromium, the microvisor is infected. If we email a file, the infection gets emailed, and Bromium cannot do anything about it. If you start the microvisor, Ron had a concern in regards to the computer's performance loss. Bromium was popular around 2012-2013. 



###### Deep Freeze : 


It restores the OS to the way you booted it the last time. It is easily beat, as if he can interrupt the boot cycle , change the boot order to a USB drive, then you would beat it. Make sure that CMOS is inaccessile or allow someone to change the boot device. A cage is a good way!



###### In-class Exercise :


X A B      JK    Q A A Z    




ABC


###### Cool Applications for Encryption 


Check out Cryptoquotes ! 
Check out Secret Decoder Ring! :

	It is a ring that had an inner dial of letters (ABCD), an outter ring with ZABCD.... The rings are rotated. If you are to encrypt a message, and you have two peoplek with these rings, they have to agree on the Encryption Algorithm : 

	1.Rotate left 3 clicks
	2. Rotate right 2 
	3. Rotate 1 to the left etc etc 


#### Substitution Cypher (Rotational Cypher):


One letter stands for another

We knew it was three words because of the spaces; if there were not any spaces then it would be very difficult 


XAB  JK   QAAZ
  E 
  O


Think of two-letter words : IS AT TO 


RON IS COOL




#### Caesar Cypher


Used by Julius Caesar to send encrypted messages to his generals. His messages were never deciphered. If bandits or enemy soldiers intercept the message, they would find a sheep skin with the message on it. The population was illiterate! 




For thousands of years, encryption was no more complicated than that. 





#### Class Announcement :


This is a scent-free college. Please do not wear perfumes, colognes, or de-odorants. 