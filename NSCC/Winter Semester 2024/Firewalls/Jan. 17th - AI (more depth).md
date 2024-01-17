# VPNs 



## Definition of VPN  : What is the definition of a **VPN**?




Public IP Address It has a public IP address (Tunnel) Host ----> Switch ---> Default Gateway ---> Internet Connection  
Private Address Public Address  
192.168.1.0/24 (24.222.1.0/26)





If a firewall only allows traffic in (solicited), by default, the router will block unsolicited traffic.

**STATEFUL Firewalls:** Remember traffic in and out.

We can do **Firewall Rules**, where you allow a specific address/port to a destination.

### On the Public Side:

A whole lot of folks from home who need to access the local area network...

We have:

#### VPNs

Without a VPN, if we have https://443/HTTPS, if we want to allow access to a page, or RDP://3389, back in the day, most network admins would put a port forwarding through the firewall. If someone was on the outside and doing port scanning, and we see 3389 open, the attacker would dump public IP addresses and attack them! It is especially worse to use default credentials. Windows does not care about CAPS.

You should NEVER forward an *RDP* Port through the server!

We would like to have ADMINs be able to access the network.

### Types of VPNs

#### Site-to-Site

The most secure of VPNs!

Requires two pieces of hardware:

- Router-to-Router
- or
- Server-to-Server (pfSense Server-to-pfSense Server)

LAN-to-LAN (Lan has switches and hosts behind it)

On the router, we program credentials for the VPN (it acts as a client-in-server). We have a tunnel between the router and the Server (IpSEC).

We go into the router with site-to-site:

The two points as part of the tunnel would have **Static IP Addresses**. If we have a public-facing access point, it would have a **Dynamic IP address** via DHCP. We set one router, which is the **Remote Gateway**. We tell the first router to connect to a public static IP address of the second router. The second router would have the same instruction but reverse. The two routers ONLY accept communications IPSEC from the other router, and vice-versa.

Back in the day, we would configure each independently. In pfSense Linux on the two routers, we would export the settings for the other device. The LAN traffic traverses the internet through an *Encrypted Tunnel*, which means there is no way for a hacker to access the information due to it being encrypted.

IpSEC tunnel traffic: traffic from the Site B local area network is considered local area traffic at Site A.

#### IP Addresses:

Reversed for *Internal Use Only!*

- 172.10.0.0
- 192.168.0.0
- 10.1.0.0

Our Lab PCs would have the 172.16 IP addresses, which is a **Private IP Address Range**. It cannot be used on the Internet publicly. 192.168 can only be used privately on a local area network.

Back to *Site-to-Site*:

Site A and Site B can talk to each other through a secure tunnel and bypass all firewall rules. If you are making a script, it is a royal pain. This is part of the assignment. If we have two sites that we want to communicate seamlessly, we would set up this tunnel. It would be told to use encapsulation. Credentials are encrypted. It is zero knowledge passwords, as the two points cannot read each other's passwords.

Back in the day, he would have a separate VPN box due to routers lacking VPN functionality or could not handle the traffic. One thing that we should be told is that this encapsulation, the more traffic it goes through the tunnel, the more hardware that I need. Both points encrypt and decrypt. If we do a speed test, he got gigabit up and gigabit down. When connecting to a VPN, the speed will go down drastically. The more traffic it has, the slower it gets. We should check the throughput on the VPN connection.

As a technical advisor, who is serving a client who would like a VPN, we place two devices in, and the client complains that the speed is too slow. Prior before, with port forwarding, there was not too much of this issue. Nowadays, since the traffic is encrypted, it slows down drastically.

With pfSense, we can scale it down. If we have pGig up/Gig down, it would tell us we need an 8-core processor 16GB server/router. When he creates this VPN, the router will create a rule/l;

Any traffic destined from Site A to Site B, send it through the tunnel (and vice versa).

**Split-Tunneling**:

"I am on a local area network. When I communicate with this network Site B, use this tunnel". But when going to Google, use the Standard IP connection. We do not want to send traffic through the VPN to go through due to the resource expenditure and the speed. We can have a third site (Site C) connected via IpSEC through the two routers; we can have Site B's router to be the main internet connection. It has the problem of single-point of failure (Site C). He knew a car dealership that set up a VPN with other car dealerships in a Star-Topology where there would be a circle of dealerships connected to a single dealership in the center. It was great at first, due to security, and to get all the connections to connect to the internet through one single point. Geographically, they spread out to the US and elsewhere, so this was unattainable. They experienced outages.

##### Client VPN

We have *OpenVPN* (easy to deploy and manage, secure), *Wireguard* (built into Unifi).



Server(openvpn) | We have a router --------------- internet -----------------lan -------------client | Network




Client-based will use a *Software application* or use something *built-in* in Windows (for example VPN are built-in).

The network admin sends a configuration file, link, and they do so to put the client software on the clients.

On the OS setup, we would set up client VPN accounts, or better with **Single-Sign-On**. When signing in to Windows, we sign in via Windows AD. We would want to use the same credentials for the VPN credentials. That is what we *need to do!* It must have **Single Sign On**. The user would get confused if they would have multiple credentials.

When signing in to the WIFI guest network, we use W00 number, which is a *Single Sign On*.

With that in mind, On the OPEN VPN server, it will pull credentials from Windows AD and use it for authentication.

On Windows, the application is launched which has a configuration file. In the background, the client PC has a configuration file that points the other client to a public static IP address, use a particular algorithm, etc., and the user does not see that!

When authenticating to the OPEN VPN server, all the traffic (avoid split tunnel with OpenVPN) all the traffic goes straight logically to the router encrypted through an IPSEC tunnel. There is also PPTV protocol (another one).

Without authentication, all the traffic is via the **Local Area Network**. Any other traffic physically traverses the internet but accesses a public IP sec tunnel.

On the PC, we have our own router and internet connection. Once authenticating to the VPN, when looking at the bits physically it goes through the local internet connection. All the traffic coming through the PC is going to one IP address.

>[!todo]
>
>Read on **Software-Based VPNs**

With the Client VPN, we need to know:

1. How many clients will connect?
2. How fast is the internet connection?

You do not want to set up a dual-core PC with 4 gigs of RAM as a router, as 5 years down the line, it would not be able to handle the traffic.

Anything sent over HTTPS:443 will be encrypted.

Question: If we use Bitdefender to access the internet. The local network is connected to a proxy which looks at traffic which the proxy would block access or downsize the bandwidth. If we have a VPN client the traffic is encrypted, and traffic is sent through. With ProtonVPN, someone was able to play a game bypassing firewall restrictions. But the router can have a rule where it would drop ALL VPN traffic.

### Peer-to-Site

Requires two pieces of hardware:








------


>[!todo]
>
>
>
>
>- **VPN Protocols:**
  - Explore the various VPN protocols like OpenVPN, IPsec (including IKEv2), L2TP, PPTP, and WireGuard. Understand their strengths, weaknesses, and use case
  - **Security Considerations:**
  - Dive deeper into the security aspects of VPNs, including encryption algorithms, key exchange methods, and how VPNs ensure data confidentiality and integrity.

- **Networking Concepts:**
  - Brush up on fundamental networking concepts such as routing, subnets, and how VPNs integrate with these concepts to facilitate secure communication.

- **VPN Deployment Models:**
  - Understand different VPN deployment models like Site-to-Site, Peer-to-Site, and Remote Access VPNs. Learn when each model is most appropriate based on organizational needs.

- **Firewall Configuration:**
  - Explore how VPNs interact with firewalls and learn about the principles of configuring firewalls to allow VPN traffic securely.

- **Authentication Methods:**
  - Look into various authentication methods employed by VPNs, including user/password authentication, certificate-based authentication, and multi-factor authentication.

- **Troubleshooting VPNs:**
  - Understand common issues that may arise with VPN connections and how to troubleshoot them effectively. This includes issues with connectivity, performance, and security.

- **VPN Best Practices:**
  - Research industry best practices for deploying and managing VPNs. Learn about optimizing VPN performance, securing VPN infrastructure, and adhering to compliance standards.

- **Software-Based VPNs:**
  - Explore more about software-based VPN solutions like OpenVPN and WireGuard. Understand their setup, configuration, and maintenance.

- **Advanced Topics:**
  - Delve into advanced VPN topics like Split Tunneling, VPN Load Balancing, and High Availability configurations.

- **VPN Security Threats:**
  - Learn about potential threats to VPNs, including man-in-the-middle attacks, VPN spoofing, and vulnerabilities specific to certain VPN protocols.

- **VPN in Cloud Environments:**
  - Explore how VPNs are deployed and managed in cloud environments, considering services provided by cloud providers for secure connectivity.

>
