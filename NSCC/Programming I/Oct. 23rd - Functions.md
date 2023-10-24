


To prevent re-doing everything again and again, we previously placed it outside of the *IF* statement. 

Repetition can be avoided in coding. 

We have a solution ...


Here is how *duplication* can be a terrible thing : 


	def main(): 
		product_price = input("Enter the product price: $") # we are storing an input value from the user
		product_total = product_price * 1.15 # to calculate tax by adding a 15% tax 
		print(f"The final price of product one is ${product_price:.2f}") 
		
		product_two_price = input("Enter the product price: $") # we are storing an input value from the user
		product_two_total = product_price * 1.15 # to calculate tax by adding a 15% tax 
		print(f"The final price of product two is ${product_two_price:.2f}") 


If someone requested three products, we could copy-and-paste our code again : 


		product_three_price = input("Enter the product price: $") # we are storing an input value from the user
		product_three_total = product_price * 1.15 # to calculate tax by adding a 15% tax 
		print(f"The final price for product three is ${product_price:.2f}") > 
		
		
		

[!hint] 
>  A good shortcut is CTRL+D. Keep hitting it to select the next occurance. If you wish to cancel, please press ESC



If we have a formatting issue, and we want to add the comma, we would go through the code and change every occurrance manually. 


Instead ... 


We can use **Functions**!



## Functions 


#### Definition : 

...A reusable section of code that we can call every time we need it to do something. aka ... *Method*. 



We have used *Functions* before :

	print()
	int()


#### Why should we use it ? 


1. Simplification : 

		They have different names to define what they do. They break down complex blocks of code


2. Bugs : 

		Prevents bugs in the code




#### How we can create a Function ? 


Use *def* , which is short for **Define**.


We give the function a **name**. We would have **parameter names**, which explain the function.


We write the code in the body of the function : 


		def printMessage():   # def  printMessage ( brackets )
			print("Hello World!")   --> indentation is important
				return  --> Returns the value


We then do a function call : 


		printMessage()



Some of the code : 


def ShowMessage(in_name):  # we create in_name parameter that

                        # is comming into the function

    print("Hello, {in_name}")

  
  

# Function is going to receive a parameter,

  
  
  

def main():

    print("Hi")  #  ----> Indentation indicates that this is

                 #        part of this function.

    name = "Delano"

    ShowMessage(name)                

    ShowMessage("Delano")  # ---> We call this function

    #It assumes "Delano" = in_name

    # When debugging a function, we are clicking on StepInto

    #It goes to inside the function, and debugs the function with the

    #parameter that has been passed.

   # If we step over it, we are back at the main function, and

   # we have the variable name again

   # 1. Create a function

   # 2. Use the debugger to see what is happening

   # If we are creating a function, it would be outside of the

   # Main block . If we define a function inside another function,

   # it would work inside the function we created it in

   # If we want to do something different, we can change that :

def showMessage(in_name, in_greeting):

    print(f"Hello {in_name}, {in_greeting}") #if we hover over the parameter in_greeting, we see the parameter

# The order that the parameter are used in does not matter. Every time the function is called, the first parameter is stored in_name, and the second in in_greeting

def main():

    showMessage(name, "Hi")

    showMessage("John", "Hello")

    showMessage("Jane", "Goodbye")

    showMessage("Bye", "Mary")

    # if passing the name first, and greeting second, keep in mind how it will work in the function.

    # We should not use a function just to print something. The function should get the string to be outputted,

    # and then, we would :

    # "return message" . Our function is receiving parameters, working with them,

def showMessage(in_name, in_greeting):

    message = f"{in_greeting}, {in_name}!"

    return message

  

def main():

name = "Delano"

print(showMessage(name, "Hi"))

message = showMessage("John", "Hello")

print(message)

showMessage("Jane", "Goodbye")

  

if __name__ == "__main__"

    main()





The *return* command












A **parameter** is a piece of data inputted into a function inside ( )


	def DisplayMessage(Greeting, name):



Functions should handle **ONLY** the processing part. 


If we do not want to repeat code, we create a **Function** to calculate taxes : 


	def calculateTax(In_product_price):
	
	product_one_total = product_one_price * 1.17 #adding 17% tax to the product value
	
	print(f"The final price for product one is ${product_one_total:,.2f}")





	def main():
	product_one_price = float(input("Enter the product one price: $"))
	product_one_total = product_one_price * 1.17 #adding 17% tax to the product value
	print(f"The final price for product one is ${product_one_total:,.2f}")




We should not have  *print* function inside the function itself. 

def main():
product_one_price = float(input("Enter the product price: $"))
calculateTax(product_one_price)
print(f"The final price for product one i s ${calculateTax(product_one_price):, .2f}")



Shouldn't the function provide us the ability to not repeat ourselves? If we want to change something in the formatting, 


We will work later with **loops** , so this way , the code would be repeated instead of copying and pasting the code. 


instead of hard coding the value, we can specifiy the tax



A good practice is to whever one declares the function, we add a few spaces to keep things clear. 



The final code, before we got sent over to the Quiz and Practice : 


def showMessage(in_name, in_greeting):
message_output = f"{in_greeting}, {in_name}!"

return message_output
return f"{in_greeting}, {in_name}!"

def addNumbers(in_number_one, in_number_two):
result = in_number_one + in_number_two
return result

def main():
name = "Delano"
print(showMessage(name, "Hi"))
message = showMessage("John", "Hello")
print(message)





> [!todo] 
> **Quiz: Functions**
> **Practice Exercise:** 
> Write a program to figure if the inputted year is a leap year.
You must use a function in your solution!
A year is a leap year if:
. It is divisible by 4 but not by 100
. It is divisible by 400
Examples:
>Enter a year: 2008
>2008 is a leap year (divisible by 4 not by 100)
.>Enter a year: 1900
>1900 is NOT a leap year (divisible by 100)
>Enter a year: 2000
>2000 is a leap year (divisible by 400)
(Hint: To get remainders, research modulus division!)

 