


1. Open a terminal : 



2. cd ~/Documents



![[Pasted image 20231026104832.png]]



3. We will make a directory called *practice*. Then, we type the following command to look at the permissions and the owner : 

		ll

![[Pasted image 20231026105109.png]]




4. Let us go into the *Practice* Directory : 





5. If we need to check the directory where we are now, we type the following command : 


		pwd



6. Let us create an empty file called "test.txt" : 

		touch test.txt



7. Let us check the permissions with the following command : 


		ll 


8. Let us change the permissions for the group to have read/write access : 

		chmod g=rw test.txt


9. Let us double-check the permissions :


		ll


10. Let us create another called "sample1.txt : 


		touch sample1.txt


11. Let us add the following text to our screen : 

		echo "Hello World!"



12. Let us add a ">" aka "Redirector" to the sample1.txt file : 

		echo "Hello World!" > sample1.txt


12. Let us check the contents : 


		cat sample1.txt


13. Let us use echo again, and add "What a great place!!" , with ">>" to append to the sample1.txt file : 


		echo "What a great place!" >> sample1.txt





Note : 

	In linux , !! is called a bang bang, which repeats the previous command.



14. We go now to use the *find* command : 

		find -name sample1.txt



> [!note] 
>  In Canada, it is now allowed to send credit card information to be sent in an email, so we can use the *grep* command to filter a line of text. 


15. Let us go to the root : 


		cd /


> [!note] 
> Look up **Sticky Bit**, which is evident in /tmp
> 




16. Let us go look inside the /etc/passwd


First colum is the name of the user, X is an encrypted password, second column is the User ID assigned, the third column is the group id		:

![[Pasted image 20231026111636.png]]


The next line has the system user :

![[Pasted image 20231026111726.png]]
(system user)



We use the following command to know how many users are there : 


		cat /etc/passwd | wc -l


	48



Let us check out the group information : 


		cat /etc/group

		cat /etc/group | wc -l 
		
		We have : 
		77


How do we know which groups we belong to ? 


		groups



Let us create a new user : 


		sudo useradd -m (makes a home directory) "puser"
		
		
		sudo useradd -M (makes a home directory without permissions) "puser"


Let us create a password for the user : 


		sudo passwd puser






Let us change the shell : 


		sh -s (changes the default shell ) /usr/bin/bash puser








		

To discover which shell we are working with: 


		echo $SHELL



We log out, and log back in as our account : 




Afterwards, let us check the groups we are in : 
	

		groups


maljokhadar adm cdrom sudo dip plugdev lpadmin sambashare


> [!todo] 
> look up lpadmin , dip , and adm groups 


Let us type : 


		which sudo


It tells us where the sudo command lives



To find out the version:S

		sudo -V




sudo -l 



![[Pasted image 20231026115246.png]]




Let us look at /etcsudoers


![[Pasted image 20231026115451.png]]

(ALL:ALL) --> ROOT can impersonate anyone and run any command. If we wish to add a user to the sudo group. We can also add their entire group to get higher privileges on specific commands


