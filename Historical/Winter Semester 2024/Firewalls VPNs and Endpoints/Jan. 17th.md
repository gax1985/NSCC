



# VPNs



What is the definition of a **VPN** ? 


	""


		Public IP Address	 It has a public IP address
                                (Tunnel)
Host   ----> Switch ---> Default Gateway ---> Internet Connection   
                Private Addess             Public Address  
         192.168.1.0/24                            (24.222.1.0/26)




If a firewall only allows traffic in (solicisted ), by default the routrer wil block unsolicitied traffic 


STATEFUL Firewalls : Remembers traffic in and out. 


We can do **Firewall Rules**, where you allow a specific address/port to a destination 





### On the Public SIde : 



A whole lot of folks from home who need to access the local area network ... 


We have : 


#### VPNs

Without a VPN, if we have https:// 443/HTTPS , if we want to allow access to a page , 

or RDP://3389 , back in the day, most network admins would put a port forwarding through the firewall. If someone was on the outside and doing port scanning, and we see 3389 open, the attacker would dump public IP addresses and attack them! It is especially worse to use default credentials. Windows does not care about CAPS. 




You should NEVER forward an *RDP* Port through the server!


We would like to have ADMINs be able to access the network 


### Types of VPNs



#### Site-to-Site

The most secure of VPNs !

Requires two pieces of hardware : 

Router-to-Router 

or: 

Server-to-Server

(pfSense Server-to-pfSense Server)


LAN-to-LAN (Lan has switrches and hosts behind it)

On the router, we program credentials for the VPN

(it acts as a client-in-server)

We have a tunnel between the router and the Server (IpSEC)


We go into the touter with site-to site :


The two points as part of the tunnel would have **Static IP Addresses**

If we have  a public-facing  access point , it would have a **Dynamic IP address** via DHCP

we set one router which is the **Remote Gateway** 


We tell the first touter to connect to a public static IP address of the second router 


The second router would have the same instruction, but reverse. 


The two routers ONLY accept communications IPSEC from the other router, and vice-versa.


Back in the day, we would configure each independently. In pfSense linux on the two routers, we would export the settings for the other device.


The LAN traffic traverses the internet through an *Encrypted Tunnel*, which means there is no way for a hacker to access the information due to it being encrypted. 


IpSEC tunnel traffic : traffic from the Site B local area network is considered local area traffic at Site A. 

#### IP Addresses :

Reversed for *Internal Use Only!*

172.10.0.0

192.168.0.0

10.1.0.0


Our Lab PCs would have the 172.16 ip addresses, which is a **Private IP Address Range**. It can not be used on the Internet publically. 192.168 can only be used privately on a local area network. 




Back to *Site-to-Site*:


Site A and Site B can talk to eachother through secure tunnel and bypass all firewall rules. If you are making a script, it is a royal pain. This is part of the assignment. If we have two sites that we want to communicate seamlessly, we would set up this tunnel. it would be told to use encapsulation


Credentials are encrypted. It is zero knowledge passwords, as the two points can not read eachother's passwords. 


Back in the day, he would haver a separate VPN box due to routers lacking vpn functionlaity or could not handle the traffic. One thing that we should be told is that this encapsulation, the more traffic it goes through the trunnel, the more hardware that I need. Both points encrypt and decrypt. If we do a speed test , he got gigabit up and gigabit down. When connecting to a VPN, the speed will go down drastically. The more traffic it has, the slower it gets. We should chech the throughput on the VPN connection. 


As a technical advisor, who is serving a client who would like a vpn, we place two devices in, and tghe client complains that tthe speed is too slow. Prior before , with port forwarding, there was not too much of this issue. Nowadays, since the traffic is encrypted, it slows down drastically. 


With PfSense, we can scale it down. If we have pGig up/Gig down, it would tells us we need a 8- core processor 16gb server/router


When he creates this VPN< the router will create a rule /l ;


Any traffic destined from SIte A to Site B , send it through the trunnel 
(and vice versa) 



Split-Tunneling : 


	" I am on a local area network. When I commuinicate with this network Site B, use this tunnel". But when going to Google , Use the Standard IP connection. We do not want to send traffic through the VPN to go through dyue to the reossource expenditure and the speed. We can have a third site (Site C) connected via UpSEc through the two routers , we can have Site B's router to be the main internet connection. It has the problem of single-point of failure (Site Cc). He knew a car dealership that set up a vpn with other car dealerships in a Star-Topoloffy where there would be a circle of dealerships connected to a signle dealershup in the centrer. UIt was great at firstr, due to security, and to get all the connections to connect to the internet through one single point. Geographically, they spread out to the US and elsewhere, so this was untainable. They experienced outages. "
	


##### Client VPN 


We have *OpenVPN* (easy to deplot and manage, secuire), *Wireguard* (built0ibn into Unifi)

								Server(openvpn)
								|
We have a router --------------- internet -----------------lan  -------------cliuent 

							|
					
						Network	


Client-based will use a *Software application* or use something *built-in* in Windows (for example VPN are built in). 


The nbetwork admin send a configuration file, link , and they do so to put the client software on the cllients 



On the OS setup, we would set up client vpn accounts ,or better with **Single-Sign On**. When signing in to Windows we sign in via Windows AD. We would want to use the same credentials for the VPN credentials . That is what we *need to do!* It must have **Single Sign On**. The user would get confused if theey would have multiple credentials 


When signing in to the WIFI guest network, we use W00 number, which is a *Single Sign On*. 

With that in mind, On the OPEN VPN server, it will pull credentials from Windows AD and use ti for authentication


On WIndows, the application is launched which has a configuration file. In the background, the client pc has a configuration file that points teh other cclient to a public static ip address ,use a particyular algorithm , etc and the user does not see that! 


When authenticating to ghen OPEN VPN server, all the traffic (avoid split tunnel with openvpn) all the traffic ghroes straight logically to the router encrypted through an IPSEC tunnel. There is also PPTV protocol (another one)


Without authentication, all; the traffic is via the **Local Area Network**. Any other traffic physically traverses the internet but access a public ip sec tunnel.


On the pc , we have our own router and internet connection. Once authenticating to the vpn, when looking at the bits physically it goes  through the local internet connection. All the traffic coming through the pc is going to one IP address. 


>[!todo]
>
>Read on **Software-Based VPNs**


With the CLient VPN, we need to know : 


1. How many clients will connect? 
2. How fast is the internet connection ? 

You do not want to set up a dual core PCC with 4 gigs of tram as a router, as 5 years down the line, it would not be able to handle the traffic. 

Anything sent over HTTPS:443 will be encrypted. 

Question : If we use BitDefender to access the internet. The local network is connected to proxy which looks at traffic which the proxy would block access or downsize the bandwithd. if we have a VPN client the traffic is encrypted, and traffic is sent through. With ProtonVPN , ssomeone was able to play a game bypassing firewall restriuction.. But the router can have a rule wherew it would drop ALL VPN traffic.


The fundamentals of a VPN has not been changed for a while, but the encryption algorithms are constantly improving. It is all about computing power!
### Peer-to-Site


Requires two pieces of hardware : 



