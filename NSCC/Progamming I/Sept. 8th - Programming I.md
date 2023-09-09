



We will dive deeper in programming , understanding our last example, and covering **Input/Output**



### Programming


We are communicating with the computer, in a manner of a conversation 

We work on a particular issue

We use high level, reserved languages like Python. Python has a set amount of instructions, and it expects input parameters. Afterwards, it outputs what it is supposed to do. 

Program:
	a set of instructions

Tasks : take an average of two numbers, check the weather for today

In every scenario, we can abstract those involved : programmer and user.


Programmer : Us!


User: someone who uses our work


It is important to consider how the coding we are doing will impact the user. 


If we are making a simple web application that produces someone's age, we would want the user to provide something. We need the date of birth. We can ask the user for the date of birth. How would you like the date of birth? which format would we like to use? we can ask the user to provide it in a particular format. We have to be clear on the input that we need from the user. 


A message is sent from the programmer to the user 

If I was the user, what message am I trying to give ?

Every problem that we will solve would have input process and an output process. 

Every program wants input and outputs the output.

The input for the program is the date of birth. The output is the current age. 

How would I get from the input to the output? --> We need the date of birth. How do we get the age. we need the date. We can ask the user, but it is easier to get the date from the system. I will get today's date and from that we can calculate the age of the user and then generate the output. 


The easiest way to determine the steps to solve an issue, determine the output! 

What do we need to get this output?

What is the process to do so? --> subtract the year, month and the day

Ex. How fast is a car travelling if it goes 50 miles in 2 hours? --> we have distance and the time. The output should be speed. To determine the speed, distance/time


### Input

An image , a line of text, fingerprint , etc ...




### Problem Solving Process



last class, we used *print* , which has (     )

Whatever we enter in the (    ) , it outputs a text in the terminal 

Variable = "NSCC"

Thus, "NSCC" will be outputted to the terminal 


We can use '    ' or "   " , unless the content we have has a quote in it. 

Ex. 

print ("It is a beautiful day!")

It will have an issue with 

print('its a beautiful day!)


Thus , use print(' ')


Multiple lines :

We can do it with multiple print statements

print("something")
print("different!")


Instead , we can do this : 

	print("It is a beautiful day!\n and it is nice")

#### Triple quotes (""")

We can print something exactly at it is written 


print("""It is a beautiful day
and it is nice!""")





We have three different methods :

print (' ')
print (" ")
print("""    """")


Our takeaway : 


We can get the same **output** many different ways!



### Asking the user for input!



If our python program is asking the user to input the name of the movie they would like to watch, 


How do I input values in python? 

##### Input 


In the same way we use the print method and passing a parameter to it, the input method receives a value in a paramter, and it will output a value, it can wait for the user to enter the input. 


When using input, it will wait until the user types something. The user hits enter after doing do, and then it will store the input to a variable : 

	name = input("What is your name?")


... and if we wish to output the name, after the user enters the name : 

	print(name)



Check this out:

We can have " " entered automatically by selecting the words, and entering " 

>def main( ):
>print('Output to the User')
>input("What is your name ?") ---> it will wait for input, but since we have not stored the information in a variable, it goes nowhere!



Thus : 

>name = input("What is your name?")


So : 

	Everything we are doing is in "main" block! make sure the indentation is the same for the content of this block. It should be on the same level. 
 
	def main( ):
	print('Output to the User')
	name = input("What is your name ? ") ---> it will wait for input, but since we have not stored the information in a variable, it goes nowhere! I added a space after the question. 
	print("Hello" + name + '!!!')