



Today's focus will be on **Client VPNs**




Our next assignment can be done from home! 



# VPN Technology




The intended purpose usually is *Enterprise VPN*


We have a *client* who is at *home*, and the **business** is away!


We could do **Port Forwarding** to get the client access, but should we ? 


Port **3389** is for *Remote Desktop*

It is problematic to port forward to your *Domain Controller*. Why? 


	Anyone can scan a range of public IP addresses, and port 3389, and come back and see all the results!
	Find an RDP-based exploit, and retreive the RDP password


We could port forward to a *web server*, but we would need to segregate the **administrative server** from the *web server*


Rather than port forwarding, we would do a **Secure Tunnel**. 



Client connects to it via a softwate clinet application, authentication happens via a particular VPN protocol, set up credentials. The client needs to know the IP information and needs the User Credentials 



Previously, we would connect the client manually and conduct the setup process. You would download the configuration from the firewall. You can also download a pre-configured client. We can incorporate SSO or single sign on. 


As compared to SSH, why is tunneling a benefit ? 


If we are at the home network, we can see devices on the internet and devices on the tunnel. Once it is connected, the gateway will treat the traffic as LAN traffic. 



In PfSense, you set up the VPN< and then implement rules in place to allow access to other subnets


ANY:ANY is dangerous!



Azure Cloud was not well protected, and in the terms of service , Microsoft indicates they are not responsible for the data. 


## Benefits for using the VPN


There are numerous benefits for using a VPN : 

1. Cost Effective : Organizations can save on power costs for offices , and have workers work from home! Also there is a reduction in connectivity costs while increasing bandwidith
2. Security : Encryption and AUthentication adds more robust security 
3. Scalability : It is easier to add new workers without adding to infrastructure costs. It is scalable to an extent such as adding users, but not that scalable!
4. Compatibility : It supports a wide variety of WAN linking options to allow secure connections via Broadband for example!


When using an Enterprise VPN client, you are far more in control than using a Consumer-Grade VPN client.


### Site-to-Site VPNs



We have a **VPN Gateway** on a network, which is responsible to a tunnel connection to **Headquarters**. It is a **Branch-to-Headquarters**. The client *does not know* that this is happening. 




### Enterprise-vs-Service Provider(Eastlink/Bell)



Eastlink can do VPN setup for organizations connecting to branches. They use **MPLS** which is a form of a VPN.



### SSL VPNs 


SSL can pass any application. 


#### Limitations 


Implementations of the client
OS sometimes does not support the client. 

#### Benefits

Easier to Deploy
Cisco loves IPSEC, on par with SSL VPNs 


IPSEC is a protocol 



## IPSEC



DH5 or Above are used. AES should be used.


When configuring the VPN server is : *pick the highest rated encryption protocol*!





### Assignment 5



>[!todo]
>
>
>We will be using **Unifi** again. He has provided us access to a live-network. We will be getting the invitations on *Monday*!
>
>
>Feel free to ask questions! 



STep1 . Instructions


Step 2. Set up VPN credentials 


We will do : 


1. Settings
2. VPN
3. VPN Server :
	   Server-Side is already set up previously! 
	   We will note it has a local IP address 142.177.220.109
4. Create RADIUS user
5. Download the Configuration File for the Client.ovpn
6. Use the Client.ovpn via the downloaded VPN client software. We can do it on any OS. 
7. Use the credentials you set up
8. Do a sceeenshot of the connected client
9. Once connected, we will be on their network. We can brose, scan and find a device, foinnd the IP address of the device, please the ip address on the browser, and take a screenshot. It is a Ullyses Printer. 