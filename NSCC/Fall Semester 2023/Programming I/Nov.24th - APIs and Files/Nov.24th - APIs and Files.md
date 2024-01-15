


We were looking at the following link : 


https://data.novascotia.ca/


Where we would have access to *data* in a form that can be exported into a *.csv* file via an API



When the data is exported into the .csv file, we **MUST** ignore the first row, due to it being *Titles*


Hypothetically, if we want to check the schedule for *ferries*, we can create a filter in Excel for the *Ferry* data type


In Python, if we have a list with all these options, and we want to filter the schedule for a certain *Ferry Type*, we would use an **IF Statement** :



	if index[1] = "string":




## Reading a File in Python


How can we *Read a File* in Python?


	access_mode = "r"
	
	file_handler = open(filename,access_mode)

	file_data = file_handler.read() (it reads all the content at once)
	
	print(file_data)
	
	file_handle.close()



We would get an error if the file does not exist!


If we wanted to *access one line*? 



	# Read a single line from the file
	file_line_data = file_handle.readline()  # file_handler.read() stored all the file content, so if we do fine_handle.readline(), it will be empty due to the contents being stored in another variable. Thus, we would need to  


