


The internet is defined by the devices that are connected to it. 

Examples : 

Devices, services, applications, protocols , packet switches, networks, links and so on. 



The internet relies on **Standard Protocols**. 

One of the main advantages of Standard Protocols : 

1. Defined the same way across the board 
2. You are able to specify the standard
3. It is well-known to everyone
4. Format of messages and their contents, such as answers and replies, are part of the standard. They remain the same. 
5. You can specify the version of the protocol


When you happen to capture network traffic on the wire, we can see the packet capture of the contents of a particular page. 

In some part of the course, we will develop one software to send and reply requests. 

The internet is about **packet switches**, where they are beyond the scope of the course. 


There is no central government of the internet. Everything collapses if something goes wrong. 

The nature of the internet is its decentralization. 

Internet Service Providers *only agree to send and receive traffic as well as forwarding the traffic*.

Internet Segmentation is evident in current events of the world, where internet access is shut down. 

You have cases of partial censorship of the internet as well. 


The internet is about links, and a connection would happen between a cellphone and the internet 



# Roadmap


## Goal 

Big Picture of the intenet 
Terminology 

## Roadmap 

What is the internet ? what is a protocol ? --> today 
Network Edge : hosts , access network, physical media
Network core : packet switching 
...




# Network Edge

Set of devices that host the server. 

We are excluding the core of the internet 

>[!question]
>
>They govern how to connect devices inside local networks? We have residential, institutional  and public mobile networks. 


To enable access to the internet , the network is set up to allow access to the services available on the internet.


At Dalhousie, we have data centers, GPUs , processors and so on, and we need a network to connect the devices and Dalhousie. 

It is true most of the traffic is coming in from outside. Consider how much traffic happens locally. 


The challenge is to connect devices inside the local network. At the Enterprise level, we have data centers, servers and so on. 

Network Edge is enabling connections between devices, and connecting the devices to the internet service provider. 


## Home Router


Access Point for the home network
Access to the internet service provider

On the home network, we have smart devices, computers and so on. We need services to connect our devices together, and to connect them to the wider internet


Technologies involving Home Router : 

1. WIFI : Most used technology on the home network. 
   
   Advantages : you do not have to manage cables. No need to manage infrastructure. No cost overhead. WIFI has a long range where it depends on the obstacles we have. Signal drops beyond 15-20 meters. On campus, we can reach the theoretical capacity.

1. Ethernet : We can have a major advantage is that it is plug and play. On WIFI, you need a password, but with Ethernet, you do not. It does not use signal, and there is no interference. Any ethernet cable is a dedicated connection. On WIFI, it depends on the quality of the signal, and how many devices are connected to the WIFI router. Ethernet connections  : 100mb/s from ISP to router and so on. It stays at this throughput
   
   Issue : the main bottleneck for any connection we have at home , regardless if it is WIFI or Ethernet, is the ISP. The bottleneck is the connection between the home router, and the ISP. 


## Enterprise Network

The objective is the same. We have to connect users to services inside the enterprise, such as computing and storage. 

All the services are hosted on the enterprise server, and incorporating edge devices. 


The *scale* is the difference. This is **Hierarchical Enterprise Architecture**. At this classroom, all the computers are connected to an access point, which is connected to a distribution switch. This is what is providing the capacity to connect. Beyond this, we have one connected classroom. To connect to other classrooms, you just switch/cable and connect the switches to one central switch. This way , if you want to connect your computer to a printer in another network, this becomes feasible. 

What is required for this course: equivalent of what is happening in your home is what is happening here in the enterprise. It is a mixture of wired and wireless technologies. Switches and routers are connected for the benefit of this architecture. If you have three cables, you would want to avoid loops. The connections between switches breaks the loops. Communications happen between these devices, and there are specific protocols to these switches. 


Why do we have switches and routers? Switches offer full capabicity/ full duplex. The ports are 100mb/s per port, and you have 100mb/s connection between routers. We build architecture in the enterprise using switches to get full speed across the network. Switches and routers handle traffic differently. 

Switches are layer 2, and routers are layer 3. 


## Data Center Networks


We have similarities. Data center networks are local networks. 

The servers provide high-computing power across the network. 

The data center components are mainly servers. If we have the global idea of the internet, we have to notice the similarities between the different types of networks. 


Data centers are parts of the decentralized internet/. 


Later we will discuss **content distribution networks**. If you distribute the content on different data centers, you would get access to the nearest data centers. 


### Discussion 


We discuss the way we see the internet. Is it better to have centralized internet vs decentralized internet. 

Cloud is decentralized architecture. You can place data control on another level. Your data is decentralized on the cloud. Having your data on your computer is the extreme decentralization.

Can you count the number of hosting services we are using ? you would be surprised . 
This is centralizing the power of holding the data, as there are only few stake holders on the internet. 

If Google changes the policy of storing your personal files, this will impact millions of individuals. Cloudflare had a big disruption, where everyone was saying the internet was shutdown. It was one provider, and it is a huge provider. alot of content online are hosted on cloudflare. Yahoo services did not go bankrupt. They disappeared, and their data was spread across multiple service providers. who will own the data? 

Technology and architecture can not be good or bad. It is about how we use them. How we rely on them to build the internet architecture is the important thing. 

Governments and countries can interfere with access to the internet based on their policies. A government may say that all ISPs under Iranian government should comply and shut down. You can only reinforce the decentralized nature of the internet. 





### Local -> ISP : Why do we need other technologies? 


When we go beyond the home router, enterprise or data center, we have multiple types of technologies. What is changing on the other side? 

Most two used technologies used at home is *Fiber* and *Wireless*, according to the manti.com vote. 


DSL -> Which context have you used this technology? **DSL** uses the phone lines. **Dialup** is the earliest form of DSL. This is comparable to cable. We use a specific type of coaxical cable in Canada/North America. Your home connection can be fiber due to the push for its adoption. Your home network is using the wireless connection to the outside world. Starlink is a new example 



### Cable 


Most frequently deployed.

The main idea is simple : we had cable tv. So the idea was to use cable tv connections for internet connectivity. 


Cable is still used in rural areas. They can go to 10 gbs/s download/ 1-2 Gb ps upload. You have peak hours when you have limited access to the internet. The cable is being shared for the home network, and everyone is sharing the bandwidth. 


### DSL


High-speed technology over phone lines. You have phone lines, which are covered cables, coming into each house. The idea was to use the same phone cables to provide internet access. This took time to deploy. Many European countries still use DSL. Phone cables are re-used. You can have up to 300m/s download 100mb/s upload. If you are more than 3 kms away from the ISP, connection drops. You are limited by the distance. 

ADSL -> up to 24 mbps download / 1 mbps upload


We are mostly downloading on the internet. We consume a lot of video content. YouTube downloads videos, and will have 100s of mbps to do this. They design these technologies on purpose to have an uplink lower speed than downloads. This is problematic during COVID, where working from home depends on having balanced download/upload rates. 


Bell Aliant has 1 gbps upload/1gbps download. How come this parity exists from fiberoptic cabling ? 

People do not need statistically all this bandwidth. If we change our behaviour to comply with the asymmetrical rate of downloads/uploads. There is no scientific reason for not providing symmetric download/upload rate
- 


### FTT


New infrastructure. It uses optical fibre cable. Speeds are 1-2 gbps symmetrical download/upload. This gets as close as possible to the end user. It is scalable to 10 gbps. We can go tens of kilometers between OLT and presides. We avoid the shortcomings of DSL. This type of fiber is of interest to developing countries. 


### Fixed Wireless Access


It has a wireless connection going to an antenna, and from the antenna to the service provider. The problem is the quality of the connection, as it depends on the environment, and affected by obstacles. it is ~ 50mbps - 1 gbps  



### Satellite


radio link to the spacecraft. GEO less than or eequal to 50 mbpos, LEO less than or equal to 500 mps. It is global, and has universal reach. Activation is quick, and latency is more than or equal to 550ms. Weather affects the connection. It is useful for remote communities, maritime and disaster recovery. 


#### High Income 32 Countries


More and more fibre optic cabling is prevalent. Cable modem is a large chunk. Geographically, we have countries like the UK where DSL is widely deployed, same as France, and you have countries where cable is the main. You also have contries where DSL is upcoming. Fibre-optic is the biggest trend. 



### Broadband Access in Canada


https://crtc.gc.ca/cartovista/internetcanada-en/

![[Pasted image 20260113093830.png]]





The objective is to have 95%-100% to 50mbps download/ 50mbps upload broadband. Rural communities has a lower adoption rate of 60%. The deployment timeline is by 2030. We will have more than this, but it depends on the technology and the geographical area. 



### Access Market to the Internet

This is a regulated market. Some countries have a regulating agency : CRTC. They regulate wholesale rates. The tariffs applied are regulated by CRTC. They insure that all internet data is open. It tries to regulate how smaller-ISPs are being built, by having them buy slots from bigger companies. 

Speeds of 50 mbps download / 10 mbps upload for fixed broadband services. Unlimited data option for fixed broadband services. Bell has 6 months to give access to all competitors. They force large companies, in some areas, to open fibre optic cabling to other competing ISPs. 



### Network Neutrality

They insure that all internet data is treated fairly. ISPs must treat all internet communications equally. If they have the same access possibility as the ISPs, there should be no difference in the traffic. They should not discriminate pricing, and all traffic should be treated equally. They are not able to throttle speeds if the user is going to YouTube. Illegal sharing is a fact, but throttling should not happen as it is discriminating. 



#### Blocking Access to a local application/website

Some ISPs push users to use a specific video platform. 
Some ISP block access to a lawful application/website. 
A content provider pays an ISP to be placed in a fast lane over the same access link. 

Who decides whether the ISP can do this or not? How would you comply with this? If ISPs do this, do you think this is allowed under network neutrality ? -> No! 















