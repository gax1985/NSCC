





When the OS is running, it is runing in something called **User Space**


Programs are running in memory, and your program is running in a section of memory with its own rights and priviledges. 



The rights and privileges have to *temporarily* be lifted to run it in protected mode (which is briefly in superuser)


If you can interrupt the program and cause it to crash, you get it to jump to a section of memory where it is not allowed to be.



Your data/Code is stored in block 2 for example. WHen the program is executing, it is executing code stored in user space. If you can direct the program to go somehwere else in memopry to access another memory, it will generate an error causing the program to crash, and normally, when the program crashes after being executed properly, you get dropped back where you were supposed to be. 


If we drop the OS controls, and you can do that by wandering in an area of the memory where it is nto supposed to be



When you crash, you end up retaining the same rights/privileges that the program had, and the OS can not put you back in the right place when it comes to rights and privileges. 



If we have a list of names stored continously , .



		 |     | |    |    |
		 sections where student info is stored. 
		 You dedicate enough memory to store 


		variable types var -- car 
	Declaring an array : storing 50 names, they will take 1000 bytes due to 20 bytes used by each program 




If you try to write data past the space reserved for the variable var - car. and we try to access space where we are not supposed to be ---> another **Buffer** , where it is the storage space


If we make the program go to another buffer, we do **Buffer Overflow**


Programmers when putting something in a list, they have to check if the move is ok, whether the programmer is going somehwere where he/she is not supposed to be


Programmers got lazy in the late 1980s-1990s. Schools were not pumping enough programmers. 


Ron went to TUNS. The program was quite challenging. When you finish the program, your code will not be doing any **Buffer Overflow**. 


The NS industry wanted to pump out more programmers, and planned to do this in 7 months. Many smaller institutes charged people large amounts of funds to teach them quickly. The programmers were not taught to prevent the buffer overflow. You would check if any measures would cause the **Buffer Overflow** by trying to do it yourself. Someone will check!


**Buffer Overflow** is common, and lately, the Juniper firewall had this vulnerability. We wont have to worry about it because of coding. We wont be trained on Buffer Overflow in programming, but he can teach us Buffer Overflow. 



He bought expensive firewalls. They were suspectable to buffer overflow. They were not tested for it. 



We will learn this in **SQL Injection**, where someone wrote a database, made it available online to access it remotely (such as student grades), there are thousands of databases written by bad programmers. They have the same lesson : People did not use good training when making them, because they did not know about them and noone taught them. 



The plan with Tony is to use VMWare to install virtual machines. We are off by a week. To supplement that, there is a window of opportunity in a workshop on **Refrencing** scheduled for Thursday. 



Today : Details on Databases!




Fundamentally, what we do works because people build things badly. Untrained people try to cut corners and cut costs. This is why **SQL Injections**, **Buffer Overflow**, etc.. exists. People are focused on getting things quickly. 



Microsoft had a QA (**Quality Analysis**) Division. Then they closed it because they were banking on people telling them these issues with their products. 



**Minimum Viable Product** : Do not take 3-4 years to put the product out, get it done quickly as soon as possible, and others will buy it. Get it done quick! ---> This is a bad idea! (example: parachutes). We put out fires because people have bad production practices. 



When we learn about **Arrays**, no one will talk about **Buffer Overflow**, the programming languages (the ones we learn initially) have safety measures preventing the existence of **Buffer Overflows**. 




## Databases



(The presentation is part of the interactive session we will do next week)



Lats week , we spoke about approaching a client/customer, and asking them what kind of information will be storing in a database that we will create. 


We are asking them to find out about their **Business Process**, and did something called "Business Process Re-Engineering", and they had to translate everything they have done on paper in a digital way --> **Business Process Re-Engineering**. He had to write the software from scratch. 


MySQL was not around. They had **C**, **Pascal**, etc...


You ask them , and you record the info in a Blueprint diagram called **ERD : Entity Relation Diagram**


#### Entity Relationship Diagrams

	Entities = Nouns 
	Relationships = Verbs
									(Verb)
	Nouns -- a Student takes a course
	Student                     Relation   


They describe the interactions between *Nouns*. When building up the diagrams, the Nouns become **boxes**, and the Relations/Verbs become Arrows 



Student ---> Course
			Takes
			(Verb)


There are many properties to these verbs . Each student can take 1 course    one:one relation 1:!   (This is ridiculous, due to students being able to take multiple courses)


Usually we say 


Student -----> many courses
Nouns    ----->     Courses
				Takes
				Verb


A student could take **no** courses 

Can a student have no courses?    can a student take **many** courses? 

                0/Many
Student  ---- >      Courses


A student can take **no** courses or **many** courses




---|   ------    K  ----

   1                     many



1 - to - many     -----K   Crows Foot Notation  number three sideways 




We have **many** students who can take **many** courses




When drawing a **Blueprint** , many-to-many relationships , the programmers will say they can not code it, and they need one more step ---> they put a table in between called a **Bridging Table**. 



Each student can enrol in **many** courses
Each course can have **many** students 



When considering the diagram, he positions himself at each entity, and says "Each"


"Each student" can take "each course" 


Which side is the One and which is the Many ? 



He stands next to the entity, and begins with "EACH", "Each Student , meaning one student, can take many courses"


"EACH" course can have "MANY" students 




	Box   --->                               Smaller Box                             <----------------     Box    
	Three Prongs                           Enrollment 
														Rach enrollment can have many courses?
														no
														Each enrolment can have one course? 
														yes




Trust in the fact, at this point, if we are sort of getting it, he is expecting us to be there (after practice, we will understand it)


We have to understand the **Database Design Process** 


He mentioned the deck example, he has pillars at an angle that he has to hoist them up. 


We have a name : **Hack and Slash Conding** : You try something, does not work? throw it. Try the next thing. 

(This happens without a design process. A bit of design goes a huge way. We are NOT building a foundation in THIS way.)


We use the **Entity  Relationship  Diagrams** to translate what they want to do in their business process into a computer program. 


When he bough the house, he had a huge dog. His landlord did not make his mortgage payments. Ron came home, and found two gentlemen infront of the house where they were actually selling the house where he was staying. 
He had to build a dog house 16 feet long X 8 Feet wide X  15 Feet high. He tried to build the roof, and the dog house fell apart due to the design not being able to hold the weight of the roof. 


Thus, spend as much time as possible designing databases!


In the last 20 years, people stopped being trained to think in terms of design!


We are looking for people who made **silly** errors. It is fun to break things for a **Good Goal**!


We need to be able to analyze the database from the **Design Phase** and up!


We want to be a part of the **Database Design Process**. We know what the adversaries will do if there is no design process. If they are not planning it properly, they are creating a **threat**. We get hired to do **Risk Assessments**. 
When we go for a work term, one of the jobs we will be doing is **Threat Risk Assessment .. aka.. TRA. 


Database will hold private information, and the information finds its way to the Dark Web, and threatens the wellbeing of the people...


Something else is done called **Privacy Impact Assessment** aka... **PIA**. We look at the design and say that there is a weakness in the design I can exploit. The combination locks , by the time we graduate, could be opened in 3 seconds. Why do they sell them still? cheapest! They did not consult the cybersecurity department. 


We have to be concerned about the confidentiality, integrity and security of our clients' data.


30% of the graduates from last year are working with these types of things (Databases)



We do not have to learn **C**, we have software that handles databases and contains all the necessary commands to build databases and the commands needed to use them. 


**DBMs** --> Database Management System 

		school
		Business
		Family


#### DBMS


	It is made up of :

		Databases

			are made up of 

				Tables


					Are made up of 
								Records
								
										Records are made up of 
													Fields
													
															Are made up of 
																	Datatypes
																				Are made up of 
																							Constraints!









#### MySQL


We need a database called **School**. we enter the command to create the database called **School** : 


>CREATE DATABASE school;


And if we would like to use the **School** database : 

>USE school;


When people try to use it , they forget this command : 

>USE school;


The commands are UPPERCASE. MySQL is NOT case sensitive. This is the standard practice!


Each command ends in a semi-colon! 

If someone enters : 

>USE school 
>....
>...
>...
>...
>;



DBMSes are made up of **Databases**, **Databases** are made of **Tables**.... We do not have **Tables** so let us create a **Table** : 



>CREATE TABLE student; 
>(This is not going to work)


In order to create a **Table**, it needs **Records**, and **Records** are made up of **Fields**.

Thus, we need to do this : 


>CREATE TABLE school (
>column1    Datatype,
>column2   Datatype,
>column3   Datatype,
>....
>);


If we put this command in one line, it will work! We have to read our code, as we will be making mistakes. The first attempt to type commands will not work. If things are not laid out clearly, then you would not be able to spot your mistakes easily. If you would like to find a bug, you show it to someone else, as if we stare at something long enough, we become blind to the obvious! Our brain fills in the stuff for us. It does not say the things that are there, but it says the things you **BELIEVE** are there. 


Debugging code will be hated by us, but it is so rewarding when you finish! 


We will make the process easier if we make it READABLE!


Code lives forever! 


Databases we write today we will be glanced at by someone else , and we wont be there!

Electricians and Plumbers when unrolling the tape, they fold a piece of the tape at the end (Make a friend... Leave an end)

Next person who has to debug your code will thank you when they have to read it, and would be able to understand what you are trying to do!



#### Creating tables with *Key Constraints* 


Create a table called Student! When creating a field in a table, we have to tell the person about the data that will be there. How do you get a bad mark in this course? you do not do that. (Bad example: CREATE TABLE Table1 "He has no idea what type of data will be stored in the table "). We want to have the student's **name** , let us call the column 'STUD_NAM.  (first part STUD is for table, second part NAM for names). We have **CHAR(60)** for setting aside enough memory for storing 60 characters in the field of the table. If the student's name is 8 characters, we will have 52 spots that will not be used for anything since it is reserved for the STUD_NAM field. What we want "Set aside 60 characters, but when you enter the data if it is does not take 60 characters, release the rest of the memory to be available for use". Today, if I try 61 characters, we will get an error message. MySQL takes care of *Buffer Overflow*. In C , which is used to program firewalls, if we use 61 characters, we will have Buffer Overflow, which will drop him in superuser shell in the memory. Thus we have VARCHAR(60)! we want to be sure that when someone is storing a record in the database, that it can not be left blank. Thus, *constraint* means "NOT NULL", and NULL is literally nothing.  Thus, *constraint* means "NOT NULL". "Every record in the database requires a primary key, and the name can not be the primary key, because people can have identical names. SSN should not be used because it is dangerous to use it for everything. Our student numbers start with W, so probably in the database the records start with W". The *student number* will be our **PRIMARY KEY**. **MAX_INT** is a global variable in all OSes. You can have COMPOSITE KEYS in a bridging table. It would have primary keys from two tables, and combines them into a new primary key made of both primary keys. 


>CREATE TABLE student ( 
>                              (Datatype)              (Constraints)
>STUD_NAM        VARCHAR(60)    *constraint*
>STUD_NUM        INTEGER              primarykey  (It has to be unique. Other records can not be equal to it)
>STUD_age          INTEGER               constraints
>
>
>)



Something displayed on the slide : 

>NOT_NULL
>UNIQUE
>PRIMARY KEY
>FOREIGN KEY
>CHECK



Databases are made up of tables, and in this example, the table is called Student. Each line describes each **Record**. 

>STUD_NUM        INTEGER              primarykey  (It has to be unique. Other records can not be equal to it)


**Records** is made up of fields,  fields are made up of Datatypes



Create a Windows 10 Education version Virtual machine. Watch videos on Intro to MySQL, Creating a table in MySQL
