


## Hints on Assignment 2 


#### The portion with the registry’s screenshot : 

export the registry file. She just wants the first 10 lines and the last 10 times. In terms of the wuaauservBK file, the file should not be too big. We are not exportingthe whole registry, we are exporting the last wuau sub key. It is only the stuff on the right and a few information things. Go back to LOCALMACHINE – SYSTREM – CurrentControlServices – wuaauserv-right click – export the file – go back and look at the file itself, you will see it is a short bit. Make sure to select the subkey ONLY. When exporting , we will see the core items. Ends in “Required privileges and HEX”. Everything that we need to restore is there. Double-check the path indicated in the file. She got 82 lines of code under that key. 


#### Explanation of the ROOT file system in Windows 

This is our computer. We always have Drive0, where our OS exists. Within the OS, we have “The Folder Structure”. The base part pf the operating system is known as ROOT, and it is written whenever we write the ROOT C:. which means “Root of C”. Some people add C:\ to represent that drive as well, but it is just represented as C:, which means there is nothing below it. As soon as we put something in the file on C, such as a folder such as C:\Users, which means this folder is in the root of the C: Drive. If we have a subfolder in Users with our name, it would be C:\Users\Mo, each is separated with a \ within the location. Within the MMC, below her name, it starts with a folder called APPDATA, where it would be C:\Users\Mo\APPDATA. If she says “Create something on the root of C”, it would be C:\sysbackups. It is called “File Navigation”. 


[[Note]]