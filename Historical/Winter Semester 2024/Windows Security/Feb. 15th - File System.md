



## The **NTFS** File System


## Permissions 


>Each file and folder has its own discretionary access control list (DACL) of who (i.e., user or group) can do what to the file system object. Permissions include configurable inheritance through the folder structure. Permissions can be basic or advanced using allow or deny assignments. Ownership of a file system object is tracked and always allows access to file system objects owned by that user or group.


## Auditing 


>Each file and folder can have its own custom system access control list (SACL) to define who is audited in the Security event log when they succeed or fail at accessing a file system object.



## Compression


>Files can optionally have their contents compressed.




## Encrypting File System (**EFS**)


>Files can optionally have their contents encrypted. Encrypted files will have *Certificates* when the encryption is done. The Windows Environment will save the **Encryption Certificate**, which will be needed to *decrypt* the files. 


>[!hint]
>
> It is a good idea to create a *backup*  of the **Encryption Certificates**!


>[!danger]
>
>**BitLocker** :
>
>According to Marie, if you lose the *Decryption Key*, you would lose access to your files! 
>


>[!note]
>
A reboot fix a lot of issues with Windows because a lot of the issues come from the *User's Side*. Linux and MacOS function at the **Kernel Level**. Drivers are *tied to the Kernel*. Linux is constantly updating because they can push put an update. Macs change their kernel instead of frequent updates. The only program that functions differently on Windows is **IIS**. This is called a *listener* , and **IIS** stands for *Internet Services*. The reason being Microsoft owns Windows, so everyone else owns everything else. Everything else (hardware, drivers, software) are owned by third-party companies. These run at the surface level. 

## Disk Quotas 


>Optionally track how much data is used on the file system by a user and potentially apply
storage limits.  It is the ability to keep track of **Disk Usage**. If we have an average employee who is given 10 GBs of storage, and they suddenly have exceeded their quota, then it would raise alarm bells , due to the possibility of an outside entity using the employee's system.  



## Automatic Bad Cluster Management



>Back in the day, it was common to *de-fragment* the hard drive. If on the last segment, it will use the bytes that it needs, and leave the rest empty. It leaves a database table where it indicates where the space starts, and where it ends. Defragmentation organizes the data, and places information at the beginning of the disk. It keeps that table up to date.  


>[!note]
>
>You can still *de-fragment* the disk!


Windows now has **Automatic Bad Cluster Management**, which takes care of fragmentation, and is adapted to the changes in drives, such as SSDs.


>[!note]
>
>*Nothing* is really deleted when you delete the file. It takes the content off the storage table, but it does not delete the data. If you really would like to delete it, you can re-write over it!


![[Pasted image 20240215085310.png]]


## Drive Letters 



>Drives get the *First-Available* **Drive Letters**. **A** and **B** were used for *Floppy Disks*, so with *A* being for the **Operating System**, and *B* for the **Programs**. 


>When installing Windows, usually the *Windows Drive* is given the letter **C**


>[!question]
>
What happens if you dual-boot Linux and Windows ? 
>
>	Instinctively, since the first available drive is available, the OS drive gets the C drive. The second OS gets the Next-Available Drive Letter or Any Drive Letter that you want. 
>


#### Drive Mapping


>When you map a drive, *You Choose the Drive Letter*! If you map a drive, you can give it any drive letter that you wish. If the physical drive is H, the mapped drive is P.  

H-Drive will have a folder called *Folder1*. She would have another folder called *Folder2*. These both sit on the Data Drive (H). She would like people to access these folders, so she maps a path to these folders. She will map to Folder1, where the drive letter P, and the drive letter F for Folder2. She can map any drive she wants to a physical location. 



When looking at a *log* or an *event* where you need to identify the location, it could identify by *Physical Location* or *Mapped Location*. Drive letter can be a logical location. 


>[!note]
>
>You can use the **Drive Letter** *only once*!


>[!hint]
>
>**Clustering** is useful in the sense of adding a number of drives *together as one drive*!
>




# Attributes 



## Basic Attributes


They existed for a while!


We can set it to : 


1. Read-Only : Reading ability only 
2. Hidden 
   
   
   Later came ...


## Advanced Attributes 


They appeared when Windows 7 was released


It involves *Encryption, Archiving*




>[!note]
>
>If we have any type of backup scenario, the file needs to be *archived*. This is a file that we do not need to have distributed during backups. 




>[!note]
>
>**Indexing** involves having a record for *where the file is*, or other *criterias*. The issue with **indexing** is the *reduction of performance*. It is recommended to use it when searching for files. You can index files in a compressed folder, and not index files used on a regular basis. 
>





# File Copying




>[!note]
>
>- A *Copied File* receives **new attributes** in the *NTFS* File System based on the **attributes of the target folder**. 
>
>
>- A *Moved File* receives **new attributes** if *moved to a different NTFS File System* , in which the attributes for the new drive would be inherited if more permissive. If the file is moved within the *same NTFS File System* , then **the attributes DO NOT change!


You can use these two realities strategically, as you would aim to move a file to a folder or NTFS drive with *more-permissive attributes*. 





# Access Control List (**ACL**)


#### Definition :
>
>
>	It is a Collection of Access Control Entries, where they identify who is able to do
>	 what to a file or a folder.





# Access Control Entry ( **ACE**)


#### Definition :
>
>
>	Identifies a entity being able to do something to a file or a folder







# Permissions 



## Default Permissions 



Every file or folder come with *default permissions*!





>[!note]
>
>#### **ROOT** Folder Permissions :
>
>Members of the **Administrators** Group have **Full-Control**!
>
>Members of the **Users** Group can **Read** and **Execute** programs!
>
>**Authenticated Users** can **Create Folders** there!
>
>**Authenticated Users** can **Create Files** and **Write Data** in *Sub-Folders* only!



>[!Note]
>
>#### **ROOT Sub-Folders'** Folder Permissions :
>
Members of the **Administrators** Group have **Full-Control**!
>
Members of the **Users** Group can **Read** and **Execute** programs!
>
**Authenticated Users** can **Create  Files and Sub-Folders**, **Modify Files and Sub-Folders**, and **Delete Files and Sub-Folders** there!
>




## NTFS Permissions 


Collection of predetermined advanced NTFS permissions



>[!note]
>
>## **NTFS Permissions :**
>
>**Write** , **Read**  and **List Folder Contents** 
>
>#### Description:
>
>###### Write : 
>
>This permission used for folders allows new files and folders to be created in the current
folder. The folder attributes can be changed and the folder's ownership and security can be
viewed. This permission used for files allows file data to be rewritten. The file's attributes can be changed and the file's ownership and security can be viewed.
>
>###### Read :
>
>This permission used for folders allows files and folder data, attributes, ownership, and
security to be viewed. This permission used for files allows the file's data, attributes,
ownership, and security to be viewed.
>
>###### List Folder Contents :
>
>This permission applies only to folders. Without this permission, the files and folders
contained in a folder cannot be listed. The user or application can still access the files if they have permission and know the exact file or folder name.
>
>###### Read and Execute :
>
>This permission used for folders allows read access to files and folders below this point. This is the equivalent of enabling Read and List folder contents. This permission used for files allows read access to the file's information and, if it is an executable file, the user is allowed to run it. This permission automatically includes the Read permission.
>
>###### Modify :
>
>This permission used for folders allows the same actions as Write and Read & execute permissions combined. The folder can also be deleted. This permission used for files allows the same actions as Write and Read & Execute permissions combined. Files can also be deleted.
>
>###### Full-Control :
>
>This  permission for **Folders** would be the same as *Modify* with the added bonus of **Changing Permissions** and allow a user to **take ownership of the folder**. This permission used for **files** allows the same actions as *Modify* plus the ability to **change permissions** and allow a user to **take ownership of the file**.
>
>###### Special Permissions :
>
>This is a type of permission can be assigned when the **pre-defined basic permissions are *not adequate* to achieve desired results**.


>[!todo]
>
>
>Research **NTFS' Birth**!
>


>[!note]
>
In Active Directory, in order to *authenticate to the domain*, you need **access to get to your object**, which involves being able to reach the file/folder.


>[!note]
>
Read and  Execute permissions need the List permission as well!



