

> [!warning] 
>  Nov. 3rd is the last day that one can withdraw with a W. The workload will increase like crazy. It would be best to avoid getting an F. The instructor may be honest with the student if the student is not doing so well. If we are struggling to keep up with one or more courses, such as  the anxiety , stress and inner dialogue, this should be completely ignored as it is natural for the brain to do so. If nutrition, anxiety and sleep are factors, and the instructor mentioned the possibility, then you can withdraw and do a reduced course load. Ron withdrew from a Masters degree. His instructor offered Ron to do a reduced workload, and Ron was gone from school for five years. It took Ron 10 years to complete the PHD. While he was doing his undergraduate degree, he withdrew from a class each semester. 




The workload will get a lot worse for the rest of the semester, and going forward. Assignments will be piling up on us. No one will tell us what to do, but it is wise to make this sort of decision if one is struggling. 


Ron is our faculty advisor.




# User Roles, Rights and Privileges



User is not defined by the username, but also where they come from. If we have someone called "My Name", their account shows as coming from *localhost*, they would be a completely different user with the same user name from another location. 



Example : 

myname@192.168.2.4 vs myname@localhost



Commands Ron tried : 

While logged in as ROOT : 

>CREATE USER myname;

;
>*myname* does not have any rights of privileges at all; the only thing the *myuser* has is :


		SHOW GRANTS for myname@localhost;
		S
		
![[Pasted image 20231031085517.png]]



The only rights that the user has is **USAGE**, so Ron typed the following command to extract information from the Users' table (where the MySQL users are listed): 


>SELECT *  FROM mysql.user;


To give privileges : 


> grant ALL on *.* to 'myname'@'localhost';


Now the user has access to EVERYTHING!


![[Pasted image 20231031085823.png]]



The user *can not* grant any privileges to any other user, but has all the other privileges


We could fix that : 


>grant grant option on * . *  to 'myname'@'localhost';



>Select * from mysql.user;



Username and where you are coming from are common issues. The actual user name is : 

		'myname'@'localhost';


They are only allowed to grand a subset of the rigths and privileges they have. 


GRANT GRANT seems like a redundant option. Let us chewck for another way : 

		let us get rid of this user


>mysql> drop user myname@localhost;


>select * from mysql.user where user = 'myname' \G


		EMPTY SET


Let us create the user : 


>create user 'myname'@'localhost' identified by 'mypassword';



We can do the following : 


>grant ALL on * . * to 'myname'@'localhost' with GRANT Options;



Now they have all the rights and privileges, as well as the **GRANT** option. At home for our own database, we can do so , but we would never do this. We would assign the user a *role* instead.


We can grant privileges to a specific databasse, a specific table, or a specific column in a specific table in a specific database. 

Let us delete the user : 

>drop user myname@localhost;


If we are granting privileges to a user at a time, we do not want to do so,. We will create a *role* instead : 



> CREATE role customerservice;



![[Pasted image 20231031090600.png]]


>CREATE ROLE customerservice; 



Ron has a database defined called 'Store'


>USE store; 


And we have one table there called "Customer": 


>SHOW tables;



>DESCRIBE customer; 




>DROP TABLE customer;



>DROP DATABASE store;





The recipe to set it up : 


>CREATE DATABASE store;


>CREATE DATABASE store;



>CREATE TABLE customer (name VARCHAR(40));


>SHOW TABLES; (to check:)


>DESCRIBE customer;



Now Ron has the database set up. He has previously created a role called **Customer Service**. Now, Ron would like to assign the privileges that a cuastomer service representative would have on the customer cable : 



>GRANT select(to view the information), update (to change the phone number), insert(to add new customers into the database, this will come from the customer rules, where the boss could need the customer service representative to do certain tasks, and they want them to have rights to a specific table) on store.customer to customerservice; 



Ron needed to do one more thing :


>SELECT FROM mysql.user where user="myname" \G


		EMPTY SET (0.000)


How do we create a user? 


>CREATE USER 'myname'@'localhost' identified by 'mypassword';


We now have a *user* and a *role*, where the rigths and privileges are assigned to a role 



Let us check their rights: 


>SHOW GRANTS for myname@localhost;


![[Pasted image 20231031091608.png]]



>GRANT ROLE customerservice to myname@localhost;


ERROR SYNTAX !



>grant customerservice to myname@localhost;


![[Pasted image 20231031091824.png]]



The customer service role aapplies to whewreever the user is coming from.


How do we remove the role from a specific user? 


>REVOKE customerservice from myname@localhost;




>SHOW grants for myname@localhost; 





![[Pasted image 20231031092105.png]]


Ron has created a lot of databases for charities. So here is our practice : 

> [!todo] 
> - [x] Create a Database named "*savetheclowns*"
> - [x] Create a table named "*donations*", with a field called **name** with the *VARCHAR* datatype
> - [x] Create a **role** named *dataentry*, with the **select**, **insert** on the *donations* table
> - [x] Create a **role** named *supervisor* , with the **select**, **insert** on the *donations* table
> - [x] Create a **role** named *dba* , with **ALL** privileges on the *donations* table (**Hint: GRANT ALL)**. 
> - [ ] Create a **user** for each role
> - [ ] Assign each **user** a *role*
> - [ ] *Test it!*



![[Pasted image 20231031092326.png]]






> [!tip] 
> To remind yourself about which user needs which role, you can name the user *data*, the supervisor *supers*. Make it easy for yourself to figure it out. 
> 


Hypothetically, you are hired by a company, and you inherit the role of a **Customer Service Representative**. Idealy, if a person gets promoted, in order for them not to keep their rights and privileges, there should be an automated script to automatically take away rights and privileges. 



> [!important] 
> **The Hacker Profile's Database is due on Nov. 7th**




>[!tldr] 
>We have no classes with Ron on Thursday 


> [!caution] 
> The next database assignment will be issued next week while the information is still fresh.
> 


> [!danger] 
> In a **Lockdown Situation**, if you can get away, get *away!*
> If you are in a **Hallway**, get inside!
> Once you are in a **Classroom**, turn off all things that might produce a sound, and turn off the lights. 



