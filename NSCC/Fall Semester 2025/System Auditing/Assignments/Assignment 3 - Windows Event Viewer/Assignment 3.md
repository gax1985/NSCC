


ISEC 2077 Security Auditing  
Assignment 3 – Windows Logs  
(Medium Assignment)  
Issued Date: October 28, 2025  
Due date: November 7, 2025  

# Preamble  

Objective: The purpose of this assignment is to learn the functioning and analysis of logged events in Windows.  

# Requirements :  

## Task 1 – Audit Policy Changes 

Establish logging on a Windows machine in the lab, a laptop or a VM and use gpedit to set Auditing of  the following events.  

For each Audit policy change, take a screen shot of the gpedit screen showing the final Audit  configuration (i.e. showing that audit Success or Failure box is ticked) for each change to the Audit Policy  

## Task 2 – Event Creation  

Create the following events such that are captured in the Windows Logs.  

1. A User account is created (Use this account for the following steps).  x
2. User account fails to login due to an incorrect password.  x
3. User account succeeds in logon.  x
4. User account is made a member of the administrators group.  x
5. User account creates a scheduled task.  
6. User account accesses a USB key or other external storage media and writes a file to the device.  X
7. User account makes a change to an Audit Policy (i.e. stop logging failed logon attempts).  x
8. User account logs out.  x
   
## Task 3 – Event Display  

Use event viewer to display these events you have created. Take screen shots of each event as required to show the detail of events displayed in event viewer (not just a list of the events) such that you can clearly read the event information.  

Create a word (PDF) document that contains the screen shots described above. Label each screen shot in the document with a description of what it is showing.

----------

## 🧑‍🏫 Step-by-Step Guide: ISEC 2077 – Assignment 3 (Windows Logs)

## ✅ Task 1 – Audit Policy Changes

**Goal:** Configure Windows to log specific security events.

### Steps:

1. **Open Local Group Policy Editor (gpedit.msc):**
    
    - Press `Win + R`, type `gpedit.msc`, press Enter.
        
    - Navigate to: `Computer Configuration → Windows Settings → Security Settings → Advanced Audit Policy Configuration → Audit Policies`
        
2. **Enable auditing for the following categories (Success/Failure as required):**
    
    - **Account Management** → Audit User Account Management (Logs account creation, deletion, group membership changes).
        
    - **Logon/Logoff** → Audit Logon (Logs successful and failed logons/logoffs).
        
    - **Policy Change** → Audit Policy Change (Logs changes to audit policies themselves).
        
    - **Object Access** → Audit Removable Storage (Logs access to USB/external drives).
        
    - **Other Policy Areas** (optional, depending on your instructor’s requirements).
        
3. **For each category:**
    
    - Double-click → Check **Success** and/or **Failure**.
        
    - Click **Apply → OK**.
        
4. **Screenshot requirement:**
    
    - Take a screenshot of each gpedit window showing the boxes ticked.
        
    - Label them: _“Audit Policy – User Account Management (Success/Failure enabled)”_, etc.
        

## ✅ Task 2 – Event Creation

**Goal:** Generate real events that will appear in the Security log.

### Events to Create:

1. **User account is created**
    
    - Open `Computer Management → Local Users and Groups → Users → New User`.
        
    - Create a test account (e.g., `TestUser`).
        
    - **Event ID:** 4720 (User account created).
        
2. **Failed login attempt**
    
    - Log out → Try logging in with `TestUser` but enter the wrong password.
        
    - **Event ID:** 4625 (Failed logon).
        
3. **Successful login**
    
    - Log in with the correct password.
        
    - **Event ID:** 4624 (Successful logon).
        
4. **Add user to Administrators group**
    
    - `Computer Management → Local Users and Groups → Groups → Administrators → Add TestUser`.
        
    - **Event ID:** 4728 (Member added to a security-enabled global group).
        
5. **Create a scheduled task**
    
    - Open Task Scheduler → Create Basic Task → Name it “TestTask”.
        
    - **Event ID:** 4698 (Scheduled task created).
        
6. **Access USB/external storage**
    
    - Insert a USB drive → Copy a file onto it.
        
    - **Event ID:** 4663 (Object access – file written to removable storage).
        
7. **Change an Audit Policy**
    
    - Go back to gpedit → Disable one of the audit settings (e.g., failed logon attempts).
        
    - **Event ID:** 4719 (System audit policy changed).
        
8. **User logs out**
    
    - Log off the `TestUser` session.
        
    - **Event ID:** 4634 (Logoff).
        

👉 _Tip:_ After each action, wait a few seconds to ensure the event is written to the log.

## ✅ Task 3 – Event Display

**Goal:** Show proof that the events were logged.

### Steps:

1. Open **Event Viewer** (`eventvwr.msc`).
    
2. Navigate to: `Windows Logs → Security`.
    
3. Use **Filter Current Log**:
    
    - Filter by Event IDs (e.g., 4720, 4625, 4624, etc.).
        
    - Or scroll and locate them manually.
        
4. **Double-click each event**:
    
    - This opens the **Event Properties** window with full details.
        
    - Confirm fields like:
        
        - **Event ID**
            
        - **Account Name**
            
        - **Logon Type**
            
        - **Time Created**
            
        - **Computer**
            
5. **Screenshot requirement:**
    
    - Take a screenshot of the **Event Properties window** for each event.
        
    - Label them in your document:
        
        - _“Event ID 4720 – User Account Created”_
            
        - _“Event ID 4625 – Failed Logon Attempt”_
            
        - etc.
            

## 📄 Final Deliverable

- Create a **Word or PDF document**.
    
- Structure it like this:
    
    1. **Task 1 – Audit Policy Changes**
        
        - Screenshot + label for each gpedit setting.
            
    2. **Task 2 – Event Creation**
        
        - Screenshot + label for each event generated.
            
    3. **Task 3 – Event Display**
        
        - Screenshot of Event Viewer properties for each event.
            

👉 _Pro tip:_ Add a short caption under each screenshot explaining what it shows. Example: _“Figure 1: Audit Policy – User Account Management configured for Success and Failure logging.”_

## 🎯 Key Event IDs Reference

|**Action**|**Event ID**|
|---|---|
|User account created|4720|
|Failed logon attempt|4625|
|Successful logon|4624|
|Added to Administrators group|4728|
|Scheduled task created|4698|
|File written to USB|4663|
|Audit policy changed|4719|
|User logoff|4634|

✅ By following this sequence, you’ll not only complete the assignment but also gain hands-on experience with **audit policies, event generation, and log analysis** — exactly what your instructor wants you to internalize.Perfect — let’s build you a **sample report outline** for your assignment. Think of this as a ready-made template where you’ll just drop in your screenshots and short captions. This way, your submission will look polished, structured, and professional.

---

# 📄 Sample Report Outline – ISEC 2077 Assignment 3  
**Windows Logs – Security Auditing**  
**Student Name:** Mohammed  
**Course:** ISEC 2077 Security Auditing  
**Assignment 3 – Windows Logs**  
**Date:** November 7, 2025  

---

## 🔹 Task 1 – Audit Policy Changes

**Objective:** Configure auditing policies in Windows using `gpedit.msc`.

### Screenshots to Include:
1. **Audit User Account Management** – Success & Failure enabled  
   *Caption:* *Figure 1: Audit Policy – User Account Management configured for Success and Failure logging.*  

2. **Audit Logon Events** – Success & Failure enabled  
   *Caption:* *Figure 2: Audit Policy – Logon/Logoff configured to capture both successful and failed logons.*  

3. **Audit Policy Change** – Success & Failure enabled  
   *Caption:* *Figure 3: Audit Policy – Policy Change auditing enabled.*  

4. **Audit Removable Storage** – Success & Failure enabled  
   *Caption:* *Figure 4: Audit Policy – Removable Storage access auditing enabled.*  

---

## 🔹 Task 2 – Event Creation

**Objective:** Generate events that will appear in the Security log.

### Events & Screenshots:
1. **User Account Created**  
   *Event ID 4720*  
   *Caption:* *Figure 5: Event Viewer showing Event ID 4720 – User account TestUser created.*  

2. **Failed Logon Attempt**  
   *Event ID 4625*  
   *Caption:* *Figure 6: Event Viewer showing Event ID 4625 – Failed logon attempt with incorrect password.*  

3. **Successful Logon**  
   *Event ID 4624*  
   *Caption:* *Figure 7: Event Viewer showing Event ID 4624 – Successful logon for TestUser.*  

4. **Added to Administrators Group**  
   *Event ID 4728*  
   *Caption:* *Figure 8: Event Viewer showing Event ID 4728 – TestUser added to Administrators group.*  

5. **Scheduled Task Created**  
   *Event ID 4698*  
   *Caption:* *Figure 9: Event Viewer showing Event ID 4698 – Scheduled task created by TestUser.*  

6. **USB Access & File Write**  
   *Event ID 4663*  
   *Caption:* *Figure 10: Event Viewer showing Event ID 4663 – File written to removable storage by TestUser.*  

7. **Audit Policy Changed**  
   *Event ID 4719*  
   *Caption:* *Figure 11: Event Viewer showing Event ID 4719 – Audit policy modified by TestUser.*  

8. **User Logoff**  
   *Event ID 4634*  
   *Caption:* *Figure 12: Event Viewer showing Event ID 4634 – TestUser logged off.*  

---

## 🔹 Task 3 – Event Display

**Objective:** Demonstrate how events appear in Event Viewer.

- For each event above, include the **Event Properties window** screenshot (not just the list view).  
- Highlight key fields: **Event ID, Account Name, Logon Type, Time Created, Computer**.  
- Ensure each screenshot is labeled and captioned clearly.

---

## 🔹 Conclusion

- Summarize what you learned:  
  - How to configure audit policies.  
  - How to generate and capture specific security events.  
  - How to interpret Event Viewer logs.  
- Reflect briefly: *“This exercise demonstrated how Windows auditing can be used to track user activity, detect unauthorized access, and maintain compliance.”*

---

✅ With this outline, your workflow is simple:  
1. Perform each step in the lab.  
2. Take the required screenshot.  
3. Drop it into this template under the right heading.  
4. Add the caption provided (or tweak wording slightly).  

---

Absolutely! Here's a detailed, printable-style ✅ **Checklist for ISEC 2077 Assignment 3 – Windows Logs**. You can use this as a lab sheet to track your progress and ensure you capture every required screenshot and configuration.

---

# ✅ Assignment 3 Checklist – Windows Logs  
**Course:** ISEC 2077 Security Auditing  
**Student:** Mohammed  
**Due Date:** November 7, 2025  

---

## 🔹 Task 1 – Audit Policy Changes

| # | Audit Category                     | Success | Failure | Screenshot Taken |
|---|------------------------------------|---------|---------|------------------|
| 1 | Audit User Account Management      | ☐       | ☐       | ☐                |
| 2 | Audit Logon Events                 | ☐       | ☐       | ☐                |
| 3 | Audit Policy Change                | ☐       | ☐       | ☐                |
| 4 | Audit Removable Storage            | ☐       | ☐       | ☐                |

📝 *Tip:* Open `gpedit.msc` → Navigate to:  
`Computer Configuration → Windows Settings → Security Settings → Advanced Audit Policy Configuration → Audit Policies`

---

## 🔹 Task 2 – Event Creation

| # | Action Performed                                      | Event ID | Screenshot Taken |
|---|--------------------------------------------------------|----------|------------------|
| 1 | Create a new user account (`TestUser`)                 | 4720     | ☐                |
| 2 | Attempt failed login with incorrect password           | 4625     | ☐                |
| 3 | Successful login with correct password                 | 4624     | ☐                |
| 4 | Add user to Administrators group                       | 4728     | ☐                |
| 5 | Create a scheduled task as the user                    | 4698     | ☐                |
| 6 | Write a file to USB/external storage                   | 4663     | ☐                |
| 7 | Change audit policy (e.g., disable failed logon audit) | 4719     | ☐                |
| 8 | Log out from the user account                          | 4634     | ☐                |

📝 *Tip:* Perform each action, then wait a few seconds before checking Event Viewer.

---

## 🔹 Task 3 – Event Display

| # | Event Description                             | Screenshot of Event Properties Taken |
|---|-----------------------------------------------|--------------------------------------|
| 1 | User Account Created (4720)                   | ☐                                    |
| 2 | Failed Logon Attempt (4625)                   | ☐                                    |
| 3 | Successful Logon (4624)                       | ☐                                    |
| 4 | Added to Admin Group (4728)                   | ☐                                    |
| 5 | Scheduled Task Created (4698)                 | ☐                                    |
| 6 | USB File Write (4663)                         | ☐                                    |
| 7 | Audit Policy Changed (4719)                   | ☐                                    |
| 8 | User Logoff (4634)                            | ☐                                    |

📝 *Tip:* Open `Event Viewer → Windows Logs → Security` → Double-click each event → Screenshot the full Event Properties window.

---

## 📄 Final Document Checklist

| Item                                      | Completed |
|-------------------------------------------|-----------|
| Screenshots labeled with captions         | ☐         |
| Screenshots embedded in Word or PDF file  | ☐         |
| Document includes Task 1, 2, and 3 clearly| ☐         |
| File named appropriately (e.g., `Mohammed_Assignment3.pdf`) | ☐         |

---

Would you like me to help you format the captions for each screenshot so they’re consistent and professional-looking in your final document?I’ve reviewed your draft document, Mohammed, and here’s a structured assessment of your progress so far on **ISEC 2077 Assignment 3 – Windows Logs**:

---

## 👍 Strengths in Your Work
- **Coverage of Required Events:**  
  You’ve listed all the major event IDs the assignment requires (4720, 4625, 4624, 4728/4732, 4698, 4663, 4719, 4634). That shows you’ve mapped the assignment tasks correctly to their corresponding Windows Security Log events.
  
- **Reasoning Sections:**  
  For each event, you’ve explained *why* auditing it matters (e.g., privilege escalation for group membership, failed logons for security monitoring). This adds depth and shows you understand the significance of each log.

- **References:**  
  You’ve already cited authoritative sources (Ultimate Windows Security encyclopedia). This strengthens your credibility and demonstrates research.

- **Audit Policy Setup Steps:**  
  You’ve documented how to enable auditing via `gpedit.msc` and listed the categories you configured (Account Management, Logon/Logoff, Policy Change, Object Access, Group Membership). This aligns with Task 1 requirements.

---

## ⚠️ Areas That Need Improvement
1. **Screenshots Missing:**  
   The assignment explicitly requires screenshots of:
   - gpedit settings (Task 1).  
   - Event Viewer properties for each event (Task 3).  
   Your text describes the steps, but the screenshots aren’t included yet.

2. **Event Descriptions Consistency:**  
   - For Event ID 4624 (successful logon), your description currently says *“alert the administrator of each failed login attempt”* — looks like a copy-paste error. It should describe *successful* logons.  
   - Double-check each description to ensure accuracy.

3. **Duplicate Section:**  
   - Event ID 4663 (USB access) appears twice with identical text. You can consolidate this into one entry.

4. **Formatting & Structure:**  
   - Add a **Table of Contents** (Word can auto-generate this once you apply heading styles).  
   - Use consistent headings for each event: *Event ID, Description, Reasoning, Screenshot*.  
   - This will make your final PDF polished and easy to navigate.

5. **Task 3 – Event Display:**  
   - You’ve described what needs to be done, but haven’t yet shown the actual Event Viewer outputs. This is critical for the assignment.

---

## ✅ Next Steps Checklist
- [ ] Insert screenshots of each **gpedit audit policy** configuration.  
- [ ] Perform the actions to generate each event (create user, failed login, etc.).  
- [ ] Capture **Event Viewer → Event Properties** for each event ID.  
- [ ] Fix the description for Event ID 4624 (successful logon).  
- [ ] Remove duplicate entry for Event ID 4663.  
- [ ] Add a Table of Contents and consistent formatting.  
- [ ] Label each screenshot clearly (e.g., *Figure 1: Audit Policy – User Account Management*).  

---

## 🎯 Overall Progress
You’re about **60–70% complete**:  
- The research, event mapping, and reasoning are solid.  
- What’s missing are the **hands-on screenshots** and some polishing of descriptions/structure.  

Once you add the screenshots and tidy up the formatting, you’ll have a strong, well-documented submission.

---

Would you like me to help you **draft the exact captions for each screenshot** (so you can just paste them under your images), ensuring they match the assignment requirements?This is a great question, Mohammed — you’ve picked up on one of the trickier parts of Windows auditing: **USB file writes**. Let’s break it down carefully.

---

## 🔹 Understanding USB Write Events

When a user copies a file to a USB drive, Windows doesn’t generate a single “USB write” event. Instead, it produces a **sequence of related events**:

1. **Device attach / recognition**  
   - **Event ID 6416**: *A new external device was recognized by the system.*  
   - This tells you a USB device was plugged in, but not whether it was used.

2. **Handle request / access attempt**  
   - **Event ID 4656**: *A handle to an object was requested.*  
   - This shows an attempt to access a file or folder (including on USB).

3. **Access attempt (success/failure)**  
   - **Event ID 4663**: *An attempt was made to access an object.*  
   - This is the key event for file operations. It will tell you if a file was written, read, or deleted.  
   - The “Accesses” field in the event details will show things like `WriteData` or `AppendData`.

4. **Optional: Access check / request**  
   - Sometimes you’ll also see **Event ID 4658** (handle closed) or **Event ID 4670** (permissions changed), depending on the action.

---
### 🔐 **Key Object Access Event IDs**

|**Event ID**|**Title**|**Purpose**|
|---|---|---|
|**4656**|A handle to an object was requested|Indicates an object was opened.|
|**4658**|The handle to an object was closed|Indicates the object was closed.|
|**4660**|An object was deleted|Tracks deletion of files, folders, etc.|
|**4663**|An attempt was made to access an object|Shows access attempts (read/write/delete).|
|**4685/4985**|The state of a transaction has changed|Related to transaction operations (e.g., file system transactions).|

---

### 📁 **Understanding File Access Duration**

To determine how long a file was open:

1. Find **Event ID 4656** (object opened).
2. Match it with **Event ID 4658** (object closed) using the **Handle ID**.
3. The time between these events reflects the duration the file was open.

---

### 🧠 **Important Fields in Event ID 4656**

|**Field**|**Explanation**|
|---|---|
|**Security ID**|SID of the user account.|
|**Account Name/Domain**|User and domain/computer name.|
|**Logon ID**|Unique ID for the logon session.|
|**Object Type**|Type of object (e.g., File, Key, SAM).|
|**Object Name**|Full path of the accessed object.|
|**Handle ID**|Unique per reboot; links related events.|
|**Process ID/Name**|ID and path of the process accessing the object.|
|**Accesses/Access Mask**|Permissions requested (e.g., ReadData, WriteData).|
|**Privileges Used**|Privileges like `SeTakeOwnershipPrivilege`.|

---

### 🧩 **Why So Many Events?**

- Object Access logs **OS-level interactions**, not just user actions.
- Applications like Word may open/close files multiple times during editing.
- Temporary files and autosaves also generate events.
- Even simple actions like listing a folder can trigger multiple events.

---

## 🔹 Instructor’s Guidance (Types 1–4)

Your instructor is essentially saying:  
- You can demonstrate **any valid combination** of:
  - **Type 1**: Device attached (6416).  
  - **Type 2**: Handle requested (4656).  
  - **Type 3**: File write success (4663 with `WriteData`).  
  - **Type 4**: File write failure (4663 with failure).  

👉 The **minimum requirement** is that you must show **either a successful or failed write** (Type 3 or 4).  
Everything else (device attach, handle request) is optional but strengthens your report.

---

## 🔹 How to Capture This in Your Assignment

For **Task 2 – Event Creation**:
- Plug in a USB drive (NTFS or FAT32).  
- Copy a file onto it.  
- Then open **Event Viewer → Security log** and filter for Event IDs: `6416, 4656, 4663`.  
- Take screenshots of:
  - The **6416 event** (device recognized).  
  - The **4663 event** showing `WriteData` (successful write).  
  - If you want, also include a **4656 event** (handle requested).  

For **Task 3 – Event Display**:
- Double-click each event → screenshot the **Event Properties** window.  
- Highlight the **Accesses field** in 4663 to show `WriteData` or `AppendData`.

---

## 🔹 About “Audit Credential Validation”

Enabling **Audit Credential Validation** is not required for your assignment, but it’s a **good idea** if you want to capture:
- Event ID **4776**: Credential validation against the domain controller.  
- Event ID **4771/4772**: Kerberos pre-authentication failures.  

👉 Why it matters:  
- It gives you visibility into **password validation attempts** (e.g., when a user logs in with wrong credentials).  
- It complements your **failed logon (4625)** events by showing *why* the logon failed (bad password, expired account, etc.).

For your assignment, it’s optional — but if you enable it, you’ll have **richer evidence** for Task 2 (failed logon attempts). That could impress your instructor.

---

## ✅ Recommendation
- For the USB write portion:  
  - At minimum, include **Event ID 4663** with `WriteData`.  
  - If possible, also include **6416** (device attached) and **4656** (handle requested).  
- For credential validation:  
  - Enable **Audit Credential Validation** — it’s not required, but it will give you extra depth and may strengthen your report.

---

This is a great question, Mohammed — you’ve picked up on one of the trickier parts of Windows auditing: **USB file writes**. Let’s break it down carefully.

---

## 🔹 Understanding USB Write Events

When a user copies a file to a USB drive, Windows doesn’t generate a single “USB write” event. Instead, it produces a **sequence of related events**:

1. **Device attach / recognition**  
   - **Event ID 6416**: *A new external device was recognized by the system.*  
   - This tells you a USB device was plugged in, but not whether it was used.

2. **Handle request / access attempt**  
   - **Event ID 4656**: *A handle to an object was requested.*  
   - This shows an attempt to access a file or folder (including on USB).

3. **Access attempt (success/failure)**  
   - **Event ID 4663**: *An attempt was made to access an object.*  
   - This is the key event for file operations. It will tell you if a file was written, read, or deleted.  
   - The “Accesses” field in the event details will show things like `WriteData` or `AppendData`.

4. **Optional: Access check / request**  
   - Sometimes you’ll also see **Event ID 4658** (handle closed) or **Event ID 4670** (permissions changed), depending on the action.

---

## 🔹 Instructor’s Guidance (Types 1–4)

Your instructor is essentially saying:  
- You can demonstrate **any valid combination** of:
  - **Type 1**: Device attached (6416).  
  - **Type 2**: Handle requested (4656).  
  - **Type 3**: File write success (4663 with `WriteData`).  
  - **Type 4**: File write failure (4663 with failure).  

👉 The **minimum requirement** is that you must show **either a successful or failed write** (Type 3 or 4).  
Everything else (device attach, handle request) is optional but strengthens your report.

---

## 🔹 How to Capture This in Your Assignment

For **Task 2 – Event Creation**:
- Plug in a USB drive (NTFS or FAT32).  
- Copy a file onto it.  
- Then open **Event Viewer → Security log** and filter for Event IDs: `6416, 4656, 4663`.  
- Take screenshots of:
  - The **6416 event** (device recognized).  
  - The **4663 event** showing `WriteData` (successful write).  
  - If you want, also include a **4656 event** (handle requested).  

For **Task 3 – Event Display**:
- Double-click each event → screenshot the **Event Properties** window.  
- Highlight the **Accesses field** in 4663 to show `WriteData` or `AppendData`.

---

## 🔹 About “Audit Credential Validation”

Enabling **Audit Credential Validation** is not required for your assignment, but it’s a **good idea** if you want to capture:
- Event ID **4776**: Credential validation against the domain controller.  
- Event ID **4771/4772**: Kerberos pre-authentication failures.  

👉 Why it matters:  
- It gives you visibility into **password validation attempts** (e.g., when a user logs in with wrong credentials).  
- It complements your **failed logon (4625)** events by showing *why* the logon failed (bad password, expired account, etc.).

For your assignment, it’s optional — but if you enable it, you’ll have **richer evidence** for Task 2 (failed logon attempts). That could impress your instructor.

---

## ✅ Recommendation
- For the USB write portion:  
  - At minimum, include **Event ID 4663** with `WriteData`.  
  - If possible, also include **6416** (device attached) and **4656** (handle requested).  
- For credential validation:  
  - Enable **Audit Credential Validation** — it’s not required, but it will give you extra depth and may strengthen your report.

---

Would you like me to **draft a sample write-up** for the USB portion (with event IDs, descriptions, and reasoning) that youGreat — here’s a polished **sample write‑up for the USB portion** that you can drop directly into your assignment alongside your screenshots. I’ll structure it the same way you’ve been doing for other events: Event ID, Description, Reasoning, and Screenshot placeholder.

---

## 📂 File Written to External Storage (USB)

**Event ID(s):**  
- **6416** – A new external device was recognized by the system.  
- **4656** – A handle to an object was requested.  
- **4663** – An attempt was made to access an object (with `WriteData` or `AppendData` indicating a file write).  
- *(Optional)* **4658** – The handle to the object was closed.  

---

**Description:**  
This policy alerts the administrator of events pertaining to attempts to access and write to an external USB storage device. The sequence of events provides a complete picture:  
- **6416** confirms that a USB device was attached.  
- **4656** shows that a file handle was requested on the device.  
- **4663** confirms whether the file was successfully written (`WriteData`) or if the attempt failed.  
- **4658** may appear to show the handle being closed after the operation.  

---

**Reasoning:**  
Auditing USB file writes is critical for detecting data exfiltration or unauthorized use of removable media. By combining device recognition (6416) with file access events (4663), administrators can determine not only that a USB was connected, but also whether sensitive files were copied onto it.  
- **Audit Success** ensures that successful writes are logged.  
- **Audit Failure** ensures that failed attempts (e.g., blocked by policy) are also captured.  
This dual approach provides visibility into both successful and unsuccessful attempts, which is important for compliance and forensic investigations.

---

**Screenshot Requirement:**  
- Screenshot of **Event ID 6416** showing the USB device recognized.  
- Screenshot of **Event ID 4663** showing `Accesses: WriteData` (successful write).  
- *(Optional)* Screenshot of **Event ID 4656** showing the handle request.  
- Label each screenshot clearly, e.g.:  
  - *Figure X: Event ID 6416 – USB device attached.*  
  - *Figure Y: Event ID 4663 – File successfully written to USB drive.*  

---

**Reference:**  
- Windows Security Log Event ID 6416 — *A new external device was recognized by the system.*  
- Windows Security Log Event ID 4656 — *A handle to an object was requested.*  
- Windows Security Log Event ID 4663 — *An attempt was made to access an object.*  
- Ultimate Windows Security Encyclopedia: [Event ID 4663](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventid=4663)

---

✅ This way, you meet your instructor’s requirement: you’ve included at least one event showing a **successful or failed write**, and you’ve optionally strengthened your report with attach + handle request events.

---

Would you like me to also draft a **parallel write‑up for the “Audit Credential Validation” events** (4776, 4771, 4772) so you cExcellent — here’s a polished **sample write‑up for Audit Credential Validation** that you can include as an optional section in your assignment. It follows the same format you’ve been using (Event ID, Description, Reasoning, Screenshot placeholder).

---

## 🔐 Audit Credential Validation

**Event ID(s):**  
- **4776** – The computer attempted to validate the credentials for an account.  
- **4771** – Kerberos pre‑authentication failed.  
- **4772** – Kerberos pre‑authentication succeeded.  

---

**Description:**  
This policy alerts the administrator whenever Windows validates user credentials during a logon attempt.  
- **4776** is generated when NTLM authentication is used, showing whether the credentials were accepted or rejected.  
- **4771** indicates a Kerberos pre‑authentication failure (for example, due to an incorrect password).  
- **4772** indicates a Kerberos pre‑authentication success.  

Together, these events provide deeper insight into the authentication process beyond the basic logon success/failure events (4624 and 4625).

---

**Reasoning:**  
Enabling **Audit Credential Validation** is valuable because it shows *why* a logon attempt succeeded or failed.  
- For failed logons, it can reveal whether the issue was an incorrect password, expired account, or other credential problem.  
- For successful logons, it confirms that the credentials were validated correctly.  
This information is especially useful in enterprise environments where multiple authentication protocols (NTLM, Kerberos) are in use. It complements the standard logon events and strengthens forensic analysis.

---

**Screenshot Requirement:**  
- Screenshot of **Event ID 4776** showing credential validation attempt.  
- Screenshot of **Event ID 4771** showing a failed Kerberos pre‑authentication.  
- Screenshot of **Event ID 4772** showing a successful Kerberos pre‑authentication.  
- Label each screenshot clearly, e.g.:  
  - *Figure X: Event ID 4776 – NTLM credential validation attempt.*  
  - *Figure Y: Event ID 4771 – Kerberos pre‑authentication failed.*  
  - *Figure Z: Event ID 4772 – Kerberos pre‑authentication succeeded.*  

---

**Reference:**  
- Windows Security Log Event ID 4776 — *The computer attempted to validate the credentials for an account.*  
- Windows Security Log Event ID 4771 — *Kerberos pre‑authentication failed.*  
- Windows Security Log Event ID 4772 — *Kerberos pre‑authentication succeeded.*  
- Ultimate Windows Security Encyclopedia: [Event ID 4776](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventid=4776)

---

✅ Adding this section will demonstrate that you went beyond the minimum requirements and explored **credential validation auditing**, which shows initiative and deeper understanding.

---

Would you like me to also **map these credential validation events into your Task 2 workflow** (e.g., failed logon → 4625 + 4771, succePerfect — let’s map **Audit Credential Validation events** directly into your **Task 2 workflow**, so you can show how they complement the required logon events. This way, your assignment demonstrates both the *basic logon tracking* and the *deeper credential validation layer*.

---

# 🔐 Integrating Credential Validation into Task 2

### 1. **Failed Logon Attempt**
- **Core Event (already required):**  
  - **4625** – *An account failed to log on.*  
- **Credential Validation Events (optional, but recommended):**  
  - **4776** – NTLM credential validation attempt (shows the account name and whether credentials were valid).  
  - **4771** – Kerberos pre‑authentication failed (if Kerberos is used).  
- **How they complement each other:**  
  - 4625 tells you *that* the logon failed.  
  - 4776/4771 tell you *why* it failed (bad password, expired account, etc.).  

---

### 2. **Successful Logon**
- **Core Event (already required):**  
  - **4624** – *An account was successfully logged on.*  
- **Credential Validation Events (optional):**  
  - **4776** – NTLM credential validation succeeded.  
  - **4772** – Kerberos pre‑authentication succeeded.  
- **How they complement each other:**  
  - 4624 confirms the logon.  
  - 4776/4772 confirm that the credentials were validated correctly.  

---

### 3. **How to Generate These Events**
- **NTLM (Event 4776):**  
  - Occurs when logging into a standalone machine or using local accounts.  
- **Kerberos (Events 4771/4772):**  
  - Occurs when logging into a domain environment.  
- **Tip:** If you’re working in a lab VM with no domain, you’ll likely see **4776** (NTLM). If you’re in a domain lab, you’ll see **4771/4772**.  

---

### 4. **Screenshots to Capture**
- For a failed logon:  
  - Screenshot of **4625** (failed logon).  
  - Screenshot of **4776** or **4771** (credential validation failure).  
- For a successful logon:  
  - Screenshot of **4624** (successful logon).  
  - Screenshot of **4776** or **4772** (credential validation success).  
- Label them clearly, e.g.:  
  - *Figure X: Event ID 4625 – Failed logon attempt.*  
  - *Figure Y: Event ID 4776 – NTLM credential validation failed.*  
  - *Figure Z: Event ID 4624 – Successful logon.*  
  - *Figure W: Event ID 4772 – Kerberos pre‑authentication succeeded.*  

---

### 5. **Why This Strengthens Your Assignment**
- Shows you understand not just *logon events* but also the **underlying credential checks**.  
- Demonstrates initiative by going beyond the minimum requirements.  
- Provides richer forensic evidence: you can explain *both the outcome and the reason*.  

---

✅ By weaving these credential validation events into your Task 2, you’ll have a more complete story:  
- *User tried to log in → credentials validated → logon succeeded/failed.*  

---

Would you like me to draft a **combined narrative flow** (almost like a case study) that strings together the sequence of events — account creation, failed logon, credential validation, successful lExcellent — let’s build a **coherent narrative timeline** that strings together the sequence of events in your assignment. This will make your report read like a case study, showing not just isolated screenshots but the *story* of what happened on the system.  

---

# 🧑‍🏫 Narrative Flow: Case Study of User Account Activity

---

## 1. **Account Creation**
- **Event ID 4720** – *A user account was created.*  
- The administrator creates a new account `TestUser`.  
- **Screenshot:** Event Properties showing the account name, computer, and time.  
- *Narrative:* *“At [time], a new account named TestUser was created on the system. This event was captured under Event ID 4720, confirming the account creation.”*

---

## 2. **Failed Logon Attempt**
- **Event ID 4625** – *An account failed to log on.*  
- **Event ID 4776/4771** – *Credential validation failed.*  
- The user attempts to log in with the wrong password.  
- **Screenshot:** Event Properties showing failure reason.  
- *Narrative:* *“At [time], TestUser attempted to log in with incorrect credentials. Event ID 4625 recorded the failed logon, while Event ID 4776 (NTLM) indicated that the credentials were invalid.”*

---

## 3. **Successful Logon**
- **Event ID 4624** – *An account was successfully logged on.*  
- **Event ID 4776/4772** – *Credential validation succeeded.*  
- The user logs in with the correct password.  
- **Screenshot:** Event Properties showing success.  
- *Narrative:* *“At [time], TestUser successfully logged in. Event ID 4624 confirmed the logon, and Event ID 4772 (Kerberos) validated the credentials.”*

---

## 4. **Privilege Escalation**
- **Event ID 4728/4732** – *User added to Administrators group.*  
- The account is granted administrator rights.  
- **Screenshot:** Event Properties showing group membership change.  
- *Narrative:* *“At [time], TestUser was added to the Administrators group. Event ID 4728 documented the privilege escalation.”*

---

## 5. **Scheduled Task Creation**
- **Event ID 4698** – *A scheduled task was created.*  
- The user creates a task named “TestTask.”  
- **Screenshot:** Event Properties showing task details.  
- *Narrative:* *“At [time], TestUser created a scheduled task named TestTask. Event ID 4698 captured the task creation, including the task path and user account.”*

---

## 6. **USB File Write**
- **Event ID 6416** – *USB device recognized.*  
- **Event ID 4656** – *Handle requested.*  
- **Event ID 4663** – *File write (WriteData).*  
- The user copies a file to a USB drive.  
- **Screenshot:** Event Properties showing `Accesses: WriteData`.  
- *Narrative:* *“At [time], a USB device was attached (Event ID 6416). Shortly after, TestUser attempted to write a file to the device. Event ID 4663 confirmed the successful write operation.”*

---

## 7. **Audit Policy Change**
- **Event ID 4719** – *System audit policy changed.*  
- The user disables failed logon auditing.  
- **Screenshot:** Event Properties showing policy change.  
- *Narrative:* *“At [time], TestUser modified the system audit policy, disabling failed logon auditing. Event ID 4719 recorded this change.”*

---

## 8. **Logoff**
- **Event ID 4634** – *An account was logged off.*  
- The user logs out.  
- **Screenshot:** Event Properties showing logoff.  
- *Narrative:* *“At [time], TestUser logged off the system. Event ID 4634 confirmed the termination of the session.”*

---

# 📊 Why This Timeline Matters
- It shows a **complete lifecycle**: account creation → failed logon → credential validation → successful logon → privilege escalation → scheduled task → USB file write → audit policy change → logoff.  
- Each step is backed by **specific Event IDs** and screenshots.  
- The narrative ties the events together into a **story of user activity**, which is exactly what security auditing is meant to capture.

---

✅ With this timeline, your report will stand out as more than just a list of screenshots — it will read like a **forensic case study**.  

