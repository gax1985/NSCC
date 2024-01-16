#!/bin/bash



elements = 'Fire Wind Water Earth'
PS3 =  'Please select your favorite element' 

select element from $elements
do

if [ $element == 'Fire' ]

	echo "You have selected Fire, the warmest of the elements!"
	break

fi 


if [ $element = 'Water' ]


	echo "You have selected Water, the coolest of the elements!"


fi


if [ $element = 'Earth' ]


	echo "You have selected Earth, Warm in the Winter, Cool in the Summer!"


fi 



if [ $element = 'Air' ]


	echo " You have selected Air, the lifeline of all living beings! "



fi 





