


Podcast : Internet Storm Center/ WiFI enabled keystroke eavesdropping | Phishing via Google Looker Studio - 


Read  --> https://www.cyber.gc.ca/en/guidance/national-cyber-threat-assessment-2023-2024


Ramped up considerably, Influence campaigns from China, he heard about oil , water, arctic , but no one knows. They are up to something. It is not a low level burn; it is a spike in activity towards individuals etc.



### Quizes 

He calculates the time to do the quiz , and he doubles it so the whole class get double-time. Normally, some of these quizes start with indicating the time it takes him to do it. Some finish it in 15-20 minutes. When we finish the quiz, he would ask to leave the room within the first hour as long as you are back by break time. If you wish to stay, please do so quietly. At TUNs , he mentioned he encountered a very complex math problem. His colleague was stressing out, and he could not remember how to complete it. Quizes and tests measure your ability to actually do the quiz/test, and not necessarily the content itself. Most of these quizes are worth 5-10%. It is more a puzzle than it is about math.



### Databases



We use them to store information. We have all kinds of symbols and words (different language ) to describe what we are doing. In the 1980s, in the computer sceince world, you would build websites. They built databases for all kinds of organizations. A lot of information on clients and employees on paper. He needed to turn it into digital representations. The information used to go in paper files. When computers, they would fill out a digital form, which looks like the paper form. It was years before throwing that old paper concept away. They started inventing ways to represent information. One of the things that happened was the beginning of building a new language to talk about manipulating data. 


With programming languages, they have many elements. We have the same --> SQL. It is a query language. How many students are in my class? what is my current grade? did I pay my tuition? where is my class located? We ask questions in English with buttons on the page. Behind the scenes, any questions you have asked lead to code developing on the fly to ask the question in structured query language. 


Relational database

	Anything you ask 


How do you represent students in a school 


Relational database: data stored in a table, in rows and columns. If we have a table called "Student", this table will keep track of the information on each student. What could we have on the student ? 

###### Student 

Student name    
Student Age
Student Address
Student Number

Student_nam
Studebt_age
Student_address
Stud_num
stud_ssn


If we are asking information about a particular student, in the query window (in the box) , what could we type in ? 

1. Student's Name : John Smith ---> there might be more than one, you might get a list, you would ask the student which one are you? sometimes in the pharmacy you encounter a patient with the same name as you. The pharmacist will search for the name + the address, then on the list it will show the name and the address. Ideally, we want something in the database that would be uniquely idewntifying the individual, and something that the individual will always know, such as **Student Number** and **SSN** ( they wont ask for it right away for general interaction; it is highly private and sensitive). We need something less sensitive. We could use everything in this record to identify the student. We could have a form to type ALL of the information on this list, and then it will search the record. Every field can be used to find the records. The records in the table have to be unique. When going through their faculty system, the data is a mess. It has largley built over time by different people. We need the key to unlock this record. 
2. Student Number : we could use it- --> what if we do not know the student number if it is a brand new student
3. **KEY** : all the fields in this list is a **KEY** --> **SSN**, **Student Number**. We choose one that we can use forever to identify this record --> **Primary Key/PK**. It is vastly important. Whatever it happens to be, a table of courses, list of teachers. every table would have a **Primary Key**. It is just a choice; we can have SSN , student number , any are candidates for primary key (sometimes called *candidates*). Primary key is a matter of choice. When vbuil;ding a table for the 1st time, it will put a number automatically assigned by the system. It starst with 1 , 2, 3 , ... it is just meant to give you a new candidate key. He is not a big fan of that being used as a primary key. He needs the key to have some relation/portion to the data. 


Just like in programming languages, the individual fields in the table (SSN, student number) have a data type associated with them. Using the data types we know : what data type would be the name ? (string). If it is one character, for example a *char* (character), we need a string : 20 character variable. In the memory , the computer will set aside 20 bytes to represent characters. If it needs more bytes, it will do it with 40 bytes.John smith does not occupy 40 bytes; it is wasted memory. If we know exactly how long something is going to be (phone number), we can set the number of characters to do that. Idealy , we want the compyter to set aside the characters it needs to represent the data. Instead of calling it *char* , we can call it *VARChar*(20). If the data takes 19 bytes, throw away the exess. If we are talking about strings, we call them VARCHArs, we give them the maximum amount of space they actually need. Sometimes we get confused where the data type should be a string or a number. The thing we need to ask ourselves when building tables / setting up data types: will we do any math with these data? if not, we would represent them as characters instead of numbers. 


We use the data type appropriate for the data


If we have to set up a table with someone's age, we set it up as an integr due to the possible need for math. 


The table (Student : stud_num etc) 
	We have no imagination for names. We can tell from  the context. 


Another name for a table : a **Relation** : why ?the guy who designed it in 1976 called it that. We call them **relational databases**. it has nothing to do with relations. We have two words for databases, and they mean the *same thing*


Would it be a good idea to add some fields (when creating the database) such as *class 1, class 2, class 3* ? if a student is taking 5 classes, we would put 5 fields in the table, but if they are taking 5 classes, we would not be putting 6 fields. We should consider it in this way to not waste space. When we define the table, the table *is what it is*. 


Let us start by building another table in the database, and we call it **course**. What shall we add? 

Course name
Course hours ( 60 hours - 2 classes a week - number of hours in class for the semester)

-------
Course name
Course Hours 


Each section is a *Record*. Each table has Many records. Each record has **Fields**, and **Fields** have **Data Types**. 

**Table --> Records ---> Fields ---> Data Type**


We need to map students to courses. Students can be taking multiple courses, or no courses. We have a list of students, and we have a list of courses, we can put 28 student names in each of the records, and fill in the person's name leading to the same problem as before of putting 5 classes in the student **records**. we do not want to duplicate data at all. 


If he has information on us for this class, he needs the information for this class only. If we keep adding the student name and student number for each course we are listed in multiple times ; it could produce input error. You only want to put the information in **once**. We needed a **Primary Key** for the example --> if we added Course_num, we would indicate the year and whether it is the fall or winter semestar. We have to find a way to enroll the students in the courses. We do not want to duplicate the data (course name information), maybe instead of class/course, in the student table, we can put in course number, which will allow me to go to the course table. The student can be in multiple courses. Do we list all the courses in the one record? no. 


The relationship between the two tables : relations between tables have nothing between actual relations between tables (duplicated term used, differentiated by context). 



How many students can be enrolled in these courses? alot! The table (student name/course hour / couse num) could say there are ALOT of students. ALOT in databases --> *MANY*. Courses can have MANY students in it. it could be 1-28. When drawing diagrams to represent databases, we have a symbol for MANY **->** AKA *Crow's FOOT*  connecting the two tables. Indicates MANY. ANy single course can have MANY students enrolled in it. Ay single student can take MANY courses. So this line connecting the two tables is called **RELATIONSHIP**, and the *type* of relationship is **MANY-TO-MANY**. Position yourself next to the table, for each record on the table, how MANY students can it have? MANY. IF we go to the next table, and ask the same question, and it is **MANY**, then it is the same thing.


In SQL, you can NOT code MANY-to-MANY relationships, but we can diagram it. Why have it then? He will give us another name for tables and relations. The term *ENTITY*, table is an entity, car is an entity : ENTITY is a noun. Eeach entity has characteristics to it. The marker is black, refillable, length/size, all these nouns are **Entities**. 

We are learning databases because we need to BREAK them.


Assume we have all the variables going into the database in a box : we call the box an *entity*. We will say "How many courses will be taken?" --> MANY! --> draw the line 


How many courses will there be ? ---> MANY ---> draw the line. 


All these diagrams is to understand the database design, it is a method of communication explaining it. A blueprint has a set of symbols describing how it is built and how it functions. When designing databases, we design them to make them work. 


His friend builds the roads : he mentioned to him that he builds physical things, and Ron creates virtual things, and that his roads are tangible. In IT, we design the system as a virtual thing; yet the approach is the same : requirements, how many cars , etc ... We have these diagrams that allow us to show it to clients and employees and inquire about the meaning to confirm it. We take the diagram to SQL programmers and they would understand what thety mean. If building a house, and we have the blueprint, and we give it to the carpenter, then they can build it. It is a *translation* between the idea and the programmers. 


In the design stage, we CAN have **many-to-many** relationships, but programmers CAN NOT code it. They take it one step further : 

### Linking Table


Idealy, what we are looking for in a relationship between two tables so it can be programmed : **One-To-MANY relationship. 



### Bridging Table 


ENROLL : 


--


---


Each record is to describe that the student is enrolled in the course. records have to have a primary key from the student table, and a primary key from the course table. 

Each of them taken together form the **primary key** for the enrol table.


Let us draw the relationship : 


We stand next to the table --> how many of those things each can have? --->

\
For each student --> how many courses enrolled in ? ---> many


For each course ---> Each enrolment refers to one student ---> one


Symbol ( sideways cross ---> many)



Enrolment table : 

How many courses listed ? many 

For each course, how many records pertaining to one enrolment?  one


Thus --> **One-to-Many 


	+ --- <



ENTITY RELATIONSHIP DIAGRAM : always refered to as **ERD**


**ERD** is the blueprint for designing databases. We give **ERDs** to the programmer, and they build it based on it. 


We should be a bit confused whther it should be one-to-many and many-to-many


Being confused is at the second stage of learning. 





What are we missing ? **Primary Key**. This table will have a large number of courses in it. 


Is there a limit to the number of tables in a database? no. The database will cease to function the bigger it gets. 




Due dates are tentative according to the knowledge that we have at the time. It is not a competition. We have to work together. If something is coming up, talk to him right away!



If an assignment is due next Monday, and something came up, we would go to him as soon as we know. Life happens! In the real world, a good manager will make arrangements of when and what can be done. 


He put an assignment up : in 2 weeks, install MySQL. Thus, it should be enough


Next assignment : more complex, we will negotiate due dates. 



Entity Relationship Diagrams : In the example, we left one entity : instructor. 
We have a student table : 

	student
	'========='
	Stud_num PK (Primary Key)
	Stud_name
	Stud_addr


If we are looking at this table, and we see addr, we should think Address. Name for name, num for Number. We would fail the assignment if we called it as such : 


	Table1
	======
	Field_1
	Field_2
	Field_3

It is too ambiguous for naming


Take the first part of the table name. Use a naming convention that describes the table and the information that belongs to it. so a table STud_table, stud_ is used for each field. Do NOT use plurals in table names. 


We have another table: 


	Course
	======
	Course_NUM PK
	Course_nam 




we have another table :

	enrolment
	==========
	stud_num PK
	course_num PK

(if we want to uniquely identity a record, and we have two or more fields making the primary key, we call it the **COMPOSITE KEY**)



We have one to many relationship between course and enrolment, and we have a one to many relation between student and enrol, and we would like to have a third table : 


	Faculty
	======
	fac_num PK (faculty number)
	Fac_nam 


So , faculty teach courses (teach is a very), students take course (entity is a noun, relation is a verb, what they do together). We want to recognize the fact that faculty teach courses. In the courses tables, we need to add a Faculty ID 



	Course
	=======
	Course_num PK
	course_nam
	Fac_num  FK     (it allows us to provide information about the faculty who teaches the course, a way to retreive info from the faculty table, describes relations) , FK ? it is Foreign Key. We know there is another table that contains the information that I need. The data exists on another table. We know that Faculty_num is a PK at the Faculty table. Foreign Key is ALWAYS a Primary Key at the other Database. 



He would like us to keep in mind that ALL of these tables together are called a **Database**, which consists of one or more tables


What is the relation between Faculty table and the course tables?

Faculty can teach many courses (from perspective at Faculty Table) one-to-many

Courses table (multiple courses can be taught by one faculty) many-to-one


Table is a **component** in a database!


Databases are made of **tables**, which are made up of **records** and **records** are made up of **fields**, and **fields** are made up of **data types**.



Question : student table and faculty table , is it many-to-many ? 

Which faculty teach this student ? start with student table, go to enrolment table, get the info, go to the course table, and you can use SQL programming statements to navigate those tables. 



He has asked us to download a free and open source version of a database management system (DBMS) , which allows us to build databases within it. We have complex enterprise DBMs that large organizations use to build their databases, but the vast number of companies that we might work for are not using those; many use a free and open source DBMs called **MySQL**.. 

We will be using **Nessus**, and another called **OpenVAS**. Nessus is paid, but OpenVAS is free. 


MySQL is NOT a database, but a DBMS (Database Management System). We can use MySQL freely to create simple-to-complex databases for any purpose. Ron's last company: when he first started, he had one copy of MySQL, and it had a database for each customer, and all the data went into its own database. So performance suffered. The customer is present on so many devices that they had to have their own DBMs. MySQL has example databases in it (practice databases). Because it is a **Relational Database**, due to relations between them, we have added a R to DBMS making it R DBMS, but no one uses RDBMS, and just stick to DBMS. 



In the next couple of classes, he will demonstrate how to use MySQL. Where do we install it? We would put it on a laptop, we could spin up a virtual machine on an external drive (put Win 10 or 11), we can take it everywhere. 



	Get started on VMWare Workstation ASAP! Virtual machines crash a lot! Backup your virtual machines! He recommends the virtual machines on the laptop. He put a reference in W3 Schools in the Course Shells. They are useful, and he wants us to live there

Look up videos for creating databases in MySQL. YouTube is our friend. Be comfortable with installing software!


We need the standalone version of MySQL not the web version!


If we see a GUI, we will not be working in it! 