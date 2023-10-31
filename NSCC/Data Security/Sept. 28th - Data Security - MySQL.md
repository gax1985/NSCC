 



## MySQL



It is an **Database Management System**

Within the **DBMS**, you create a *databases* made up of *tables* which are made up of *records* which is made up of *fields* which is made of *Data Types* and *Constraints*


Database --> Tables --> Records --> Fields --> Data Types + Constraints 



We will start with ...


1. Create a Database
2. )USE____; 
3. CREATE table;



Go sloooooow! 



(iFrame : in a website, it would be divided in different sections called *frame*. iFrames can be made into 1 pixel. You would not be able to see it. It is quite common as a compromise technique. Check out the new "GPU Compromise". Look up "compomised routers with a compromised firmware. It opens a backdoor via SSH. It would pass any login credentials to the attacker, and a TCP packet that would be scanner-proof?(last bit might be wrong? but look up the article)")



Ron : He did a security analysis for an organization, where he found a compromise on the router. The router was quite inexpensive consumer-level routers. In the firmware, it was watching for a partciular packet pattern. If you sent a special packet with a special bit pattern added to it to gain access. The developer of the firmware placed it there in order to make his life easier. The manufacturer said they can not do anything about it, and to buy the newer version. The municipality had to get rid of every single router they had. 


CVE Number : Common exploit, it is given a number my MITRE*. Take a look at **MITRE**! Check out **Internet Storm Center**


(Dependa-Bot : New malware implementing backdoors to GitHub repos affecting "Dependa-bot", which deals with dependencies)



Readings and References --> MYSQL Command Manual + start with "MySQL's School - Create a Database", which we get a description of the command. Here is the command : 

	CREATE DATABSE database-name


and ...


	CREATE TABLE Persions (
	
			PersionID int) --> if we have a primary key, make it an integer
			LastName varchar(255)


Scroll down to the bottom, where we see examples showing us how to do it. He suggests this morning to go to the course shell, open W3Schools open, and check out *LinkedIN Learning* where we can find *MySQL videos* (Check them out on Friday evening). It is learning a new language, where the more we interact with people, the better our language skills get. It just takes time and practice. 


We shall be working in the command line most of the time. The statements we write are done in the command line. It strips away all the GUI-based shortcuts. Later on, you will get to HATE GUIs, as it would be quicker to use the command line interface. 


ROOT account : HIghest level of privileges.  Very shortly in the next couple of weeks, we will set up user accounts with certain restrictions, where it is called "Roles". Generally, do not work as a root level. Mean-time detection : Attackers can be in your system with root-level privileges for a long time until detected. 

User Authentication Control : It is the message asking for your permission. You can set it to not give you this message, or a prompt instead with YES/NO. 


Let us get *MySQL* booted : 


1. Open the Windows Terminal as an Administrator
2. Navigate to where MySQL is installed :

	C:\Program Files\MySQL\MySQL Server 8.0\bin>

3. Type the following command to get **MySQL** started : 

>mysql -uroot -p 

4. We are in the *MySQL Shell* : 

5. Onwards, let us create a Database called *School*

>mysql> CREATE DATABASE School;

6. If we wish to show the databases we have :

>mysql> show databases;

7. Let us select the database we would like to use : 

>mysql> USE school;

8. Let us see which tables we have : 

>mysql> show tables;


	We should see an empty set

9. He would like to know what the table looks like, so when we get down to this level : 

Database ---> Tables --> Records ---> Fields > Data Types +Constraints
												X (Records)

>mysql> describe student1; 

10. If we wish to know which database we are in : 

(to be looked up)

11. If we have an entry, we can try to increase the characters in VARCHAR, it WILL NOT WASTE memory. If it is VAR, then that WILL affect the memory. 

12. Every Table needs a primary key! His table has a primary key called "StudentID". The table that we have created does not have a primary key. We need to delete it and create it again via
>mysql> DROP TABLE student

13. Ron would like us to use the student ID as the primary key of the table. so, he would like the following : 



>mysql> CREATE TABLE Student (
>
>			Stud_ID            INT                            Primary Key ,
          Stud_NAME     VARCHAR(255)           	 
>);


(Ron has added a module on Brightspace called **"Creating Databases"**. Check it out! At the end of the slideset there is an ERD descriptions and tables, between now and next class, he wants us to create these tables. Some things we have not covered, such as "Foreign Keys". This is a challenge, W3Schools --Command -- 


He challenges us to do something with minimal instructions, and then another task that has NO instructions. We might get there, and we may not. How do I do this? where do I look? I will try a bunch of things, and go until you can't. When you come back to class, we will have questions that we have tried to answer outselves, and error messages. Please reach out to each other. If someone figures it out, help others in class, but do NOT give the answer away. Master :
**Self-Directed Learning** )


He wants us to : 


1. Create a Table called ("Student")

(W3 Schools page -- Create Tables page ) (CREATE TABLE Student (name of field DATATYPE, NAMEOFFIELD DATATYPE); 

(if you are communicating the design, they want to see what you **have set a side**, and what **you have  built**.)

                                 Datatype                                     Datatype

Student 1

Student 2 


Student 3





(Remeber: when working with databases, to make it easy for others to work with the same database, please use a descriptive name that is understandable)

(He will put something on Brightspace : tinyint with values from 0-255, how many bits would take to store it ? 1 bit. 4 bytes to store an ip, 32 bits . Unsigned integers (no negative values), but he can assign it in both positive and negative, we are giving up half the value to indicate whether it is positive or negative. If this ID is not going to be 4 billion, we can use a smaller datatype of 4 bytes. Every time we store something in the database, it would use 4 bytes. This is for good memorty management. This was developed in accordance to how expensive memory used to be - 64K. Memory management/waste were VERY important. Memory right now is cheap! If we had 64Bits of memory on the lunar module on the 1967 Moon landing, it would be important.)


(Y2k : The year stored in memory were 2 digts , 99- , in 2001 it came up with 1899 , as he saw it happen. One person stored the year as a one digit. He had to go in and change the data structure to 4 numbers. The heart of the matter : it is up to us! It should be light in terms of memory, yet not causing problems)




(If we donwload the latest version 0.34, it changes the name of the daemon. Ron's version is 3.0. )


(When he was in DBMS to see what  databases he has, he used the following command :

show daatabases; )


(What happens in the Blueprint stage is critical)



Next Class: 


We will built it, but TRY IT!!!



