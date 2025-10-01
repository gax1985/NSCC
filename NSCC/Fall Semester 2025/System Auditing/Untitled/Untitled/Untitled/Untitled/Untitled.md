


Switch#conf t

Enter configuration commands, one per line. End with CNTL/Z.

Switch(config)#vlan ?

<1-4094> ISL VLAN IDs 1-1005

Switch(config)#vlan 20

Switch(config-vlan)#?

VLAN configuration commands:

exit Apply changes, bump revision number, and exit mode

name Ascii name of the VLAN

no Negate a command or set its defaults

remote-span Add the Remote Switched Port Analyzer (RSPAN) feature to the VLAN

Switch(config-vlan)#name VLAN-20

Switch(config-vlan)#exit

Switch(config)#exit

Switch#

%SYS-5-CONFIG_I: Configured from console by console

  

Switch#conf t

Enter configuration commands, one per line. End with CNTL/Z.

Switch(config)#int

Switch(config)#interface fas

Switch(config)#interface fastEthernet 0/1

Switch(config)#interface fastEthernet 0/1

Switch(config-if)#?

cdp Global CDP configuration subcommands

channel-group Etherchannel/port bundling configuration

channel-protocol Select the channel protocol (LACP, PAgP)

description Interface specific description

duplex Configure duplex operation.

exit Exit from interface configuration mode

ip Interface Internet Protocol config commands

lldp LLDP interface subcommands

mls mls interface commands

no Negate a command or set its defaults

shutdown Shutdown the selected interface

spanning-tree Spanning Tree Subsystem

speed Configure speed operation.

storm-control storm configuration

switchport Set switching mode characteristics

tx-ring-limit Configure PA level transmit ring limit

Switch(config-if)#switch

Switch(config-if)#switchport ?

access Set access mode characteristics of the interface

mode Set trunking mode of the interface

nonegotiate Device will not engage in negotiation protocol on this

interface

port-security Security related command

priority Set appliance 802.1p priority

protected Configure an interface to be a protected port

trunk Set trunking characteristics of the interface

voice Voice appliance attributes

Switch(config-if)#switchport mode trunk

  

Switch(config-if)#

%LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/1, changed state to down

  

%LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/1, changed state to up

  

Switch(config-if)#?

cdp Global CDP configuration subcommands

channel-group Etherchannel/port bundling configuration

channel-protocol Select the channel protocol (LACP, PAgP)

description Interface specific description

duplex Configure duplex operation.

exit Exit from interface configuration mode

ip Interface Internet Protocol config commands

lldp LLDP interface subcommands

mls mls interface commands

no Negate a command or set its defaults

shutdown Shutdown the selected interface

spanning-tree Spanning Tree Subsystem

speed Configure speed operation.

storm-control storm configuration

switchport Set switching mode characteristics

tx-ring-limit Configure PA level transmit ring limit

Switch(config-if)#switchport

Switch(config-if)#switchport ?

access Set access mode characteristics of the interface

mode Set trunking mode of the interface

nonegotiate Device will not engage in negotiation protocol on this

interface

port-security Security related command

priority Set appliance 802.1p priority

protected Configure an interface to be a protected port

trunk Set trunking characteristics of the interface

voice Voice appliance attributes

Switch(config-if)#switchport trunk ?

allowed Set allowed VLAN characteristics when interface is in trunking mode

native Set trunking native characteristics when interface is in trunking

mode

Switch(config-if)#switchport trunk allowed

Switch(config-if)#switchport trunk allowed vlan ?

WORD VLAN IDs of the allowed VLANs when this port is in trunking mode

add add VLANs to the current list

all all VLANs

except all VLANs except the following

none no VLANs

remove remove VLANs from the current list

Switch(config-if)#switchport trunk allowed vlan add ?

<1-4094> VLAN ID of a allowed VLAN when this port is in trunking mode

Switch(config-if)#switchport trunk allowed vlan add 10

Switch(config-if)#switchport trunk allowed vlan add 20

Switch(config-if)#exit

Switch(config)#int

Switch(config)#interface Fa

Switch(config)#interface FastEthernet 1

Switch(config)#interface FastEthernet ?

<0-9> FastEthernet interface number

Switch(config)#interface FastEthernet 1/1

Switch(config-if)#?

cdp Global CDP configuration subcommands

channel-group Etherchannel/port bundling configuration

channel-protocol Select the channel protocol (LACP, PAgP)

description Interface specific description

duplex Configure duplex operation.

exit Exit from interface configuration mode

ip Interface Internet Protocol config commands

lldp LLDP interface subcommands

mls mls interface commands

no Negate a command or set its defaults

shutdown Shutdown the selected interface

spanning-tree Spanning Tree Subsystem

speed Configure speed operation.

storm-control storm configuration

switchport Set switching mode characteristics

tx-ring-limit Configure PA level transmit ring limit

Switch(config-if)#switchport mode access

Switch(config-if)#switchport access vlan 10

Switch(config-if)#switch

Switch(config-if)#switchport ?

access Set access mode characteristics of the interface

mode Set trunking mode of the interface

nonegotiate Device will not engage in negotiation protocol on this

interface

port-security Security related command

priority Set appliance 802.1p priority

protected Configure an interface to be a protected port

trunk Set trunking characteristics of the interface

voice Voice appliance attributes

Switch(config-if)#switchport access ?

vlan Set VLAN when interface is in access mode

Switch(config-if)#switchport access vlan 10 ?

<cr>

Switch(config-if)#exit

Switch(config)#

Switch(config)#inter

Switch(config)#interface 2/

Switch(config)#interface 2/1

Switch(config)#interface 2/1

^

% Invalid input detected at '^' marker.

Switch(config)#

Switch(config)#in

Switch(config)#interface F

Switch(config)#interface FastEthernet 2/1

Switch(config-if)#switchport mode access

Switch(config-if)#switchport access vlan 20

Switch(config-if)#exit

Switch(config)#int

% Incomplete command.

Switch(config)#in

Switch(config)#interface Fa

Switch(config)#interface FastEthernet 0/1

Switch(config-if)#no shut

Switch(config-if)#exit

Switch(config)#int

Switch(config)#interface 1

Switch(config)#interface F

Switch(config)#interface FastEthernet 1/1

Switch(config-if)#no shut

Switch(config-if)#exit

Switch(config)#int

Switch(config)#interface F

Switch(config)#interface FastEthernet 2/1

Switch(config-if)#no shut

Switch(config-if)#exit

Switch(config)#copy run start

^

% Invalid input detected at '^' marker.

Switch(config)#exit

Switch#

%SYS-5-CONFIG_I: Configured from console by console

  

Switch#copy run start

Destination filename [startup-config]?

Building configuration...

[OK]

Switch#