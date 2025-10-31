---
title: "Windows Remote Management - Win32 apps"
source: "https://learn.microsoft.com/en-us/windows/win32/winrm/portal"
author:
  - "[[stevewhims]]"
published:
created: 2025-10-28
description: "Windows Remote Management (WinRM) is the Microsoft implementation of the WS-Management Protocol, which is a standard SOAP-based, firewall-friendly protocol that allows interoperation between hardware and operating systems from different vendors."
tags:
  - "clippings"
---
## Windows Remote Management

Windows Remote Management (WinRM) is the Microsoft implementation of the [WS-Management protocol](https://learn.microsoft.com/en-us/windows/win32/winrm/ws-management-protocol), which is a standard Simple Object Access Protocol (SOAP)-based, firewall-friendly protocol that allows interoperation between hardware and operating systems from different vendors.

The WS-Management protocol specification provides a common way for systems to access and exchange management information across an IT infrastructure. WinRM and the [Intelligent Platform Management Interface (IPMI)](https://learn.microsoft.com/en-us/windows/win32/winrm/windows-remote-management-glossary#i) standard, along with the [Event Collector service](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc785056\(v=ws.10\)#event-collector) are components of the set of features known as [Hardware management](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc785056\(v=ws.10\)).

The intended audience for Windows Remote Management is IT professionals—who write scripts to automate the management of servers—and independent software vendor (ISV) developers, who want to obtain data for management applications.

To obtain management data from local and remote computers that might have [baseboard management controllers (BMCs)](https://learn.microsoft.com/en-us/windows/win32/winrm/windows-remote-management-glossary), you can use: WinRM scripting objects; the WinRM command-line tool; or the Windows Remote Shell (WinRS) command-line tool. If the computer runs a Windows-based operating system version that includes WinRM, then the management data is supplied by [Windows Management Instrumentation (WMI)](https://learn.microsoft.com/en-us/windows/win32/WmiSdk/wmi-start-page).

You can also obtain hardware and system data from WS-Management protocol implementations running on operating systems other than Windows in your enterprise. WinRM establishes a session with a remote computer through the SOAP-based WS-Management protocol rather than a connection through DCOM, as WMI does. Data returned using the WS-Management protocol is formatted in XML instead of as objects.

The [Intelligent Platform Management Interface (IPMI)](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/ipmiprv/ipmi-provider) WMI provider is a standard WMI provider with classes that obtain BMC sensor data from computers with the appropriate hardware. You can access IPMI data by using: the WinRM scripting API; WMI [scripting](https://learn.microsoft.com/en-us/windows/desktop/WmiSdk/scripting-api-for-wmi); or [COM](https://learn.microsoft.com/en-us/windows/desktop/WmiSdk/com-api-for-wmi) APIs.

## Run-time requirements

WinRM is part of the operating system. However, to obtain data from remote computers, you must configure a WinRM [listener](https://learn.microsoft.com/en-us/windows/win32/winrm/windows-remote-management-glossary#l). For more information, see [Installation and configuration for Windows Remote Management](https://learn.microsoft.com/en-us/windows/win32/winrm/installation-and-configuration-for-windows-remote-management). If a BMC is detected at system startup, then the IPMI provider loads; but even if not, the WinRM scripting objects and the WinRM command-line tool are still available.

## See also

- [About Windows Remote Management](https://learn.microsoft.com/en-us/windows/win32/winrm/about-windows-remote-management)
	A collection of articles about: the public Microsoft Web Services for Management (WS-Management) protocol specification; WinRM architecture; relationship to WMI; hardware management with the IPMI provider; and WinRM configuration and installation.
- [Use Windows Remote Management](https://learn.microsoft.com/en-us/windows/win32/winrm/using-windows-remote-management)
	A collection of articles about how to use the WinRM scripting API to manage hardware.
- [Windows Remote Management reference](https://learn.microsoft.com/en-us/windows/win32/winrm/windows-remote-management-reference)
	Contains the scripting interfaces defined by WS-Management automation. Also contains class definitions of the WMI classes created by the IPMI provider and classes that communicate with the IPMI driver to obtain [baseboard management controller (BMC)](https://learn.microsoft.com/en-us/windows/win32/winrm/windows-remote-management-glossary#b) data.

---

## Additional resources

Training

Module

>[!bonus]
>
>>[Manage single and multiple computers by using Windows PowerShell remoting - Training](https://learn.microsoft.com/en-us/training/modules/manage-single-multiple-computers-use-windows-powershell-remoting/?source=recommendations)
>
>This module explains how to use remoting to perform administration on remote computers.

Certification

[Microsoft Certified: Windows Server Hybrid Administrator Associate - Certifications](https://learn.microsoft.com/en-us/credentials/certifications/windows-server-hybrid-administrator/?source=recommendations)

As a Windows Server hybrid administrator, you integrate Windows Server environments with Azure services and manage Windows Server in on-premises networks.