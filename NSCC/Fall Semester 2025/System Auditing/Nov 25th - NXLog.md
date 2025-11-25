
Ron asked us to be able to absorb Windows log information, and convert it to JSON.

You will need extensions to deal with Windows and to deal with JSON files.

Extensions are library routines that are loaded by NXLog to process such information, and without them, it can not do it.

You will also need an **Input Module**, which is meant to absorb, from some source, the logging information that are coming into it. 

The Input Module has to take the file, make sure it speaks it language, and process it.

The **Output Module** is dedicated to outputting the information. In our case, our output module needs to speak JSON.

Once we have these pieces in the configuration file, we can absorb the data into NXLog, and in our case, we will send the information to a log file.

We can tell it to do multiple things with the Windows Log information. Instead of sending it to a log file, we can choose to send it somewhere else. We have circumstances that involve pipeline processors that process these logs. 

We can do both things. 

We need to establish a **Route** between the Input Module and the Output Module. 

We have an Input Module reading logs from a log file, and two output modules sending them somewhere else. We need to establish a route between input and output. 

The Route is meant to establish a connection between *Input* and *Output* modules. 

Input1 --> Output 1 
Input1 --> Output 2

Extensions --> allows peaking the language
Input --> Receive the Information
Output --> Send the information somewhere
Route --> Establishes a connection between Input and Output. 

Does the error messages make more sense now when you read them ? 

If you are doing a setup where you have multiple Windows systems sending their logs to one endpoint, you would configure the protocol to use and its settings in the **Input Module**. 