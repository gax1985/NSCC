# VPNs

## Definition of VPN

A **VPN** (Virtual Private Network) is a technology that establishes a secure and encrypted connection over the Internet, allowing users to access a private network from a remote location.

## Networking Overview

Consider a typical network setup:

rustCopy code

`Host ----> Switch ---> Default Gateway ---> Internet Connection               Private Address             Public Address       192.168.1.0/24                          (24.222.1.0/26)`

- **Public IP Address (Tunnel):** Refers to the public-facing access point that connects to the internet.

### Firewall Concepts

- **Stateful Firewalls:** Remember traffic in and out, allowing only solicited traffic by default.
- **Firewall Rules:** Specify allowed addresses/ports to a destination.

## VPNs and Security

### HTTPS and RDP Access

- Without a VPN, port forwarding was commonly used for HTTPS (443) or RDP (3389), posing security risks.
- Port scanning could reveal open ports, and default credentials were vulnerable.

### VPN for Remote Access

- **VPN Types:**
    - **Site-to-Site:** Connects two networks securely.
    - **Client VPN:** Allows individual devices to connect securely.

### Site-to-Site VPN

- Most secure VPN type.
- Requires two pieces of hardware: Router-to-Router or Server-to-Server.
- LAN-to-LAN connectivity.
- Utilizes IpSEC for an encrypted tunnel between routers/servers.
- Static IP addresses for the two tunnel endpoints.
- Traffic between sites bypasses firewall rules securely.

#### IP Addresses:

- Use private IP address ranges: 172.10.0.0, 192.168.0.0, 10.1.0.0.
- Lab PCs may have IP addresses like 172.16.x.x (private range).

#### Encapsulation and Speed Considerations

- Traffic encrypted in the tunnel.
- Encapsulation may slow down speed, necessitating hardware considerations.
- Throughput on the VPN connection should be checked.

#### Split-Tunneling

- Allows selective routing through the VPN.
- Useful to avoid resource expenditure and maintain speed.

### Client VPN

- **VPN Protocols:**
    
    - **OpenVPN:** Easy to deploy and manage, secure.
    - **Wireguard:** Built into Unifi.
- **Client VPN Setup:**
    
    - Software application or built-in OS functionality.
    - Configuration files or links provided by network admin.
- **Single Sign-On (SSO):**
    
    - Preferable for user convenience.
    - Use Windows AD credentials for VPN authentication.
- **VPN Traffic Flow:**
    
    - All traffic routed through VPN for security (avoid split tunneling).
    - Authenticated traffic encrypted via IPSEC tunnel.

## Peer-to-Site VPN

- Similar to Site-to-Site but involves connecting individual devices to a central network securely.
- Requires two pieces of hardware.

----------------------------------------




