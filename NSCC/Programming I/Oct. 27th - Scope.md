


It is a good practice to intialzie all over variables. We have a function, and it would have a parameter(param1), *param1* is a parameter just like a local variable, since it is part of the if statement that is part of the global portion due to indentation. 



![[Pasted image 20231027105106.png]]


is *var1* a global variable? yes. If we call it in the **someFunction** would *var1* be available for the remainder of the program? when we are creating global variables (assume we do not have *var1*) we are working with something of a value that came from outside of the function. In this instance, we have a dependency that is outside of teh function. We do not want that!


If we have the same thing with the execption of adding :

	var1 = 9


When we do this, it creates a local variable with the same name. When we say inside of the function : 

	print var1

it is referring to the local one. This is executed, it assigned 9 to the local variable, and it ended the exzecution. Var1 after the execution is gone from memory. 


![[Pasted image 20231027105647.png]]

![[Pasted image 20231027105717.png]]


![[Pasted image 20231027105818.png]]


Parameters behave like a local variable. X is the same way. Y is a global variable, due to indentation. Z is global, inside the IF statement, which is part of the main block. Z is global. What is the lifetime of those variables? when will they be created and when will they end ? 


W is a parameter of the function. W is the same as X, it resrvers a space in the memory. It returns X , and then it is gone. In the next portion, W and X get destroyed in memory. It finishes what it is doing. 


If SomeFunction(6), we lose the value. Variable Y is declared, and it gets 3 assigned to it. Variable Z exists in the if statement. When the program ends, it gets destroyed. It starts existing when declared, and stops existing when the program ends. 


If Y > 2 , Z is never created, and the function is not called. The solution is to **initialize the variable**. 




#### Quiz's Incorrect Answers : 



![[Pasted image 20231027111219.png]]


![[Pasted image 20231027111359.png]]



# Modules and Encapsulation 


It comes from **Object-Oriented Programming**. It refers to something that is hidde. We need to know how to use it, but we do not need to know how it works under the hood. It is like driving a car : you can drive the car, but you do not need to know how the engine works. 


When you consider working with **Functions**, we want it to be used by other programmers as well. They need to know how the parameter is passed, but not how it is coded. If we have a special script that I do not want to share the part, we can keep it hidden. Imagine coming up with a special algorithm and I do not want everyone to know it, we *encapsulate* it. We tell everyone : "You can use it, but it is secret!"


What are we hiding ? 

1. Implementation
2. Details of the Function
3. Make it available as an **Interface**. It is everything we have contact with.


In a video game, the screen is showing the levels, character, and the interface in general. How the game is coded does not matter to the user. 


#### Modules


We can use the **Module**, we use the *import* key word. 



###### Why Use them ? 

It is easier to use the code.

It simplifies the code

It makes it easier to make changes. 


		If we created a Function, and let the class use it, such as in the Grass Calculator, we pass the 5 parameters, and it returns the total cost. Everyone has access to the Function, and everyone can use it. By checking the code, we realize that we are using just IF blocks. If we want to improve it, we can re-structure the code, but the only thing that does not change is the way you use the function. It does not matter to anyone else what you have done, as long as the way you use it remains the same. 




In the VSCode example he has shown us, he reused a block of code from one script , pasted it into another. Instead of writing everything , he did this : 


		import tax_calculator --> This is the file name of the script
		import random
		
		def main()L
			random.ranint(1,10)



If we want to import the specific method : 

		from tax_calculator import calculate_tax
		
		


![[Pasted image 20231027113040.png]]


![[Pasted image 20231027113133.png]]


When we do this :


def main():



When running a method, we have to define it and run it. if we remove :


		def main():


In the class example, we set everything as global. If we bring everything from the file with : 


		from tax_calculator import * 


it executes EVERYTHING from the original file



With libraries, normally we would initialize variables. We can use the main method from the other script, and put everything in its own spot. 



Everytime we are coding, we are keeping everything LOCAL. 


If we have code defined in its own block, the code is contained within its own specific method. This is why we are using def main() . 

if __ name __ == "__ main __"  

it is checking if it is running from the file




Keep everything contained!



Remember : 



![[Pasted image 20231027114639.png]]





