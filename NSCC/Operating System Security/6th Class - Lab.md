



## User Accounts



#### System Accounts


They tend to run the services in the background. Sometimes it is created automatically.


All the services are being run by a user, which is the **System Account**.


On *Task Manager*, we can select the *Services* tab. We see a lot of local system , local service , etc.


Sometimes when installing an application, it is a good idea to give it a system user name. It is due to a regular user's account needing to update the password every so often. 

Sometimes it is a good idea to use the system account when dealing with networking tasks, and services. 

It is still a good idea to pick a good password for the system account. The OS uses system accounts to check if the process is allowed to run. An example is "Windows Remote Management", where a local system account would not work.  Sometimes you see a System Administrator account. Database server's service is running from a system account as well. 


You would not set a password for a System account, but usually a password for it is already set. 


#### Superuser Account


The Windows equivalent of a *root* account on Linux


It is quite dangerous if it is not managed properly. 


He mentioned that in the early days of WIFI, his neighbour had installed an open WIFI network, so he managed to log in and access the router's administration page. Most people do not change the default credentials for their networking equipment. 


The **Suepruser Account** has the highest privilege on the operating system.


#### Regular User Account


The **Regular User Account** is an account that has moderate privilege. The *Regular User Account* is not allowed to make changes to the system files and properties. 


The **Regular User Account** can only make changes to the Regular User's environment. 

We can add new users if we are the **Superuser** or **Administrator**, as well as controlling options involving whether the **Regular User** can change the password. 


There are also another group of users called **Power Users' Group**, where they can install applications. 


There are also **Remote Users' Group**. 


**Regular User Account** is limited in terms of rights. 



#### Guest User Account


A built-in account for user access. The user can not change the password, description etc. Guest has the same access as a local user. If the Guest account is enabled, the guest account would not have a password. For auditing, we would not be able to specifically know who did what in a guest account. 


If we have 12 different users, groups can be used to change settings for all the users. It would be easier than changing permissions for each individual account. 


There is a hierarchy in terms of how it is done. IF he is a member of seven groups, and one groups allows access while the other groups restrict access, then the restrictions trump the permission. 


Group accounts are used to manage user accounts. There is no password for Guests. You can belong to as many groups as you want. 


Sometimes we get an **Orphaned Account**, where it is an account that lost its username. Every account has an identifier, which is a unique ID that helps in identifying people. You do not refer to the user by the unique ID, but sometimes you can use the unique ID. 



#### Remote Service Account


Usernames and passwords for **Remote Service Accounts** are stored on remote systems. These accounts are used to access a service or program on a remote server. 



#### Anonymous User Account


The account needs no password. It has the lowest privileges. 



## Windows Access Control function



The **User Access Control(UAC)** function noptifies you before making changes. The changes that trigger it are : 



Install/Uninstall applications
Changing firewall settings
Installing drivers and ActiveX controls
Installing/Configuring Windows updates
Adding/Removing/Changing user accounts and account types
Accessing another user's files and folders
Changing parental controls
Running the Task Scheduler
Restoring Backyp system files
Changing the **User Access Control(UAC)** function. 



#### Administrative Group Mishaps : 

	If we are to make changes to User Access Control Options, we would need administrative rights. What he saw people do is to take a Network Group (EVERYONE group within the network) and add it to their local ADMIN group, which allows everyone in this group to make changes, which is a hugely risky endeavour. The group policy change would give a regular user administrative rights across the organization's entire network. An insider job would be disasterous to the company. It is not a good idea to give someone administrative rights just to make life easier for the IT personnel.


It is a good idea to consider the impacts of a change in options pertaining to the users' permissions. In case of a breach, an administrator can log everyone out remotely, and force everyone to change their passwords on their next login. 



##### Note :


When logging in to a system, the system will default to letting a member of the domain sign in.