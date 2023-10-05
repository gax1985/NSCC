


Student 

 PK           stu_id              INTEGER
                 stu_name       VARCHAR
                 stu_dob           DATE





Faculty 

PK         fac_id           Integer
             fac_name    VARCHAR





Course


PK          course_id      INTEGER
              course_name  VARCHAR
              course_full boolean




Class



PK        class_id       INTEGER
            class_day    VARCHAR
            class_time
            class_room  VARCHAR

FK        course_id
FK        fac_id 




Enroll



PK,       FK      class_ID
PK,       FK      stu_id
                       class_day  VARCHAR
                       class_time
                       class_room
FK                   course_ID
FK                   fac_id



Note : 

Whenever we reference a field in a table :



If we are in the STUD table, we select a field called "stud_nam". The reason we can do that ( a field in a table called stud_name), the actual name of that is not stud_name (much like your phone number being the 7 numbers because everyone had an idea to add the area code. In Pictou, you used to be able to dial the last four numbers. Now the area code is needed), stud_name's actual name is student.stud_name



Students are wondering how to link fac_id in enrollment to fac_id in Faculty. Something like : 


select fac_name   FROM enroll,faculty 

where enrol.fac_id = Faculty.FAC_ID; 



We can say : 



select faculty.fac_name   FROM enroll,faculty 

where enrol.fac_id = Faculty.FAC_ID; 


This will give the names of all faculty 



local field name = tablename.fieldname






Look into **INSERT** statements in W3 Schools 




#### My Method


###### 1. Create a Table : 


>CREATE TABLE student (
>stu_id int NOT NULL,
>stu_name varchar(255),
>stu_dob DATE,
>PRIMARY KEY (stu_id) 
>);