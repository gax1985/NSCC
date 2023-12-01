


Pi Symbol 
Sigma 


TT (lowercase R.A, R.E) (Sigma(aka sigma) > 2(Relation-Think Table))

PI





Tables 

R Table

A  B  C 

1 2 3
4 5 6
7 8 9 




(In Math do the stuff inside the perinthesis)


(Sigma R.A > 2 (R)) 

every query in mySQL returns a table. 


If we are to do Select R.A > 2 : 


4 5 6 7 8 9



S Table

D  E  F 
1  2  3 
4  5  6
2  8  9


Sigma R.A > 2(R)









Inner Join

R X S 

SELECT R.B, R.C,S.E, S.F
FROM R inner join S
ON R.A = D.A






JOINS are a fundamental statement in use all the time when doing queries, joining databases , etc ...

Sometimes we did a SELECT Join where we select column from multiple tables and display them as a result. We can do this with a JOIN statement. 


Remember in highschool Algebra, where we would be asked to reduce the mathematical equation to its smallest form. 


Most companies we would work for would never ask us to do relational algebra, or make databases small


We should go to W3 Schools , where they have exercises where we can try JOINS.



We are looking at Inner Join, Smaller Join, Cross Combine. 


We want to combine R and S to produce a final result. 


SELECT R.B, R.C, S.E, S.F from R InnerJoin S on R.a=S.D

This will produce a new result called T, and it will have the columns that we listed here 
(R.B , R.C , S.E , S.F --> Due to them being listed in the SELECT statement)


R inner Join S on R.A = S.D

Which rows R.A = S.D



R.B   R.C    S.E   S.F




Starting from R innerjoining S, we want to find rows where R.A = S.D  :



JOIN And INNER JOIN are the same thing 

Symbol :  |X|



to match : 

The name of the column has to be the same (with the same name ) 
domain of the column has to be the same ( exactly the same type of variable)


Most of the time, we do not do that for a couple of reasons : 


1. We need to be explicit about what the program will do. The intentions has to be clear, such as adding two variables for example. 
2. When using JOINs, place the ON condition in




LEFTJOIN/Left Otter Join =X| 


The symbol looks like open arms pointed to the left side.  


R =X| S  (everyone from R gets to go, S depends on the condition)






How might we use this ? 


Let us say , that instead of A B C D E F , assume the table STUDENTS, and the table COURSES, and we have STUD_ID, COURSE_ID (in the STUDENTS), and COURSE_ID and COURSE_NAME (in the COURSES table). 

Some students registered for courses already (Student 1 registered for course 1,  student 2 has not registered )






We want students who registered for the course. We need student ID and course name, and we want to use JOIN to do it. 



Let us try the select statement first : 



SELECT the two things we want to show : 

>SELECT STUD_ID, COURSE_NAME

>FROM STUDENTS JOIN COURSES
>
>ON STUDENT.COURSE_ID = COURSE.COURSE_ID



If we want to see COURSES that do not have any registered students: 

We want course names that are NULL in some circumstances

We can do a LEFT JOIN from COURSES


If we do : 


SELECT COURSE_NAME 
FROM STUDENTS LEFTJOIN Courses
ON Student.Course_ID = Course.Course.ID






============================



SELECT  Courses.COURSE_NAME, 

FROM 

		(SELECT COURSE_NAME, STUDENT.COURSE_ID 
		FROM STUDENTS LEFTJOIN COURSES
		ON STUDENT.COURSE_ID = COURSES.COURSE_ID; 
		AS T (it means that the entire result is to be known as "T"))


WHERE T.COURSE_NAME = NULL; 


Every Query Returns a **Table**


If we want to return the *course_name* that has no one in them


SIMPLIFIED ....



------------------




SELECT STUDENT.COURSE_ID, COURSE.COURSE_NAME 
FROM STUDENT LEFTJOIN COURSE
ON STUDENT.COURSE_ID = COURSE.COURSE_ID
WHERE COURSE_NAME = NULL;


---------------------------------




## CROSS X 




CROSS JOIN or aka CROSS-PRODUCT 


RESULT :

T (ALL THE COLUMNS FROM BOTH TABLES)


T.A          T.B          T.C       T.D       T.E        T.F

1              2               3          7          2           3 
1              2                3         4          5           6
1                2               3        2           8           9
4                  5             6 

There is NO MATCHING CONDITION


Each row from the table on the *left* is paired with the row from the table on the *right*

Number of rows in the results = 3 X 3


WHEN you do a join, temporarilty the database does a CROSS PRODUCT, then SELECTS temporarily the Cross Product. 



JOIN = CROSS THEN SELECT (Gigantic Result, Only selects the data matching the condition)






The syntax for LEFT JOIN and RIGHT JOIN is different






CREATE A SINGLE TABLE DATABASE, where it would include my records collection , artists, albums, descriptions. The challenge is to create a single table database for my own use, where we would use it most likely on a personal basis. We might have commands from various programs that we are using in our courses(like things I have difficulty remembering). It would be something that would start my own personal MySQL database that would grow over time. 


Topics : Birthdays, Christmas presents, Wishlist, Tablet Options


The idea is to maintain *database awareness skills*, and he will try to put one little database with each course that he is teaching us. He had a conversation with 2nd-year students, and they mentioned that they study MySQL in the first year, and then never touch MySQL again. So, it would help to take all the basics that we have learned in the Data Security course, and reflect upon how much we have learned. We want to keep track of our newly-gained knowledge. Ron will try to add things like that. 

> [!todo] 
> Try to find a fun, single-table database to use for our own lives
> 

> [!todo]
>A second-year student has built a little network that he has set up at home to practice networking. We need something to maintain all the knowledge we have gained. 



> [!warning] 
> He will do *one more assignment*, and **Two Quizes**. The assignment will involve JOIN, submit queries, take screenshots showing what you have done. The quizes will be simple. The things we did not get to will be covered in other courses. From a security perspective, we spoke of *Roles Rights and Responsibilities* , where we define what the person can and can't do. MySQL Injection is difficult to cover in this course: we have just learned it, and SQL Injections involve web applications, which we have not touched yet. 
> 



> [!important] 
> Next semester, we will cover **Linux Scripting**. 



If we know how to do a FOR and WHILE loop in PowerShell or BASH, we would know how it works, but the syntax will be different. Brian will be teaching us Server Exploits. Brian works for Gran Thorton. 


Everything we do next semester will be built on top of the knowledge we have gained this semester. Next summer, all of our lives will change. Next summer, we go to the work term, we get first taste of what it feels like to work, and some will come back and change courses, or would have a new interest they would like to pursue. 



