


# Penetration Testing



## Jan. 8th


### Ethics of Hacking Summary

**Types of Hackers:**
1. **White Hat**: Ethical hackers aiming to improve security.
2. **Grey Hat**: Often break laws but without malicious intent; may have political motivations or seek fun.
3. **Black Hat**: Criminal hackers with various motivations, primarily for financial gain.

**Historical Context:**
- The terminology originates from 1920s films for easy visual identification during the Silent Era.
- Kevin Mitnick’s lockpicking business card exemplifies hacker ingenuity.

**Types and Motivations of Hacking:**
1. **Types**: 
   - Ethical hacking
   - Grey hat hacking
   - Black hat hacking

2. **Motivations**:
   - Curiosity
   - Puzzles
   - Recognition and Fame
   - Revenge
   - Financial Gain
   - Patriotism
   - Politics

**Historical Hacks:**
- **1950s**: First password hack by Allan Scherr at MiT to bypass computer time limitations.
- **1970s**: Phreaking for free calls using whistles emitting 2600 Hz tones.
- **1980s**: War dialing to find open modems, leading to viruses, worms, and Trojans.

**Certifications:**
- **Vendor-Neutral**: CISSP, CISA, Security+, CEH, CISM, GSEC, SSCP, CASP+, GCIH, OCSP, PenTest+.
- **Vendor-Specific**: Cisco, Check Point, Microsoft.

**Deciding What to Secure:**
- Protecting data provided to organizations or stored on personal devices is crucial.
- Unauthorized bandwidth use is unethical and illegal.
- Temptation to copy and use proprietary software is widespread but illegal.

**Ethical Issues in Hacking:**
- Professional hackers have a societal responsibility.
- Activities should build and improve existing technology.
- Hacking skills should be used for learning and teaching.

**Assignment:**
- Form teams of 3-4.
- Identify entry points in a building, including doors and emergency exits.
- Assign roles and create a thorough building diagram.
- Document all potential access points and locking mechanisms.
- Locate security cameras and remain discreet.



------------


## Jan. 13th




### Reconnaissance Summary

**Objectives:**
1. Identify techniques for performing reconnaissance.
2. Discuss methods used in social engineering.
3. Identify phases of footprinting.

**Definition:**
- Reconnaissance: A preliminary survey to gain information, identifying targets, and developing methods to attack successfully.

**Legal Reconnaissance:**
- Publicly available information (Google Maps).
- Gathering information from the internet, customer service, interviews, facility tours, and forming friendships with staff.

**Questionable Reconnaissance:**
- Port scanning, scanning WiFi networks, reading unattended documents/mail, and picking up trash.

**Illegal Reconnaissance:**
- Creating a front company for fraudulent purposes.
- Probing, deep scanning, or taking documents from a desk is considered theft.

**Social Engineering:**
- Relies on people being trusting and helpful.
- Successful attacks often exploit naivety and human error.

**Social Engineering Techniques:**
1. **Impersonation**: Imitating another person or role.
2. **Exploiting Greed**: Offering financial incentives to manipulate individuals.
3. **Exploiting Ignorance**: Manipulating those unaware of security practices.
4. **Blackmail**: Coercing individuals by threatening to expose compromising information.
5. **Deception**: Gaining information by posing as an employee or consultant.

**Physical Intrusion:**
- Requires knowledge of schedules, floor plans, security procedures, and fake or stolen ID cards.
- Once inside, valuable information can be acquired.

**The Lufthansa Heist Example:**
- Largest cash robbery in the U.S., highlighting the magnitude and complexity of such crimes.

**Avoiding Suspicion:**
- Do not gather all information from a single source.
- ‘Inside jobs’ simplify access but increase risk of exposure.

**Insider Threats:**
1. **Malicious insiders**: Inflict harm with their access.
2. **Negligent insiders**: Make errors, risking security.
3. **Infiltrators**: External actors with unauthorized access.

### Communication Media and Social Engineering Summary

**Email Attacks:**
- Fake emails from seemingly legitimate sources ask users to log in to false websites.
- Hackers send email invitations to join competitions, requiring sensitive information.

**Phishing:**
- Tricking users into providing private information.

**Spear Phishing:**
- Targeted phishing using personalized emails to deceive specific individuals or organizations.

**Whaling:**
- Using spear phishing techniques to target senior executives with customized content.
- Known for its significant financial impacts.

**Instant Messaging:**
- Social engineers befriend victims to gather information or direct them to malicious websites.

**Telephone Communication:**
- Social engineers manipulate background sounds and voices.
- Help desk personnel are common targets.
- Often impersonate technicians.

**Countering Social Engineering:**
- Do not provide information to unknown individuals.
- Avoid disclosing confidential information over the phone.
- Do not type sensitive information in front of unknown people.
- Verify website security before submitting information.
- Use different usernames/passwords for different accounts.
- Implement Multi-Factor Authentication (MFA).
- Verify credentials of individuals asking for passwords.
- Keep confidential documents locked.
- Lock or shut down computers when away.
- Help desk employees should authenticate callers.
- Use official contact details from the website.

**Baiting:**
- USB sticks loaded with malware can compromise systems or destroy target computers.

**Dumpster Diving:**
- A source of sensitive information from documents or hardware discarded improperly.

**Proper Discarding of Refuse:**
- Security policies should define sensitive information and its disposal.
- Use crosscut shredders and locked trash receptacles.
- Outdated hardware should be disposed of securely to prevent data theft.

**Prevention Guidelines:**
- Develop and implement a recycling and trash-handling policy.
- Ensure consistent and systematic trash handling to prevent data theft.


------------


# Jan. 20th




### Objectives Summary

**Key Objectives:**
1. Understand how scanners function.
2. Trace the development history of scanners.
3. Identify various types of scanning.
4. Identify different scanners.

**Scanners' Roles:**
1. Find and fix vulnerabilities in remote machines on a network.
2. Examine and report vulnerabilities on local and remote hosts.

**Types of Scanners:**
- **Active Scanners**: e.g., Port scanner (examines port conditions).
- **Passive Scanners**: e.g., Network Monitor (captures packets on the network).

**Historical Context:**
- Early scanners appeared before ARPANET, monitoring connections between mainframes and terminals.
- **War Dialer**: Automated scanner script dialing a range of phone numbers to connect remote computers.

**Scanner Evolution:**
- Initially UNIX-based, later expanded as the internet grew.
- Modern scanners automate network vulnerability examinations.

**Scanning Techniques:**
- **Ping Scanning**: Checks if a remote host is active.
- **TCP Connect Scanning**: Attempts connections with all ports on a remote system.
- **Half-Open/Stealth Scan (-sS)**: Sends SYN messages; avoids detection by not completing connections.
- **UDP Scanning (-Su)**: Sends 0-byte UDP packets; slower but necessary.
- **IP Protocol Scanning (-sO)**: Examines supported IP protocols on a target host.

**Popular Scanners and Tools:**
- **Nmap (Zenmap)**: Comprehensive scanner.
- **Unicornscan**: Faster, especially with UDP.
- **tcpdump/WinDump**: Command-line packet analyzers.
- **Wireshark**: GUI-based packet analyzer.

**Vulnerability Identification Tools:**
- **Nessus**: Scans for security vulnerabilities.
- **NeXpose**: Commercial vulnerability testing.
- **OpenVAS/GreenBone**: Open-source Nessus.
- **QualysGuard (SaaS)**: Network discovery and vulnerability management.
- **SAINT**: Vulnerability detection and exploitation suite.
- **SATAN**: Early network vulnerability scanner.

**Exploitation Tools:**
- **CORE Impact**: Commercial vulnerability testing and penetration tool.
- **Metasploit**: Network vulnerability tool with extensive functions.
- **Bettercap**: Multi-functional tool for WiFi, Bluetooth, and network reconnaissance.
- **Kali Linux**: Contains around 600 penetration-testing tools.

**Final Notes:**
- Scanners help identify network weaknesses and known vulnerabilities.
- They provide crucial insights into the vulnerabilities of target systems.
- Early computing had numerous but poorly known security vulnerabilities.

I hope this summary helps! If you need more details or adjustments, please let me know.