



We can open a file with :

	1. File Name
	2. Extension


The file has to be placed in the *same folder* as the Python script


## Access Modes 


It indicates *what to do* with the file


r - Read
w - Write
a - Append



###### Example : 


	file_name = 'myFile.txt'
	access_mode_variable = 'w'
	
	# Open a File Handle - This will create a file if it does not exist
	
	myFile = open(file_name, access_mode_variable)
	
	# Write in the file : 
	myFile.write("Hi There \n")
	myFile.write("How are you? \n")
	
	# If we wish to add to the file, instead of overwriting to it : 
	
	# We can change access_mode_variable = 'a'
	
	access_mode_variable = 'a'
	
	myFile.write("I am good, how about you? \n")
	myFile.write("I am good thank you! \n")
	
	
	
	# Close the file (after you are done)
	
	myFile.close



