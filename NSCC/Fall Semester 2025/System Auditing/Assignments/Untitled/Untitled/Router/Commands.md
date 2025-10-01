


## Removing NetFlow Configuration via CLI

**Step 1: Access the Router CLI**

1. Click on the 4321 router
2. Go to the **CLI tab**

**Step 2: Enter Configuration Mode**

```
Router> enable
Router# configure terminal
```

**Step 3: Remove NetFlow from Interfaces**

First, you need to remove NetFlow from any interfaces where it's applied:

```
Router(config)# interface GigabitEthernet0/0/0
Router(config-if)# no ip flow monitor [monitor-name] input
Router(config-if)# no ip flow monitor [monitor-name] output
Router(config-if)# exit
```

Repeat for each interface (like GigabitEthernet0/0/1, etc.)

**Step 4: Remove Flow Exporters**

```
Router(config)# no flow exporter [exporter-name]
```

**Step 5: Remove Flow Monitors**

```
Router(config)# no flow monitor [monitor-name]
```

**Step 6: Remove Flow Records (if any)**

```
Router(config)# no flow record [record-name]
```

**Step 7: Exit and Save**

```
Router(config)# exit
Router# write memory
```

## To Find Existing NetFlow Configuration Names:

If you don't remember the names, use these commands to view them:

```
Router# show flow monitor
Router# show flow exporter
Router# show flow record
Router# show run | include flow
```



--------------------------


## Sub-Interface Creation



Router> enable

Router# configure terminal

Router(config)# interface GigabitEthernet 0/0/1.10

Router(config-subif)# encapsulation dot1Q 10

Router(config-subif)# ip address 192.168.10.1 255.255.255.0

Router(config-subif)# exit

Router(config)# interface GigabitEthernet 0/0/1.20

Router(config-subif)# encapsulation dot1Q 20

Router(config-subif)# ip address 192.168.20.1 255.255.255.0

Router(config-subif)# exit

Router(config)# end