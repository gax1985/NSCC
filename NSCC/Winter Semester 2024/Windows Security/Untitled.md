




We have **Folder1**, and we would like for the staff to be able to *do everything* : 


Write to modify : Write read list etc


And we have **Casual Staff**, and we just need them to read the documents : 


Read and Execute (execute includes *read* and *list*, as it needs to look at the files and list them.


Anything put inside **Folder1** *automatically inherits* the permissions of the *Folder* or the *File Above it*. Everyone *inherits* these permissions



Inside **Folder1**, there are *Confidential Documents*, and we need the regular staff to be able to look at them , but *not the casual staff* : 


There is a folder named *Confidential*, which the regulars would have permissions from read to modify. For Casuals, how do we change it? you break inheritance! This is where it gets tricky : 

>1. The minute we **break the link**, *we end the inheritance*. 
>2. The folder has zero permissions now!
>3. Make sure all the backend people (admins , owner etc ) to continue to have permissions
>4. You convert all the permissions to EXPLICIT, where the permissions are assigned by the administrator/owner. 
>5. We want to make sure Casuals do not have the permissions. We would have removed them, and they are given READ and LIST
>6. We broke inheritance, converted permissions to explicit, given read and list to the intended users, and we now need to turn Inheritance BACK ON! The reason being the files being created inside the folder


We can add permissions while inheritance is enabled, but we can not remove permissions if inheritance is enabled. 


One of the things Microsoft kept from the DOS 16-BIT days is a horrible option called **Block**, which allows us to check a box to *Block Permissions*! We can let the casuals have read and execute, and then we can *block each of these permissions* from them. 


The issue is **Blocks are not *inherited***! 

Anyone using it would be using it for a *temporary purpose*. We would first break inheritance. 


**Blocks** do not *appear in reports*! 


In most companies, you would have a staff member ()marketing for example ) and there is a new job open for two years and they would work in the HR department. This persons gets added to **HR GROUPS**. The person gets new permissions according to the new group. When their work term in HR ends, it is often done that they are never taken out from the marketing team. They would have full permissions in marketing, and permissions in a group they do not belong to anymore. If this employee sees something in HR that they are not meant to, the security admins get in trouble for not detecting it. Automation and frequent permissions reports are essential. 



## Policies

>[!note]
>
>A Policy is as good as *how well it is written*, and *how well it is implemented*!
>


 A lot of people do not know that these policies exist! 



### Confidentiality



What happens when you have to write a report on your colleagues? 

What happens if the employee knows that the report is written about them ? 



Biggest issue is **NTFS Permissions**. 




# Shared Permissions



Assigned directly to Files and Folders. 



### Share


Anything we need to access from outside of the basic network, whether from a different VLAN, different Subnet, Offsite etc...


#### Share Permissions


They function differently than NTFS permissions. 


It is a very common thing to add a $ sign to the Share Name. It is an industry standard to put it in front of the name, indicating it is a System file, so it wont show up, or place it at the end, which means it is shared, and that the user is looking at the share not the NTFS. 


We have Read Write List , Read , Read/Execute modify and full


Share : Full, read , change


##### Full

We have everything! 



###### REEAD 


Read List and Execute



If the staff has WRITE/MODIFY and the casuals have READ< and we would like to share it...


Share Folder 1 

Give the staff FULL SHARE PERMISSIONS. Why give them full ? The share permissions work differently than NTFS. Change allows anything read-modify. What happens is we end up with EFFECTVIE PERMISSIONS< which looks at NTFS, looks at the SHARE, applies POLICY OF LEAST PRIVILAGE, and whatever is left becomes the actual permissions. If staff have full share (write to modify), and the casuals have read and executre, the leftover permuissions are READ AND EXECUTE. 


When someone is working offsite or off network, they should not be able to make changes to those envirtonments, instead of giving everyone full, we give them read. When looking at these permissions , the leftovewr is READ permissions, and that is what they get. 


>[!todo]
>
>Read about **Effective Permissions**



Give the Casuals READ Permissions to the share



Most people have **HOME DIRECTORY**, due to Office365, Your Home Directory is *Cloud-based Storage*, due to the organization keeping sensitive information offline from the cloud


## Home Directory 


We have a folder, and inside this folder, meveryone in the com,pany would gha e their own folder. 


Staff1 , Staff2, Staff3, ...


Home directories themselves are set up by the server, and because it creates it as a home directory, it automatically gives the required permissions. What they do is give Staff1 Full NTFS permissions, Staff2 would have FULL, and noone else aside from the DFomain Admin or trhe SERVER would not be able to access a private file. The HOME Folder should have its access managed. The standard is to go back in to change other folders' permissions, and we would break inheritance, and we would break the default full permissions to the appropriate permissions. 



We would change where the documents sit. We can prevent storing data on the local machine instead of the cloud. 


We have REDIRECTION, where we redirect the items to their *Home Folder* in order to have proper security in place. It could also sync across to their laptop, or prevent access off-site, where they owuld have to connect to the network or store it offline. 


How would you accomplish this ? 



The worst thing you can do is storing things on the Desktop. It is the easiest folder to reach. 



## Class Exercise



1. We will open Active Directory USers and Computers 
2. New OU called "Practice"
3. Leave  "Protect Container from Accidental Deletion" on 
4. Now we have an OU called Practice 
5. Inside the Practice OU, create a NEW GROUP called PRACTICE_GP
6. We will accept the defaults. This is a GLobal Security Group. We only have Distro Groups when we have a mail system.
7. Create a new user with first name "Practice" and the last name "User"
8. We need a User Login name. Give them a login name "puser"
9. It automatically fills in NETBIOS name
10. We will give them a password. "Passw0rd"
11. Set it to "Never Expire". We are likely to use this user again. 
12. Lets add the user to our group. Properites == Members -- Add Puser 
13. Now puser is a member of practice_gp group
14. Open File Explorer 
15. Created a new Folder"  PracticeCompany" 
16. Go To Properies
17. Select Security 
18. In the Security Tab , System has full control.. Admin has full control, and the users for the netowrk have read and execute ( which include list and read by default). We see Special Permissions, select Advanced, and we would see more information. We see that the administrator has full control to this folder only and they have not inherited the permission from anyone. She saw that because she logged into the system as the Administrator, which makes her the creator and the owner of the folder, which she has full control. She saw she inherited fuyll control from the drive itself. She sees System inheriting permissions from the H drive. Creator/Owner inherited permissions from the drive itself. She is not sure about the special permissions, and some of them have full inheritance over the folder, subfolder and all the files. If we are not sure about them , we can click on Affective Permissions, or under Permissions select User select View , and she would see more permissions. Admin is allowed permissions to this folder only. In Advanced permissions ,we would see permissions we did not talk about. 
19. We have Traverse and List : Traverse allows movement across folders without seeing what they are moving through , and list allows you to see the files. 
20.  Grey Permissions are Implicit/Inherited Permissions 
21. Open PracticeCompany, create a new folder called Folder1
22. Create another folder called Folder2
23. Inside folder1, create a folder called Folder1A
24. Let us go back up one level 
25. Go to Folder1's Properties --> Security
26. We see all the default permissions being greyed out, which means they followed her over. 
27. She would like to add the group by selecting Edit --> add to the users the practice_gp group
28. Give the practice group the default permissions : read/list/execute, they cannot add or delete anything from the folder. 
29. If you click on Practice, the practice group's permissions are Black and not grey. it means they are explicit, which means she can change them as she pleases. They are not inherited from anywhere. 
30. Go to Folder1, and select folder1A 000?> properties >? security ? practice group's permissions are grey
31. If we go to Advanced, we see the group inherited the permissions from Practice Company's 1 , where she added them and assigned permissions. 
32. She can at this level, even though they are inherited. Select Practice group, and see tthat some permissions are blocked and some are not. We can add permissions, but not take away their inheritance. 
33. Modify is the top level not including full control. Apply Modify 
34. Now we see Modify is black on this level 
35. It does not say modify and write, it only gives the highest level of permissions. It applies to this folder subfolder and files. Inheritance carries on below. 
36. It has read and execute, which are inherited from PracticeCompanyFolder1. 
37. Let us go back to Practice Company .  


>[!note]
>
>Make sure to *re-enable Inheritane for the subfolder* ,and then to **Convert Permissions to Explicit**.


Select Advanced Sharing. We see we have some additional abilities. Select "Share the Folder", by default, it will pick the name. Make sure you recognize we add a $ sign at the end of the name to let the user know that this is a share. 


If you have a high-security server, you can make the wallpaper red or orange, and if someone is in a place where they should not be, they will be apparent. 


"Limit Number of signed in users" : number of users are limited to 20 if a personal computer , but on a corporate network, a large number is selected . 


If you have a share/folder, it is likely shared for a reason. It is a good idea in the comments to say "This is this person's share"

It is good to place things like creation date and a contact name. 


Use the comment fields to give yourself information. 


Go to Permissions. Everyone has "Read" permissions to a share. Everyone means authenticated and non-authenticated users (anyone who can access the network). Since this is a terrible idea, we we would give admin full rights, and add the practice_gp full control rights. Add the Domain_admins group and give them full control. Why is it ok to give the practice_gp full control? it will give them full NTFS permissions. she will next take the everyone group out.

- Best thing when setting up a printer is to **Not Give it a Gateway**!


Click on File and Storage Services,  Click on Shares. Automatically see sees informaiton about her shares. Some we will see such as NETLOGON and SYSVOL are created on every network that is accessible BEFORE authenticating to the network . Why? Keys, certificates, Startup scripts etc..


Within SYSVOL, we have secured areas available after authenticating. We have access to view all her shares. There is a folder to a share, we see informaiton about the share, see the contents of the share, see the description , see who has what permissions to that share, we can see if there is any special setting on that share. We would have access to see all the managed pieces. We will be looking at and creating scripts to view share information. 


	She opened file explorer, H drive, PracticeCompany, we did not discuss attributes. Open Folder2, Properties, in Properties select General , advanced , by default allow this folder to have contents indexed. We see "Compress contents to save disk space" and "index content". When it comes to indexing, they would store some words stored in the file index, and it would not save generic words like "and, but, for , etc". 


Right Click , Propeties, Select Compress (Compressed folders are not the same as zipping a file). We would see a little icon on the top part of the folder where it would indicate it is compressing. Anything placed inside this folder is automatically compressed. 


Go to Properties --> Advanced >> Encrypt .  Complete the encryption. It showed her it is encrypted for the user who encrypted it. This is the certificate that is created when the process is done. It should show a little lock icon on the folder to show when it is encrypted. The certificate is stored by default in the Certificates. We can go to Certificates, makes an export, place it in another folder so the certificate does not get encrypted.



DO NOT USE DENY. BREAK INHERITANCE


icackles is an old DOS command for running reports. 


Chnage is the same as MODIFY/WRITE . Change or Modify is the same thing . Pick the Equivalent






