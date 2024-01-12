


If you have an unknown quantity of files, or you have an excess of information, set up a separate table, and assign each picture (if you have pictures for example) a primary key, and set it up as a foreign key in the other table 


#### Assignment 2 

Do not use the word LOCAL.

	LOAD DATA  (do not use LOAD DATA LOCAL INFILE) --> LOAD DATA INFILE \\<file path> (backslashes are escape characters, make sure you have read/write privileges on the directory)


###### Step 1 : 

Start with an ERD diagram 


**Note** : country ID, another file with all the country names. We do NOT want duplicate data, or input anomalies, or any errors. The table has to be explanatory for the data it contains. There are *no plurals* in the table names. 

If we have multiple pictures on file, we want one picture per hacker. The primary key cannot be a hacker's name for example. 

Note: 

References are not needed in the database.


Note: 

Images will be the Datatype **BLOB**


#### Formative Assignment


There was a noticeable lack of data. He would not necessarily attribute it to a *Lack of Data*, as Ron was able to find information on individuals. When doing this, he would like us to picture that each profile is printed and sent to somebody. The end of each profile should end at the page boundary. Some of us did really good layout work. 


We are going to turn this collected information into a database. 


Other individuals took effort to make it presentable. 


We must put **References**, not Bibliography. It must be in APA format. 


###### To everyone : 

	My boss asked me for the assignment. I need to keep this job. Do your best!


A number of individuals missed points in naming the file. If everyone called the file "Assignment 1", so imagine if he had 100 individuals sending him the file as "Assignment 1". He needed to force rigor in our writing. The last point : regardless where we are working, you will be required to meet a reporting format, which is proprietary depending on the institution. Not doing so is starting off on a bad foot. 


There are 200 names in the waiting list in this program. Among those names, someone is very eager to get into the program, so do your assignments. If someone did not do the assignment, he needs a written explanation on why some of us did not do the assignment, and it would involve a meeting with Student Services to review their commitment to the program.  The explanation needs to be submitted by the end of the week. 


We will be entrusted with an entity's secrets, so professionalism is key. 



###### Side Note : 


Nessus has a free community version. It used to be *Home Edition*, but they changed the name. It has limitations on it, where you can only scan a few machines at a time, and can not be used commercially. He used to buy a commercial Nessus license every year. He used to do a lot of money on doing network scans for clients. It used to cost $1250 per year. Now it is 2000-3000 a year. Do not buy the license if you do not have the clients to pay for it.  


It is called **Nessus Essentials**. Please make sure you write all the usernames and passwords. When doing network scanning, we will stary with *nmap*. 




Sidenote: on the situation in Israel : 


1. Massive cyber intelligence failure
	- It is possible they did it old-school : person-to-person etc...
2. Massive human intelligence failure 
	- With metadata, you can see that things have changed, and you can see that there is a ton of traffic. 






#### MySQL


In the school database :

>show table
>
>
>(table shown)
>
>
>describe faculty1;
>
>
>(table shown, with two fields)
>
>
>SELECT * FROM faculty1;
>
>
>(All the data is shown from faculty1)
>
>
>TRUNCATE table1; ---> removes the data from the table
>
>
>SELECT * FROM faculty1;
>
>(NO DATA)
>
>(Now, we move data into the table)
>
>
>system cat try.txt (invalid command)
>
>system type try.txt;
>
>(This shows the data inside)
>1     Ron
>2     Marie
>3     bryansql


We have an *empty* table. So the command for showing the contents of a file in Windows is *type* and in Linux it is *cat*.


Now, we can output the contents of the file into the table : 


>load data infile "D:\\locationfolder\\try.txt" into table faculty1;
>
>
>(Data is loaded into the table. to check ....)
>
>
>SELECT * FROM faculty1;
>
>(Data is shown)
>


If we go to the folder where the folder that contained try.txt, and right-click on it, and select *Properties* then *Security* and you can see who has access. 


We go to **Permission Entry**, add your **Username** if it is not there. 


In Windows, there is an *inheritance* aspect. In OS Security, the key term to remember is **Defective Privileges**, which is a combination of all : file, directory and account. 



**Presenter** :



Anti Human Trafficking work term 

He got emails, names, addresses. He used the techniques he learned in class to look for those people. The Anti Human Trafficking entity would be happy to train you in the field, and he used proprietary methods to do so, as well as open-source intelligence methods as well. 


If interested in OSINT, it is a great work term to learn more. The key is : ask questions!


There is a serious Human Trafficking problem in Nova Scotia. 






























