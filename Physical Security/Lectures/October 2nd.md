#### Enable Local Admin Account on our Lab Machine

Open all the TCP ports in the firewall ( start with this)


Go to local firewall, create an Inbound Rule for all TCP ports :

from [ ..... ]

The machine we are targeting (our own local machine), we have to turn UAC to **Zero**. 


If we type UAC in the run window


UAC comes up when you try to do something such as a restricted activity, and it is the user authentication control (UAC) (move the slider to **zero**)

If you do so remotely, we would not get the message.


>[!howto]
>
>Win + R
>Type the following :
"Lusrmgr.msc" --> Local User Manager. msc (console)
This brings up the list of users
Select Administrator
Select Edit 
General Tab -- > Uncheck Account is **Disabled**

Enable local administrator Account (Administrator)
Turn UAC to Zero
Go to the Firewall
Open all TCP ports

Run Un-Credentialed Scan through loopback
We will try :
1. Because of our inability to turn off the Firewall, Phil will try to open all the TCP ports on the remote lab machine and see if it works for the scan --> if that works, open all the TCP ports on the local lab machine.
2. Few days ago, the machine was swapped, and it was tested on the other machine.


Ron had alot of experience with Network Administrators not being happy with enabling the Local Administrator account. We are trying to get the highest level of privileges. We are looking for an Administrator account with the ability to turn off the firewall. This is necessary for proving vulnerabilities. It is like trying to find hazardous materials in the building, and someone is upset about you being inside the building. 



When doing a Vulnerability Audit, what should you do with it ?

 1. You secure it
 2. You Destroy 
 3. You Give it Back to the Customer
 4. You do what the customer asks! X



We can do the remote scan against the other machine in the pod, but you need to create a new inbound rule allowing all the connections on the remote machine. 




If interested, we will have one more class for the vulnerability scan on Monday (where we can complete the scan) and it will include a review class on Chapter 2. The following Wednesday, we will have a quiz on Chapter 2, and the things mentioned in Class. 


The next section we will be doing is **Electronic Elements** on *Chapter 6*. We will have two sessions with Pods (with Arduino), and we will build sensors. 


Quiz --> October 9th (Wednesday)



We are doing reports on two machines : 

1. Local Machine
2. Remote Machine


If we want to go ahead and run a scan after that to scan the rest of the machines, we can!

James IP Address : 172.16.139.99  .
My Machine : 172.16.139.174 --> . \ Administrator 123456


Every month, Microsoft releases an update for Microsoft Office. It is possible (when getting an error) :

1. They have not updated it in the past couple of months
2. When building the image for the computer we work on, it is possible that the Microsoft Office installed to the image had previous credentials ( or them not running monthly checks)


If we go to BestBuy and we buy a pc with Windows and Microsoft Office, you could sign up for Office 365, and have two versions of MS Office on your machine. 