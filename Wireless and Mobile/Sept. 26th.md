


  

### 802.11 – ARCHITECTURE  
 The basic building blocks of 802.11 is a Basic Service Set (BSS)  
 A BSS is a collection of that make up the WLAN  
 A Basic Service Area (BSA) is the coverage an AP provides  
 A WLAN running in infrastructure mode always has one or APs  
 An independent WLAN without an AP is called and ad-hoc  
network  
 Independent STAs can connect in a decentralized fashion  
 If a STA in in its BSA is can communicate with others STAs in  
the BSS  
9

### 802.11 – ARCHITECTURE  
 To connect two BSSs, 802.11  
requires a distribution system  
(DS) as in intermediate layer  
 BSS1 connects to the DS  
 Which connects to BSS2  
 How does STA1 in BSS1  
connect to STA2 in BSS2?  
 802.11 defines and AP as a  
STA providing access to the  
DS  
 Data moves between a BSS  
and the DS through the AP  
10

##### Definitions for the terms in the context of IEEE 802.11:

1. **Access Point (AP)**: An access point is a device that allows wireless devices to connect to a wired network using Wi-Fi. [It acts as a bridge between the wireless clients and the wired network, providing connectivity and managing data traffic](https://en.wikipedia.org/wiki/Wireless_access_point)[1](https://en.wikipedia.org/wiki/Wireless_access_point).
    
2. **Distribution System (DS)**: The distribution system is the infrastructure used to connect multiple access points within a wireless network. [It enables communication between different basic service sets (BSS) and integrates the wireless network with other wired networks](https://www.geeksforgeeks.org/ieee-802-11-architecture/)[2](https://www.geeksforgeeks.org/ieee-802-11-architecture/)[3](https://en.wikipedia.org/wiki/Wireless_distribution_system).
    
3. **Portal**: A portal is a logical entity that connects a wireless local area network (WLAN) to other networks, such as a wired LAN or the internet. [It serves as a gateway, allowing data to flow between the WLAN and external networks](https://www.geeksforgeeks.org/ieee-802-11-architecture/)[2](https://www.geeksforgeeks.org/ieee-802-11-architecture/).
    
4. **Distribution Service**: The distribution service is a set of functions provided by the distribution system to manage the delivery of data frames between stations within the network. [It ensures that data is properly routed to its destination within the extended service set (ESS)](https://www.informit.com/articles/article.aspx?p=24411&seqNum=7)[4](https://www.informit.com/articles/article.aspx?p=24411&seqNum=7).
    
5. **BSSID (Basic Service Set Identifier)**: The BSSID is a unique identifier for a basic service set (BSS) within a wireless network. [It is typically the MAC address of the access point’s radio interface and is used to distinguish between different BSSs within the same network](https://en.wikipedia.org/wiki/Service_set_%28802.11_network%29)[5](https://en.wikipedia.org/wiki/Service_set_%28802.11_network%29)[6](https://www.cbtnuggets.com/blog/technology/networking/8-components-of-a-802-11-wireless-service-set).


### 802.11 –  ARCHITECTURE  
 IEEE also defines the operating  
frequency range for 802.11  
 802.11 standard provides  
frequency bands for use in Wi-Fi  
communications: 900 MHz, 2.4  
GHz, 3.6 GHz, 4.9 GHz, 5 GHz,  
5.9 GHz, 6 GHz and 60 GHz.  
 Each frequency band contains  
channels which break the band  
up into smaller frequency ranges  
11

### 802.11 –  ARCHITECTURE  
 Sound travels in waves  

 >[!definition]
 >
 >###### Wavelength : 
>
 >>Completing the repeating  pattern   
>
>###### Amplitude
>
 >Waves height   
  >
  >###### Frequency 
  >
>>The rate at which a wave  repeats 
>
>###### Speed = 
>
>>**Wavelength** X **Frequency**
>
>![[Pasted image 20240926122546.png]]
>
>

802.11 –  
ARCHITECTURE  
 A look at some frequency  
ranges and their names  
13

802.11 – ARCHITECTURE  
 Who uses what  
![[Pasted image 20240926122615.png]]


![[Pasted image 20240926122655.png]]

AN OVERVIEW OF WIRELESS TECHNOLOGIES  

> 
>There are 3 major technologies that WLANs use :
> 
 Infrared  
 Narrowband  
 Spread Spectrum  


>#### Infrared  
 IR light cannot be seen by the human eye.  
 Used for single room uses because it cannot penetrate walls, ceilings or floors  

>#### Narrow Band  
 Narrow band technology uses microwave radio waves to transmit data  
 The most common uses are cordless phones and garage door openers  


AN OVERVIEW  
OF WIRELESS  
TECHNOLOGIES  
>#### Spread Spectrum  

- To move over radio waves, data must modulate on the carrier  
signal or channel  
 
>#### Modulation:
  It is the process of varying one or more properties of  
a periodic waveform, with a separate signal called the  
modulation signal that typically contains information to be  
transmitted  
 Modulation defines how the data is placed on the signal  
 For example, spread spectrum modulation means data is  
spread across a large-frequency bandwidth instead of  
travelling across just one frequency band  
 So, a group of frequencies is selected, and the data is spread  
across this group  
 **Spread Spectrum is the most used WLAN technology**!



AN OVERVIEW OF WIRELESS TECHNOLOGIES  
 Spread Spectrum uses the following methods;  
 Frequency-Hopping Spread Spectrum (FHSS) where data hops to other frequencies to avoid  
interference that can occur over a frequency band. Hopping from on frequency to another happens  
at split second intervals, thus making it difficult for a threat actor to jam the signal  
 Direct Sequence Spread Spectrum (DSSS) spreads data packets simultaneously over multiple  
frequencies. Sub-bits are added to a packet as it travels across the frequency band and are used for  
recovery. Sub-bits are called “chips” and every bit of the original is represented by multiple bits  
called the chipping code  
 Orthogonal Frequency Division Multiplexing (OFDM) has the bandwidth divided into a series of  
frequencies called tones, which allow for a higher throughput than FHSS or DSSS  
 Orthogonal Frequency Division Multiplexing Access (OFDMA) is the multiuser extension of the  
single-user OFDM. ODFMA has a throughput 3X high then OFDM for short packets of data or  
multiple endpoints. OFDMA combines transmissions and sends frames to multiple endpoints  
simultaneously and is more efficient with lower latency transmission. This makes it ideal for IoT,  
Video, Online Gaming and Automation.17


------------


## Free Scanning Tool


### inSSIDer


This is  free application, where it contains a **Frequency Spectrum Analysis** portion of the UI. We we would see is a section for the *2.4GHZ* channels, where the selected WIFI network would have its 2.4GHZ channels it is using, and on the vertical side of the graphs for 5GHZ and 2.4GHZ show the strength of the frequency ( it ranges from -90 going up to -30 , where -30 is the highest, lower numbers are better). 

If we are trying to interrupt a wireless network, we would generate *noise*. If we had the ability to put a radio in the environment, makes the signal stronger, and broadcasting it on the same channel of the WIFI network we are targeting. 


Signal to Noise Ratio : Signal  - the Noise ( preferably + or - 36db)

In class, we noticed that there is noise on the Edurom. the number is fluctuating rapidly (when it should be stable). We saw noise. The Access Point could boost the  signal of the network to counteract the noise, but this is bad. We should instead decrease the strength of the signal, choose another channel, and find out what is causing this noise. 


We are seeing 4 antennas for the access point : two antennas broadcasting on 2.4GHZ ( 1 and 6) , and 149 and 153 in 5GHZ.

There could be a nearby Wireless Access Point broadcasting on a 80-wide channel (5ghz)

He has done a ping request to google. If the ping time is dancing from high to low, this is called **Jitter**. 



#### Increasing/Decreasing Signal Strength / Switching to Another Channel


If we are in an environment with a lot of interference, you should do **Channel Mapping**. Unifi devices can increase/decrease the signal strength, or broadcast on a different channel. 

If a wireless network is experiencing noise on the 5GHz or 2.4GHz bands, decreasing the strength of the signal can have several effects:

1. **Reduced Coverage Area**: The most immediate impact is a reduction in the coverage area of the wireless network. Devices that were previously within range may no longer be able to connect.
    
2. [**Improved Signal-to-Noise Ratio (SNR)**: In some cases, reducing the signal strength can improve the Signal-to-Noise Ratio (SNR) because the network might avoid picking up as much interference from distant sources](https://documentation.meraki.com/MR/Wi-Fi_Basics_and_Best_Practices/Signal-to-Noise_Ratio_%28SNR%29_and_Wireless_Signal_Strength)[1](https://documentation.meraki.com/MR/Wi-Fi_Basics_and_Best_Practices/Signal-to-Noise_Ratio_%28SNR%29_and_Wireless_Signal_Strength). However, this is highly situational and depends on the specific environment and sources of noise.
    
3. [**Potentially Lower Throughput**: With a weaker signal, the data rate may decrease, leading to lower throughput and potentially slower network performance](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/wireless/ap_wireless_signalstrength_c.html)[2](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/wireless/ap_wireless_signalstrength_c.html).
    
4. [**Increased Retransmissions**: A weaker signal can lead to more data corruption, requiring more retransmissions between the transmitter and receiver, which can degrade overall network performance](https://www.velocenetwork.com/tech/what-is-wifi-noise/)[3](https://www.velocenetwork.com/tech/what-is-wifi-noise/).
    

In general, while reducing signal strength might help in very specific scenarios, it is often more effective to address the sources of noise directly or to change the channel or frequency band to one with less interference.

###### Enterprise-Grade Solutions to this Problem

### Software controller

Allows the access point to *only pick non-overlapping channels*. You can set it to do so automatically on a schedule. 


Guidance : Establish a baseline, and then deal with issues as they arise. 


Why wouldn't we want to increase the signal strength ? 

If the access point is a circle, and devices are within the circle, they can access the network. Devices outside of the range of the network would not be able to join it. If there is interference, and the signal is increased, that would mean that others may be able to try joining the network now, and thus affecting the security of the network. 


If we turn the power down, everyone inside the room will have excellent reliable connections to the access point, and we may need more access points. 

Wireless devices cannot speak and listen at the same time. 

attenuation would affect the signal reaching a wide area .


If we had an access point transmitting on 14db on the 149 channel, and there is a house within the range of the wireless network (imagine a large circle, and the house within it), houses trasmit usually on the 80 mhz channel at a known signal strength. To combat this, we could subtract the signal strength of our access point from the signal strength of the offending party, and then this way, the house could not listen in to our network. We may need another access point if there is a client who is not able to connect to our network. 



Channels UNI-1 , UNI-2a UNII-2c (Extended)


In Halifax, there is a lot of radar traffic from ships since this is a harbor city. 5 GHZ channels like to use the UNIII-2c channels, and the radar signal often interferes with the 5GHZ WIFI networks. 
The effect on radars is minimal, but to be on the safe side, we would be advised to use different channels. 

The 5GHZ WIFI channels could affect naval navigation, so there are certain precautions that we would have to prevent this, which limits our choice in channels. 


WIFI 6E


We are at this point from 2020 onwards. It goes from 5925 MGHZ to 7125MHZ. We would not have much interference except for other access points. The channels go beyond 59, 29 , 14 , 7 and 20, 40 , 80 , 160 mghz, we have UNII5 , UNII6 , UNII7, UNII 8 .... ( This is called **6GHZ Channel Allocations**). The total new range is 1200MHZ ( from 5925 to 7125).



