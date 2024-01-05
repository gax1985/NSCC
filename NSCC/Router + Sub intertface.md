


Router ---> .20 Sales VLANs  (including PC1 and PC3)
        --------> .30 ADMIN VLAN (including PC2 and PC4)


We place an ACL on .20, and this is where we **DENY** PC2, so it wont enter Sales VLAN


We are denying PC2 out of the router. If we ping PC2 from PC1, it reaches there, and PC2 tries to reply, and the reply is blocked. PC1 sent a ping, response never came back, and we get "Request Timeout"


If we ping from PC2 to PC1 and PC3 , we would get "Destination Host Unreachable" 

The "Destination Unreachable" tells us "Something is blocking me" due to a "Firewall" or an "ACL" on the rourter. We are intentionally blocking access . A hacker on 30 VLAN would know. 


If there is no machine there, with nothing blocking "Request time out".  






If we are to put the ACL on the 0.30 sub-interface , we would like to place it closest to the source. It is not a standard ACL, it is an Extended ACL. It would not be blocking traffic going out from the router, but traffic getting in. You would be blocking PC2 from getting in. PC2 cant get to the 0.99 sub-interface. What if we have another VLAN that we want PC2 to access in the future? 


If you are blocking PC2 from getting into the Sales VLAN, you can place the ACL to the closest area. 


We are not scanning nmap from the command line, we need to verify the IP addresses by at least two people. We need to confirm the IP addresses are correct. 
