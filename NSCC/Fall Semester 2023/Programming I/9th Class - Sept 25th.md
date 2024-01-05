

#### Sept 29th Due Date for the Assignment + Tech Check 2


Today we handle **Decisions** within a programming context.


#### The choices we make depend on different conditions!


You need *elements* to make a decision!

Ex. If the user maintained a bank account with a balance over $1000, take away *Transaction Fees*


We call these a **Condition :

Any statement that is either **True** or **False** 


AI Question : What is a Bolean in Python? 






If we want a variable called *answer* , and you want the script to do something when a user responds with a specific answer, then it is an **IF Statement**. It is usually a comparison !


If the expression we are doing is true or false, we add lines of code that I want to be executed if the statement is *true*



We can evaluate individual statements in VSCode by right-clicking on the statement, and then selecting "Evalute the Statement in Debugger "


If we add the following line beneath the *if* statement : 


>answer = input("Would you like express shipping?")
>If answer = "yes";
>		print("That will be 10 dollars extra!")
>print("Have a nice day!")   ---> will this statement be displayed if I entered "No"? 
>
>**YES**... Because the indentation is not the same as the *if* statement



Another variation : 

>answer = input("Would you like express shipping?")
>If answer = "yes" or answer == "Yes" ;
>		print("That will be 10 dollars extra!")
>print("Have a nice day!")   
># Adding "or" adds other possibilities for the *if* statement 




>answer = input("Would you like express shipping?")
>If answer = "yes";
>		print("That will be 10 dollars extra!")
>print("Have a nice day!")  
>		print("Will this text be displayed?") ---> NO.  The previous line "print("Have a Nice Day!") with its indentation breaks the *if* statement. If we execute the code, we will get an error, as this indentation starts another  block of code!
>


---> will this statement be displayed if I entered "No"? 
>
>**YES**... Because the indentation is not the same as the *if* statement




>answer = input("Would you like express shipping?")
>If answer = "yes";
>		print("That will be 10 dollars extra!")
>		print("This is some code ...1 ")
>		print("This is some code ...1 ")
>		print("This is some code ...1 ")
>		print("This is some code ...1 ")
>		confirmation = input("Are you sure you want to add $10?")
>		if confirmation.upper() == "YES";
>			print("That will be extra $10")
>			print("This is some code ...1 ")
>			print("This is some code ...1 ")




>answer = input("Would you like express shipping?")
>If answer = "yes";
>		print("That will be 10 dollars extra!")
>		print("This is some code ...1 ")
>		print("This is some code ...1 ")
>		print("This is some code ...1 ")
>		print("This is some code ...1 ")
>		confirmation = input("Are you sure you want to add $10?")
>		if confirmation.lower() == "yes";
>			print("That will be extra $10")
>			print("This is some code ...1 ")
>			print("This is some code ...1 ")




Another example involving *if* statement : 


>number = input("Could you provide me with your favorite number?")
>if number > 50;
>		print("You like large numbers!")
>#Will this code get executed successfully ? **NO** ...
>#Why? it is because it is a string! so we can fix it in two ways (as shown in class ): 



>number = int(input("Could you provide me with your favorite number?"))
>if number > 50;
>		print("You like large numbers!")


###### Or ...



>number = input("Could you provide me with your favorite number?")
>if int(number) > 50;
>		print("You like large numbers!")



The variable *number* will still hold a string ... we have to convert it each time into an integer to do math. The best way then is ...

>number = int(input("Could you provide me with your favorite number?"))
>if number > 50;
>		print("You like large numbers!"

Then *number* will **ALWAYS** remain a number.

If we have hardcoded a numerical value, as in the following example : 

>value = 100


Then we would **NOT** need to convert it to an integer ...





Another possibility : 

>number = input("Could you provide me with your favorite number?")
>if int(number) >= 50;
>		print("You like large numbers!")


It is a good idea to test edge cases with many possibilities.


###### Strange Example : 

>total = 99 

>if(not total >= 100): 
>	print("This is true")

The NOT flips the statement, same with !


#### Comparisons Operators


This will include : 


	== Equal to
	!= is not equal to 
	> is greater than
	< is less than
	<= is less than or rqual to 
	>= is greater than or equal to
	

In other languages, we can *negate* a value such as the following : 


	(!(variable))


But this does **NOT** work in Python...



##### Write it in the way you would say it  ... 


1. If a course is completed = send a certificate to the student

>if course_completed == "yes";

2. If  the value is less than 10 : 

>if value > 10 ; 







#### Quiz + Class Exercise



If we have a question with a **radio button** (a multiple choice-situation with four answers) then selecting the radio button will ALWAYS have just *one* answer. 


If we have a question with a **checkbox** ...

- [ ] 

then there are two possibilities !


 
###### STICK TO HUMAN-FRIENDLY METHODS!


-----------------------------------------------------------


#### Exercise : 


**Pay Calculator**

	Write a program that takes  two pieces of input data –  a pay rate per hour and  the number of hours  worked – and output the  total pay. Any hours over  40 are paid at time and a  half.


###### Method : 

1. Logically , assess the *inputs* , *outputs* and the desired outcome. 
	1. Inputs : 
		1. Pay Rate Per Hour = RatePerHour
		2. Number of Hours Worked = WorkHours

	2. Outputs :
		1. Total Pay : TotalPay

3. Desired Outcome :
	1. Any hours over 40 are paid time and a half ...
			WorkHours > 40 ;


