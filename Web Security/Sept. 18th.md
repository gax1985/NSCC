


# Apache


It represents 90% of websites

It runs on Linux, Windows, MacOS, etc. 

Before Apache arrived, we had several platforms to work with, such as ..


For a basic website, Apache does it well


## IES

Windows's own

It had so many problems


#### Linux/Apache System Calls

We have two websites, one with Apache/Linux, and the other running on IES/Windows

We were shown two graphs of the system calls on each Apache and IES, and IES is far more complicated compared to Apache


### Apache Demonstration


If we go to see what Apache is doing :

	sudo service apache status

This gives us Apache2's current status. 

On Kali Linux, it asks you for the password when asking for administrative privileges.

To start the service, if it is not running : 

	sudo service apache2 start


Open up your browser, and type in 

	http://localhost

in the address bar : 

if we get the Apache Status Page, we are all good !



The configuration file for Apache is located in : 

	/etc/apache2/apache2.conf

This is what we use to get Apache to listen in on various ports, load certain modules, we can implement measures to increase security, Sites-Enabled and Sites-Disabled indicates which sites should be present, and which should not. 

Although, there is nothing there about the Status Page. To look at its configuration files, it is located at : 

	/var/www/html


Copy the ```index.html``` file to make a duplicate :

cp /var/www/html/index.html /var/www/html/index.html-bak

Blank out the index.html file :

	sudo nano index.html

Since we have done this with the *sudo* command, the file would inherit the **root permissions**. Which command can we use to change the permissions ? answer is ...

	chmod



# LAMP


L for Linux
A for Apache
M for MariaDB or MySQL
P for PHP


Oracle bought out SQL. MySQL is currently owned by Oracle, but the free licensing might change. 

Someone created MariaDB for that reason, and it is guaranteed to be free.

MariaDB is already installed on Kali. But he wanted to point out something involving MariaDB : 


	cd /etc


You will see a *mysql* folder

	cd /etc/mysql

We will see a mariadb.conf. So, sometimes you will not find MySQL there, or just inhabited by MariaDB!

Let us check the status of mysql : 

	sudo service mysql status 

Output :

	
○ mariadb.service - MariaDB 11.4.3 database server
     Loaded: loaded (/usr/lib/systemd/system/mariadb.service; disabled; preset: disabled)
     Active: inactive (dead)
       Docs: man:mariadbd(8)
             https://mariadb.com/kb/en/library/systemd/


It is not a good idea to run MySQL together with MariaDB or other SQL-based services at the same time, due to the port usage being the same!


Let us check out PHP :

	cd /etc/php

We have version 8.2. Check what version of the application/service you are running, as sometimes there could be a conflict of required versions!

	php -v

We are running *8.2.21*! If we run into version-related issues, check online for resources!


To check the status of all the services :

	sudo service --status-all


>[!note]
>
>He worked for an organization that tried to change from MySQL to MariaDB, and the process is pretty tedious for an organization that has a lot of databases ...


>[!info]
>
>The website for the competition is : 
>
>http://cybersecuritychallenge.ca

>[!todo]
>
>Read up on : 
>
>- [ ] REST-APIs


>[!danger]
>
>There is a **Quiz** available!


# REST-APIs


There was one individual who created a standard of APIs.




## JSON


It is a very lightweight, human-readable file that is used for configure the *Data Exchange between the **Server** and the **Client***.




