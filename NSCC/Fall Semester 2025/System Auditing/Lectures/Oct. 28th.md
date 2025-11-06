

When looking at endpoints : 

1. We need *profiles* on our endpoints 
   
   We deploy to the machines based on the roles the machine will play. 
   When the machine's role is done, it gets re-imaged.
   We will find things that users have installed, like extensions.
   Server technicians will open and close ports all the time. 
   We capture network traffic with wireshark.
   We capture Windows events on the **Windows *Event Viewer****. 
   
   >[!example]
   >
   >Describe what might be possible types of behavior that you imagine an endpoint would have if *it has been compromised* ?
   >
   >>1. Failed Login Attempts 
   >>   
   >>   Think about **State Transitions**. You have a machine at rest , where no one logs in, Suddenly, you have a bunch of *failed logins*, then a **user logs in**.
   >>   
   >>   Reasonable Threshold : **5 Attempts**
   >>   Lockout time (after fails) : **30 minutes - 1 hour**
   >>   
   >>   >time is largely irrelevant. 
   >>   >What is important is the **Alert Status**! 
   >>   >
   >> Attackers try to do this on Friday, where they know like clockwork to get locked out, then via *social engineering*, 
   >>   
   >>   Avoid lockouts in a medium security environment. Instead, lockout permenantely until someone talks to them. 
   >>   
   >>   >it is human nature to do so, where users make errors.
   >>
   >> If they operate within the threshold, if they try 9 times out of 10, and on the 9th attempt went through, what other things might they do ? 
   >> 
   >> 
   >> # Attackers' Methods :
   >> Local Login Attempt (many ways to enable it)
   >> Booting from an External Device
   >> 
   >> Look at MITRE ATTACK Killchain  :
   >> 
   >> Persistence --> Scheduled Tasks 
   >> Enumeration 
   >> Logout
   >> 
   > 
   >> 
   >> >
   >> >Avoid putting Sensitive Information on laptops
   >> >Encrypt Everything
 >
 >**Check/Escalate Privileges** --> **Alert Status** --> Lockout for 30m-1hr --> until manually restored
 >
>># Lockout Methods :
>>
>>1. ActiveDirectory : Disable the account --> Disabled state at the *Account Level* --> **Cutoff Network Access**.
>>   
>>   
>   
>Machine at rest -- failed login -- user logs in -- Privilege Escalation -- alert status -- logout 
>(not normal behavior )
>
>## steal data
>Exfiltration Methods : 
>
>USB Drives --> There is an event for that 
>
>You can enforce a *policy* to stop someone from copying a flash drive. If someone manages to do that, then they defeated this policy. 
>
>What would the last thing the attacker might do before logout ? 
>Delete the log --> If they have done so, the last entry would be "Logs Deleted!" --> **catastrophic if the logs are *local* only!**
>
>There are two principles at Endpoints : 
>
>1. Never store the logs on the local endpoints
>2. There should *never* be a successful local login on a device that are designated as *Network-Only Logins* --> There should never be a local login entry in the events --> If this happens, then there should be a sequence of events that should be triggered. 
>3. Logs should *always* be **decentralized**! 

>[!time]
>
># Log Retention 
>
>We make a buffer that is **2048 bytes**
>
>Circular Buffer --> Supposed to be a *Circle* , where when it gets full, it goes back to the beginning and overwrites the first entry --> this is wrong!

>[!critical]
>>No not use a **Circular Buffer**! Write to a file instead ! Normally, when it reaches the last portion of the buffer, it writes the buffer to a file (Circular Buffer)

>>[!important]
>>
>>The short answer is :
>>
>>>`Keep the Logs Forever and Ever ...` --> *until **Someone in Authority** comes in and says to get rid of them*!
>>
>
>PCI-Compliance will have a required length of time to store logs for. 
>
>You can have a baseline for expected behavior.
>If behavior of networks has radically changed, such as a *growth in peer-to-peer systems*, this would change the network *fundamentally*!
>
>
>
>
>
 


>## Scripting : 
>
>Understand information available to describe each of these things --> Event Codes (failed login, login locally , login remotely , etc ... )

  
 
# Event Types : 

# Error


# Warning 

Information

Success Audit

Failed Audit


You have to Decide : 

1. Successes --> keep them if you are tracking that. 
2. Failures
3. Both

All Windows applications have the ability to write logs 


# Windows Logs 


## Application

Information on installed applications 

## Security 

We will work with it a lot 


## System (not much there)


## Setup 


## Forwarded Events 

Decentralized Logs 


## Applications and Services 





Event Properties Standard fields • Log name – name of the event log where the log is stored. • Source – service, component or application that created the event. • Event id – specific code for specific type of event (learn these) • Level –severity assigned to the event • User – the user account involved or the user context of the Source (check event specific info) • Opcode – assigned by the source. (investigate the source) • Logged – Date & Time • Task Category – assigned by the source. (investigate the source) • Keywords – assigned by the source • Computer – device that logged the event (remember remote access) • Description Event Specific info SEE eventlogedit from Shadow Brokers, https://www.securityweek.com/event-logs-manipulated-nsa-hacking- tool-recoverable 

>[!warning]
>
Companies should *never* use Home-Editions for business purposes !

Microsoft has some recommended policies for Security Auditing of Windows Events!


Audit Policy Audit policies dictate the creation of event records Access Through: 

gpedit -> computer configuration -> windows settings -> security settings -> advanced audit policy configuration (then expand tab in left menu) -> System Audit Policies Microsoft Audit policy 

recommendations: https://docs.microsoft.com/en-us/windows-server/identity/ad- ds/plan/security-best-practices/audit-policy-recommendations 


Powershell cmdlets :
• Get-eventlog • Get-winevent 


---
## Overview of Windows Event Logs

Windows uses the **Event Viewer** to record and organize system activities into logs. These logs are essential for administrators, developers, and security analysts to understand what’s happening under the hood.

## 📘 Application Log

- **Purpose:** Records events from installed applications and software.
    
- **Typical Entries:** Errors, warnings, or informational messages from programs like Microsoft Office, SQL Server, or third-party apps.
    
- **Use Case:** Diagnosing app crashes or misbehavior.
    

## 🔐 Security Log

- **Purpose:** Tracks security-related events like login attempts, resource access, and privilege use.
    
- **Typical Entries:** Successful and failed logins, file access, account lockouts.
    
- **Use Case:** Crucial for auditing and forensic investigations. You'll use this log heavily for security analysis.
    

## ⚙️ System Log

- **Purpose:** Logs events from Windows system components.
    
- **Typical Entries:** Driver failures, service start/stop events, hardware issues.
    
- **Use Case:** Troubleshooting OS-level problems. While it may seem sparse, it’s vital for diagnosing system stability.
    

## 🛠️ Setup Log

- **Purpose:** Captures events related to system setup and updates.
    
- **Typical Entries:** Windows installation, updates, and upgrade processes.
    
- **Use Case:** Useful when tracking installation issues or update failures.
    

## 🌐 Forwarded Events

- **Purpose:** Aggregates logs from other machines in a network.
    
- **Typical Entries:** Events forwarded from remote systems via Windows Event Forwarding (WEF).
    
- **Use Case:** Centralized monitoring in enterprise environments. Think of it as a decentralized log collector.
    

## 🧩 Applications and Services Logs

- **Purpose:** Contains logs from specific services and apps beyond the default categories.
    
- **Typical Entries:** Events from services like DNS, PowerShell, Windows Defender, etc.
    
- **Use Case:** Deep dives into specialized logs. These are more granular and tailored to specific roles or features.
    

## 🧭 Where to Learn More

Here are some excellent resources to study and explore further:

- ManageEngine: Types of Windows Event Logs
    
- Microsoft Community Hub: Understanding Windows Server Event Logs
    
- PhoenixNAP: Windows Event Logs Explained
    
- Tech Buzz Online: Beginner’s Guide to Windows Event Log Analysis



---

**Windows Event Viewer standard fields include key metadata like Event ID, Source, Level, and Time Created. These fields help identify, categorize, and analyze system and application events.**

Here’s a breakdown of the most common _standard fields_ found in the **Event Properties** window of Windows Event Viewer:

---

## 🧾 Standard Fields in Event Properties

| **Field**         | **Description**                                                                     |
| ----------------- | ----------------------------------------------------------------------------------- |
| **Log Name**      | The name of the log file (e.g., Application, Security, System).                     |
| **Source**        | The software or component that generated the event (e.g., Service Control Manager). |
| **Event ID**      | A numeric identifier for the event type (e.g., 4624 for successful logon).          |
| **Level**         | Severity of the event: Information, Warning, Error, Critical.                       |
| **User**          | The user account under which the event occurred.                                    |
| **OpCode**        | Describes the activity type (e.g., Info, Start, Stop). Often unused.                |
| **Logged**        | Timestamp of when the event was recorded.                                           |
| **Task Category** | A subcategory of the event source (e.g., Logon, File System).                       |
| **Keywords**      | Tags that help classify the event (e.g., Audit Success, Audit Failure).             |
| **Computer**      | The name of the computer where the event occurred.                                  |
| **Description**   | A detailed explanation of the event, often including parameters and context.        |

---

## 🔍 Where to View These Fields

- Open **Event Viewer** (`eventvwr.msc`)
- Navigate to a log (e.g., Security)
- Double-click any event → The **Event Properties** window will show these fields

---

## 📚 Learn More

To study these fields and their meanings in depth, check out:

- [Microsoft Learn: Event Viewer Overview](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/basic-audit-policy)
- [Ultimate Windows Security: Audit Policies and Event Viewer](https://www.ultimatewindowssecurity.com/securitylog/book/page.aspx?spid=chapter2) [Ultimate Windows Security](https://www.ultimatewindowssecurity.com/securitylog/book/page.aspx?spid=chapter2)
- [ExpertBeacon: Definitive Guide to Windows Event Viewer](https://expertbeacon.com/the-windows-event-viewer-a-2600-word-definitive-guide/) [expertbeacon.com](https://expertbeacon.com/the-windows-event-viewer-a-2600-word-definitive-guide/)


---

## 🔍 Step 1: Filtering Logs

Filtering helps you narrow down events based on criteria like Event ID, source, or time.

### 🛠 How to Filter:

1. Open **Event Viewer** (`eventvwr.msc`)
2. Navigate to a log (e.g., Security)
3. In the right-hand pane, click **Filter Current Log**
4. Use these fields:
    - **Logged**: Choose a time range
    - **Event level**: Information, Warning, Error, Critical
    - **Event IDs**: Enter specific IDs (e.g., 4624 for logon)
    - **Keywords**: Audit Success, Audit Failure
    - **User** or **Computer**: Optional filters

👉 Try filtering for Event ID `4625` (failed logon attempts) in the Security log. What do you notice?

---

Absolutely! Let’s break down the contents of your document step by step so you can understand and study each part clearly. I’ll guide you through the key concepts, explain their purpose, and offer insights into how they’re used in real-world scenarios.

---

## 📋 1. Types of Events in Windows Logs

Windows logs categorize events into five types:

- **Error**: Something went wrong (e.g., app crash, failed service).
- **Warning**: Potential issue that might need attention.
- **Information**: Routine operations (e.g., service started).
- **Success Audit**: A security-related action succeeded (e.g., successful login).
- **Failure Audit**: A security-related action failed (e.g., failed login attempt).

These types help you quickly assess the severity and nature of an event.

---

## 📚 2. Primary Windows Logs

Each log serves a different purpose:

|**Log Name**|**Purpose**|
|---|---|
|**Application**|Logs from installed applications (e.g., Microsoft Office, SQL Server).|
|**Security**|Tracks logon attempts, access to shared resources, and audit events.|
|**System**|OS-level events: drivers, services, hardware issues.|
|**Setup**|Records OS installation and update events.|
|**Forwarded Events**|Collects logs from other systems via subscriptions (uses WinRM over port 5986).|
|**Applications & Services**|Contains service-specific logs (e.g., DNS, PowerShell). Useful for long-term analysis.|

---

## 🗃️ 3. Log Retention

- Logs are **overwritten when full** unless configured otherwise.
- Retention is important for compliance (e.g., legal or regulatory requirements).
- Best practice: **archive logs regularly** and retain them based on your organization’s policy.

---

## 🔍 4. Filtering Logs

You can filter logs to find specific events:

- Filter by **event type**, **time**, **event level**, or **user**.
- Create **custom views** to save filters for reuse.
- Export filtered logs to a file for reporting or analysis.

---

## 🧾 5. Event Properties – Standard Fields

Each event contains metadata that helps identify and analyze it:

|**Field**|**Description**|
|---|---|
|**Log Name**|Which log the event belongs to.|
|**Source**|The app or service that generated the event.|
|**Event ID**|Unique identifier for the event type (e.g., 4624 = successful logon).|
|**Level**|Severity (Information, Warning, Error, etc.).|
|**User**|The user account involved in the event.|
|**Opcode**|Describes the activity (often unused).|
|**Logged**|Timestamp of when the event occurred.|
|**Task Category**|Subcategory of the event source.|
|**Keywords**|Tags for filtering and classification.|
|**Computer**|Device that recorded the event.|
|**Description**|Detailed explanation of the event.|

🔍 _Tip:_ You can investigate the source to understand Opcode and Task Category better.

---

## 📦 6. Log Record Storage

- Stored in **binary XML format** with `.evtx` extension (older: `.evt`).
- Location: `C:\Windows\System32\winevt\Logs`
- View XML version in the **Details tab** of an event.
- Logs can be **forwarded remotely** using Windows Event Collector and WinRM (port 5986).

---

## 🛡️ 7. Audit Policy

Audit policies control which events are logged:

- Access via:  
    `gpedit.msc → Computer Configuration → Windows Settings → Security Settings → Advanced Audit Policy Configuration`
- Microsoft’s recommendations:  
    [Audit Policy Best Practices](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/audit-policy-recommendations)

---

## 💻 8. PowerShell Cmdlets

Use PowerShell to query logs:

- `Get-EventLog`: For older logs (basic usage).
- `Get-WinEvent`: More powerful, supports XML queries and newer logs.

---

## 🧪 9. In-Class Exercise – Event ID Examples

Explore these categories and their Event IDs:

|**Category**|**Event IDs**|
|---|---|
|Account Management|4720–4799 (e.g., 4720 = user created)|
|Logon Events|4624, 4625, 4776|
|Shared Objects|5140, 5142–5145|
|Scheduled Tasks Access|4698–4701|
|File/Folder Access|4656–4658|
|External Storage Access|4663|
|Audit Policy Changes|4719|
|Log Cleared|1102|

🧠 _Note:_ Logon events should mostly appear on **Domain Controllers**, not local machines.

---

## ❓ 10. Why Not Log Everything?

**Answer:** Logging everything consumes system resources and storage.

- Too much logging = performance impact.
- Best practice: **test and tune** audit policies in your environment.

---

Would you like to practice analyzing a specific Event ID next, or explore how to set up centralized logging with WinRM and GPOs?