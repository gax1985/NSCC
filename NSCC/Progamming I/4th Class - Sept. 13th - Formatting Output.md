



We would like out applications to output values in the way we like them to. 


Examples of format changing :


1. Currency Formatting 
2. Desired number of decimal points 
3. Outputting number values as strings ( no need to do *str( )* for the result of the mathematical equation)



We can use the *round* function. What this does is to **modify the original number variable to only store the desired decimal places**. In the Salary example, when working with the variable's contents, we had to use the *float* option to have decimals, but we will have too many decimal places. We can limit the decimal places in accordiance to my wishes : 


		round(totalpay,2 "numberr of decimal places")


*round* does not always round to the desired decimal places. It will not always return a new number variable with **exactly** the desired number of decimals.  


We will learn other resources to work with the input. 


### *format*  Function


If we would to output two values, we would use this function to resolve the issue of the *round* function not giving us two decimal places :

	#output
	print("Your total weekly pay is {:.2f}".format(totalPay))




or


	#output
	print("Your total weekly pay wit bonus of %{:.2f} is ${:.2f}".format(bonus,totalpay))



### TODO



Prepare for **Tech Check 1**. It involves the following : 

1. Input-Output Processing
2. Number and String variables and conversions


###### Quiz :

It will involve the following : 


1. Variables
2. Strings
3. Numbers


(Figure out the **Input** for the task, and the **Output** for the task)





