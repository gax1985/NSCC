Today we will continue focusing on network performance. 

We will focus today on **Network** **Delay**, **Packet** **Loss** and **Throughput**


# Packet Delay 


We will measure the time needed to transfer a packet. 


We have : 

Propagation Delay D*prob* = length of physical link(s) / propagation speed (~2x10^8 m/s)-> s

Dtotal = dprocessingdelay + dqueuedelay + dtransmissiondelay + d*probagationdelay*



Ping and Traceroute are tools that hellp you compute this delay




## Queue (aka Buffer)

Queue has finite capacity 
Packet Loss happens because the packet arrives to a full qoeue
Packet Loss happens also because of Packet Switching
Congestion happens frequencly over the Internet


#### Queueing and Loss Interactive Animation
If you have an incoming rate of 500 packets/s, and you have an outgoing transmission rate of 1000 packets/s. There is *no delay in here* due to the **First In, First Out** rule. There may be processing delays. If we change the transmission rate of the *outgoing interface* to 250 packets/s , some packets are waiting in the queue. Any additional packets coming in will experience queueing delays. When the queue is full, we may have some troubles. 

When you ave the incoming rate = outgoing rate, in may cases, you may experience Packet Losses.

You do not have buffers for incoming packets. They go to the procesisng units , check for errors and look for the next hub. All interfaces tend to have incoming and outgoing packets. Incoming packets go directly to the processing units.

If you have a reasonably desiged router, we tend to have dedicated processors for these tasks. When we look at the Forwarding Table, the main problem comes from *Congestion*

# Throughput 


It is what we use to measure the speed of the connection. Measured in *Bits/S*.


You can measure an average over a long period of time. IPerf Tool is used to measure the speed of the connection. 

If we have a computer downlaoading content from the server, we have a *link capacity* between the client and the router, and *link capacity* between the router and the server.


1. Server sends bits (fluid in an example water pipe ) through the pipe. 
2. The pipe can carry the fluid Rserver < Rcomputer 

We take the **minimum value**. This bottleneck will define the throughput. 


1. Between Server and client Rs < Rc  
2. Back from client to Server Rs > Rc

Bottlenecks happen at the **edge of the router**. Knowing where the bottleneck is is a complex problem. We have to accept it.

If someone else at home is connected , we find out the remaining R by substracting the Rs from the R belonging to the remaining client. 

If you have a video streaming client, the bottleneck can shift dynamically. 

Consider that you can translate the quality of the contents in Megabits/S , if we are near the router's antenna, we would check if there is anyone competing with you in this connection. 

This is complex, and this is why we have the tools.


How can we compute end-to-end delays ? 




### Example


Three-Link Example 


Transmission rates : Ri(bits/s) X 3 nodes (server , first hop , second hop, client)

End to end delay = sum of transmission delays  = P / Ri for i = 1,2,3

Propagation Delays = Di/c for i=1,2,3 --> Distance between computer and first router/speed of the propagation of the signal


- There is a waiting period to receive the last bit of the packet before we can start with the next packet. 
- Store and Forward : We have to receive the whole packet + process it + forward it

Transmission Delay between the 2nd (slower) and 3rd (faster), it takes more time to send over a lower-speed lane

The size of the rectangle 



End to End day = ( P/R1 + D1/c) + (P/R2 + D2/c) + (P/R3 + D3/c)

When we have correct representation, we can have a clearer view of end-to-end delay.


He is assuming we are examining network components. The OS system is ideal, and when we start transmission on the NIC, we experience these delays. 

The rectangle gets smaller because of higher speed, we have lower trannsmission delay. 






Processing Delays

Queueing Delay = Qt/


(Size of Packet/R1<- transmission rate from 1st computer to the next hop>)




Assuming R2 < R1 and R2 < R3 





If you have three computers connected to trhee servers : 

1. Calculate the Minimum of Rc for each, Minimum of Rs for each and the Central Link is shared equally -> R/3, Rs , R/3)

---

In practice we deploy measurement tools over the networks. 

Network Monitoring gives performance indicators for Network Administrators. 

Jitter : Statistical variation of the delay. How is changing from packet to packet? 

Quality of Service : Aggregation of Delay, Jitter, Loss and Throughput.

Service Level Agreements can be contracted between ISP and the enterprise client. The ISP will commit to deliver a quality of service defined by maximum delay, maximum packet loss, and throughput.

 On the higher level, we get **Quality of Experience Indicator**, which is for the user's experience. It is measured by a simple metric used in all the software we are using in the settings --> It is not a scientific assessment , as it is a 5-star rating.




## Questions : 

1. Is VOIP sensitive to packet loss ? 

This is what happens in practice. The brain , if there is packet loss, reconstructs the auditory message. It is less sensitive to packet loss. 

If it is senstive to packet loss, we would number all the packets with checksums, the audio message will make no sense if it arrived in chunks. 


2. Is file transfer delays sensitive? 

The delay will not impact the final product. This is way different from losing packets. You would be less senstive to delay as compared to packet loss. 


3. Is VOIP delay-senstive? 

Yes it would! The message would be broken up to a degree where you would not understand it. 
Propagation delays would affect a call from Canada to Australia. 

4. Are file transfers requiring minimym throughput? 

It is Elastic Traffic, where if you give more space  you get more traffic.

5. Is VOIP minimum throughput-affected?

Yes you would need a number of kbs/s to have a VOIP call to make the audio understandable. 



# Video-over-IP


Application | Packet Loss Tolerance | Throughput Requirement | Delay Tolerance 


File Transfer | No - zero |  Elastic Service
Voice Chat | Yes - some loss | Less Elastic - Needs | yes a range  Few kbps-sm 1 Mbps | 100 msec
Video Streaming | yes |  Frew kbps, 5 Mbps | few seconds | few seconds
Gaming | Yes | Few Kbps | 100 msec
---

# Lecture PDF 


