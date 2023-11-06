




Last class, we studied *How to Repeat Events in Python*. 


We saw that in real-life, we had to repeat lines of code with *Loops*


Last class, we studied the *FOR* loop. Today , we will study the *WHILE* loop. 



## FOR Loops



Print a message 33 times : 

		for steps in range(33):
			mycode



Print Items in a Shopping List : 

		for item in items:
			mycode


Print 45 name cards for a party guest list :  

		for count in range(45):
			mycode


If we wish to update inventory prices : 


		for product in product_list:
			mycode






![[Pasted image 20231106103815.png]]






def main():

		count = 0
		
		for steps in range(100000000):
			count += 1 (To increment the counter)
			print('')
	print(f"The Final Count is {steps}")	

if __ name __ == "__ main __ "
		main()




We can import the library *time*, to give it 1 second while it does something 





What if we do not know how many times to repeat the event ? 



![[Pasted image 20231106104623.png]]



What if we don’t know how exactly how many
times to repeat an event?

» Read students names until user wants to stop
» Prompt the user for input until they provide valid input
» Read records in a files
» Keep guessing until you get the right answer




We can use the **WHILE** loop : 

While Loops allow you to execute until a
particular condition is true

def main():
answer = @

o
while answer !=4:

answer = int(input("What is 2 + 2? "))

print(f"YES!!! 2 + 2 = {answer}")

if _ _name__ == "__main__":
main()




![[Pasted image 20231106105220.png]]



The variable that controls the *for* loop is defined in the *for* loop pattern




In the *while* loop, we have to declare the variable **BEFORE** the *while* condition is instated :

		answer = 0
			while answer !=4:
				answer = int(input("What is 2+2?"))



When the *while* loop, if we want to give an error message : 



		answer = 0
			while answer !=4:
				answer = int(input("What is 2+2?"))
				if answer != 4:
					print("Nope! Try Again!")


This is the most efficient way to do so : 

![[Pasted image 20231106105720.png]]


To refine it further : 


while answer != 4:
	answer = int(input("What is 2 + 2? "))

	if answer != 4:
		print(‘Nope. Try again!‘)
if answer == answer - 1 or answer == answer +1:

‘ print(' So close, keep trying...")

print(f'YES! You got it! 2 + 2 = {answer}')



![[Pasted image 20231106110040.png]]


![[Pasted image 20231106110229.png]]



What will happen in this *turtle* situation ? 


![[Pasted image 20231106110247.png]]


We start a variable *counter* = 0 

If the counter is less than 4, 
	it enters the loop , executes at 0, 
		then executes at 1 , increases counter by 1, 
			it keeps going, until the counter is 4 ( it will execute , 0 , 1 , 2 , 3 )





The different here : 



![[Pasted image 20231106110446.png]]




If we want it drawn four times, we use the *FOR* loop. 


We can replicate the *FOR* loop with WHile, but we have to declare a variable (counter = 0), and increment the counter :



![[Pasted image 20231106110555.png]]



How many times will it be drawing it? 

>Five Times, due to <= 4 :

It will run for counter 0, counter 1, counter 2 , counter 3, counter 4



![[Pasted image 20231106110700.png]]






How many times will it be drawing it? 


![[Pasted image 20231106110711.png]]


It will draw it three times! 






How many times will it be drawing it? 


![[Pasted image 20231106110758.png]]


The counter is never incremented, so the counter will always be ZERO :


AKA... INFINITE LOOP


![[Pasted image 20231106110836.png]]



Remember : 


Using the WHILE loop, it need a control variable before the loop, and the increment must be done inside the loop




**Infinite Loop Demo**: 



While Loops allow you to execute until a particular condition is true:

  

def main():

count = 0

  

while count < 100:

print(count)

print(f"The Final Count is {count}")

  

if __name__ == "__main__":

main()




To fix it : 



		def main():

		count = 0

  

		while count < 100:

			print(count)

			# count = count + 1 (We want to repeat that after the equal sign)

			count += 1 # (We can use a count operator like * for multiplication for example)

			# It is the same as count = count + variable (if we have set that variable to a number )

  

		time.sleep(0.5) # To Slow it down by half a second

  

		print(f"The Final Count is {count}")

  

if __name__ == "__main__":

main()


![[Pasted image 20231106111639.png]]




> [!todo] 
> 
>	Quiz: Repeating Events Until Done
>
>	Practice Exercises:
>
	Etch-a-Sketch: Using turtle, have the user to
		enter a pen color, a line length, and an angle.
		Following, draw a line based on their
		specifications. Let them specify new lines over
		and over until they enter a line length of 0.
		When the user specifies a line length of 0 stop
		drawing.
>Secret Number: Ask the user to guess a
>	number from 1 to 100. After the user inputted a
>	value, trying to guess the number, tell them
>	“higher” or “lower” according to their guess. At
>	the end, once the user get's the correct
>	number, display how many guesses were
>	needed. 
>


