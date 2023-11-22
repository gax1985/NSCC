




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


If you are in *Private Practice* : 


Attain : 

> [!danger] 
>  Errors and Omissions Insurance


The insurance company will pay your Legal Bills if you are sued. If you are intentionally doing something wrong, it is called *malficience*. If you are consulting for a company, make sure you have this insurance. You can google "How can I find a list of databases that are susceptible to MySQL Injections". We are not to act upon this information, as we would need to know to develop a web interface for interacting with the MySQL database. We can practice on our database : 


SELECT hacker WHERE 1=1; 




Tomorrow morning, we have three Test Drive Students (perspective students). 





There is another technique : 


# Blind SQL Injection 


Look it up on Google!


Think about how we can guard against this: 


We have a *Web Form* that people fill out, where it says : 


	Enter Student Number : BOX

Behind the scenes, in the browser, we have Java Script translating the input into a MySQL query. The query gets sent to a *Web Server* , where it gets sent to a *DB Server* to get executed on. 


This is true for all websites we visit. 


Web Form 

builds **Query**

then, 

it gets passed to the **Application Web Server**, 


then, 


It gets sent to the **Database Server**. 





We figure out the **Design Reference Threats**, and figure out the ways to *protect the Design*. You figure out the probability of a threat, and then you plan the protections accordingly. 



If we have a client, who has a higher probbablity of someone condusting an **SQL Injection** attack of 100%. Where would this protection be placed ? on the JavaScript. There is something called "**Input Validation**", where you get prompted to enter the correct type of characters in their query. The JavaScript on the web form will be checking the inputs, generates an error message where the user does not leave the browser yet, and before anything gets submitted. It is *helpful to the user*, *does NOT waste time and resources*, and *provides a bit of security against SQL Injections*. Is that enough as a protection ? No. The organization has a lot of control of what can be done on their systems. If a query is built with a hacker bypassing input validations, if the web server is just receiving the forms, and then sending it to the database, we can place **Input Validation on the Application Web Server, where the organization can exercise more control, and the hacker would not have access to it**. There is an option called **Application Proxy**, where *it actually understands the information. It would build the query, check if it gets valid results*. It would be able to decrypt HTTPS traffic. The *Application Proxy* knows which application is running, depending on the sophistication of it, it would run tests, get results and then decide whether or not to send it. 


Most web applications have an *Application Proxy*. Application Proxies guard against **Inbound Traffic**. Depending on the organization, we might have "Web Application Proxy" that guards against *Outbound Traffic from the users*, where for example it prevents porn sites and gaming sites, logs and monitors web access. It does not allow you to have direct access to the internet. If we send out for example encrypted HTTPS traffic, the encryption key that we have in the browser is only good for the *Web Application Proxy Server*. The message gets *decrypted, analyzed, re-encrypted and sent back*. Assume every organization has a *Web Application Proxy*. We have the ability to model things, and they are SPECIFIC to the Application it is guarding. All of SQL is a problem, because we allow users to enter text that gets passed as a query against the Database. 


There is another guard we can place there :

	Whatever the user entered as a query is NEVER sent to the database. The User Query gets STOPPED On the APplication Web Server. In the Proxy, there are set and defined commands there. For most publically-facing applications, there are a limited set of things you can do. So, based on the query, one of the acceptable commands is sent to the database. AT NO POINT does the user text EVER gets sent as a direct command. 

Most people rely on **Input Validation** on the *Browser*, and on the *Web Application Proxy*






# Shodan Video



https://null-byte.wonderhowto.com/how-to/find-vulnerable-webcams-across-globe-using-shodan-0154830/


We can check a vulnerability in Windows XP for example, we can see thousands of vulnerable web-facing devices on the internet. 



Using Shodan is a great way to see what is out there. If we are doing port forwarding, it could show up on Shodan due to it being publically facing .


Connect via TOR or a VPN. Take precautions, and DO NOT DIRECTLY access it 


Grabbify or CANARY TOKENS


Make sure you are hiding yourself a little bit. 



1. It comes down to be a good searcher :


>We have different syntaxes shared by the community. It can be found on Shodan's Twitter page : 
>
>
>https://twitter.com/shodanhq
>
>VSAT ---> Gives a satellite-connected device, where VSAT is indicated in the login query.
>
>Satlink ---> Satellite System. Connected and moving all over the world. 
>
>
>A random VSAT link ,. (ports 23, 80, 161 were open). 



We can visit the IP Address that we got from Shodan would take us to a page (we could add ip:port on the browser, and it would normally ask us for a password. Surprisingly, some do not, and on the video, he was able to check out the manufacturer's page and see the default credentials in the manual .




## Shodan's Web Cams : 



We type "*Webcam*" in the search, and we would get results with connected web cams. Useful information would be the **Manufactuer**. Then we can check the manual, and keep trying default credentials, or try it without a password. 




Look up "/CGI-bin/guestimage.html" where it would bring us to vulnerable webcam's pages. 





> [!todo] 
> Try looking on **Shodan** for *MySQL Vulnerable Databases. 
> 


> [!tip] 
> Check out the **Vulnerable Baby Monitors Hacker Story** 


