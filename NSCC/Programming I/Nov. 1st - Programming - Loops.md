


We want to avoid *repititions* in coding : Here is what **Loops** are for!


![[Pasted image 20231101104921.png]]



Instead of repeating the same statement, we can do the *for* loop : 


(counter ) = name given to a variable
range(10) = number of times this counter is being repeated 

		for counter in range(10):
			print('Hello')


There are two types of *loops* :



## FOR loop 


It repeats a specific number of times; a number determined by the user
We have the *counter()* variable , which increments automatically by one each time the loop repeats


![[Pasted image 20231101105218.png]]



The *counter( )* variable is going to start in a range of 10.
It goes *0 , 1 , 2 , 3 , ...*


There is no *counter( )* variable per se ; it is just there to indicate the number of times it is going to repeat. We can name it whatever we want, but we must **NOT** use a variable that we are using already.

If we have *counter(5)* :

0 , 1 , 2 , 3 , 4 


We do not have to use the counter :

**![[Pasted image 20231101105453.png]]


We are printing the *counter* in that case, so it will be 0, 1, 2 , 3 , ...

![[Pasted image 20231101105604.png]]


The *Turtle* is used to draw something!

> [!error] 
> We should **NEVER** name a Python file with the same name as a *module* we are importing
> 



> [!note] 
> We can have a *for* loop inside of another *for* loop 
> 


![[Pasted image 20231101111142.png]]

The inner *for* loop will corospond to the first interetation. Let us discuss the steps :


1. range(0) : for the first 0, the second range will be (0) , then increment to 1 , 2 , 3
2. range (1) : it will be 0, 1 , 2 , 3 
3. range (2) : 0, 1 , 2 , 3 
4. range (3) : 0, 1 , 2 , 3 

It will execute **16 times** in total !


The order in which it will happen :

1. it will start with 0. It will go through the code turtle.forward, turtle.right, and then it will execute the **imbedded for loop** (0, 1 , 2 , 3 )
2. it will go with 1 .  It will go through the code turtle.forward, turtle.right, and then it will execute the **imbedded for loop** (0, 1 , 2 , 3 )
3. it will go with 2.  It will go through the code turtle.forward, turtle.right, and then it will execute the **imbedded for loop** (0, 1 , 2 , 3 )
4. it will go with 3.  It will go through the code turtle.forward, turtle.right, and then it will execute the **imbedded for loop** (0, 1 , 2 , 3 )



![[Pasted image 20231101111845.png]]




We can use variables to control our range : 


		numberOfSides = 6


![[Pasted image 20231101112606.png]]


Now , let us ask the user to tell us the *Number of Sides*!


![[Pasted image 20231101112715.png]]



![[Pasted image 20231101112934.png]]


As we can see from the slide, we can indicate the beginning of the range : 


>for counter in range(5,10) # 10 is not included, so it will be 5, 6 , 7 , 8 , 9
># The value of **Counter** goes up by one until it finishes the 9th interation (10 is NOT included)


If we do not want to increment the counter by 1, we can add a third parameter !


![[Pasted image 20231101113158.png]]


![[Pasted image 20231101113233.png]]


The final value in the range is **11** , so it is out of the range. 


We can add a *negative* value!


![[Pasted image 20231101113413.png]]


It does **NOT** work with *float*!



Every time we use *range* , it creates a list. We can specify the list that it will go through : 



![[Pasted image 20231101113642.png]]



The *for* loop will go through the list's elements. Each time it will assume one of these indicated values. 


We can have a list with *strings* in it!

![[Pasted image 20231101113749.png]]


Every time, it will assume one value!




Or, instead of creating a list, we can output *values*!



![[Pasted image 20231101113827.png]]



Every cycle these are repeated, it will assume the **color** from the list indicated!



> [!warning] 
> Next Class : We have **Tech Check 4**, which focuses on *Functions*
> 



