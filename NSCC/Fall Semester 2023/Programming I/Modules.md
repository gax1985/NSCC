

They are like a huge library. You have functions that you can use


Let us take a glance at the *math* module



You can use all these functions when you import the module



How can we use one of these modules ? 


>import math


Let us try it!

	import math 

	def main() :

	print(math.ceil(10.48754))
	print(math.exp(2,3))



Python comes with building functions, but the modules are available for anyone. There are libraries built in, and other modules that you can import on demand. 

--------------------------------------------------------------------------------------------------------------------


We will work on a practice exercise today 


Input Output Practice Exercise 2 PPT


1st one : assign value to variable etc... 
2nd one : Assign this to that etc ..
3rd one : Pseudocoding Challenge



Paint Shop Exercise ---> end up in GitHub Classroom---> Clone the repo --> Tere is the README which explains the challenge --> create pseudocode --> try to solve it ! (We have expected output , it will ask for 3 inputs , and then asks how many gallons of paint you need for a specific room? )




Scratch Pad : 
=====================

What we need ? 

The amount of paint to cover the walls of the Family Room 

What we know ?

1 gallon of paint = 150 square feet
Rectangular-Room

What should we do? 

Ask the user for the width of the two walls, and the height of the room 


width_of_wall_1  = 
width_of_wall_2 =
height_of_room  = 



His Pseudocode : 


1 - Program Start
2 - Declare variable for # of sq. ft. covered by one gallon of paint and set it to 150
3 - output information explaining the process
4 - prompt the user for the dimensions of the room (length, width and height)
5 - Calculate the area of the walls by totalArea = (length * height * 2) + (width * height * 2)
6 - Divide the area by 150 square feet and round number of gallons up to the nearest whole number
7 - Display number of gallons needed
8 - Program End