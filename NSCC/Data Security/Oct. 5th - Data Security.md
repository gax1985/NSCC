


Start putting some data in each table!


three of four students in the database, add some instructors to the data base
add class times

Enrollment database

With with : 


INSERT 


Order matters ! 

Observe : 


>/* to specify which columns to add the values to, order matters! */

>INSERT INTO table_name (column1, column2 ,column 3)



Another command to try : 


>ALTER TABLE tablename
>ADD column name datatype;
>ALTER TABLE Customers
>ADD Email varchar(255);
>ALTER TABLE 



Turn it into FOREIGN KEY first 



#### Differences between Strings and other Variables


If we have a field in a table ( a record, fac_id ), and it is of the type **INTEGER**, and it is a **PRIMARY KEY**. 


FACID INT PRIMARY KEY

fac_name VARCHAR(253)


INSERT INTO FACULTY (FAC_NAME)
VALUES ('Ron'); (strings go in '   ')

(this is a brand new table, with nothing stored yet)

We can not put a value in a record, and not have a primary key in the same record (remember : if declared PRIMARY KEY, it also has CANNOT BE NULL)



- what is wrong with the following statement? 

> INSERT INTO FACULTY (FAC_ID, FAC_NAME)
> Values ('1','Ron');




He is trying to put a string ( a character), this is not '1'. If placed in (1) it is like an image. We need to put a number in as a number!



ALTER *TABLE*


MODIFY *DATATYPE*




#### Retrieving Data


This is asking a question : **QUERY**

> SELECT 


SELECT means : "Show me everything = * "

so : 


> SELECT * FROM (TABLENAME), 


In W3SCHOOLS, go to SELECT Statement 


If we do NOT want to see all the names, we can do the following ; 

> SELECT fac_name FROM FACULTY;


This is NOT the real name of the field, but this is an abbreviation. The actual name of that field is : 

>SELECT faculty.fac_name FROM faculty; 

(This is important, because we will get into more complex situations involving multiple tables later on).



Hypothetically, give me a name from a faculty member : 


We could : 


> SELECT * FROM faculty;


or :


>SELECT fac_id FROM faculty WHERE fac_name (comparison operator : simplest one is "=" )



Hypothetically, what if we would like to retrieve data from two tables. If we need to find the name of faculty "amber" that teaches two classes. 

Ron would like us to build this query : 

We need faculty table and the class table 

We can retrieve info from a Foreign Key , which will lead to the other table where the value is a Primary Key

HINT : If you want to test it, look for faculty members in your faculty table where teachers are not teaching classes 

Go to class table, for each fac_id, get the name 



>SELECT faculty.fac_name FROM faculty WHERE class.fac_id=

(When you make a spelling error, and you have an error "No faculty name in the table", and you get surprised because you know you have entered the information. Your brain expects that you have typed the right thing in. Your colleagues have a fresh perspective, so they spot the spelling error. When we review lines of code, we are not actually seeing with our eyes, but with our brains. Our colleagues would see the error with their eyes.  When writing an assignment, ask someone to proof-read it for you, as they would have a neutral perspective).

Solution : 

>mysql> SELECT faculty.fac_name FROM faculty,class WHERE class.class_room=NULL;

###### Ron :



There is something wrong with the Database design. We do NOT Want to type the same value in the same table. It makes input errors possible,, and creates an ANAMO:Y. Unless it is a foreign key, we do not want the same value in multiple tables, and we DO NOT want to have the same value in multiple records. 



If we are doing a database, and we are entering student information , and we are entering the country of origin, It would be redundant to keep entering CANADA. Or if someone would actually enter CANADA as CADANA, then while retrieving this info it would not appear. 

If we have a second table, that indicates COUNTRY : _________ . He was teaching a class in SMU, where he used a permanent marker accidently there. If we have a country.countryid, we can have a foreign key with COUNTRYID. We can retrieve the information by using the country id. This makes searching better, and it is a good way

Ask yourself : are there fields in there we can remove, to make things smoother and better? Please ponder this question deeply. There is a possibility that he  needs to schedule an appointment for himself on Tuesday, as he could very well not be able to come. He will leave us with some tasks. He will contact us over the weekend. Next class, he wants to propose changes to the database. 


A VALUE SHOULD BE IN THE DATABASE only ONCE. 

for student_name , it only appears once in the class table. How do we differentiate between students in the students table? with the student ID. We can have two students with the same name, but if we have records for one student, we would not have their name in multiple locations on the same table. 

Check out W3Schools 



He has not modified the course shell in Networking Class since taking over from Marie. Ignore the assignment due dates for now. He will change everything. 


Hint : We can use the UPDATE command to update a specific field. In the second half of the class, we will use the WHERE command. 




If you take the VOLCHERAN SECURITY TRAININGH, which should be available, there is a hint to "Not leave the computer unlocked for longer than 5 minutes "


Trick question : "How long should you leave the computer unattended"?

Course mentioned 5 Minutes, but in truth , the answer is Never! So, he had an issue with security awareness training delivered that way, where you have to score 80% on a multiple-choice test that has unlimited retries. 