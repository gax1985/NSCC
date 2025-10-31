

# Part 1 : Router Configuration


## Creation  of a Sub-Interface


### Commands used :

`en`
`conf t`
`int gigabitEthernet 0/0/0.1`
`encapsulation dot1Q 1`
`ip address 192.168.99.1 255.255.255.0`
`no shut`
`exit`





-----------------
# Part 2 : Switch Configuration


## Creation  of VLANs

### Commands used :


- enable
- config terminal
- vlan 1
- name VLAN
- int fa 0/1`
- switchport mode access
- switchport access vlan 1
- exit
- exit
- show vlan







-----------

# Part 3 : Netflow Monitor Creation









---------

# Part 4 : Netflow Exporter Creation








-----------

# Part 5 : Netflow Collector Creation









---------










