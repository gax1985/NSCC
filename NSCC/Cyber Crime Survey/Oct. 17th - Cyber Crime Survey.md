



# Encryption


We started to look at this the other day. 


Characterists of Hashing ? 


1. one-way
2. Unique output


What do we use it for? 


1. Confidentiality : Passwords
2. Integrity 



When you get an email with student information, you are moving from server to server. To the user, it looks like one machine. We have Single-Sign-On. Each of these servers requires a login. The way it works is , when you create a password, Windows does not store your password. 



When you create a password in a Windows system, it hashes what you have entered. If you entered "Password123", it wont store "Password123", but the hash of it. Hashes are all the same size. It puts the password in the memory. When you go to another server (Brightspace etc...) , the computer/server that you are on takes the hash, and passes it to another server. The second server uses the hash. The hash is stored in memory on your pc. We have tools that extract it. When you log in to the other machine, it is expecting the hash of the password. 


Thus, if you are a hacker who extracted the hash of the password from the memory, you can use the hash to log in to the other servers. As long as you have the hash of the password, you can pass it around. It is called **Pass-The-Hash**. 


## Integrity


Verifies the file that was sent to you was not edited or modified in transmission.



## Authentication 


We talked about it 



## Non-Repudiation


This makes sure that evidence that has not been tampered with



## Obfuscation 


It is the act of hiding something




## Plaintext  ------------------> Digest

It is the input of the Hashing process




#### Examples: 


MD5 


- New hashing algorithm is developed due to the existance of collissions , which is two different texts producing the same hash. 




## Cryptography 


This is what we are thinking of when thinking of encryption. 


#### The Caesar Cipher 


you rotate by three characters to the right, and then you can read off the coded message. 



#### Substitution Cipher


If we have a single-letter substitution, when you figure out if there is a Z or an O, we can do a frequency analysis of letters, and we check which characters come up often. We can get clues if we put spaces in there. 



- There were three students who graduated, with one being the type if they have learned something, they would actually create it. They studied crypto-malware, and he made it for fun. Himself and someone else wrote a demonstration program for the cyber booth, where they set up a couple of computers on the network. When you hit "Start" , it starts a timer of the time left until you decode a message to stop a bomb. The key was exchanged between two malicious entities on the network. You would have to capture the network traffic, and people had 50 seconds to do it. He wrote it for fun, because he wanted to demonstrate what he has learned in order to test himself. 




## Encryption Algorithms




Plain Text --- Algorithm ---- Cipher text --- decryption algoritm --- plain text 





The issue is : 



We could have a system where two individuals, with one in China, and one in Canada in order to send messages back and forth. They would agree on a complicated algorithm, and everything went fine until someone figures the encryption/decryption algorithm, which can be done. Encryption algorithms get broken all the time. 


Problem #1 We have to assume that the adversary figured out the encryption algorithm. We need something else for the encryption algorithm , which is the **key**. We would agree that the key is one of the pair's birthday. 


If we have a **key**, and we sent someone to **Russia**, **North Korea** and **Alabama**, and we all have our encryption keys, and one of the individuals gets caught, and the key was extracted from them. If the key is known, we need a new key. Now we have a problem. The key has to be changed somehow. We can not encrypt the key, because without the new key, you can not decrypt the message. In the WWII and the Cold War, there were a lot of ingenious methods to do this like **Steganography**.  If he whispered the key while walking next to a cafe , someone could hear it. There is no solution that could not be overheard. This is referred to **Key Exchange Problem. 



Since the key is the same that he used is the same for the other individual as well, we refer to this as **Symetric Key Encryption/Cipher**


Problem :


Key is the letters **KZ**, for each letter, he will move the alphabet so the letter of the key is underneath the letter of the alphabet.


For example,. if he wanted to ecrypt his last name : 


M A C L E O D 
X Z  X Z X Z X


For the first letter in the message, the letter is X, the X is placed under A


The message is BAD. He would like to encrypt it. 


ABCDEFGHIJKL
XYZABCDEFGH
ZABCDEFGHIJ


READ DOWN TO ENCRYPT, UP TO DECRYPT



The only way is to practice!


The letter in the key tells you which letters to line up under A. If we do not know the key, we cannot decrypt the message. Brute-force happens with trying endless possibilities.



## Accepted Standard of Encryption



We can prove mathematically that to break the encryption, it would have to be the expected lifetime of the sun. The Encryption Standard is based on the length of the key, and the algorithm



In the 1970s, Canada needed a really good encyrption standard. Canada had to come up with an Encryption Standard that was difficult to break with Brute-Force. The way it works is mathematicians from all over Canada are invited to participate, and they would have two years to come up with one. They will come together in a conference, and propose the encryption standard. Everyone else in the competition is there to prove your Encryption Standard can be broken. 


Out of the conference, a new encryption standard will be agreed upon. The result is : 



##### The Data Encryption Standard 



It is always refered to as **DES**. It was a wonderful encryption. It has symmetric key encryption, and it was used for communications, top-secret research etc. In the 1990s, this proved to be broken. We would need a new Encryption Standard. During the next two years, everything was going to be broken. Someone noticed something : They noticed that **DES** could be broken only once. If you took the encrypted text, and encrypted the same text again with the same encryption standard, it was harder to break. It took three encryptions, and made it impossible to break 




Plain Text -----------> DES -----------> Cipher Text (Encrypted messager)




Cipher text --------> DES ------------> New Cipher Text 



New Cipher Text  --> DES -----------> Final Cipher Text


(You only decrypt the message once)



This worked! People called it **3DES**, and became known as **Triple-DES**. 



They went back to the conferences and after a standard period of time, a new encryption algorithm was born...


They produced the **Advanced Encryption Standard**, aka ... **AES**.  It is used for the top-secret communications today!



The problem : these are computationally difficult to break based on the computers that we have today. The algorithm (in the future with Quantum Computing) would be broken in days instead of the lifetime of the sun. 



**AES** is a symmetric key algorithm, but still has that **Key Exchange Problem**. On the plus side, it is *fast*. It required little computational resources to encrypt and decrypt text. 



The reason the keys are created is that the malicious actors will eventually break it. 


The challenge was : create an algorithm that would not be broken. 


The solution was **RSA**. The malicious actors could know the algorithm , know the key but can't decrypt it. 


How it works : 


The key is in two pieces : **Public Key** and **Private key**.


##### The Public Key

Can be shared! You can encrypt the message to encrypt it, but you need the **Private Key** to decrypt it



##### The Private Key 

You would need it to decrypt the message. Each private key is different 



To send a message, get the destination's public key, use your private key, encrypt the message, the receiver decrypts the message with their public key 



###### The Key Exchange Problem


One is compromised. His private key is compromised but that does not matter. 




## Asymmetric Key Cryptography 



Both sides are not the same. It is known as **PKI** or **Public Key Infrastructure**. 


This is used when you type in the browser : 


>https://.....



The traffic is *encrypted* when you visit this website. Consider where you use that, such as Google, Gmail, Bank's website , ...

When the account is established, Google sends you their Public Key, it goes in the Certificates Store on your pc, and the next time you need to communicate with Google, your pc takes Google's Public Key and sends it off to Google. This is how Encrypted Web Traffic is done. *Certficates* are public and private keys. 



There is a problem : Assymetric Key Cryptography is slow, and needs a lot of processing poiwer . We do not want everything we send back and forth on a website to go through Public Key Encryption. It would be nice to use Symmetric Key Encryption. But we have the *Key Exchange Problem*. The only thing this is used for is to **Exchange the Symmetric Key**. You use a public key and a private key, then encrypt the Symmetric Key and send it off. 


The Private Key is never exchanged, but you can publish your Public Key. It allows them to send you encrypted messages. If someone's Private Key is compromised, an encrypted message can be decrypted. 


If someone compromised your encryption key, you would be able to re-generate your keys. 




##### SSS


Used for Wireless Communication. We are establishing a Wireless link ( such as a WIFI access point), and the traffic is encrypted. 




AND
======
0      0    0 
1      0    0
0      1    0
1      1    1



OR 
=====
0   0   0
0  1    1
1  0    1
1  1    1



XOR
=====
0   0   0
0   1   1
1   1   0
1   0   1



Coded message in BINARY : 


1 0 1 1 0 1 0 1 1 1


We will use XOR encryption with the key : 


1 0 1 1 


1 0 1 1 0 1 0 1 1 1

1 0 1 1 1 0 1 1 1 0 

XOR-----------

0 0 0 0 1 1 1 0 1 1

Decrypt ---------

1 0 1 1 1 0 1 1 1 0 

-------

1 0 1 1 0 1 0 1 1 1 



This is known as **RC4**, which is known as **WEP**. 



The algorithm is REALLY fast! It is very easy to break though. This is part of the wireless security is easily broken. The people who were driving the change behind this is **PCI** or **Payment Card Industry**. If you are in a business that accepts credit cards, you have to be **PCI-Compliant**. The auditor will know whether you are PCI-Compliant or not. **WEP** was no longer PCI-Compliant. Thus, **WPA** and **WPA2** was born. 


They were using **AES**, but there was another problem. The router uses a Single Symmetric Key. Wireless is a radio signal. All that is needed is an antenna. Networking technology was invented by hippies. 



The symmetric key, 1011 in the example, when you log in to a wireless system, there is the **Key Exchange Problem**. The key has to be encrypted. **Pre-Shared Key** was used, or known as **PSK**. We would use that in order to encrypt the message. 


What would we think the **Pre-Shared Key** of the wireless system? the pass phrase!



Question : What happens if there is no password? 

Answer : it is not encrypted then! 



What would happen that is a weak passphrase, or a dictionary word ? There are lots of software you can get , 


The passphrase is hashed, the hash is sent. The hash can be hijacked by someone else. 




You can not take a hash and rebuild the hashed entity. When logging in to a computer, and when a password is typed, the hash is checked. What is the pre-shared key that is needed? your password. The password can be used to encrypt. The hash of the password can be seen , and for the sake of argument, it may look like this : 

	D 1 0 X Z 7


and the passphrase : 

>PENNYISAFREELOADER



We know the hashing algorithm, such as MD5, or SHA256(256-bit key). (Base64 is an encryption). If we know the algorithm and we type things in, we get hashes. We can do so until we get a hash that is exactly like the hash for the password. so what we need is a huge database of hashes, and the corresponding text that made those hashes. 


Table (MD5)
========
hashes
hashes
hashes

Table (SHA256)
=======
hashes
hashes
hashes



Regardless of the input, you get a set size for the output. The tables are called "**Rainbow Tables**". We need the hash of the passphrase, so since it is a radio signal, we can walk around with an antenna, we get the hash, feed it to the rainbow table, it gives us the *passphrase*, on the condition that the hash is in the *Rainbow Table*. 


People have short passwords, easy to guess passwords, Dictionary passwords....


The most popular password on the internet is : 

>PASSWORD


Even if it is spelled this way : 


P 4 $ $ W 0 R D



##### Solarwinds Hack


Solarwinds had an update server where updates are dispatched. The update server had a password of :

>PASSWORD


China hacked into it, placed malware on the Update Server, and then everyone who updated their Solarwinds software caught the malware. 





## Challenge 


When connecting to a Wireless Access Point, when the first connection happens, the key is sent. You would have to be listening exactly at the time when they are first connecting, or , you can send a special packet called **DEAUTH** packet, when logs them off, so the devices reconnect automatically. You would keep sending this packet, and you capture the passphrase. This is why wireless networks are so easy to crack. Also, If it is a short , common phrase, dictionary password, anyone can break into it. What you want is 25 characters, something that makes no sense, it is not a known word. 




Hint : Password retries when it comes to brute-forcing is usually 5 minutes after 3 failed attempts. 


CAPTCHA requires software that is intelligent. CAPTCHA by-passers exist.  


If you have a website with CAPTA to a website that bypasses CAPTCHA, then they have access to all the data on your target website. 


Streaming services are a large vulnerability, because we are not watching the packets they are sending us. 



### Public Key Cryptography


Uses a key pair : a private key and a public key. To encrypt it, we would use the receiver's public key, and the receiver would decrypt it with their private key. 



#### ECC 


aka **Ecliptic Curve Cryptography**: 


It plots a mathematical function that produces a C shared curve. It plots two intersect points on that curve, and the points are your public key and the other is the private key. 


When Ron designed neural networks, they would have hundreds of dimensions 




### Is there an encryption that is impossible to break ? 


YES!



There is a military technique called **One-Time-Pad**. They are flash papers. Assume today we are sending a message, the sender and receiver would both have a pad, they tear the cover page off, and the keys are entirely randomly generated. One of the things you can do is the ping-pong ball used in the lottery. There is chaos math because it would be impossible to predict the winning numbers. Computers need a *seed* to generate a random number. This is why the computer generated random numbers are called **Pseudo-Random Numbers**. Computers can not just think of a random number; it needs a starting point or *seed*. Over time, if someone got lazy when generating the one-time-pad, so they are not truly random, you can break the encryption. The weakness is : 

THE CODE IS NOT TRULY RANDOM


If the pad is stolen, it is made of highly-flammable chemical, so it is called *Flash Paper*. 

There is no algorithm involved in the One-Time-Pad. There are similar encryptions that do the same, but it is still a computer-generated number. 


RSA is usually used in the PKI infrastructure, you use public-private key pair, and immediately upon establishing the connection, you use AES or symmetric encryption. Public-Private Key Encryption solves the Key Exchange Problem. 


When you set up a VPN, you would select the *Encryption Standard* to use, and the *Hashing Standard* to use. The hashing algorithm (SHA256 for example) is used for the passwords and certificates, and for encryption we can use 3DES (which is still good until 2050). AES is better to use. It depends on what you are sharing.  


Do NOT dispose of hard drives in the trash. Take the hard drive, take a good drill, drill two holes in it, and beat it with a sledgehammer. You can de-gause them with a magnet, but the only true way is to physically destroy the hard drive. You can not use it for optical drives, which means they need to be smashed too.  


Check : 

Oliver North and the Iran-CONTRA standard



### Question : 

If we are placed in an organization that did not have any policies for anything, an we are looking at the Wireless network (WPA-AES) , what kind of standards we should recommend? 


### Answer : 


A minimum of 35-characters.


#### Scenario : 

If we have a target who frequents MacDonalds, chances are their device is set to automatically connect to the network. The only identifier for the network is the SSID. We would take the computer, and a wireless router, you make the SSID the same as their SSID, and the password the same, you go to the target's office, park outside, and then their computer connects to it. 



Most of the digital world does not abide to good security. We would have two types of audits : **Compliance Audit**, which means a standard is there, and the **Performance Audit**, which means that good security is in place. So companies could pass a **Compliance Audit**, but could fail the **Performance Audit**. The thing is, they have to get this audit every few years, so that means that they could do very poor security practices. 


Password managers are a good option, but they can be easily lost. If we connect the phone to a wireless network on vacation, the phone will constantly try to find this wireless network. You can remove the old saved passwords. 


We can set a duplicated wireless access point with the exact same name and password that is not connected to anything, and set it next to our building. 


Check out **Evil Twin Attack**. Shopping malls name their SSID the name of the store "Lululemon". You can sit outside the store, create a cloned wireless access point with a strong antenna, and all the machines in the store are connected to you. 




