

# The Blog Room on **TryHackMe


>[!todo]
>
>>[!mission]
>>
>>You are tasked with hacking into the **TryHackMe**'s ***Blog Room***. Find the **usernames**!
>>


>[!tools to use]
>
>WPScan
>
>>[!info]
>>
>>WPScan is an open-source WordPress vulnerability scanner that can be used to identify potential security issues within a WordPress website. It can scan for vulnerabilities, including:
>>- Known vulnerabilities in plugins and themes
>>- Misconfigured files and directories
>>  - Outdated software and plugins
>>  - Common web application attacks

Here's an example of how you can use some of its options:

To start with, we'll first download the tool using pip:


`pip install wpscan`

Now that it's installed, let's scan a WordPress website. Let's say I want to scan [www.example.com](http://www.example.com/) :

`wpscan --url www.example.com`

WPScan will then start scanning the site and providing information about any vulnerabilities or issues it finds.

WPScan also allows you to specify specific plugins, themes, or user agents to target in your scan:

`wpscan --plugins=jetpack --themes=twentyseventeen --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"`

This command will scan for vulnerabilities in the Jetpack plugin and Twenty Seventeen theme, using a custom user agent.

WPScan also includes an update option:

`wpscan --update`

This option can be used to find outdated plugins and themes on your WordPress site and recommend updates.

These are just some basic examples of how you can use WPScan. It's worth noting that the tool has many more features and options, so be sure to check out its documentation for more information.


