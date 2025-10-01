



# ISEC 2077 Assignment 2 Part 2 - Netflow Collector Todo List

## STEP 1: Packet Tracer Model (Individual - Must verify with instructor BEFORE physical implementation)

### VLAN Configuration

- [x] Create VLAN 10 on Switch-PT (for PC0 and first network segment) ✅ 2025-10-01
- [x] Create VLAN 20 on Switch-PT (for PC1 and second network segment) ✅ 2025-10-01
- [x] Name VLANs appropriately (e.g., VLAN10-NET1, VLAN20-NET2) ✅ 2025-10-01

### Switch Port Configuration

- [x] Configure FastEthernet0/1 (router connection) as **trunk port** ✅ 2025-10-01
    - [x] Change from `switchport mode access` to `switchport mode trunk` ✅ 2025-10-01
    - [x] Allow VLANs 10 and 20 on trunk ✅ 2025-10-01
- [x] Assign FastEthernet1/1 (PC0) to VLAN 10 ✅ 2025-10-01
    - [x] `switchport access vlan 10` ✅ 2025-10-01
- [x] Assign FastEthernet2/1 (PC1) to VLAN 20 ✅ 2025-10-01
    - [x] `switchport access vlan 20` ✅ 2025-10-01

### Router Sub-Interface Configuration

- [ ]  Create sub-interface for VLAN 10 (e.g., GigabitEthernet0/0.10)
    - [ ]  Configure 802.1Q encapsulation: `encapsulation dot1Q 10`
    - [ ]  Assign IP address (e.g., 192.168.10.1/24) - this will be default gateway for PC0
    - [ ]  Enable interface: `no shutdown`
- [ ]  Create sub-interface for VLAN 20 (e.g., GigabitEthernet0/0.20)
    - [ ]  Configure 802.1Q encapsulation: `encapsulation dot1Q 20`
    - [ ]  Assign IP address (e.g., 192.168.20.1/24) - this will be default gateway for PC1
    - [ ]  Enable interface: `no shutdown`
- [ ]  Enable main physical interface: `no shutdown` on GigabitEthernet0/0

### IP Address Updates

- [ ]  Change PC0 IP from 192.168.1.2 to 192.168.10.2
    - [ ]  Set subnet mask to 255.255.255.0
    - [ ]  Set default gateway to 192.168.10.1 (router sub-interface)
- [ ]  Change PC1 IP from 192.168.1.3 to 192.168.20.2
    - [ ]  Set subnet mask to 255.255.255.0
    - [ ]  Set default gateway to 192.168.20.1 (router sub-interface)

### Netflow Monitor Cleanup & Configuration

- [ ]  Remove FlowMonitor-1 (the extra monitor)
- [ ]  Create **NEW** Flow Monitor for VLAN 10 sub-interface (IN traffic)
    - [ ]  Configure for Netflow version 5
    - [ ]  Name appropriately (e.g., VLAN10-IN)
- [ ]  Create **NEW** Flow Monitor for VLAN 10 sub-interface (OUT traffic)
    - [ ]  Configure for Netflow version 5
    - [ ]  Name appropriately (e.g., VLAN10-OUT)
- [ ]  Create **NEW** Flow Monitor for VLAN 20 sub-interface (IN traffic)
    - [ ]  Configure for Netflow version 5
    - [ ]  Name appropriately (e.g., VLAN20-IN)
- [ ]  Create **NEW** Flow Monitor for VLAN 20 sub-interface (OUT traffic)
    - [ ]  Configure for Netflow version 5
    - [ ]  Name appropriately (e.g., VLAN20-OUT)

### Flow Exporter Configuration

- [ ]  Create Flow Exporter for VLAN 10 collector
    - [ ]  Set destination IP to 192.168.10.2 (PC0's VM will run collector)
    - [ ]  Set export protocol to Netflow version 5
    - [ ]  Configure UDP port (typically 2055 or 9996)
- [ ]  Create Flow Exporter for VLAN 20 collector
    - [ ]  Set destination IP to 192.168.20.2 (PC1's VM will run collector)
    - [ ]  Set export protocol to Netflow version 5
    - [ ]  Configure UDP port (typically 2055 or 9996)
- [ ]  Apply exporters to corresponding monitors

### Packet Tracer Testing & Verification

- [ ]  Test ping from PC0 to PC1 (should work via inter-VLAN routing)
- [ ]  Test ping from PC1 to PC0
- [ ]  Verify VLAN assignments: `show vlan brief` on switch
- [ ]  Verify trunk configuration: `show interfaces trunk` on switch
- [ ]  Verify router sub-interfaces are up: `show ip interface brief`
- [ ]  Verify Netflow configuration: `show flow monitor`
- [ ]  **Get instructor verification that Packet Tracer model is working** ✓

---

## STEP 2: Physical Implementation (Can work with partner)

### Physical Cabling

- [ ]  Cable Computer 1 to switch port (for VLAN 10)
- [ ]  Cable Computer 2 to switch port (for VLAN 20)
- [ ]  Cable switch to router with trunk connection
- [ ]  Verify all physical connections

### Configure Physical Router

- [ ]  Apply VLAN 10 sub-interface configuration from Packet Tracer model
- [ ]  Apply VLAN 20 sub-interface configuration from Packet Tracer model
- [ ]  Configure NEW Netflow monitors for both sub-interfaces (IN and OUT)
    - [ ]  Ensure Netflow version 5
- [ ]  Configure NEW Flow exporters pointing to:
    - [ ]  VM on Computer 1 (192.168.10.x)
    - [ ]  VM on Computer 2 (192.168.20.x)
- [ ]  Apply monitors to sub-interfaces (both input and output)

### Configure Physical Switch

- [ ]  Create VLANs 10 and 20
- [ ]  Configure trunk port to router
- [ ]  Assign computer ports to appropriate VLANs

### Configure Computers & Bridged VMs

- [ ]  Computer 1: Set IP addressing for VLAN 10 network
- [ ]  Computer 2: Set IP addressing for VLAN 20 network
- [ ]  Bridged VM 1: Configure static IP in 192.168.10.x range
- [ ]  Bridged VM 2: Configure static IP in 192.168.20.x range
- [ ]  Install ManageEngine Netflow Analyzer on both VMs
    - [ ]  Download from [https://www.manageengine.com/products/netflow/](https://www.manageengine.com/products/netflow/)
    - [ ]  Configure to listen for Netflow v5 on correct UDP port

### Physical Network Testing

- [ ]  Test connectivity between VLANs
- [ ]  Verify routing between networks
- [ ]  Confirm VMs can communicate on network

---

## STEP 3: Netflow Collection & Traffic Generation

### Start Collectors

- [ ]  Start Netflow Analyzer on VM 1 (VLAN 10)
- [ ]  Start Netflow Analyzer on VM 2 (VLAN 20)
- [ ]  Verify both are listening for Netflow exports

### Generate Traffic

- [ ]  Send traffic from VLAN 10 to VLAN 20
    - [ ]  Ping, HTTP, FTP, etc.
- [ ]  Send traffic from VLAN 20 to VLAN 10
- [ ]  Generate varied traffic types for better demonstration

### Verify Flow Collection

- [ ]  Check Netflow Analyzer on VM 1 shows captured flows
- [ ]  Check Netflow Analyzer on VM 2 shows captured flows
- [ ]  Verify flow details (source, destination, protocol, ports)
- [ ]  Take screenshots of captured flows

---

## STEP 4: Final Demonstration Preparation

### Documentation

- [ ]  Document network topology diagram
- [ ]  Document IP addressing scheme for both VLANs
- [ ]  Document router configuration commands
- [ ]  Document switch configuration commands
- [ ]  Prepare screenshots of:
    - [ ]  Router configuration (`show run`)
    - [ ]  Switch VLAN configuration
    - [ ]  Netflow monitor status
    - [ ]  Captured flows in both Netflow Analyzers

### Demonstration Checklist

- [ ]  Show physical network setup to instructor
- [ ]  Demonstrate inter-VLAN communication
- [ ]  Show router Netflow configuration
- [ ]  Display captured flows in both Netflow Analyzers
- [ ]  Explain configuration choices
- [ ]  Be prepared for comprehension questions

### Before Demo

- [ ]  Verify all equipment is working
- [ ]  Ensure both VMs are running Netflow Analyzer
- [ ]  Have recent traffic captured and visible
- [ ]  Save all configurations

---

## Notes & Reminders

**Critical Points:**

- Step 1 (Packet Tracer) is INDIVIDUAL and must be verified by instructor before proceeding
- Must use **separate 192.168.x.0/24 networks** for each VLAN
- Must create **NEW** monitors (not reuse existing IN/OUT monitors)
- Must use **Netflow version 5** for all monitors
- Each sub-interface needs both IN and OUT monitors
- Each VM runs its own Netflow Analyzer collector
- Physical implementation can be done with partner, but comprehension test is individual

**Common Issues to Avoid:**

- Not converting router port to trunk on switch
- Forgetting to enable physical interface before sub-interfaces
- Wrong encapsulation VLAN numbers
- Incorrect default gateway on PCs
- Netflow exporters pointing to wrong IPs
- Not starting Netflow Analyzer before generating traffic