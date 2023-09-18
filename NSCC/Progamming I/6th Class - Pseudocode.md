



We have the **Coffee Shop** issue. First, we need to set up a plan!


The plan : what is being asked of us? We are going to create a console that would take a coffee shop order. We need to calculate **tip**, **tax**, and **total cost**. 


The program will prompt the user to enter the number of cups they wish to order, and the tip percentage. 


We have the **input** , as number of cups and tip percentage. 


We have the **output**, which is total amount(pre tax and tip), tip percentage, tip amount (in cash) and the final bill amount, which would include the tip amount and tax amount. 


We ask the user for the **number of cups** and **tip percentage**. We have total cost per cup. 


Now let us do the problem in VSCode : 


>#Student Name:    

	#Program Title:  

	#Description:    

  

	def main(): #<-- Don't change this line!

	#Write your code below. It must be indented!
	
	#Setting up the cost per cup
	
	cost_per_cup = 1.80

	#Setting up the tax amount in decimals 

	tax_percentage = 15/100

	#Display Welcome message for the user!

	print("\n\n\nWelcome to my coffee shop \n\n\n ")
	number_of_cups = int(input(PLease enter the number of cups you wish to order : "))

	#Prompt the user for the tip percentage 

	tip_percentage = float(input("Please enter the tip percentage (e.g. 15%) : "))

	print(number_of_cups)
	print(tip_percentage)

	#It is easier to check the lines of code as you code to fix issues, instead of waiting until the end


	#Now it is time to calculate the total cost before tax 

	total_cost = ( number_of_cup * cost_per_cup)

	print(totalcost)   #Just to test if int would work with float

	#He did not have to convert because both values are numerical. He did not need another float method to convert it

	#Let us check the tax amount

	tax_amount = tax_percentage * total cost

	print(tax_amount)

	#Calculate the tip amount

	tip_amount = total_cost * tip_percentage/100
  
	  #Let us test the tip_amount
	  print(tip_amount)

	#Let us do the final cost of the bill, which would include the tax and the tip

	final_cost = total_cost + tax_amount + tip_amount
	print(final_cost) #... to test it out


	# Now, we should output to the client the final cost of the bill. How do we do so ?

	#Output the final cost of the bill !

	print("\n\n Your Coffee Shop Bill \n\n")
	print("Cost before tax: ${:,2f}".format(total_cost))
	print("Tax amount(15%): ${:.2f}".format(tax_amount))
	print("Tip Amount({}%): ${:.2f}".format(tip_percentage, tip_amount))

	#If we do not want decimal places for the tip_percentage:
	print("Tip Amount({:.0f}%): ${:.2f}".format(tip_percentage, tip_amount))


	#Now for the final costs!
	print("Final Cost including tax and tip: ${:.2f}".format(final_cost))

	#Your code ends on the line above

	  #Do not change any of the code below!

	if __name__ == "__main__":
	 main()




#### Pseudocode


It is our first step into **System Analysis and Design**. It helps us plan for our program. It is similar to the Coffee Shop exercise. We have to understand the problem in order to plan our approach to resolve it. 


We are dealing with simple problems now. Later on, we will start using some *Decision Elements* such as **if* statements**. It is useful to have a **Flow Chart**. It is a tool used to write the outline of the problem. There is **no standard syntax** for it. We can accomplish the same result in many ways. There is no right or wrong, or specific syntax. If we have to output, we would use the print( ) method, or output to the user. The developer has to be clear, and human-friendly! 


We are sketching a solution in plain english!


Example of **Pseudocode** : 


1. Start of program
2. Create two variables, called **name** and **message**. 
3. Prompt the user to enter their **name**. 
4. Set a message to be "Hello", then say their **name**, then ". Have a Nice Day!"
5. Print the value of the **message**. 
6. End of program 


We are entering the steps to code the problem! We use plain English to explain the plan. If we take a look at the **Tech Check 1**, once we do the pseudocode, we would add it as comments!




Let us do a pseudocode for a **Baseball** application: 


"Write acode to read the name of a baseball team, number of games won, number of games lost, and display the name of the team and the percentage of the games won"


#### Pseudocode : 


1. Start the program 
2. Prompt the user for the baseball team's name
3. Prompt the user for the number of games won
4. Prompt the user for the number of games lost
5. Calculate the total number of games played by adding the number of games won to the number of games lost
6. Calculate the percentage of games of games won, by dividing the number of games won / total number of games and then multiplying the number by a 100.
7. Display the name of the team, and their percentage of games won
8. End program 



Let us take the **pseudocode** and plug it in the code!



