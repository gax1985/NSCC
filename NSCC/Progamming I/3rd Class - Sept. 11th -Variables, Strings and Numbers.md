


### Variables 


What is a variable ? 


		Something that holds a value or information. It is a container, a box , or something that holds something. While coding, if I want to output a value to a variable, I have to access it. Name = something, we would use "Name". print(name) would show its contents. 


If we need to hold more values, we would create more variables, each containing a value in it. 


If I want to see what is inside the variable, we would reference the variable by name.


	name = input(what is your name?)


We have rules (nice to do):


No spaces 

	How did we tackle it?  Underscore

Case-sensitive 

	It is different to name a variable "Cat" or "CAT" rather than "cat"

We can not start with a *number*

	We can not name a variable "1star" , but we can do "star1"


We should be *descriptive* , but not too long

	favouriteSign , not yourFavouriteSignInTheHoroscope

Use a casing **scheme**

	camelCasing --> starting the first word with lower case, and additional words start with a capital letter
	PascalCasing --> capital letter at the beginning of each word



Which of the following would we think make good names for variables? 

1. Variable1 --> not descriptive enough
2. First name --> not good due to spaces
3. Date --> it is good enough, but would be better to be more descriptive. Too generic at times, and might be reserved in the programming language. Try to avoid common words to avoid variable name clashing 
4. 3Name --> cant start with a number
5. DOB --> might be good if we know what it refers to
6. DateOfBirth --> better than the previous one
7. YourFavouriteSignInTheHoroscope --> too long


###### Combining Variables and Strings 


We can do so with the plus or + sign


###### Manipulating Contents of a Variable


Variables allow you to manipulate the contents of a variable

>message = "Hello World!"
  print(message.lower())  ---> lower case
  print(message.upper()) ---> upper case 
  print(message.swapcase()) --> swap cases between words
( ) --> indicates that we are modifying the variables

*print* is a function, inside the 1st (  ) the function receives a parameter, the 2nd ( ) get the content of the variable and work with it. 




In BrightSpace, we have Python Program Code Template. Click on it, and it is a start point for every code that we have. 



### Numbers


###### Common Operations


 "+ Addition"
"- substraction"
"* Multiplication"
"/ Division"
"% Modulus "


Keep in mind the **order** of things! We have priorities!


###### Order of Operations 

( ) parentheses

** exponent (e.g , **2 squared ** cubed)


total (10-6) / 2 + \                                                        (Backsplash , if we do not use it, we will get an error, ) 
6 -8



What is wrong with this picture ? 

	#input section ad declare variables
	salary = input("what is your weekly salary? ")
	bonus = input("What is your bonus?")

	#processing
	totalPay = salary + bonus

	#output section
	print(totalPay) 

It took the input as a string, thus it grabbed the two answers and stuck them together 2000500 

Input statements takes *strings*

When we use strings with the + sign, it puts them together


We can convert values with *functions* to convert from one datatype to another!

int(value)  ---> converts to an integer
long(value) ---> converts to a long integer 
float(value) ---> number that holds decimal places
str(value)    ---> converts to a string


Which function should we use? Since we might have fractions, it is best to select float


We can fix the code in two ways : converts the value on the spot with the float method , or , we can do the conversion later.

Integer vs long Integer ---> longer numbers


Here is how we can fix the code :


Try it without the latter conversion : 




	#input section ad declare variables
	salary = float(input("what is your weekly salary? ")
	bonus = float(input("What is your bonus?")

	#processing
	totalPay = salary + bonus

	#output section
	print("The total pay for the week is $" + str(totalPay)) 




TO DO : 
===========



Prepare for Tech Check #1 

	Inout-Processing-Output
	Number and String variables and Conversion

Practice : 

	Create programs for :

		Restaurants:
			12% of restaurants in the US are pizzerias
			There are 70000 pizzerias in the US
			** Calculate the estimated number of restaurants in the US

		==================
		Possible solution:
		pizzerias =0.12 X number of restaurants

	70000 = 0.12 X number of restaurants

		Thus...

		number of restaurants = 70000 / 0.12

------------------
			
		Pizza
		Population Growth

Quiz on : **Variables**, **Strings** and **Numbers**





