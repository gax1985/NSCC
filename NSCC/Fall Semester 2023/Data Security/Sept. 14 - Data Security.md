



### Quiz


We are figuring out a puzzle!



How many unique values that can be represented in bits ? 




Number of unique values ? 



Range ? 



If we have 1-Bit, we can do 2 values, and the range is 0-1
If we have 2-Bits, we can do 4 values, and the range is 0-3.
If we have 3-Bits, we can do 8 values, and the range is 0-7.
If we have 4-Bits, we can do 16 values, and the range is 0-15.

If we have 5-Bits, we can do 32 values, and the range is 0-31.
If we have 6-Bits, we can do 64 values, and the range is 0-63.
If we have 7-Bits, we can do 128 values, and the range is 0-127.
If we have 8-Bits, we can do 256 values, and the range is 0-255.


If we have 9-Bits, we can do 512 values, and the range is 0-511

If we have 10-Bits, we can do 1024 values, and the range is 0-1023

If we have 11-Bits, we can do 2048 values, and the range is 0-2047
If we have 12-Bits, we can do 4096 values, and the range is 0-4095

and so on ... 



How many digits it would take to represent teh following decimal numbers ?

Answers :

1. 6 Bits 
2. 7 Bits 
3. 8 Bits


In 123.254, if we convert the two decimal values above before and after the dot to binary, how many binary digits are required to represent it? 




For each value, what is the hexadecimal representation? 


Hexadecimal numbers go from 0-F , how do we write 5 in HEX ? 5 

A 10
B 11
C 12
D 13
E 14
F 15 


What is the HEX representation for each binary number ? 


0101   1110 

 5         E



1110 1011 

  E       B

1111  1111
  F       F

1011  1111

  B     F






#### Reasons why he does this test :


There are numbers we need to memorize : 


Standard asking value for keys on the keyboard is 128 values (including numbers letters, etc). How many keys in bits are represented? 7 Bits (128)

We need double the amount , 256 , we need 8 Bits = 1 Byte = 256 values to represent numbers, letters , etc ... 


When buuying RAM, the increments of RAM goes 1024 = 1meg
2048 = 2meg



When putting up Netmasks that are : 

FF , FF  , 0. 0  = /16 Network's Netmask   
255 . 255 . 0 . 0

Each column is represented by 8 bits


Everything is 1 is part of the network address ( in a Netmask )



If a /24 network, 

255 . 255 . 255 . 0 

We will slash 24 bits of it ( We are figuting out the Network's address and slashing it) 

In a /24 , the first three cotetes witll make up the network address

The last octet stores 8 bits. 


0 is the address of the network 
255 is the broadcast address

Thus, 
on /24 network = 254 machines 


255 . 255 . 255 . 0   Netmask 

192. 168 .2 .0   Network address

192 . 168 . 2. 255 Broadcast address  

192 . 168 . 2 . 68 


I know it is the IP address because I would know it by comparing it to the netmak is I have it . 



If we have ... 


192.168. 0 . 0  


We can have 65,536 values


We will deal with port numbers . Every port number means something 


192.168.2.68 : 80    Port 80 is for a web server 


Port number is stored in a 16 bit value.  36 ?


We have TCP 6  protocol ICMP protocol  1    UDP



We use 8 Bits - 1 Byte = How many possible protocol numbers? 256  protocols , 2^8


If we are figuring out protocols : 


If someone is browing , TCP 

If streaming , UDP

ICMP for checking if another system is alive


ANy network we look at , we see a maximum of 5 protocols, but most of the time, we just see the 3 , TCP / ICMP / UDP 


If we see 15 protocols being in use on your network, it is highly suspicious. At that point, we are dealing with a **Protocol Scan**. Specialized systems would use special protocols not in use anywhere else. 


If we are looking at traffic on a machine, and we see port 80, we would typically see 2000 ports in use a day. Port numbers are like radio channels. 


CB HAM radios, it was the form of voice communication. Everything done on the internet, except video, was done on CB Radio. It was common to have one in a car. There was a game called Fox Hunt when you would gather 50 cars and hide in certain places in HRM. They had 16 channels on the radio, and everyone would agree in advance on the channel ahead of time. 

Port numbers are like that . When 2 computers communicate, they have to have a channel that they speak on . If we are speaking to a web server, we are probably on Port 80.  

If we would like to share a file remotely/access a printer, you can contact it on port 445. 

	You can do this simultaneously as it is on separate channels!

On average, ports in use are 2000 ports, calling updates, surfing the web etc. ..


In order for this to work, the computer has to be listening (the server) for incoming communication. The standard is port 80, and it will be listening for the connection .


Databases might listen on port 3306. 

If we would like to log in to remotely control the computer, we would SSH into it on Port 22. If the computer is listening on port 22, it will be available!



When Microsoft started making webservers on Windows, Port 80 was enabled automatically and waiting for connections. If he was a hacker, he would send a signal on port 80, and it would asnwer it. It was done for conveninence's sake. It took years to shut it down. Each of these ports are doorways into our computers. 


In our 1st classes, if you go to a public network, you will see requests sent to port 80, or port 3306 for checking databases, or SSH port 22, etc ... They would routinely scan for ports. What happens if you look at your network and one node in your office is speaking to 20000 ports. It can be ... 


1. A crypto mining bot speaking to other bots in a botnet, and controlled by an entity --- > drop everything and investigate it! but it turns out someone is doing online multiplayer gaming WoW, Half-Life etc. No Gaming Allowed on the network since the behaviour of the node is suspicious. 
2. If you see 5000 ports in use, it is double the average so to be investigated 
3. if 10000 ports, shut it down right away 


When Skype arrived, they did not realize that when downloading and using Skype, you would agree to act as a router for Skype. One CEO's computer was managing a large number of computers in the Skype network. It is not malicious but it iis a a bad idea. 



Port numbers stored in 16 bits = 65536 


Protocols stored in 8 bits = 256 

How many protocols you see on average on a daily basis ? 3-5


65536 


On average , how many ports that a computer accesses ? 2000


If we have a netmask of 255.255.0.0 , how do you represent it in binary ? 

11111111.11111111.00000000.00000000



with HEX , 

FF . FF .  0  .  0



Everything we do in cyber security is a puzzle!


If we are looking at our desktop, we do not know if someone got in or not. 

Start thinking " I am in a puzzle, what clues do I have? "


If I was a hacker trying to get it, what would I do? We recognize patterns such as  a port scanner, a botnet , a game , etc ...


Our 1st task is "If it is a puzzle, what clues do I have to solve it?"


READ NETWORK TRAFFIC!


1 1 1 1   What is it in HEX ? F





We have to install MySQL on a Windows 10 VMWare Virtual Machine!


VMWare licenses all expired. They have new license keys, and we are getting them through email. He got a messgae mentioning the necessity to check the Junk mail folder. 




