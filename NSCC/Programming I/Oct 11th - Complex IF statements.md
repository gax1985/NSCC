

I want to execute an entire block of code as a condition for an **IF** statements. For example : 



deposit = input ('how much would yuou like to deposit?')
if float(deposit > 100 :

print ('you get a free toaster')


else :


       print("Enjoy your mug!")

print ("Have a nice day!")


So if the deposits are more than a 100, we give a message they get a free toaster! If less than 100, the second print statement gets executed, due to indentation. So, we get two IF statements in one. 


	Code in else statements gets executed if the IF statement is not true
	It is always good to test the boundaries, so 50 , 150 etc 

BOOLEAN expressions will always have a value that is either true or false 


Another way to work is via BOOLEAN variables, we would have the condition same as before : 


>if float(deposit > 100 :

		free_toaster = true --> if the deposit is greater than 100 they get a free toaster, so the boolean is set to TRUE
>if free_toaster:
>	print('enjoy your toaster!')


Every time you use an IF statement, it expects it to be TRUE or FALSE. So if we have a BOOLEAN variable, it is already returning TRUE or FALSE


We have the BOOLEAN variable. What will happen when we enter 50 for a deposit? it is going to run the code to see (we enter :50)

>if float(deposit) > 100:
>	freetoaster = true
>if free_toaster:
>	print("Enjoy your toaster!")


We get an "REFERENCE ERROR! free_toaster is not defined" The reason being it is false, and free_toaster has only been set to TRUE in this conditional statement. 


So we fix it like this : 


>free_toaster = false --> sets it by default to FALSE, so this way, we avoid the error
>>if money > 100
>	freetoaster = true
>if free_toaster:
>	print("Enjoy your toaster!")


What we have done is **Initialization** of the variable! So we always have to : 


- [ ] **Initialize the variable!**
	Declare variables before entering the IF statements



Why are we doing this? BOOLEAN variables make it more complicated. We could have used *else* for example. So, depending on the amount of conditions to test, it makes sense to use a BOOLEAN variable to assess it. We call it a **FLAG Variable**. 



We have *if* statements, *identations*, we have more opportunities for errors : 


>free_toaster = false --> sets it by default to FALSE, so this way, we avoid the error
>>if money > 100   ---> common mistake " : "
>(watch for indentation)	freetoaster = True   --> capitalize
>if free_toaster:
>	print("Enjoy your toaster!")



Test this code : 


>import random
>
  >
>
def main():
>
        # Generate a random number between 1 and 2
>
  >  randomNumber = random.randint(1,2)
>
>  
>
># Tell them if it is heads or tails :
>
    >if randomNumber == 1:
>
   >     print("Heads!")
>
  >  else:
>
        print("Tails!")
>
># Display this message to everyone
>
  >
  >
>
>    print("Have a great day :D")
>
  >
>
i>if __name__ == "__main__":
>
        main()




Now, we can modify it slightly : 

>import random
>
  >
>
def main():
>
        # Generate a random number between 1 and 5
>
  >  randomNumber = random.randint(1,5)
>
>  
>
># Tell them if it is heads or tails :
>
    >if randomNumber == 1:
>
   >     print("Heads!")
>
  >  else:
>
        print("Tails!")
>
># Display this message to everyone
>
  >
  >
>
>    print("Have a great day :D")
>
  >
>
i>if __name__ == "__main__":
>
        main()




Sometimes, we would like to test miltiple conditions, so we will have different outcomes. Here is an example : 


	If you are in Canada, say "Hello!"
	If you are in France, say "Bonjour!"
	If you are in Italy, say "Buongiorno!"


So , for instance, in this case, we are tasting the country, which happens by comparing it to a specific value:


>country = input("Where are you from?")
>
>if country == "CANADA" :
>	print("Hello!")
>elif country == "FRANCE":
>	print("Bonjouir!")
>elif country == "ITALY"
>	print("Buongiorno!")
>else:
>	print("Aloha/Hola,G'day")
>



What is the difference beteen *elif* and *if* ? *if* does not evaluate ALL other values. So, *elif* in this situation, after determining the country is NOT Canada, it checks if Germany is TRUE, if it is not, then another *elif* checks if the country is France. The final *else* is for the end, where we have checked if the country is Canada, Germany and France. They are all chained together. If Canada is TRUE, none of the others get executed. If you are in Germany, that code gets executed, but the France line does not get executed. For the **ELSE** to be executed, all three have to be FALSE. 

	Note : Watch out for indentations!


SOmetimes we will have decisions to test. In ortder to take the next step, it depends on a combination of factors : 

1. If I win the lottery, but only win $5 , I can't retire
2. If I get 1 million dollars but I did not win, I can't retire
3. I can only retire if I win the lottery and the prize is over 1 million. 



Now, we use the **AND** statement in the *if* statement : 


># AND will only evaluae as true if both conditions are TRUE
>
>won_lottery = True
>big_win = True
>
>#Print statement only executes if BOTH are true: 
>
>if won_lottery and big_win:
>		print("I can retire")



Now , **Truth Tables** would help!


If either conditions are true, we want to use the **OR**


	If it is Saturday or Sunday I can sleep in 


># OR will only evaluae as true if either conditions are TRUE
>
>Saturday = True
>Sunday = False
>
>#Print statement only executes if BOTH are true: 
>
>if Saturday or  Sunday:
>		print("I can Sleep in")



We can combine multiple *OR* statements :



>if month == "Sep" or month =="Apr" \
>or month == "Jun" or month == "Nov" :
>		print("There are 30 days in this month"
>
>
>Student = True
>want_improve_resume = True
>
>if state and year_in_program == 1 \
>and want_Improve




Wer can combione and/or


>if country == canada and \
>pet == moose or pet ==beaver:
>		print("Do you play hockey too?")


	Make sure to test all possible combinations :
	
	Country = Canada, Pet = Moose
	Countr = Canada, pet = BEAVER
	Countr = Canada, pet = MOOSE
	Countr = Canada, pet = beaver # Problematic last statement



Order of evaluation : 


if country == canada and pet ==-moose \   # this gets evalated first 
pr pet == beaver : 

priunt (blablabla)



We fix it with this : 


if country == canada and \           # assesses as one expression 
(pet ==-moose or pet = beaver)    # this gets evalated first # Then it tests this or this
pr pet == beaver : # Then it returns if everything is true or false


Remember : Order matters . AND takes priority first 


When in doubt , add **parentheses** whenever we combine and/or in a single *IF* statement. It will be easier to read



Sometimes we have multiple condictions where using and / or will not work : 


If it is Monday, check if there is coffee. If not , go to the nearest cafe. 

We have to check if a condition is true, if not true , check the other. 

Only if it is Monday


**Nested IF Statements**


>monday = True
>FreshCoffee = False
>
>
>If monday:
>
>
>		if not freshcoffee:
>			print(go buy it)                       # Indentation is critical, as it determines the order
>		print(I hate mondays
>Print("Now we start work")
>





Lets try *elif* :



>monday = True
>FreshCoffee = False
>
>
>If monday:
>		print(I hate mondays
>elif not freshcoffee:
>		print(go buy it)                       # Indentation is critical, as it determines the order
>Print("Now we start work")




#### We have the next Tech Check next week!


