
# CarrierPigeon 

  

  
Confidentiality is the concern. 


Non-E2EE Messaging --> stored Plain Text

  

Message scanning for illegal activity 

  

Tagging daata-as deleted --> Soft Deleting --> It is kept on the server 

  

  

Privacy is in threat!

  

  

  

How to solve this problem ? 

  

  

## Decentralized Communication 

  

  

He uses ESP32 , low cost microcontroller , has WIFI, Bluetooth and Firmware can be written in many languages. 

## LoRa Protocol

Radio protocol using Spread Spectrum modulation

Long Range

It is the physical layer of LoRaWAN , a low power wide area network.

You can extend with antennas !



## Steps 


1. Initialize the server, start the file system, and open access point. 
2. There are defined configurations in LoRa, such as spread vector (signals are not the same, longer message times but more accurate messages. If you want speed, you lose integrity. )
   
   >[!Configuration]
   >
   >>`LORA_SPREADING_FACTOR = 7`

1. It allows one device at a time. It is using a web socket event handler. 
2. Crypto is done on relay
---

# CoPilot Explanation 


# 📖 CarrierPigeon: Privacy Through Hardware

### 🔒 The Problem: Messages Aren’t Safe

- **Plain Text Storage**: Many messaging apps keep your words unencrypted on servers.
    
- **Scanning**: Companies or governments may scan these messages for “illegal activity.”
    
- **Soft Delete**: Even if you delete a message, it often remains stored in the system.
    
- **Result**: Your privacy is at risk — your conversations aren’t truly confidential.
    

### 🕊 The Idea: Decentralized Communication

Instead of relying on big servers, **CarrierPigeon** uses small devices to send messages directly.

- No central authority.
    
- No permanent storage.
    
- Messages travel like whispers between radios.
    

## ⚙️ The Hardware: ESP32

- **What it is**: A tiny, low-cost microcontroller (like a mini computer).
    
- **Features**:
    
    - Built-in **Wi-Fi** and **Bluetooth**.
        
    - Can run code written in many languages (C, Python, MicroPython, Arduino).
        
- **Why it matters**: Cheap, flexible, and perfect for DIY communication projects.
    

Think of it as the **brain** of CarrierPigeon — small but powerful.

## 📡 The Protocol: LoRa

- **LoRa = Long Range Radio**
    
- Uses **Spread Spectrum Modulation** (signals spread across frequencies, harder to intercept).
    
- **Range**: Can reach kilometers with very little power.
    
- **Layer**: It’s the physical foundation of **LoRaWAN**, a network for low-power devices.
    
- **Boosting**: Add antennas to extend reach even further.
    

Imagine LoRa as the **wings** of CarrierPigeon — carrying messages far and wide.

### 🛡 Why This Protects Privacy

- **No central server**: Messages don’t sit in a company’s database.
    
- **Peer-to-peer**: Devices talk directly to each other.
    
- **Harder to scan**: Spread spectrum makes interception more difficult.
    
- **True deletion**: If you don’t store it, there’s nothing to “soft delete.”
    

## 📚 DK-Style Summary

- **Problem**: Centralized messaging = privacy leaks.
    
- **Solution**: Decentralized hardware + radio.
    
- **ESP32**: The brain.
    
- **LoRa**: The wings.
    
- **CarrierPigeon**: A system where your words fly free, without being trapped on servers.


---

Creator's Github : 


https://github.com/LeoL6

https://github.com/LeoL6/carrier-pigeon

Look at Meshtastic 

---

**CarrierPigeon is a DIY encrypted messenger using ESP32 and LoRa radios, while Meshtastic is a more advanced, community-driven mesh network protocol built on similar hardware. Both aim to protect privacy and enable off-grid communication.**

Let’s break this down DK-style — bold headings, visual metaphors, and simple explanations that build layer by layer.

---

# 🕊 CarrierPigeon: Your Private Radio Messenger

### 🔐 The Problem

- **Messaging apps store your words** on servers.
- **They scan messages** for “illegal” content.
- **Deleted messages aren’t really gone** — they’re just tagged.

🛑 _Privacy is under threat._

---

### 🛠 The Solution: Build Your Own Messenger

CarrierPigeon uses:

- **ESP32**: A tiny computer with Wi-Fi and Bluetooth.
- **LoRa radio**: Sends encrypted messages over long distances.
- **Browser UI**: You connect to the device and chat securely.

---

## 🧠 ESP32: The Brain

- Runs the firmware.
- Hosts a Wi-Fi hotspot.
- Serves a webpage for chatting.
- Talks to the LoRa radio.

🧩 _Think of it as the control center._

---

## 📡 LoRa: The Wings

- Sends messages wirelessly.
- Works over kilometers.
- Uses very little power.
- Doesn’t need cell towers or Wi-Fi.

🕊 _Your message flies like a pigeon — quietly and far._

---

## 🔐 Encryption: The Armor

- Uses **NaCl secretbox** (XSalsa20 + Poly1305).
- Adds **HMAC** for message authentication.
- Performs **Diffie–Hellman key exchange** in the browser.
- Encrypts every message with a fresh **nonce**.

🧪 _Only the intended recipient can read your message._

---

## 🔄 Message Flow

1. **Connect to ESP32 Wi-Fi**
2. **Open the chat page**
3. **Exchange keys securely**
4. **Encrypt your message**
5. **Send via LoRa**
6. **Receiver decrypts and reads**

📬 _No servers. No snooping. Just radio and math._

---

# 🌐 Meshtastic: The Mesh Network for Everyone

### 🧭 What Is It?

Meshtastic is an **open-source mesh communication system** using LoRa radios. It’s like CarrierPigeon, but:

- **Multi-hop**: Messages bounce across devices.
- **Mesh routing**: Finds paths through the network.
- **AES-256 encryption**: Strong security.
- **Apps for Android, iOS, and desktop**.

🌲 _Perfect for hiking, festivals, emergencies, or off-grid life._

---

## 🧱 Meshtastic Layers (DK-style)

|Layer|Role|Analogy|
|---|---|---|
|0: LoRa Radio|Sends raw signals|Carrier pigeon flying|
|1: Zero-Hop|Direct messages|Whisper to a friend|
|2: Reliable Hop|Adds retries|Echo until heard|
|3: Multi-Hop|Mesh routing|Message passed down a line|

🔁 _Messages can travel across many devices to reach their destination._

---

## 🧠 Smart Features

- **Managed flooding**: Broadcasts without chaos.
- **Next-hop routing**: Direct messages with path control.
- **GPS tracking**: Share your location.
- **Telemetry**: Battery, signal, uptime.

📱 _You can chat, track, and monitor — all off-grid._

---

## 🆚 CarrierPigeon vs Meshtastic

|Feature|CarrierPigeon|Meshtastic|
|---|---|---|
|Encryption|NaCl + HMAC|AES-256|
|Routing|Point-to-point|Mesh multi-hop|
|UI|Browser-based|Mobile + desktop apps|
|Setup|DIY firmware|Community ecosystem|
|Use Case|Private chat|Group communication|

🧪 _CarrierPigeon is a lab experiment. Meshtastic is a full ecosystem._

---

Would you like a DK-style visual comparing CarrierPigeon and Meshtastic side-by-side? I can generate that next!
