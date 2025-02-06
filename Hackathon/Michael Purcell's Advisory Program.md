He went into a 2 year program, and it was cohort based. They did 6 courses and moved along. Today, we still have 6 courses, but you may not always take 6 courses. If any have been in an advising model, and how to move forward, it is all manual. If he has 10 students, it is easy. If we have 100 students, it gets tedious.

He gets transcript, passing success mark , and then move along into a two year program. He needs the data brought in, and it is more of a conversation about the plan, and the plan goes to the registrar.


>[!todo]
>
>- [ ]    


Questions : 

1. In what we format do we need the transcripts to be ? (Peoplesoft)



He goes manually into folders 34-35 , he would suggest that we do not want to look at all the programs, and to simplify it a bit. He would open a page :

Program Name
Year #

All the courses as listed.


If someone failed a course, Michael would copy all the plans, place them into the students folder, then the admin would go to Peoplesoft, grab the transcript of what they completed so far, and he needs us not to scrape data from those. He would open the transcript, the plan, as he is advising and talk about how they are successful and how he could help, go over which course the student passed , and indicate the course that the student has failed. Visually his method is effective, but it is too much to do this for 100 students. That is his advising method. 

When the advising is finished, what we want to do at the end of the meeting is to have a plan that looks like a table : 

courses this semestar, courses next semestar 

Everything is blocks, and he would type in the information manually 


Total units of courses enrolled, and the scheduling would schedule the course for the students 



Demands :

take the student at the start, figure out the academic plan (24/25) , assume any student that starts with one of these plans, one column required courses ( originally blocks ), and we need to populate Off-Sequence  sheet


Put the academic plan for the program you are using in a table/database ( all the needed courses for cybersecurity ) and then download all the courses that someone needs to take in order to complete the program.

Search by ID, and the student's information populates. He would like to get some format where we have the student ID, student name , courses taking now, courses they need to take, and sketch it in a way to provide the information clearly. If you are approcahing it from Systems Design, you would not do a build and test, but he also included grades for 1200 courses. He has a sheet where every grade is recorded in, so he needs it to be the source to output the **Student's Grades**. The source of the data is a Report from Peoplesoft. We would not be pulling from Peoplesoft, and he manually gets this spreadsheet. The spreadsheet is filled with pseudodata, which we will use to see the format of the Excel rows and columns. The Peoplesoft sheet is every course that a student has taken at the time he ran the report. 

The next semester, we would run the same thing, except we would update the information. It is only active students, and it accounts for failed and dropped courses as well. 


Term is what date it is from | 21 is the year | Fall Start 8 | 5 is spring | 1 is January / Winter start


Course code is mandatory !
Course Title 
Student ID is mandatory 
Student Name
Grade 
The Program They are In


We could do the data by Semestar, but maybe we want to import the ADVISING MAP Table (PDF to look at) and if we distill that into the courses + Import Completed Grades



Completed - all courses | Current Semester | New Semester | 


He needs to be able to edit the plan. He is happy to manually do things, but the document needs to be in a way that he can input data. 


Usability and Presentation 


If we failed one course, where should it be placed ? should it be a different table for the failed courses? --> Michael's Response : For each student, the easiest format for this is Input The Course PLan , as you get Grades Enter Them,. He checks what is missing, and above that he has current semester




#### Flow - 2nd Time:


The problem :

He has the sheet pre-populated with what the plan looks like. The old method is problematic when a student fails a course, and he would cut and paste


Needed :

Block : Current Semestar
Another Block : Previous Semester


Excel Spreadsheet : Does it account for any currently withdrawn students from the course? Michael : It will account for a withdrawn course 

Michael : It would be everything to date from the time the student is active. The PDF Map for 2022 is different. 

We need to account that the map will change.

Question: Alternate Pathways --> There were arrows from some courses to another. If one course is red (failed), the next selection would also be read ( visually indicate a blocked pathway). In the map, does it show which courses depend on the other course? 
It needs to be useful for the people to solve. The first solution would be to have an automated view of a dashboard of a pathway. The second would be to know which other implication ( if this is red --> This is red --> What is the alternate option? )


Michael : He would like to see : 
1. The plan that will go to the registrar ( current semester ) : he needs the previous info, and thus he manually gets the transcript ( fetch the transcript)
2. Where is the students that failed courses ? He does it via Excel Query 

	A system that is quick advising 


Question : The interface we are looking at , what is the format needed? 


Michael : What they need to see is : see the history for courses + what needs to be registered right now ( map piece instead of going manually and downloading the document). The act of moving things around is more time than advising. 


Map : 2022/2023 Data . We have Fall and we have Winter. If we come up with a model that works, it needs to be adapted going forward to the new year


Question : In the Excel sheet, is the required courses listed? 

Michael : In a one year program , we have the **Fall**, and **Winter**. You will have two files for each program : **Year 1** and **Year 2**


The arrows are indicative of the pre-requists. 


The map is not in a spreadsheet. 

 Peoplesoft is the source of the data 


Michael : The only time we will have **Final Grades** is at the end of the semester. This would be every course taken since the student was active. 

Michael : Ultimately, we need something we can *Send to the Registrar*. If we are in a Diploma Program, the four fields would be every semester. The Registrar needs to place the students in the needed six courses. Ideally, focusing on **How can I advise the student of what they have *completed*, what they *need to do*. 

Michael : Completed Courses  (+ Grade-if passed)| Incompleted Course

Michael : at the end of every semester, he will pull the file. We will not do anything on Peoplesoft's side. He would like to know (bonus) : how do we get an advising plan , who passed , who failed , which courses completed, and which courses need to be completed. 
you would pull data from the spreadsheet, and each semester, for whichever format you use to make this form, you need to pull the data from it. Which students are on track ( from the list of all the people who completed courses), and which courses failed courses . **Who does need to see-list +  who he does not need to see**? 


Note : if he is calling up student records, he has one particular thing in mind. He does not care about two semesters ago. He does not need to see it every time. 

Question : If you are advising a student :  Name --> What classes are available to fulfill+ the requirement --> what classes are needed? Which information you want to see immediately ? 

Answer : Column of all the courses needed in the program
some of them have grades
courses not completed 

Completed | Not completed 


It should be movable like a Kanban board.  He pulls up the little map thing, and then he drags and drops the needed item. 


Question : What do you want displayed ? What are the courses completed  | grades  || What are the courses needed 


Question : 