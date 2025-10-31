


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

1. A User account is created (Use this account for the following steps).  
2. User account fails to login due to an incorrect password.  
3. User account succeeds in logon.  
4. User account is made a member of the administrators group.  
5. User account creates a scheduled task.  
6. User account accesses a USB key or other external storage media and writes a file to the device.  X
7. User account makes a change to an Audit Policy (i.e. stop logging failed logon attempts).  
8. User account logs out.  
   
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

✅ By following this sequence, you’ll not only complete the assignment but also gain hands-on experience with **audit policies, event generation, and log analysis** — exactly what your instructor wants you to internalize.