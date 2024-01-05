


We are installing **Microsoft Visio 2021**, and we are downloading it from **Azure Education** :

[https://portal.azure.com/?Microsoft_Azure_Education_correlationId=323f58ba-dbf3-43b7-a3d4-7a8e013577ef#view/Microsoft_Azure_Education/EducationMenuBlade/~/overview] 



Lats time we worked with **Truth Tables**, so we can use them to *analyze Propositions*. There are relations between them such as **AND**, **OR**.


It is great when building an application, and perfect for testing. We use a **truth table** to attain every possible combination. 



We have a more visual approach which is **Logic Circuits**, but they are both tools to analyze **Boolean Expressions**.




When using **P , Q ** , we are representing one proposition, which returns one value : True or False 



In this scenario, we have a Bicycle Rental Dewcision : 



P : It is a sunny day (Proposition because it is TRUE or FALSE)
Q : Bicycle needs maintainancew ( True or False?)
R : I have extra money for renting a bike (True or False? )


We have **three** propositions, and the P , Q and R are representations. 


How many **rows** in this problem's **Truth Table**?



2 ^ (3) = 8 



Expression (P and not q) : I will rent a bke uit is is sunny day and bike does not need maintainance)



Expression Qo r T : I will rent a bike if the bike needs maintainance or I have extra money for renting one)




## Logic Circuits


One difference with truth tables : 




Gated Circuits : proporsitions on  an AND circuit 


       True
A 

                               =                 Truer (since it is AND)

B 
      True 


A         False 

        (Curved outlet: OR)      =               True ( since one is true)


B             True




        

                                It flips it!
A            (Triangle Circuit : Inverter :: the NOT)     = false      
''
true





Challenge :


p

true

                 curved  OR true    = True

q

false

                                                These are connected into =    AND circuit   =  False (since they are not both TRUE) 

R

true

                   AND circulte     = False
S

F


We need a specifc value for each proposition.. In the truth table we are solving the true is p = true , q = false , r = true and s = false and






Lets translate it into a Bollean expression : 



NOT( (P or Q) and (R and S) )




Check out  : 



https://academo.org/demos/logic-gate-simulator/




## Microsoft Visio 2021




More Shapes 
		Electrical Engineering 
			Analog and Digital Logic





On the left side, we have all the shapes that we need, and we are using the TWO on the TOP : LOGIC GATE + INVERTER.



We click and drag it to the area. 



HINT : Check out LinkedIn Learning, YouTube for Microsoft Visio/Logic Circuits Tutorials and Walkthroughs. (Sidenote : check codeacademy.com for MySQL code totorials. Very streamlined and hands-on).




Challenge #2 : 

Start with 

NOT((P or Q)  and (Q and S))


P

          OR Circuit                        |
												|		
Q 
|
|
Q is connected to : ===  =Both are connected to AND Circuit ---which                                               in turn is ---------===connected to a NOT circuit
|
|
                AND Circuit 
|
S





#### CHALLENGES : 


Draw circuits for the following : 


1. (p and q) or (r and s) : 
	1. Will it be TRUE if p=FALSE q = TRUE R=TRUE and S=FALSE ? 
2. (p or q) and (not q or r):
		1. Will it be true if p = True, q = TRUE and r = FALSE  and s=FALSE?
3. (p and not q) and (q or r):
	1. Will it be TRUE if p = TRUE, q = FALSE and r = TRUE? 
4. not((p or q) and (r or not s)):
	1. Will it be true if p = FALSE , q = FALSE , r = TRUE and s = FALSE?