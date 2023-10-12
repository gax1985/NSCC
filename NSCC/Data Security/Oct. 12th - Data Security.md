



There was going to be a quiz next week, but it has been postponed.

The quiz is a week from **Thursday**, so in two weeks. We will have a big assignment, which forces us to use different data types.


Quiz Notes : 

[https://nscconline.brightspace.com/d2l/le/content/280886/viewContent/4225350/View]

Reference Manual :

[https://nscconline.brightspace.com/d2l/le/content/280886/viewContent/4234200/View]
Ron has placed some links on Brightspace. There are concepts we need to know for the quiz. 


We have been using **INSERT** to enter data in the table. Ron recommends the **LOAD DATA** command, which you place all the data in a textfile, and then it does it in one go. This is how we would do it in our career. 


We also have the **SELECT** statement to retrieve data. 


We have : 

- How to load data : 

[https://nscconline.brightspace.com/d2l/le/content/280886/viewContent/4294547/View]

- **SELECT** statement video : 

[https://nscconline.brightspace.com/d2l/le/content/280886/viewContent/4294470/View]

-**ERD Diagrams** : 

[https://nscconline.brightspace.com/d2l/le/content/280886/viewContent/4294397/View]



**Blob** :

	Binary object. Allows you to add pictures for example into the database. When shopping online, the product would have multiple photos of it. The photos are stored as a **Binary Blob** within the database. 




When constructing a database , we are making a repository of knowledge. We start with **Raw Facts**, which tend to be disorganized. You could record the weather everyday, and eventiually yuou want to use the weather information. We have to be able to arrange the facts in a way to address them, query them and represent them. So, we take **Raw Facts** and turning them into :

**Raw Facts --> Structured Data -->** **Information --> Decisions**


We take data in order to produce **Information. 


In order to have good information, we need good data. The good information allows us to make decisions.

We place all of these things into a **DBMS** like MySQL, where we can have multpiple databases. Keep in mind that because we are working in relational databases, with relations between data, we can say it is a **Relational Database Management System**. 


Ron wants us to think about what goes into a *DBMS*


We have : 


Databases 
	Tables
		Records
			Fields
				Data Types
					Constraints ( not NULL, etc)

This is how we see the database. There are a lot of things in the background. Keeping track what is inside the DBMS. The information on the tables themsevles, and how they relate to eachothr. We have **Primary Keys**, which have **Constraints**, so the database have to keep that in mind. So Primary keys have to be NOT NULL. 


Foreign Keys add a lot of complexity. A Foreign Key is pointing to a Primary Key in another table. If the other table does not exist, the DMBS will give you an error. There is a whole proccess we have not discussed which is if you have a foreign key defined as a primary key in another table, and they delete the table, you can use **Cascade**, so if that happens, foreign keys will give errors due to the missing dependencies. 


Imagine the necessary programs running into the DMBS to take care of that. There is a tremendous amount of overhead work to watch what you are doing. All of this is known as ... **Metadata**



Metadata 

	Data about Data


We have metadata all over the place. If we send something via email, the file is the data. If you are visiting a website (CNN) the story is the data. The packet has other things besides the file, such as your MAC address, the size of the packet in bytes, and all this is part of the data you are looking at. 


When making a phone call, the phone company keeps track of all the information pertaining to the call. All this is metadata, so it is data about data. 


You might think, and you would be wrong, that this increases all this complexity, increases the security risk of your information, so it is easier for a malicious actor to do something they should not do. The opposite is true. Havin8g all this information in a DB<MS where it keeps track of all that happens. If we keep it as a text file, there is a high vulnerability, as nothing is watching it. The DMBS is looking at your SECURITY. Are you allowed to view it, or change it? It is all part of the metadata. Using the DMBS to store information , we are getting an increased level of security by taking advantage of the security features provided in the DMBS. 


The text file is protected by the Anti virus for example, but if we know more about offensive security, it is not much protection. 


We are doing **ERD** diagrams now when we are trying to figure out the databases we are making. If he is going to help us with it, he might look at the way we build the ERTD diagrams to see if it makes sense. All he needs to do is to see a *high-level representation*. So : 



Course 
--------------

PK    | Primary Key 
---------------------------------



He wants to spend time with this design, to see if we coded it ourselves or have a developer make it. When Ron will give us an assignment, here is how he wants us to do : 


Assignment instructions is equivalent of business roles. A good designer who is customer-facing is really good at getting information from the customer. "Tell us about waybills ..."  you have this conversation to discvoer the business roles. The designer now draws the ERD diagrams. They do not know which language will be used to make it happen. This way, he can design the ERD diagram, present it to the customer, and run it by them. This is akin to an architect presenting the blueprints for the house. If we are doing the assignment, whichi indictaes to draw an ERD diagram, which is way before coding. We hhave to work with a blueprint. When designing a network, we can make designs like in Packet Tracer. 


From here, we take the ERD diagrams, hand it off to Coders, Development section , and then they produce a complex database with tables with relations keys constraints etc... We do not want to go this far, and create a database with all those designs in it, and then show it to the customer. The customer has no idea about programming. The first thing we will show to the customer is the ERD diagram. "Does this make sense?  Does it fit your needs? "


The quiz will be Database concepts, so this is what we have discussed. 


Ron will do something in future years, which is to get the students to make a video of themselves involving what they want to learn, and what they know. After 30 days, he would ask them to make another video. 


Ron is trying to keep us from suffering, so checking out the mentioned links earlier will cut down on our suffering. 



#### Relationships Between Tables




STUDENT  ------------->     COURSE 



**Cardanality** :

	A student can take many courses  



Could you have a student registered in school but taking no courses? Yes!

Students can take Zero or Many courses. Let us say we have a rule that we can not be registeredi n a semestar without taking a course (for example). We have to take at LEAST one course. That means students take AT LEAST one, possibly many courses, but NOT zero.


Each semestar, a student MUST take ONE COURSE, but can NOT take more than one course 

One and only one 
|   |    --> looks like a telephone pole (students must take one-and-only one.First line is the minimym, and the second line is the maximum). 

This is derived from business rules. 


Deans says "Student must take one course ", we add a |   and a maximum of | 


1 to many    |   <

You MUST take ONE course, but you can take MANY



Departments have chairs. Michael is tyhe chair of the department. a person can be a chair of ONE department, but every department has to have AT LEAST ONE CHAIR. So this is an ecxample of one-to-one |--|


In our practuce database, a student can tyake many courses **<** . Each course can have MANY students (<)


Each student can take MANY courses. 


When trying to figure our cardinaility , position yourself by the first take, ask yourself "for each record/student, the student can take one course? many? no courses" ytjemn you decide on the cardinality. Go to the second table, and you ask the same question. 


If Ron is teaching a class with just ONE student. A course can have one-0to many students. I to < . 


Many to Manmy relationship >< 


Can we code this ? NO! You can not code MANY TO MANY relationship. What do we do? We put a **Bridging Table** in there 



Table -----<Table> ----Table


Each student can enroll in MANY courses


Each Course can have MANY enrollments. 


We can not code MANY TO MANY because the foreign and primary keys will not work.



We started with **RAW FACTS** --- processed into -- DATA --- which produce Meaning --- Information 


We can take disorganized facts, put some structure into it, and turn it into structured data. 


What is a **Record** made of? **Fields**. 



This is all leading itno your quiz. He is trying to summarize things we learned in the last month. 



One thing to consider when building a table, an **Entity** is a noun.  


Entity-relationship diagrams , relations are turning into an entity. 


So the place is the verb. Entity relationship diagram , whcih is the verb? relationship 


If everything made sense, we should get a 100% on the quiz. It is not difficult, as it is just concepts. 


If we start with **Raw Facts** procces s them into data, we get Infotrmation . 



A database is made up of Tables, tables made of records, recordws made of relations of fields, can we code many to many? anything wrong with many-toman y in ERD diagramn ? no / Crowfoot notation --> cardanility . 


A faculty member can ONLY work for ONE department. What is the relation between faculty table and the 



faculty tabvle                             department table 

                      |    ---------                    | 


We do NOT use plurals. We do not call it departments, just department 


There is nothing wrong with one-to-one. 


Many faculty   >     ----------------        |        one department 



A department can ONLY have ONE chair, faculty member can be a chair of ONE department 


|                --------------            |




This is all we need to know to get 100%, so he expects us to get 100%. 


ROn uses quizes to make sure we are studying. Most of his quizes are open book (if he used a textbook). Since there is no book, it is just a temperature check. Ron is more concerned with the outcome of assignments. Alot of Ron's courses, except cyber crime due to research, if we are set in a creer in psychology, one of the first courses is a survey courser, which is "This is all about your discipline"


We have one survey course, which is cyber crime survey. The other cpourses; adssignments are hands-on. We have to be ABLE TO DO SOMEthing , and not just talk about it. He tries as much as possible to give 100% on assignments. The school hates that. This is an outcomes-based-college, and we either we can do it or cannot do it. Ron took a course on marking, and Ron asked "Why are we doing marking?" it is like binary. 1 or 0. The marks are there becauset he comm8unity insists that they do. Failure - 60 - 75- 100. There weren't any marks between them. He will do his best whenever we get an assignment that we are ALL able to do it, it is not necessatrily we get 100%. The assignment shows effort. 



