 NixOS 2024!


## Switch #1 

>[!commands]
>
>>[!VLAN creation]
>>enable
>>configure terminal
>>vlan 9
>>name VLAN9
>>vlan 10
>
>>[!Switch Port Assignment]
>>**Bryce** 
>>interface fastEthernet 0/2
>>switchport mode access
>>switchport access vlan 9
>>
>>**Mohammad**
>>interface fastEthernet0/3
>>switchport mode access
>>switchport access vlan 9
>

>[!trunking]
>
>>[!switch 9]
>>>```
>>>switchport trunk encapsulation dot1q
>>>switchport mode trunk 
>>>copy run start


>[!trunking]
>
>>[!switch 10]
>>>
>>>
>>>

## Switch #2 





>[!commands]
>
>>[!VLAN creation]
>>enable
>>configure terminal
>>vlan 9
>>name VLAN9
>>vlan 10
>>name VLAN10
>
>>[!Switch Port Assignment]
>
>>**Cassandra** 
>>interface fastEthernet 0/2
>>switchport mode access
>>switchport access vlan 10
>
>
>>**Rhys**
>>interface fastEthernet0/3
>>switchport mode access
>>switchport access vlan 10
>


