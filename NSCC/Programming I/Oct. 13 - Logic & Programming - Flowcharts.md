


## Flowcharts 


- This is to map a specific business process, and we are mapping it out before SUDO Code and Coding. 
- We are trying to understand a specific process. For example, if we wish to understand how grading happens at NSCC :

	1.  We have students
	2. We have courses
	3. We have grades. If grade > 60% , then PASS!



We design it to understand the proccess. We can think about it in terms of writing *pseudocode* resulting in understanding!




Simple real world example : 




![[Pasted image 20231013104323.png]]

Oval shape : where it starts , and where it ends
Rectangle   : The act of checking for traffic 

aftetr getting the info, decision time 

Is the bus coming? yes , then see if it is stuck in traffic , then 

Is the bus coming? no



We can have different colors, to make it easier to comprehend. All the diamonds are conditions to test


Rectangle - Actions being taken at that specific time. 


example : 


![[Pasted image 20231013104640.png]]



Do NOT make it way too complex. 

![[Pasted image 20231013104757.png]]


![[Pasted image 20231013105002.png]]
This is a real-world example of an excessively-confusing flowchart , which poses some questions : 

1. Where does it start? 
2. Where does it end? 
3. How many days did this take?

We make a **Sub-Process**. We place it in a black box, and give it a name. 



> [!example] 
>  A simple Flowchart for our commute to and from NSCC. 
>  
>  **Steps :** 
>  
>  1. Wake up 
>  2. Shower 3
>  3. . Brush your teeth etc
>   
>   A lot of steps! 



Flowchart for our commute to and from NSCC. 


Steps : 

1. Wake up
2. Shower 
3. Brush your teeth etc


A lot of steps! 


Instead of throwing all of this, we can create another Flowchart for that specific process. 





Whenever we have :

1. Oval shapes : start/end
2. Rectangle : action
3. Diamond : Decisions





#### Visio's Steps :


1. Create a "Basic FLowchart"
2. Let us select the Oval shape to indicate the **Start**
3. Add a rectangle pertaining to the **Action** "Ask the user for the deposit amount"
4. Add a diamond shape pertaining to the **Decision** "Is the amount over 100?"
5. Add a rectange for the **Action** pertaining to the outcome of the previous *Decision* "It IS over 100"
6. Add a rectange for the **Action** pertaining to the outcome of the previous *Decision* "It is NOT over 100", which is "Display 'Have a wonderful day!'"

> [!info] 
>  If we have something to add, which is if it is over 100, they get a free toaster. Do we need another diamond ? No!

7. Add a rectangle for the **Action** pertaining to the outcome of the previous *Decision* "Get them a free mug!"




If we have one question (True of False), we would have something like what we have done.
If we have nested IF statements (if we are checking for Fresh Coffee if it is Monday), this would be a **Diamond**, followed by another **Diamond**.


> [!todo] 
>Do a flow chart for **Shipping Charges** and **Hogwarts' Sorting Hat   


###### Shipping Calculator 

>[!example]
>Ask the user to enter the amount for their total purchase. If their
total is under $50 add $10, otherwise shipping is free. Tell the
user their final total including shipping costs and format the
number, so it looks like a monetary value.

> [!todo] 
Don't forget to test your solution with:
>1. a value > 50 
>2. a value < 50
>3. a value of exactly 50
 





**Answer :**

![[Pasted image 20231013114200.png]]



##### Hogwarts Sorting Hat


> [!example] 
> Write a program that generates one of four random numbers. If
it's the first number, the program will display a message
indicating the user is assigned to *Gryffindor*. If it's the second
number, assign them to *Hufflepuff*. If it's the third, it's *Ravenclaw*.
If it's the fourth, they're in *Slytherin*. 




**Answer :**

![[Pasted image 20231013113919.png]]
Who do we have **one** diamond instead of *four*? it is because we have one decision, which yields four different results



question : What if we ask the student for their last name ? the hat then decides to pre-define students to their respective houses (making each student's life into a sheer hell)



##### Hogwarts Sorting Hat


> [!example] 
> Write a program that assigns students to their respective houses according to their last name(the head wizard of Hogwarts bribed the hat). If
it's the last name is *Potter*, the program will display a message
indicating the user is assigned to *Gryffindor*. If  the last name is *Melfoy*, assign them to Slytherin.












> [!important] 
> We have a **Tech Check** next class! 