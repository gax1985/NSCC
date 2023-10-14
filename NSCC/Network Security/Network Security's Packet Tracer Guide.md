


## Part One

1. Add 4 PCs and one Switch (2960)

2. Add notes next to all 4 PCs IP Address Subnet Mask Vlan # Vlan name FA 0/#

3. Add connector from PCs to Switch (black connector) TAKE NOTE OF WHICH ETHERNET PORT YOU'RE CONNECTING TO ON THE SWITCH. PC1 = FA 0/1, PC2 = FA/02, ETC.

4. Go to CLI on the switch and follow CONFIG VLAN 20 + 30 instructions

## Part Two - CLI Commands

**VLAN 20**

- enable
- config terminal
- vlan 20
- name Sales
- vlan 30
- name Admin
- int fa 0/1
- switchport mode access
- switchport access vlan 20
- exit
- exit
- show vlan

[confirm vlan 20 (Sales) has FA 0/1] [repeat for fa 0/3] **VLAN30**

- enable
- config terminal
- int fa 0/2
- switchport mode access
- switchport access vlan 30
- exit
- exit
- show vlan

[confirm vlan 30 (Admin) has FA 0/2] [repeat for fa 0/4]




End Result : 


![[Pasted image 20231011131525.png]]




Result from PINGing from PC2 to PC3 : 


![[Pasted image 20231011133229.png]]



V2: Trunk lines (switchport mode trunk) : 


![[Pasted image 20231011133309.png]]


1. ## SWITCH3: CLI

> enable
> conf t 
i> int fa 0/5 
> switchport mode trunk
> switchport trunk allowed vlan 1-30 
> exit  
> show interface trunk 
> conf t 
> vlan 20 
> name sales  
> vlan 30 
> name admin  
> exit   
> int fa 0/1  
> switchport mode access 
> switchport access vlan 20  
> exit  
> int fa 0/2 
> switchport mode access 
> switchport access vlan 30`
    
## SWITCH0: CLI


>en 
>conf t 
>int fa 0/5 
>switchport mode trunk 
>switchport trunk allowed vlan 1-30 
>exit   
>show interface trunk 
>conf t 
>vlan 20  
>name sales 
>vlan 30 
>name admin 
>exit  
>int fa 0/3 
>switchport mode access 
>switchport access vlan 20  
>exit  
>int fa 0/4 
>switchport mode access 
>switchport access vlan 30

## PC3: Command Prompt


>ping 192.168.20.100  
>ping 192.168.30.200   


## Examples
    
    `Image 1: Trunk Image 2: SWITCH0 Config Image 3: SWITCH3 Config`