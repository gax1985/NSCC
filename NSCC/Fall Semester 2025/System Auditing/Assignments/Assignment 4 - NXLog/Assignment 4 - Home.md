
# NXLog Installation 


Step 1: Review the nxlog resources available on your brightspace shell beginning with the “About NxLog”  
link.  
Step 2: On a VM, go to the nxlog link in brightspace and download and install the latest Community  Edition for Windows. (NOT THE 30 DAY FREE TRIAL). Scroll down on the download page and download  user manuals and any reference guides and review these manuals before running the program.  
Step 3: Review the video linked at “Syslog Explained”. This video does not use NxLog but does  
demonstrate configuring the router for export of syslog messages to a syslog server. NxLog will function  
as our syslog server in a future assignment.  
Step 4: On your VM, run nxlog in the foreground and show your instructor that it is running.

# NXLog 

To accomplish this task you must modify your nxlog.conf file to contain: 


Part 1. the xm_json and syslog extensions 

Part 2. an input Module that can retrieve Windows logs from the SECURITY log file (local file on your machine). You must identify the correct local windows log file. 

Part 3. an output Module that can convert the Windows log events to json or syslog and direct the result to a new local log file in json or syslog format in a folder where you have write privileges. 

Part 4. a Route from the input module to the output module. Display the contents of your Log file (Step 4 below). Steps. Step 1. Stop the nxlog service Step 2. Modify the .conf file Step 3. Restart the nxlog service Step 4. Look in the file location specified for the new json or syslog log file and show the contents to your instructor

This is a great adjustment. Since you are already midway through the **About NXLog** page (specifically at "Native W3C parser"), you have covered the high-level architecture. You are actually ahead of where I thought you were.

Here is your **Updated Battle Plan** to finish by **Saturday, November 22nd** (3 days early), adjusted for your current progress and specific documentation references.

### The Strategy: "Sprint & Verify"

We will divide the work into two main chunks: **Input Configuration** (Today) and **Output/Routing** (Tomorrow).

---

### Day 1: Friday, Nov 21 (Theory & Inputs)

**Goal:** Finish the conceptual reading, set up the `nxlog.conf` skeleton, and configure the Input (Part 2).

|**Time**|**Activity**|**Details**|
|---|---|---|
|**15 Mins**|**Finish Reading**|Finish the "About NXLog" page. **Note:** You can skim the "Supported Formats" list. Focus on the **Architecture** or **Deployment** sections if they appear at the bottom.|
|**15 Mins**|**Flashcards (Quiz)**|Import and run the Anki deck I created. This counts as your "Active Recall."|
|**10 Mins**|**Setup**|Stop the service (`sc stop nxlog`), backup your existing `nxlog.conf`, and open the file for editing .|
|**15 Mins**|**Part 1: Extensions**|Configure `xm_json` and `xm_syslog`. _Ref: PDF Manual Sections 4.6 & 4.12_ .|
|**30 Mins**|**Part 2: Inputs**|Configure `im_msvistalog` to read the **Security** channel. _Ref: PDF Manual Section 15.1_ (Note: The PDF prompt provided implies `im_msvistalog` is the correct module for Windows Vista/2008+ logs, which includes modern Windows) .|

#### Day 1 To-Do List:

- [ ] Finish reading "About NXLog" web page.
    
- [ ] Complete 20 Anki Cards.
    
- [ ] Create `nxlog.conf.bak`.
    
- [ ] Write `<Extension>` blocks for JSON and Syslog in `nxlog.conf`.
    
- [ ] Write `<Input>` block using `im_msvistalog`.
    
    - _Subtask:_ Ensure the `Query` or `ReadFromLast` directives are correct for the **Security** log .
        

---

### Day 2: Saturday, Nov 22 (Outputs & Finish)

**Goal:** Configure where the data goes, connect the pipeline, and demonstrate it works.

|**Time**|**Activity**|**Details**|
|---|---|---|
|**10 Mins**|**Warm-up**|Quick Anki session (10 cards) to refresh memory.|
|**30 Mins**|**Part 3: Outputs**|Configure `om_file`. You need to define the output file path and use `Exec to_json();` to format the data .|
|**15 Mins**|**Part 4: Route**|Connect your Input to your Output using the `<Route>` block .|
|**20 Mins**|**Verification**|Restart service (`sc start nxlog`). Check the output file. **Take a screenshot for your instructor** .|

#### Day 2 To-Do List:

- [ ] Write `<Output>` block using `om_file`.
    
    - _Subtask:_ Verify you have write privileges to the target folder .
        
    - _Subtask:_ Add `Exec to_json();` inside the output block .
        
- [ ] Write `<Route>` block connecting the Input ID to the Output ID .
    
- [ ] Start NXLog service.
    
- [ ] Open the destination log file to verify JSON entries are appearing.
    

---

### Productivity Rules (Applied to Your Context)

#### 1. The 80/20 Rule (Pareto Principle)

**"20% of the documentation covers 80% of the assignment."**

- **Context:** You are currently reading about the "Native W3C Parser."
    
- **Application:** Does your assignment ask you to parse W3C (IIS Web Server) logs? **No.** It asks for **Windows Event Logs (Security)** .
    
- **Action:** You can safely **skim or skip** the W3C section. Focus your deep reading _only_ on the sections related to **Input** (Windows Events), **Output** (Files), and **Extensions** (JSON/Syslog). Ignore the rest for now.
    

#### 2. The "Input/Output" Ratio (The 4x Rule)

**"Spend 4x time understanding the module structure (Reading) before typing the config (Writing)."**

- **Context:** You are about to configure `im_msvistalog` (Part 2).
    
- **Application:** Don't just copy-paste code you find online. Spend 10 minutes reading the PDF Reference Manual specifically on **im_msvistalog** (or the `im_msvistalog` example in the PDF) . Understand _why_ you are selecting the "Security" channel.
    
- **Result:** When you finally type the 5 lines of code (Output), it will work immediately, rather than spending hours guessing why it failed.
    

#### 3. "Eat the Frog"

**"Do the hardest/most annoying task first thing in the morning."**

- **Context:** **Part 2 (The Input Query)** is likely the hardest part because Windows XML queries can be tricky.
    
- **Application:** Schedule Part 2 for **Friday evening** (or your first available deep-work slot) while your brain is fresh from reading the documentation. Do not leave the Input configuration for late Saturday night.
    

---

Instructor Check-in:

Since you are reading the docs now, look for Example 53 in the provided PDF (Page 48, ). It explicitly shows how to configure im_msvistalog to read the Security log.

**Would you like to look at Example 53 together to knock out Part 2?**