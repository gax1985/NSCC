



When assigning an IP address, the Gateway would look into the ARP table and check if it exists. If it does not, then it sends a packet to the MAC address associated with the PC's NIC. 


Setting 30 in the third octet (192.168.30.100), does it make it go on that VLAN? NO! It is simply a reminder for later, when we will set up a VLAN called 30. 


Switch configuration : 


		enable
		configure terminal
		vlan 20
		name division1
		vlan 30
		name division2
		exit
		exit
		show vlan


Now, let us configure the interfaces to assign them to the VLANs :

SWITCH1

		configure terminal
		interface fastEthernet 0/3
		(Next, we have to configure to the access modew)
		switchport mode access
		switchport access vlan 20
		
		
		interface fastEthernet 0/4
		(Next, we have to configure to the access modew)
		switchport mode access
		switchport access vlan 30
		
		
		show run (to see the configuration)
		
		(We have made changes to the configuration of the switch. The configurations are currently on the RAM. When the switch turns off, they go away. We need to copy everything from the RUN configurations to the STARTUP configurations)
		
		
		copy run start             (Only configuration file that will remain is the STARTUP, but we can have many Configuration files if we wish)
		
		

SWITCH 2


		enable
		configure terminal
		vlan 20
		name division1
		vlan 30
		name division2
		exit
		exit
		show vlan
		(end - goes back to the beginning)
		
		(if one misspells it)
		
		vlan 30
		no name (cancells the name)
		
		
		(Vlans are ready)



SWITCH 1 ( to trunk)



		enable
		configure terminal
		interface fastethernet 0/1
		switchport mode trunk
		switchport trunk allowed vlan 1-30 