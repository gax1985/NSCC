---
title: "Windows Event Collector (im_wseventing) | NXLog Platform Documentation"
source: "https://docs.nxlog.co/agent/current/im/wseventing.html"
author:
  - "[[this guide]]"
published:
created: 2025-11-21
description: "Documentation for NXLog Agent's Windows Event Forwarding input module and how to collect Windows events remotely."
tags:
  - "clippings"
---
## Windows Event Collector (im\_wseventing)

This module collects Windows events forwarded by Microsoft Windows clients with *Windows Event Forwarding (WEF)*. It takes the role of the collector (Subscription Manager) to accept events over the [WS-Management](https://learn.microsoft.com/en-us/windows/win32/winrm/ws-management-protocol) protocol. WS-Eventing is a subset of WS-Management used to forward Windows events.

In comparison, the [im\_msvistalog](https://docs.nxlog.co/agent/current/im/msvistalog.html) module collects Windows events locally or remotely; however, it requires an NXLog Agent instance running on Windows. See [Windows event collection](https://docs.nxlog.co/integrations/os/windows-event-log.html#windows-event-collection) for more information. On the other hand, the *im\_wseventing* module can be used on all supported platforms, including GNU/Linux systems, to remotely collect Windows Event Logs without requiring additional software installed on the log source.

|  | To examine the supported platforms, see the [list of installation packages](https://docs.nxlog.co/agent/current/install/modules-by-package.html). |
| --- | --- |

## Overview of Windows Event Forwarding

WEF is a service that enables forwarding administrative and operational event logs from a Windows server to a central location. There are two roles in a WEF setup:

- the Windows Event Collector (WEC), also known as a Subscription Manager, which is a server configured to receive events;
- the WEF client, also known as a forwarder, which is a machine configured to forward events to the collector.

The link between the two is known as a subscription, and it can be configured either as a push or pull service.

NXLog Agent can act as a WEC by configuring the *im\_wseventing* module to collect forwarded events, thus using the push method. Windows machines are then configured as WEF clients, forwarding events to NXLog Agent. The advantage of this method is that you can configure clients to forward their events via Group Policy, removing the overhead of managing a list of clients from which events are to be collected.

The connection between the WEC and the client is mutually authenticated and encrypted using Kerberos by default. However, if you cannot implement Kerberos authentication in your environment, an HTTPS option using certificate-based authentication is also possible. NXLog Agent supports either of these authentication methods.

In this documentation, we refer to the machine where NXLog Agent is installed as the WEC server and the Windows machine forwarding events to it as the WEF client.

|  | While other products, such as IBM WebSphere DataPower, implement the WS-Eventing protocol, the *im\_wseventing* module’s primary purpose is to collect and parse forwarded events from Microsoft Windows. Therefore, we cannot guarantee compatibility with other products. |
| --- | --- |

## Using Kerberos authentication

### Configure Kerberos on Linux

This section explains how to configure a Microsoft Active Directory domain user to be used with Kerberos authentication on a Linux machine. Once these steps are complete, NXLog Agent can be configured as a Windows Event Collector with WEF clients forwarding events to it.

The steps and examples below assume the following values:

- `example.com` is the FQDN of the Active Directory domain.
- `EXAMPLE` is the name of the Active Directory domain.
- `linux` is the name of the Linux WEC server.

#### WEC server prerequisites

For Kerberos authentication to work successfully, the Linux machine acting as a WEC server must meet the following prerequisites:

- The OS must return the correct hostname.
- The machine must be configured with a static IP address.
- DNS settings must point to the same DNS server used in the Active Directory domain.
- The time must be synchronized with the Active Directory domain.

Refer to the documentation of your operating system for instructions how to configure and verify these settings.

#### Create and map the Active Directory domain user

1. On the Active Directory domain controller, create a new user as follows:
	1. The account name should match the hostname of the Linux WEC server.
	2. Set a password for the user.
	3. Disable the **User must change password at next logon** option.
	4. Enable the **Password never expires** option.
	5. The account should have the **Kerberos AES 128 bit encryption** and **Kerberos AES 256 bit encryption** options enabled.
2. On the DNS server, create an A record for the Linux WEC server with an associated PTR record for reverse lookup.
3. On the Active Directory domain controller, open a command prompt and execute these commands. Use the same `<password>` that was specified when the above user was created. These commands map the domain account to the Kerberos principal names and generate two keytab files containing the shared secret.
	```console
	> ktpass /princ hosts/linux.example.com@EXAMPLE.COM /pass <password> /mapuser DOMAIN\linux -pType KRB5_NT_PRINCIPAL /out hosts-nxlog.keytab /crypto AES256-SHA1
	> ktpass /princ http/linux.example.com@EXAMPLE.COM /pass <password> /mapuser DOMAIN\linux -pType KRB5_NT_PRINCIPAL /out nxlog.keytab /crypto AES256-SHA1
	```
	Refer to the Microsoft documentation for more information on the [ktpass](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ktpass) tool.
4. Copy the resulting `hosts-nxlog.keytab` and `nxlog.keytab` files to the Linux host.

#### Configure Kerberos on the WEC server

1. Confirm that the Kerberos krb5 client and utility software are installed on the WEC server. The required package can be installed, for example, with `yum install krb5-workstation` or `apt install krb5-user`.
2. Edit the default Kerberos configuration file, usually located at `/etc/krb5.conf`.
	1. In section `[domain_realm]`, add:
		```console
		.example.com = EXAMPLE.COM
		example.com = EXAMPLE.COM
		```
	2. In section `[realms]`, add:
		```console
		EXAMPLE.COM = {
		 kdc = example.com
		 admin_server = example.com
		}
		```
	3. Use `ktutil` to merge the two keytab files generated above.
		```console
		# ktutil
		```
		The output:
		```
		ktutil:  rkt /root/hosts-nxlog.keytab
		ktutil:  rkt /root/nxlog.keytab
		ktutil:  wkt /root/nxlog-result.keytab
		ktutil:  q
		```
	4. Validate the merged keytab.
		```console
		# klist -e -k -t /root/nxlog-result.keytab
		```
		The output:
		```console
		Keytab name: FILE:/root/nxlog-result.keytab
		KVNO Timestamp           Principal
		---- ------------------- ------------------------------------------------------
		   5 17.01.2021 04:16:37 hosts/linux.example.com@EXAMPLE.COM (aes256-cts-hmac-sha1-96)
		   4 17.01.2021 04:16:37 http/linux.example.com@EXAMPLE.COM (aes256-cts-hmac-sha1-96)
		```
	5. Either copy the keytab into place, or merge it if there are already keys in `/etc/krb5.keytab`.
		- To copy the keytab:
			```console
			cp /root/nxlog-result.keytab /etc/krb5.keytab
			```
		- To merge the keytab and validate the result:
			```console
			# ktutil
			```
			The output:
			```console
			ktutil:  rkt /etc/krb5.keytab
			ktutil:  rkt /root/nxlog-result.keytab
			ktutil:  wkt /etc/krb5.keytab
			ktutil:  q
			```
			Validate:
			```console
			# klist -e -k -t /etc/krb5.keytab
			```
			The output:
			```console
			Keytab name: FILE:/etc/krb5.keytab
			KVNO Timestamp           Principal
			---- ------------------- ------------------------------------------------------
			   <other entries>
			   5 17.01.2021 04:20:08 hosts/linux.example.com@EXAMPLE.COM (aes256-cts-hmac-sha1-96)
			   4 17.01.2021 04:20:08 http/linux.example.com@EXAMPLE.COM (aes256-cts-hmac-sha1-96)
			```
		- Verify that the access permissions of the `/etc/krb5.keytab` file allow the user that NXLog Agent is running under to read it. If not, Kerberos authentication will fail as described in the [Troubleshooting](https://docs.nxlog.co/agent/current/im/#troubleshooting) section.
3. Test that the authentication with Active Directory is working successfully when using the keytab. Run the following command on the Linux WEC server and if the configuration is correct a ticket-granting ticket (TGT) will be created and cached. This step should be executed with the user that NXLog Agent is running under, by default the `nxlog` user.
	```console
	# kinit -kt /etc/krb5.keytab http/linux.example.com@EXAMPLE.COM
	```
4. Verify the ticket was obtained by running `klist` with the same user as the previous step:
	```console
	# klist
	```
	The output:
	```
	Ticket cache: KCM:0
	Default principal: http/linux.example.com@EXAMPLE.COM
	Valid starting     Expires            Service principal
	28/01/21 11:41:44  28/01/21 21:41:44  krbtgt/EXAMPLE.COM@EXAMPLE.COM
	    renew until 04/02/21 11:41:44
	```
5. Configure and run NXLog Agent. See the [configuration example](https://docs.nxlog.co/agent/current/im/#example-kerberos) below.
6. Make sure the port defined in the *im\_wseventing* configuration is accessible from the WEF clients. The local firewall rules on the Linux WEC server may need to be updated.

### Configure Kerberos on Windows

1. Install and configure Kerberos for Windows, such as [MIT Kerberos](https://web.mit.edu/kerberos/dist/).
2. Configure NXLog Agent to use the [setenv](https://docs.nxlog.co/agent/current/config/general-settings.html#setenv) global directive to:
	1. Set the Kerberos keytab path.
		```config
		setenv KRB5_KTNAME=%INSTALLDIR%/krb5.keytab
		```
		config
	2. Disable the replay cache. Note that the value is case-sensitive.
		```config
		setenv KRB5RCACHETYPE=none
		```
		config

### Configure the WEF Client

In this example, WEF is enabled on a single Windows node by editing the local policy of the server. To enable WEF on multiple nodes, a group policy on the domain should be configured.

1. Run `gpedit.msc` and go to **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Event Forwarding**.
2. Open and enable the **Configure target Subscription Manager** setting.
3. Click **Show…** beside the **SubscriptionManagers** option.
4. Type into the **Value** field:`Server=http://linux.example.com:80,Refresh=30`.
5. Open command prompt and run `gpupdate /force`.
6. At this point the WinRM service on the Windows client should connect to NXLog Agent. If [LogConnections](https://docs.nxlog.co/agent/current/im/#config-logconnections) is set to `TRUE` a connection attempt should be logged in `nxlog.log` and you should soon start seeing events arriving.

|  | The `Refresh` interval represents the time in seconds and on production systems should be set to a higher value (e.g. `Refresh=1200`). When the Windows client is set to reconnect too frequently it will result in a lot of connection/disconnection messages in `nxlog.log`. |
| --- | --- |

### Configuring Kerberos on Windows

The steps and examples below assume the following values:

- `example.com` is the FQDN of the Active Directory domain.
- `EXAMPLE` is the name of the Active Directory domain.
- `wecserver` is the name of the WEC server.

#### WEC server prerequisites

Before configuring Kerberos authentication, the Windows host acting as a WEC server needs to satisfy the following requirements:

- The OS must return the correct hostname.
- The machine must be configured with a static IP address.
- DNS settings must point to the same DNS server used by the domain controller.
- The time must be synchronized with the domain controller.
- If a firewall is enabled, it must allow inbound TCP traffic on port 8080 (or the port of your choice) to the WEC server.

#### Configure DNS Server settings

On your Windows DNS Server:

1. Open **Server Manager** and navigate to **Tools** > **DNS** to open **DNS Manager**.
2. Verify that `Host (A)` and associated pointer `PTR` records exist for the WEC server.
3. If not, expand *<server\_name>* > **Forward Lookup Zones** and right-click on your domain name.
4. Select **New Host (A or AAAA…)**.
5. Enter the WEC server details and enable the **Create associated pointer (PTR) record** option.
6. Click **Add Host**.

#### Create and map the Active Directory domain user

1. On the Active Directory domain controller, create a new user as follows:
	1. The account name should match the hostname of the WEC server.
	2. Set a password for the user.
	3. Disable the **User must change password at next logon** option.
	4. Enable the **Password never expires** option.
	5. The account should have the **Kerberos AES 128 bit encryption** and **Kerberos AES 256 bit encryption** options enabled.
2. Note down the account logon name, e.g., `winserver@example.com (EXAMPLE\wecserver)`
3. Open a command prompt and execute these commands. Use the same `<password>` that you specified when you created the above user. These commands map the domain account to the Kerberos principal names and generate two keytab files containing the shared secret.
	```console
	> ktpass /princ hosts/wecserver.example.com@EXAMPLE.COM /pass <password> /mapuser EXAMPLE\wecserver -pType KRB5_NT_PRINCIPAL /out hosts-nxlog.keytab /crypto AES256-SHA1
	> ktpass /in hosts-nxlog.keytab /princ http/wecserver.example.com@EXAMPLE.COM /pass <password> /mapuser EXAMPLE\wecserver -pType KRB5_NT_PRINCIPAL /out krb5.keytab /crypto AES256-SHA1
	```
	This will result in a single `krb5.keytab` file containing both principals.
4. Verify the keytab file:
	```console
	> ktpass /in krb5.keytab
	```
	The output should be similar to the following. The warning message can be ignored.
	```console
	Existing keytab:
	    Keytab version: 0x502
	    keysize 95 hosts/wecserver.EXAMPLE.com@EXAMPLE.COM ptype 1 (KRB5_NT_PRINCIPAL) vno 17 etype 0x12 (AES256-SHA1) keylength 32 (0xfda8dc9a12445f01773179ec94ea9441317846741366759b9cd03da7d291013b)
	    keysize 94 http/wecserver.EXAMPLE.COM@EXAMPLE.COM ptype 1 (KRB5_NT_PRINCIPAL) vno 18 etype 0x12 (AES256-SHA1) keylength 32 (0xd351a92138a72c87ab04fee9ff8d6f769048125b81c47cd141d1f41ced52bbbf)
	    WARNING: No principal name specified.
	```
	Refer to the Microsoft documentation for more information on the [ktpass](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ktpass) tool.

#### Configure the WEC server

1. Download the relevant MIT Kerberos for Windows package from the [MIT Kerberos Distribution Page](https://kerberos.org/dist/).
2. Execute the package and follow the wizard to perform a **Complete** installation.
3. Once installation is complete, restart the WEC server.
4. Copy the `krb5.keytab` file created in the previous section from your domain controller to `C:\Program Files\nxlog` on your WEC server.
5. Open `C:\ProgramData\MIT\Kerberos5\krb5.ini` with a text editor and add the following configuration:
	```
	[libdefaults]
	default_realm = EXAMPLE.COM
	default_keytab_name = "C:\Program Files\nxlog\krb5.keytab"
	default_tkt_enctypes = aes256-cts-hmac-sha1-96
	default_tgs_enctypes = aes256-cts-hmac-sha1-96
	default_ccache_name = c:\Windows\Temp\krbcache
	forwardable = true
	[domain_realm]
	.EXAMPLE.com = EXAMPLE.COM
	EXAMPLE.com = EXAMPLE.COM
	[realms]
	EXAMPLE.COM = {
	 kdc = dc.EXAMPLE.com:88
	 admin_server = dc.EXAMPLE.com
	}
	```
	Change `dc.EXAMPLE.com` according to the name of your DNS Server.
6. Open command prompt and execute the following commands:
	```cmd
	> cd C:\Program Files\MIT\Kerberos\bin
	> klist -e -k -t "C:\Program Files\nxlog\krb5.keytab"
	```
	cmd
	The output:
	```cmd
	Keytab name: FILE:C:\Program Files\nxlog\krb5.keytab
	KVNO Timestamp         Principal
	---- ----------------- --------------------------------------------------------
	  15 01/01/70 00:00:00 http/wecserver.EXAMPLE.com@EXAMPLE.COM (aes256-cts-hmac-sha1-96)
	  16 01/01/70 00:00:00 hosts/wecserver.EXAMPLE.com@EXAMPLE.COM (aes256-cts-hmac-sha1-96)
	```
7. Execute the following command to test that the authentication with Active Directory is working successfully when using the keytab. If the configuration is correct, a ticket-granting ticket (TGT) will be created and cached.
	```cmd
	> kinit -kt "C:\Program Files\nxlog\krb5.keytab" http/wecserver.EXAMPLE.com@EXAMPLE.COM
	```
	cmd
8. Verify the ticket was obtained:
	```cmd
	> klist
	```
	cmd
	The output should be similar to:
	```cmd
	Ticket cache: API:krb5cc
	Default principal: http/wecserver.EXAMPLE.com@EXAMPLE.COM
	Valid starting     Expires            Service principal
	03/18/23 00:07:14  03/18/23 10:07:14  krbtgt/EXAMPLE.COM@EXAMPLE.COM
	        renew until 03/19/23 00:07:13
	```
9. Configure and restart NXLog Agent. See the [configuration example](https://docs.nxlog.co/agent/current/im/#example-kerberos-windows) below.

#### Configure the WEF Client

In this example, WEF is enabled on a single Windows node by editing the local policy of the server. To enable WEF on multiple nodes, a group policy on the domain should be configured.

1. Run `gpedit.msc` and go to **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Event Forwarding**.
2. Open and enable the **Configure target Subscription Manager** setting.
3. Click **Show…** beside the **SubscriptionManagers** option.
4. Type into the **Value** field: `Server=http://wecserver.example.com:8080/wsman,Refresh=30`.
5. Open command prompt and run `gpupdate /force`.
6. At this point, the WinRM service on the Windows client should connect to NXLog Agent. If [LogConnections](https://docs.nxlog.co/agent/current/im/#config-logconnections) is set to `TRUE` a connection attempt should be logged in `nxlog.log` and you should soon start seeing events arriving.

|  | The `Refresh` interval represents the time in seconds and on production systems should be set to a higher value (e.g. `Refresh=1200`). When the Windows client is set to reconnect too frequently it will result in a lot of connection/disconnection messages in `nxlog.log`. |
| --- | --- |

## Configuring WEF to use HTTPS

To set up Windows Event Forwarding over HTTPS the following steps are required:

- X509 certificate generation using either OpenSSL or the Windows certificate manager,
- configuration of the NXLog Agent *im\_wseventing* module,
- configuration of Windows Remote Management (WinRM) on each Windows client.

These steps are covered in greater detail below.

|  | We will refer to the host running NXLog Agent with the `im_wseventing` module as ***WEC server***. We will use the name ***WEF client*** when referring to the Windows hosts sending the logs using WEF. |
| --- | --- |

Certificate requirements:

- The WEF client certificate must have the `X509 v3 Extended Key Usage: TLS Web Client Authentication` extension.
- The WEC server certificate must have the `X509 v3 Extended Key Usage: TLS Web Server Authentication` extension.
- Make sure that the intended purpose of the certificates are set to `Client Authentication` and `Server Authentication` respectively.

|  | If these extended key usage attributes are not set you will likely encounter an error when trying to configure WEF and the connection to the server will fail. |
| --- | --- |

### Generating the certificates with OpenSSL

*To use the Windows certificate manager skip to the next section.*

To facilitate the generation of certificates using OpenSSL, the following scripts are available in our [public git repository](https://gitlab.com/nxlog-public/contrib/tree/master/windows-event-forwarding):

- `genca.sh` - generates the CA certificate and private key.
- `gencert-client.sh` - generates the WEF client certificate and exports it together with the CA in PFX format to be imported into the Windows certificate store.
- `gencert-server.sh` - generates the WEC server certificate to be used by the `im_wseventing` module.

Refer to the [readme file](https://gitlab.com/nxlog-public/contrib/-/blob/master/windows-event-forwarding/Readme.md) for instructions on the scripts.

|  | When generating the certificates please ensure that the CN in the WEC server certificate subject matches the reverse DNS name. Otherwise, you may get errors in the `Microsoft Windows/Event-ForwardingPlugin/Operational` event log saying `The SSL certificate contains a common name (CN) that does not match the hostname.` |
| --- | --- |

If you are using an intermediary CA please make sure that the `ca-cert.pem` file contains—in correct order—the public part of every issuer’s certificate. The easiest way to achieve this is to 'cat' the `pem` certificates together.

For more complex requirements follow on how to set up a CA and generate certificates with OpenSSL.

### Generating the certificates with the Windows certificate manager

For more information on creating certificates under Windows see this document: [Request Certificates by Using the Certificate Request Wizard](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc754490\(v=ws.11\)).

Make sure to create the certificates with the required extensions as noted above. Once you have issued the certificates you will need to export the WEC server certificate in PFX format. The PFX must contain the private key, the password may be omitted. The PFX file can then be converted to the PEM format required by *im\_wseventing* using `openssl`:

```console
openssl pkcs12 -in server.pfx -nocerts -nodes -out server-key.pem
openssl pkcs12 -in server.pfx -nokeys -nodes -out server-cert.pem
```

You will also need to export the CA certificate (without the private key) the same way and convert it into `ca-cert.pem`.

### Configure NXLog Agent with the im\_wseventing module

You will need to use `server-key.pem`, `server-cert.pem` and `ca-cert.pem` for the `HTTPSCertKeyFile`, `HTTPSCertFile` and `HTTPSCAFile` respectively.

Optionally you can use the [QueryXML](https://docs.nxlog.co/agent/current/im/#config-queryxml) option to filter on specific channels or events.

See the [configuration example](https://docs.nxlog.co/agent/current/im/#example-https) below for how your `nxlog.conf` should look.

Once the configuration is complete you may start the `nxlog` service.

### Configuring WinRM and WEF

Configure WinRM on the client for certificate-based authentication and enable Windows Event Forwarding. These steps can be automated for ease of deployment across multiple clients. See the [example PowerShell script](https://gitlab.com/nxlog-public/contrib/-/tree/master/windows-event-forwarding/wef-client-script) in our public git repository.

1. Install, configure, and enable Windows Remote Management (WinRM) on each WEF client.
	1. Make sure the Windows Remote Management (WS-Management) service is installed, running, and set to *Automatic* startup type.
	2. If WinRM is not already installed, see these instructions on MSDN:[Installation and Configuration for Windows Remote Management](https://learn.microsoft.com/en-us/windows/win32/winrm/installation-and-configuration-for-windows-remote-management).
2. Check that the proper client authentication method (Certificate) is enabled for WinRM. Issue the following command:
	```console
	winrm get winrm/config/Client/Auth
	```
	This should produce the following output:
	```console
	Auth
	 Basic = false
	 Digest = true
	 Kerberos = true
	 Negotiate = true
	 Certificate = true
	 CredSSP = true [Source="GPO"]
	```
	If Certificate authentication is set to *false*, it should be enabled with the following command:
	```console
	winrm set winrm/config/client/auth @{Certificate="true"}
	```
	|  | ```console winrm set winrm/config/client/auth @{Basic="false"} ``` |
	| --- | --- |
	1. Import the CA and WEF client certificates if you used OpenSSL to generate these.
		1. Open the Certificate MMC snap-in for the Local Computer (`certlm.msc`).
		2. Right click on **Trusted Root Certification Authorities** and select **All Tasks** > **Import…**. Import the `client.pfx` file. Enter the private key password if set and make sure the **Include all extended properties** check-box is selected.
		3. Repeat the previous step to import the certificate to the **Personal** certificate store.
			|  | After importing is complete, expand **Personal** > **Certificates** and double-click on the WEF client certificate to check if the full certificate chain is available and trusted. |
			| --- | --- |
	2. Grant the *NetworkService* account the proper permissions to access the WEF client certificate by using the [Windows HTTP Services Certificate Configuration Tool (WinHttpCertCfg.exe)](https://www.microsoft.com/en-us/download/details.aspx?id=19801) and check that the *NetworkService* account has access to the private key file of the client authentication certificate by running the following command:
		```console
		winhttpcertcfg -l -c LOCAL_MACHINE\my -s <certificate subject name>
		```
		Where `LOCAL\my` refers to the `Personal` certificate store of the `Local Computer` and `<certificate subject name>` is the `CN` value that was specified when creating the WEF client certificate. For example:
		```console
		winhttpcertcfg -l -c LOCAL_MACHINE\my -s winclient.example.com
		```
		If *NetworkService* is not listed in the output, grant it permissions by running the following command:
		```console
		winhttpcertcfg -g -c LOCAL_MACHINE\my -s <certificate subject name> -a NetworkService
		```
	3. In order to forward *Security* events, the `Network Service` account needs to be given access to the *Secuity* Event Log. Refer to the section on [Forwarding events from the Security log](https://docs.nxlog.co/agent/current/im/#forwarding-events-from-the-security-log).

Next, configure the policy on the WEF client to enable event forwarding. In this example, WEF is enabled on a single Windows node by editing the local policy of the server. To enable WEF on multiple nodes, a group policy on the domain should be configured.

1. Run the **Group Policy** MMC snap-in (`gpedit.msc`) and go to **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Event Forwarding**.
	1. Right-click the **Configure target Subscription Manager** setting and select **Properties**. Enable the setting, and under **Options** click the **Show** button to add a server address.
	2. Add at least one setting that specifies the NXLog Agent WEC server. The *SubscriptionManager* properties window contains a **Help** pane that describes the syntax for the setting. If you have used the `gencert-server.sh` script the subscription manager string should be in the following format:
		```console
		Server=HTTPS://<FQDN of im_wseventing>:<port>/wsman/,Refresh=<Refresh interval in seconds>, IssuerCA=<certificate authority certificate thumbprint>
		```
		An example would be as follows:
		```console
		Server=HTTPS://nxlogserver.example.com:5985/wsman/,Refresh=14400,IssuerCA=57F5048548A6A983C3A14DA80E0626E4A462FC04
		```
		To find the IssuerCA fingerprint, open Certificates MMC snap-in, expand **Local Computer** > **Personal** > **Certificates** and open the CA certificate. Copy the `Thumbprint` from the `Details` tab. Please make sure to eliminate spaces and the invisible non-breaking space that may be present before the first character of the thumbprint on Windows 2008.
	3. To find the IssuerCA fingerprint, open Certificates MMC snap-in, expand **Local Computer** > **Personal** > **Certificates** and open the CA certificate. Copy the `Thumbprint` from the `Details` tab. Please make sure to eliminate spaces and the invisible non-breaking space that may be present before the first character of the thumbprint on Windows 2008.
	4. After the *SubscriptionManager* setting has been added, ensure the policy is applied by running:
		```console
		gpupdate /force
		```
	5. At this point the WinRM service on the WEF client should connect to NXLog Agent. If [LogConnections](https://docs.nxlog.co/agent/current/im/#config-logconnections) is set to `TRUE` a connection attempt should be logged in `nxlog.log` and you should soon start seeing events arriving.

## Forwarding events from the Security log

In adherence to [C2-level Security](https://learn.microsoft.com/en-us/windows/win32/secauthz/c2-level-security), access to audit data of security-related events is limited to authorized administrators. WinRM runs as a network service and by default does not have access to the *Security* log, therefore it will not be able to forward *Security* events.

To give it access to the *Security* log on Windows 2008 and newer the `Network Service` account should be added to the `Event Log Readers` group.

To give it access on older versions of Windows:

1. Open Group Policy Editor by running `gpedit.msc`.
2. Go to **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Event Log Service** > **Security**.
3. Right click on the **Configure Log Access** and click on **Edit**
4. Enable the policy and under **Log Access** enter:
	```console
	O:BAG:SYD:(A;;0xf0005;;;SY)(A;;0x5;;;BA)(A;;0x1;;;S-1-5-32-573)(A;;0x1;;;NS)
	```
5. Run `gpupdate /force` to apply changes.

## Troubleshooting

WEF if not easy to configure and there may be many things that can go wrong. To troubleshoot WEF, check the Windows Event Log under the following channels:

- `Applications and Services Logs/Microsoft/Windows/Event-ForwardingPlugin`
- `Applications and Services Logs/Microsoft/Windows/Windows Remote Management`
- `Applications and Services Logs/Microsoft/Windows/CAPI2`

The `Operational` log for these channels is enabled by default. The `Analytic` and `Debug` logs may also prove useful and can be enabled from the Windows Event Viewer as follows:

1. From the menu click on **View** and select **Show Analytic and Debug Logs**.
2. Under each of these channels, click on the **Debug** log and in the **Actions** pane select **Enable Log**.
3. Repeat the previous step for the **Analytic** log when available.

Unfortunately the diagnostic messages in the Windows Event Log may not always be helpful and in some cases may even be missing. In such cases searching for the error code on the internet may point to more useful information. This section provides troubleshooting tips for commonly encountered issues.

### The SSL certificate name does not match the hostname

The WEF client fails to connect to the WEC server and the `Microsoft/Windows/Event-ForwardingPlugin/Operational` Event Log contains the following error:

```log
The SSL certificate contains a common name (CN) that does not match the hostname.
```

log

This error occurs when the CN in the WEC server certificate does not match the reverse DNS. Run `nslookup <server_ip>` on the client and verify that the correct name for the server is returned. You can use the `openssl` tool on the WEC server to verify that the subject CN matches the same name by using the following command:

```console
openssl x509 -in server-cert.pem -text -noout
```

If the FQDN and the reverse DNS of the WEC server are not properly set up, the WinRM service may fail to connect to the CRL URL to download the revocation list. In that case an error messages will be logged under `Applications and Services Logs/Microsoft/Windows/CAPI2` as follows:

```log
<Result value="80092013">The revocation function was unable to check
revocation because the revocation server was offline.</Result>
```

log

If a secure connection cannot be established between the WEF client and the WEC server, the `Microsoft/Windows/Event-ForwardingPlugin/Operational` Event Log may contain the following error:

```log
The forwarder is having a problem communicating with the subscription manager
at address https://nxlogserver.example.com:5985/wsman/.
Error code is <error_code> and the Error Message is <error_message>.
```

log

Note that the error message can sometimes be empty.

When using HTTPS, this event is logged with `Error code 2150858882` when a certificate matching the specified IssuerCA thumbprint is not found. Verify that the thumbprint specified does not have any invisible characters as explained in this [Microsoft support article](https://support.microsoft.com/en-us/topic/certificate-thumbprint-displayed-in-mmc-certificate-snap-in-has-extra-invisible-unicode-character-c9e58dcb-f39a-d0a1-f7fc-bcaaa6fe64e4). Additionally, check that the thumbprint specified is for the CA certificate and not the WEF client, and that it can be found under **Local Computer** > **Personal** in the Certificates MMC snap-in.

When using Kerberos, this event may be logged with `Error code 2150858999` and the following message:

```log
The WinRM client cannot process the request.
It cannot determine the content of the HTTP response from the destination computer.
```

log

This error can occur when authentication fails on the WEC server side and NXLog Agent responds with a `400 Bad Request`. In such case the NXLog Agent log file contains the following error:

```log
ERROR [im_wseventing|wsevents] GSS-API error gss_accept_sec_context - type: major code: 851968, msg: Unspecified GSS failure.  Minor code may provide more information
ERROR [im_wseventing|wsevents] GSS-API error gss_accept_sec_context - type: minor code: -1765328203, msg: Key table entry not found
ERROR [im_wseventing|wsevents] [im_wseventing.c:1898/im_wseventing_create_kerb_auth_response()] Internal error
```

log

Carefully revise the steps required to [Configure the WEF Client](https://docs.nxlog.co/agent/current/im/#configure-the-wef-client). In particular make sure that the hostname on the WEC server is resolved to the same hostname as specified in the keytab principal. Run `nslookup <server_ip>` on the WEC server and verify that the name returned is correct. For example if the principal in the keytab is specified as:

```console
http/linux.example.com@EXAMPLE.COM
```

Then the name returned by `nslookup` should be `linux.example.com`.

This error can also occur if the user that NXLog Agent is running under is not able to read the keytab file. Check the access permissions of `/etc/krb5.keytab` and verify that they allow at least `Read` access to the user. By default NXLog Agent runs with the `nxlog` user. If the keytab file was manually copied, the access permissions may have been changed.

### Configuring im\_wseventlog to log connections

By default the module does not log connection attempts which would otherwise be useful for troubleshooting purposes. This can be turned on with the [LogConnections](https://docs.nxlog.co/agent/current/im/#config-logconnections) directive. Note that the Windows Event Forwarding service may disconnect during the TLS handshake with the following message logged in `nxlog.log` when *LogConnections* is enabled. This is normal as long as there is another connection attempt right after the disconnection.

```log
INFO connection accepted from 10.2.0.161:49381
ERROR im_wseventing got disconnected during SSL handshake
INFO connection accepted from 10.2.0.161:49381
```

log

See the Microsoft documentation on [Windows Event Forwarding to a workgroup Collector Server](https://learn.microsoft.com/en-us/archive/blogs/thedutchguy/windows-event-forwarding-to-a-workgroup-collector-server) for further instructions and troubleshooting tips.

## Configuration

The *im\_wseventing* module accepts the following directives in addition to the [common module directives](https://docs.nxlog.co/agent/current/config/common-settings.html). The [Address](https://docs.nxlog.co/agent/current/im/#config-address) and [ListenAddr](https://docs.nxlog.co/agent/current/im/#config-listenaddr) directives are required.

### Required directives

The following directives are required for the module to start.

| `Address` | This mandatory directive accepts a URL address. This address is sent to the WEF client to notify it where the events should be sent. For example, `Address https://nxlogserver.example.com:5985/wsman`. |
| --- | --- |
| `ListenAddr` | This mandatory directive specifies the address of the interface where the module should listen for WEF client connections. Normally the *any* address `0.0.0.0` is used. |

### TLS/SSL directives

The following directives are for configuring secure data transfer via TLS/SSL.

| `HTTPSAllowUntrusted` | This boolean directive specifies that the remote connection should be allowed without certificate verification. If set to `TRUE` the remote will be able to connect with an unknown or self-signed certificate. The default value is `FALSE`: all HTTPS connections must present a trusted certificate. |
| --- | --- |
| `HTTPSCADir` | This specifies the path to a directory containing certificate authority (CA) certificates, which will be used to check the certificate of the remote HTTPS client. The certificate filenames in this directory must be in the OpenSSL hashed format. A remote’s self-signed certificate (which is not signed by a CA) can also be trusted by including a copy of the certificate in this directory. |
| `HTTPSCAFile` | This specifies the path of the certificate authority (CA) certificate, which will be used to check the certificate of the remote HTTPS client. To trust a self-signed certificate presented by the remote (which is not signed by a CA), provide that certificate instead. |
| `HTTPSCAThumbprint` | This optional directive, supported only on Windows, specifies the certificate thumbprint of the certificate authority (CA), which is used to look up the CA certificate from the Windows certificate store. The hexadecimal fingerprint string can be copied straight from Windows Certificate Manager (*certmgr.msc*), whitespaces are automatically removed. This directive and the [HTTPSCADir](https://docs.nxlog.co/agent/current/im/#config-httpscadir) and [HTTPSCAFile](https://docs.nxlog.co/agent/current/im/#config-httpscafile) directives are mutually exclusive. |
| `HTTPSCertFile` | This specifies the path of the certificate file to be used for the HTTPS handshake. |
| `HTTPSCertKeyFile` | This specifies the path of the certificate key file to be used for the HTTPS handshake. |
| `HTTPSCertThumbprint` | This optional directive specifies the thumbprint of the certificate that will be presented to the remote server during the HTTPS handshake. The hexadecimal fingerprint string can be copied from Windows Certificate Manager (*certmgr.msc*). Whitespaces are automatically removed. The certificate must be imported to the `Local Computer\Personal` certificate store in PFX format for NXLog Agent to find it. Run the following command to create a PFX file from the certificate and private key using OpenSSL:  ```console $ openssl pkcs12 -export -out server.pfx -inkey server.key -in server.pem ```  When the global directive [UseCNGCertificates](https://docs.nxlog.co/agent/current/config/global-settings.html#usecngcertificates) is set to `FALSE` the private key associated with the certificate must be exportable.  - If you generate the certificate request using Windows Certificate Manager, enable the **Make private key exportable** option from the certificate properties. - If you import the certificate with the Windows Certificate Import Wizard, make sure that the **Mark this key as exportable** option is enabled. - If you migrate the certificate and associated private key from one Windows machine to another, select **Yes, export the private key** when exporting from the source machine.  On the contrary, when the global directive [UseCNGCertificates](https://docs.nxlog.co/agent/current/config/global-settings.html#usecngcertificates) is set to `TRUE` the private key associated with the certificate does not have to be exportable. In cases like TPM modules, the private key is always nonexportable.  The usage of the directive is the same in all cases:  ```console HTTPSCertThumbprint    7c2cc5a5fb59d4f46082a510e74df17da95e2152 ```  This directive is only supported on Windows and is mutually exclusive with the [HTTPSCertFile](https://docs.nxlog.co/agent/current/im/#config-httpscertfile) and [HTTPSCertKeyFile](https://docs.nxlog.co/agent/current/im/#config-httpscertkeyfile) directives. |
| `HTTPSCRLDir` | This specifies the path to a directory containing certificate revocation lists (CRLs), which will be consulted when checking the certificate of the remote HTTPS client. The certificate filenames in this directory must be in the OpenSSL hashed format. |
| `HTTPSCRLFile` | This specifies the path of the certificate revocation list (CRL) which will be consulted when checking the certificate of the remote HTTPS client. |
| `HTTPSKeyPass` | With this directive, a password can be supplied for the certificate key file defined in [HTTPSCertKeyFile](https://docs.nxlog.co/agent/current/im/#config-httpscertkeyfile). This directive is not needed for passwordless private keys. |
| `HTTPSSSLCipher` | This optional directive can be used to set the permitted SSL cipher list, overriding the default. Use the format described in the [ciphers(1ssl)](https://www.openssl.org/docs/man1.1.1/man1/ciphers.html) man page. |
| `HTTPSSSLCiphersuites` | This optional directive can be used to set the permitted cipher list for TLSv1.3. Use the same format as in the [HTTPSSSLCipher](https://docs.nxlog.co/agent/current/im/#config-httpssslcipher) directive. Refer to the OpenSSL documentation for a list of valid [TLS v1.3 cipher suites](https://www.openssl.org/docs/man1.1.1/man1/ciphers.html#TLS-v1.3-cipher-suites). The default value is:  `TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256` |
| `HTTPSSSLCompression` | This boolean directive allows you to enable data compression when sending data over the network. The compression mechanism is based on the zlib compression library. If the directive is not specified, it defaults to `FALSE` (the compression is disabled).  \|  \| Some Linux packages (for example, Debian) use the OpenSSL library provided by the OS and may not support the zlib compression mechanism. The module will emit a warning on startup if the compression support is missing. The generic deb/rpm packages are bundled with a zlib-enabled libssl library. \| \| --- \| --- \| |
| `HTTPSSSLProtocol` | This directive can be used to set the allowed SSL/TLS protocol(s). It takes a comma-separated list of values which can be any of the following: `SSLv2`, `SSLv3`, `TLSv1`, `TLSv1.1`, `TLSv1.2` and `TLSv1.3`. By default, the `TLSv1.2` and `TLSv1.3` protocols are allowed. Note that the OpenSSL library shipped by Linux distributions may not support `SSLv2` and `SSLv3`, and these will not work even if enabled with this directive. |

### Optional directives

| `AddPrefix` | If this boolean directive is set to `TRUE`, names of fields parsedfrom the `<EventData>` portion of the event XML will be prefixed with `EventData.`. For example, `$EventData.SubjectUserName` will be added to the event record instead of `$SubjectUserName`. The same applies to `<UserData>`. This directive defaults to `FALSE`: field names will not be prefixed. |
| --- | --- |
| `CaptureEventXML` | This boolean directive defines whether the module should store raw XML-formatted event data. If set to `TRUE`, the module stores raw XML data in the [$EventXML](https://docs.nxlog.co/agent/current/im/#eventxml) field. By default, the value is set to `FALSE`: the `$EventXML` field is not added to the event record. |
| `ConnectionRetry` | This optional directive specifies the reconnection interval. The default value is `PT60.0S` (60 seconds). |
| `ConnectionRetryTotal` | This optional directive specifies the maximum number of reconnection attempts. The default is 5 attempts. If the WEF client exceeds the retry count it will consider the subscription to be stale and will not attempt to reconnect. |
| `Expires` | This optional directive can be used to specify a duration after which the subscription will expire, or an absolute time when the subscription will expire. By default, the subscription will never expire. |
| `GssDllName` | This optional directive specifies the name of the GSSAPI provider DLL on Windows. It is not available on Linux. The default value is `gssapi64.dll`, which is compatible with [MIT Kerberos](https://web.mit.edu/kerberos/dist/). If the module logs a "Failed to load gssapi64.dll" error, it cannot find the DLL file.  To address this issue, you need to add two environmental variables. Append the DLL file path, for example, `C:\Program Files\MIT\Kerberos\bin\gssapi64.dll`, to the `PATH` system variable, then append the same for the user variables for the account NXLog Agent is running under (system). Once you have added both, reboot your computer. |
| `HeartBeats` | Heartbeats are dummy events that do not appear in the output. These are used by the WEF client to signal that logging is still functional if no events are generated during the specified time period. The default heartbeat value of `PT3600.000S` may be overridden with this optional directive. |
| `LogConnections` | This boolean directive can be used to turn on logging of connections. Since WEF connections can be quite frequent and excessive it could generate a lot of noise. On the other hand it can be useful to troubleshoot clients. This is disabled by default. |
| `MaxElements` | This optional directive specifies the maximum number of event records to be batched by the client. If this is not specified the default value is decided by the client. |
| `MaxEnvelopeSize` | This optional directive can be used to set a limit on the size of the allowed responses, in bytes. The default size is 153600 bytes. Event records exceeding this size will be dropped by the client and replaced by a drop notification. |
| `MaxTime` | This optional directive specifies the maximum amount of time allowed to elapse for the WEF client to batch events. The default value is `PT30.000S` (30 seconds). |
| `Port` | This specifies the port on which the module will listen for incoming connections. The default is port 5985. |
| `Query` | This directive specifies the query for pulling only specific Event Log sources. See the MSDN documentation about [Event Selection](http://msdn.microsoft.com/en-us/library/aa385231.aspx). Note that this directive requires a single-line parameter, so multi-line query XML should be specified using line continuation:  ```config Query    <QueryList>                                                 \              <Query Id='1'>                                          \                  <Select Path='Security'>*[System/Level=4]</Select>  \              </Query>                                                \          </QueryList> ```  config |
| `QueryXML` | This directive is the same as the [Query](https://docs.nxlog.co/agent/current/im/#config-query) directive above, except it can be used as a block. Multi-line XML queries can be used without line continuation, and the XML Query can be directly copied from Event Viewer.  \|  \| Commenting with the `#` mark does not work within multi-line Query directives or QueryXML blocks. In this case, use XML-style comments `<!--   -->` as shown in the example above. Failure to follow this syntax for comments within queries will render the module instance useless. Since NXLog Agent does not parse the content of QueryXML blocks, this behavior is expected. \| \| --- \| --- \| |
| `SubscriptionName` | The default value of `NXLog Subscription` may be overridden with this optional directive. This name will appear in the WEF client logs. |
| `MaxConnections` | With this optional directive it is possible to set the maximum number of allowed concurrent/active connections for a listening TCP socket. If not specified, the default value is `4294967295`, unlimited. When the limit is reached, the incoming connection will be rejected and an error message is shown in the selflog |
| `ConnectionIdleTimeout` | This optional directive defines the maximum time in seconds before NXLog Agent closes TCP connections without traffic. The minimum timeout value is 15 seconds. If this directive is not specified, NXLog Agent does not close idle TCP connections. |

## Fields

The following fields are used by *im\_wseventing*.

The actual fields generated will vary depending on the particular event’s source data.

`$raw_event` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

A string containing the [$EventID](https://docs.nxlog.co/agent/current/im/#eventid),[$EventType](https://docs.nxlog.co/agent/current/im/#eventtype),[$EventTime](https://docs.nxlog.co/agent/current/im/#eventtime),[$Hostname](https://docs.nxlog.co/agent/current/im/#hostname), and [$Message](https://docs.nxlog.co/agent/current/im/#message) from the event.

`$ActivityID` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

A globally unique identifier for the current activity.

`$Channel` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The Channel of the event source (for example, `Security` or `Application`).

`$EventData` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

Event-specific data. This field is mutually exclusive with [$UserData](https://docs.nxlog.co/agent/current/im/#userdata).

`$EventID` (type: [integer](https://docs.nxlog.co/agent/current/language/types.html#type-integer))

The event ID specific to the event source.

`$EventTime` (type: [datetime](https://docs.nxlog.co/agent/current/language/types.html#type-datetime))

The timestamp that indicates when the event was logged.

`$EventType` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The type of the event, which is a string describing the severity. This is translated to its string representation. Possible values are:`CRITICAL`, `ERROR`, `AUDIT_FAILURE`, `AUDIT_SUCCESS`, `INFO`,`WARNING`, and `VERBOSE`.

`$EventXML` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The raw event data in XML format. This field is available if the module’s [CaptureEventXML](https://docs.nxlog.co/agent/current/im/#config-captureeventxml) directive is set to TRUE.

`$ExecutionProcessID` (type: [integer](https://docs.nxlog.co/agent/current/language/types.html#type-integer))

The ID identifying the process that generated the event.

`$ExecutionThreadID` (type: [integer](https://docs.nxlog.co/agent/current/language/types.html#type-integer))

The ID identifying the thread that generated the event.

`$Hostname` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The name of the computer that generated the event.

`$Keywords` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The keywords used to classify the event, as a hexadecimal number.

`$Level` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The level of the event as a string, resolved from [$LevelValue](https://docs.nxlog.co/agent/current/im/#levelvalue). Possible values include: `Success`, `Information`, `Warning`, `Error`, `Audit Success`, and `Audit Failure`.

`$LevelValue` (type: [integer](https://docs.nxlog.co/agent/current/language/types.html#type-integer))

The level of the event.

`$Message` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The message from the event.

`$MessageID` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The unique identifier of the message.

`$Opcode` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The Opcode string resolved from OpcodeValue.

`$OpcodeValue` (type: [integer](https://docs.nxlog.co/agent/current/language/types.html#type-integer))

The Opcode number of the event as in EvtSystemOpcode.

`$param1` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

Additional event-specific data (`$param1`, `$param2`, and so on).

`$ProviderGuid` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The globally unique identifier of the event’s provider. This corresponds to the name of the provider in the [$SourceName](https://docs.nxlog.co/agent/current/im/#sourcename) field.

`$RecordNumber` (type: [integer](https://docs.nxlog.co/agent/current/language/types.html#type-integer))

The number of the event record.

`$Severity` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The normalized severity name of the event. See [$SeverityValue](https://docs.nxlog.co/agent/current/im/#severityvalue).

`$SeverityValue` (type: [integer](https://docs.nxlog.co/agent/current/language/types.html#type-integer))

The normalized severity number of the event, mapped as follows.

| Event Log Severity | Normalized Severity |
| --- | --- |
| 0/Audit Success | 2/INFO |
| 0/Audit Failure | 4/ERROR |
| 1/Critical | 5/CRITICAL |
| 2/Error | 4/ERROR |
| 3/Warning | 3/WARNING |
| 4/Information | 2/INFO |
| 5/Verbose | 1/DEBUG |

`$SourceName` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The event source which produced the event.

`$Task` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The task defined in the event.

`$UserData` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

Event-specific data. This field is mutually exclusive with [$EventData](https://docs.nxlog.co/agent/current/im/#eventdata).

`$UserID` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The Security Identifier (SID) of the account associated with the event.

`$Version` (type: [integer](https://docs.nxlog.co/agent/current/language/types.html#type-integer))

The version number of the event.

## Examples

|  | Due to a limitation in the Windows Event Log API, queries with more than 22 clauses will fail, producing the following error message:  The workaround for this limitation is grouping clauses and/or splitting the filter across multiple queries. In the example below, the filter consists of 6 EventIDs; however, these count as 2 in terms of the aforementioned limitation.  Combining clauses in groups  ```xml <QueryXML>     <QueryList>         <Query Id="0">             <Select Path="Security">*[System[(EventID=6416 or EventID=6424 or EventID=4732) or (EventID=1102 or EventID=4719 or EventID=4704)]]             </Select>         </Query>     </QueryList> </QueryXML> ```  xml |
| --- | --- |

Example 1. Collecting logs from WEF clients with Kerberos authentication on Linux

This configuration enables a WEC server on Linux. It will listen for logs on port 80 and use Kerberos authentication. See [Configure Kerberos on Linux](https://docs.nxlog.co/agent/current/im/#configure-kerberos-on-linux) above for more information.

nxlog.conf

```config
<Input wseventing>
    Module              im_wseventing
    Address             http://LINUX.EXAMPLE.COM:80/wsman
    ListenAddr          0.0.0.0
    Port                80
    SubscriptionName    test
    <QueryXML>
        <QueryList>
            <Query Id="0">
                <Select Path="Application">*</Select>
                <Select Path="Security">*</Select>
                <Select Path="Setup">*</Select>
                <Select Path="System">*</Select>
                <Select Path="ForwardedEvents">*</Select>
                <Select Path="Windows PowerShell">*</Select>
            </Query>
        </QueryList>
    </QueryXML>
</Input>
```

config

Example 2. Collecting logs from WEF clients with Kerberos authentication on Windows

This configuration enables a WEC server on Windows. It will listen for logs on port 80 and use Kerberos authentication. The two [setenv](https://docs.nxlog.co/agent/current/config/general-settings.html#setenv) global directives are required on Windows to specify the Kerberos keytab path and disable the replay cache. See [Configure Kerberos on Windows](https://docs.nxlog.co/agent/current/im/#configure-kerberos-on-windows) above for more information.

```config
setenv KRB5_KTNAME=%INSTALLDIR%/krb5.keytab
setenv KRB5RCACHETYPE=none

<Input wseventing>
    Module              im_wseventing
    Address             http://wecserver.EXAMPLE.COM:8080/wsman
    ListenAddr          0.0.0.0
    Port                8080
    <QueryXML>
        <QueryList>
            <Query Id="0">
                <Select Path="Application">*</Select>
                <Select Path="Security">*</Select>
                <Select Path="System">*</Select>
            </Query>
        </QueryList>
    </QueryXML>
</Input>
```

config

Example 3. Collecting logs from WEF clients over HTTPS

This configuration receives Windows logs over HTTPS. Two queries are specified, the first for hostnames matching `foo*` and the second for all other hostnames.

nxlog.conf

```config
<Input wseventing>
    Module              im_wseventing
    ListenAddr          0.0.0.0
    Port                5985
    Address             https://linux.example.com:5985/wsman
    HTTPSCertFile       %CERTDIR%/server-cert.pem
    HTTPSCertKeyFile    %CERTDIR%/server-key.pem
    HTTPSCAFile         %CERTDIR%/ca.pem
    <QueryXML>
        <QueryList>
            <Computer>foo*</Computer>
            <Query Id="0" Path="Application">
                <Select Path="Application">*</Select>
            </Query>
        </QueryList>
    </QueryXML>
    <QueryXML>
      <QueryList>
        <Query Id="0" Path="Application">
          <Select Path="Application">*</Select>
          <Select Path="Microsoft-Windows-Winsock-AFD/Operational">*</Select>
          <Select Path="Microsoft-Windows-Wired-AutoConfig/Operational">*</Select>
          <Select Path="Microsoft-Windows-Wordpad/Admin">*</Select>
          <Select Path="Windows PowerShell">*</Select>
        </Query>
      </QueryList>
    </QueryXML>
</Input>
```

config