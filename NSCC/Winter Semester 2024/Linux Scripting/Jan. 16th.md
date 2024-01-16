



# IF Statements in BASH



If sum do


You end the conditional statement by spelling the name backwards. so , FI!





You can have nested if statements. If something is true, check if if it is trye tghen do


If sum else , 


If something is true, 
do something 
else, do something else


if some test, 


if + elseif + esle (if the first are true, the else statement at the end wont get executed)



If not variable=1 then do



If a length of a script > 0  with a -S next to the string variable




## Contents of the Slide : 


Conditional statements

IF

If

if [ <some test> ]

then

<commands>

fi

if [ <some test> ]

    then

    <commands>

fi

Operators

|   |   |
|---|---|
|Operator|Description|
|! EXPRESSION|The EXPRESSION is false.|
|-n STRING|The length of STRING is greater than zero.|
|-z STRING|The lengh of STRING is zero (ie it is empty).|
|STRING1 = STRING2|STRING1 is equal to STRING2|
|STRING1 != STRING2|STRING1 is not equal to STRING2|
|INTEGER1 -eq INTEGER2|INTEGER1 is numerically equal to INTEGER2|
|INTEGER1 -gt INTEGER2|INTEGER1 is numerically greater than INTEGER2|
|INTEGER1 -lt INTEGER2|INTEGER1 is numerically less than INTEGER2|

Nested IF

if [ <some test> ]

            then

                if [ <some test> ]

                            then

                            <commands>

                fi

    <commands>

fi

IF THEN ELSE

if [ <some test> ]  
        then  
                <commands>  
        else  
                <other commands>  
fi

IF ELIF ELSE

if [ <some test> ]  
        then  
                <commands>  
        elif [ <some test> ]  
                then  
                        <different commands>  
        else  
                <other commands>  
fi




---------------------------------------------------------------------------------------------------------



The IF Structure : 



If [ <some test> ] 
then
commands. .... 


else 

othercommands...


fi 




_______


do the ELIF ( command in the slide structure)


_________



# Case Statement


case <variable> in 
	<pattern1>)
		<commands>
		;;
	<pattern2>









## On the topic of placing *then* on the next line : 













# Permissions


Each group of permissions is represented by a 3-bit number


If you would like to owners of the group to have all the privileges


If you wish to have read write and execute, 777 ( owner | group | others )


If you wish to have read and write for all , 666 ( owner | group | others )


If you wish to have execute rights for all , 111 ( owner | group | others)





=================================================



SELECT !



Select a variable from a LIST , 



#!/bin/bash



options='Run Load Save Quit'
PS3='Select an Element'

>[!note]
>
>The **PS3** variable is unique to the *select* statement. The *select* statement is expecting it! 


select option in $options
do

	if [ $option == 'Quit' ]


		then
			break
	fi
	echo 'You Chose $option'


done






Exceptions for teh SELECT loop : 


1. If you push ENTER only, it displays the menu again 
2. If any choice is not in the list, then the value is NULL




----------------------------------------------------------------------------------------------------





UNTIL loop : 
=========



#!/bin/bash


counter = 1 

until [$counter -gt 10]

do

echo $counter

((counter++))


done
























Starting Thursday, We will have little programming/scripting challenge. We would have an hour/hour and a half. We would have a **Medium Scriping Assignment** , **Harder Scripting Project**, and the **Final Project**




