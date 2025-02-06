





if [ <some test> ]

then

<commands>

fi

if [ <some test> ]

    then

    <commands>

fi





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





if [ <some test> ]

      then

  if [ <some test> ]

      then

      <commands>

  fi

    <commands>

fi





if [ <some test> ]  
  then  
  <commands>  
  else  
  <other commands>  
fi




if [ <some test> ]  
  then  
  <commands>  elif [ <some test> ]  
  then  
  <different commands>  
  else  
  <other commands>  
fi