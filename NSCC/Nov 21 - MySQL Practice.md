




# Example Tables 



## HACKER 

HACK_ID **PK**
HACK_NAME 
ARRESTED **BOOLEAN**



## COUNTRY

COUNTRY_ID **PK**
COUNTRY_NAME 

## ARREST

ARREST_ID (if a hacker ID is not in "Arrest", there were never arrested) **PK**
HACKER_ID **FK**
SENTENCE
CRIME_DESCRIPTION
DATE_OF_ARREST




SIGMA Symbol -->  refers to *Select*


SigmaSymbol (Hacker_ID) (HACKER)


SELECT [What you want] FROM [Tables Involved] WHERE [Conditions that have to match to get a result]


For example : 

>We would like to show a list of ALL the Hackers who were arrested

SELECT (hacker.hack_name) FROM HACKER WHERE Hacker.ARRESTED = 1





Example :

>We would like to know the Hacker names of those who were arrested, and the country where they are from 



SELECT HACKER.HACK_NAME, Country.name 
FROM HACKER, Country 
WHERE HACKER.arrested = 1;




For Example :


> If we wanted the Sentence, Crime Description and Date of the Arrest, Hacker name, whether they were arrested, country name where they are from


SELECT hacker.hack_name, country.country_name, arrest.sentence, arrest.crime_description, arrest.DATE_OF_ARREST
FROM HACKER, COUNTRY, ARREST
WHERE hacker.arrested = 1 AND 

(We need to know the country ID) 

hacker.country_id = country.country_id;




Let us build an **Affiliation Bridge** and an **Affiliation Table**


## AFFIL_BRIDGE

HACKER_ID **PK FK**
AFF_ID **PK** **FK**


## AFFILIATION
AFF_ID **PK**
AFF_NAME



A more complex example now ... 

> If we wanted the Sentence, Crime Description and Date of the Arrest, Hacker name, whether they were arrested, country name where they are from


SELECT hacker.hack_name, country.country_name, arrest.sentence, arrest.crime_description, arrest.DATE_OF_ARREST
FROM HACKER, COUNTRY, ARREST
WHERE hacker.arrested = 1 AND 

- We need to know the country ID) 

(hacker.country_id = country.country_id) AND

( AFF_BRIDGE.HACKER_ID=HACKER_ID) AND

( AFF_BRIDGE.AFF_ID = AFFILIATION.AFF_ID )


SELECT [What you want] FROM [Tables Involved] WHERE [Conditions that have to match to get a result]






#### Integration with Python



You have a reporting screen with boxes, and a query : 


"I want a Hacker Name from Romania"


It will take this string, add MySQL options to it, and then submit a query 


You can have a **list of queries** available, and you can select the query that you want. You can build an example by building an example, and filling in values. Ron mentioned that if he had a *reporting screen*, it would have the names of all of the fields in the table. People who generate reports could type what they wanted in those boxes. You would not really place the field name, but you would indicate to the user what type of information they should type in that field. The query would then be executed on the MySQL database. 



Hypothetically, if we took the previous query, and added one more condition : 


OR 

( 1 = 1 );


He would get a lot of information that does *not* match the query




> We want **Hacker Names** who *were arrested*


SELECT Hacker.HACK_NAME
FROM HACKER
WHERE hacker.arrested = 1 
OR
1=1 ;


###### What will be get ?

	We will get the hacker names with a lot of non-matching information. 1=1 will ALWAYS be true, then we will get ALL the names . 

Adding "1=1" is called *SQL Injection*''



# SQL Injection 



#### How does it work? 


Syntax changes to keep up with protections against it



##### Example :


>We would like to see our Grades. We are on *Brightspace* at the Login Screen, where we are asked to enter the **Student Number**, where we would enter "W0XXXXX". Behind the scenes, the program builds a *query* : 


SELECT * FROM  grades 
WHERE grades.W# = (Variable equaling what the student typed in);


The *Variable* the student enters will be substituted for "W12345"


When we add :

	1=1;

As in : 


SELECT * FROM  grades 
WHERE grades.W# = "W12345" OR 1=1;


The line would end at the ; normally, so there is a way to bypass that end



Basically, we can make the original query non-valid, like *disallowing* **AND**, **OR**, etc ... 

or : 

"How do we get an = sign in there without it being detected ?"



There are lists of **Online Databases That are suseptable to MySQL Injection Attacks**. If you are working with a company with a published online database, we would need appropriate permissions from the CEO in writing. We would need it as described as **"Color Of Right"**, which is :

	You are getting permission from someone who ACTUALLY has permission


If someone has conducted an action without the necessary permissions, that person could face legal consequences, but that someone could face a confusing *Color of Right* permissions issue (where it is indicated that are specifically permitted to conduct an action). The question is : Will someone cheat while doing so? will they do another action on top of a specifically allowed action? 



Imagine if you are an Electrician tasked with wiring a house, and the house burns down, you could face legal consequences. Ron mentioned an inspector who inspects rigs, and they discovered that after that person did the inspection, a part on the rig was installed backwards, and someone got injured.

Thus :


> [!warning] 
> Make sure you have enough permissions!
> 



