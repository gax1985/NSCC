


A **VMX** file is a configuration file for a VMWare Workstation Virtual Machine


**NVRAM** file stores the BIOS of the virtual machine


**VMDK** File is a virtual hard drive


	We should have 3 VMDK files for the assignment


Question : Is there a performance penalty in splitting the virtual machine's virtual hard drive  into smaller multiple files (over multiple files)? 

Answer : There is a general performance penalty when splitting the virtual hard drive over multiple files (more performance than read/write speeds)


There is a *Dynamic Hard Drive* where when we create it, it expands the size of the virtual drive on demand. This is beneficial as it preserves hard drive space until it is needed 


VMWare tools are installed within the virtual machine, and it helps improve the virtual machine's performance (for example when shutting down the virtual machine), allows shared folders and two-way clipboards , etc... 

We can control the maximum size that a dynamically-expanding drive can have


Snapshots enable us to revert back to an optimal state for the virtual machine. In class, there was an attempt to delete the *SYSTEM32* folder located in the *Windows* directory to break it. This is done after taking a snapshot of the virtual machine


###### Snapshot

	It is simply a record of all that changes that happened. It is NOT a full copy of virtual machine. 


###### Cloning 

We can do a **Linked Clone**, which involves a connection between the clone and the original virtual machine, and a **Full Clone**, which replicates the virtual machine. 

###### Cloning vs Copying the Virtual Machine folder


**Cloning** is a much thorough option, as cloning changes the names of all the files in the virtual machine folder to rid us of any conflicts in the file naming. If we were to copy the virtual machine's folder, then when adding it to the VMWare Virtual Machine library, we would have to change the name of the virtual machine that we copied, or change the name of the copied virtual machine to avoid any conflicts.


Sidenote : Docker containers are similar to virtual machines, but quite different. Virtual machines run on a hypervisor (type I or type II). In a container, we have our hardware, host operating system, and a virtualized application. If he is developing a web app, he can move the container to a different machine, and it will run. It is a type of virtualization that is not virtualizing hardware, but virtualizing the container engine. In terms of emulation vs virtualization, a virtual machine virtualizes hardware, but for containers, it virtualizes the OS to run the application. 


If you delete a virtual machine, then a snapshot will not work as it requires the original virtual machine which was the source of the snapshot. In Snapshot Manager, you would be allowed to go back beyond your last snapshot.


Once you delete the original virtual machine, you will not find it in the *Recycle Bin*. Snapshot will not recover a virtual machine, but it will take you back to a previous state for the virtual machine if it exists. Snapshots take 2GBs of space. If you do automated snapshots, you have to manage them in a way that adapts to the available disk space. We can do **Incremental Backups**. Once a week, do a full clone, and then through the week, do incremental snapshots. You can start with a fresh machine for every lab!







