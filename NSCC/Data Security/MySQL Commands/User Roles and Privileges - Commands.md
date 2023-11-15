

# Database Commands : 


"Create a database AbcCorp"

## Create a Database 


	CREATE DATABASE database_name;


## Use a Database 


	USE database_name;



---------------------------------


# Tables Commands


"Create a table in the database called employee that has four columns called empid (integer, primary  key) name (varchar), salary (decimal), and phonenumber (varchar)."

## Create a Table 


	CREATE TABLE table_name ( column1 datatype, column2 datatype, column3 datatype, ); 


>CREATE TABLE employee(
>empid int NOT NULL,
>name VARCHAR(255),
>salary decimal,
>phonenumber VARCHAR(255),
>PRIMARY KEY (empid) 
>);


----------------------------------




# Roles 



"Create a role called clerk ... "


## Create a Role 


	CREATE ROLE clerk; 



## Grant Privileges to a Role 


" ... and grant privileges to this role that will allow SELECT privilege on  
employee.empid, employee.name and employee.phonenumber but no access to employee.salary"


	 GRANT SELECT (empid, name, phonenumber) ON AbcCorp.employee TO clerk; 


	GRANT priv_type [(column_list)] [, priv_type [(column_list)]] ON [object_type] priv_level TO user_or_role;












