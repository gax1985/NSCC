---
title: "Logon types in active directory - ManageEngine ADAudit Plus"
source: "https://www.manageengine.com/products/active-directory-audit/learn/what-are-logon-types.html"
author:
  - "[[ManageEngine]]"
published:
created: 2025-10-28
description: "There are several types of logons such as Network logon, Interactive logon and NewCredentials logon. Understand the different logon types and how they can be audited. ADAudit Plus is a unique Active Directory solution that helps you get user logon data easily."
tags:
  - "clippings"
---
A user logs on to a system to gain access to the computer and the files on the network. In Windows, there are several ways a logon can occur locally, and remotely. System admins need to keep track of the logon types to be abreast of any security vulnerabilities in the organization's network.

The following is a list of the types of logons, along with their codes, found in the Windows security event log:

- ##### Interactive (Logon Type 2)
	Interactive (Logon Type 2)- This type of logon happens when a user logs on to the computer. Read in detail [here](https://www.manageengine.com/products/active-directory-audit/kb/what-is/logon-type-2.html "Here"). ![](https://www.manageengine.com/products/active-directory-audit/learn/images/what-are-logon-types-1.png)
	Successful Interactive logon (Event ID 4624) on Event Viewer
- ##### Network (Logon Type 3)
	This type of logon occurs when a user or computer logs on to the computer from the network. Read in detail [here](https://www.manageengine.com/products/active-directory-audit/kb/what-is/logon-type-3.html "Here").
- ##### Batch (Logon Type 4)
	This type of logon is used by batch servers. Scheduled tasks are executed on behalf of a user without human intervention.
- ##### Service (Logon Type 5)
	This type of logon is used for services and service accounts that logon to run a service. Read in detail [here](https://www.manageengine.com/products/active-directory-audit/kb/what-is/logon-type-5.html "Here").
- ##### Unlock (Logon Type 7)
	This type of logon occurs when a user unlocks their machine.
- ##### Network Cleartext (Logon Type 8)
	This type of logon occurs when a user or computer logs on to the computer from the network, and the password is sent in clear text.
- ##### NewCredentials (Logon Type 9)
	This type of logon occurs when a user uses the 'RunAs' command to run an application.
- ##### RemoteInteractive (Logon Type 10)
	This logon type occurs when a user remotely accesses the computer through RDP applications such as Remote Desktop, Remote Assistance or Terminal Services. Read in detail [here](https://www.manageengine.com/products/active-directory-audit/kb/what-is/logon-type-10.html "Here").
- ##### CachedInteractive (Logon Type 11)
	This type of logon is recorded when a user logons to the computer without having to contact the domain controller, since the network credentials are locally stored on the computer.

Logs with event IDs 4624 and 4625 are generated every time there is a successful or failed logon on a local computer, respectively.

**Auditing logon activity with ADAudit Plus**

**ADAudit Plus** user logon monitoring and auditing capabilities provide real-time activity reports. Administrators can centrally audit, monitor and view pre-configured reports and schedule reports to be delivered to their inbox.

###### To obtain Logon Reports,

- Log in to the **ADAudit Plus** web console.
- Click the **Reports** tab → **Local Logon-Logoff**.

Select the report of your choice, and see information about currently logged on users, logon failures, computers startup and shutdown time, and more.

Have a glimpse of some of the ADAudit Plus reports by viewing the screenshots of (i) **Logon Activity** report, (ii) **Currently Logged On Users** report, and (iii) **Computer Startup and Shutdown** report, below.

![](https://www.manageengine.com/products/active-directory-audit/learn/images/what-are-logon-types-2.png)

A user logon activity report on ADAudit Plus

![](https://www.manageengine.com/products/active-directory-audit/learn/images/what-are-logon-types-3.png)

The currently logged on users report in ADAudit Plus

![](https://www.manageengine.com/products/active-directory-audit/learn/images/what-are-logon-types-4.png)

Computers' startup and shutdown time report in ADAudit Plus

###### In these reports, you can obtain information such as:

- Who logged on to the workstation?
- When did the user last logon to the workstation?
- What kind of logon was it?
- When was the workstation last started up and shutdown?

#### About ADAudit Plus

ADAudit Plus is a real-time Active Directory auditing tool that offers 200+ reports and email alerts, including various logon and logoff reports. The different ways to logon to systems can be distinguished by ADAudit Plus, and this can help the organization understand employee behavior with regards to IT, and thwart insider and outsider attacks. It is also a valuable solution for companies that need to adhere to compliance mandates.

Managing user logon activity need not be complicated at all. Try ADAudit Plus for auditing all your workstations.

