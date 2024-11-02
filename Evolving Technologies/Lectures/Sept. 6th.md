


# Shodan


port 514 

#### Syntax 

port :3389 country:CA


If we wish to target a random organization ,

>
>	port:3389 country:CA

Port : 554 webcam

Another example : 

VNC's port and enter the country code 



Apache server ( new update : 


http.


ssl v.2 is very old. It is an old web appplication that has a ton of vulnerabilties 

ss,version:sslv2-ssl.version:tlsv1,tlsv1.2,tlsv1.3

ssh port:22,3333

vuln:CVE-2014-....




## Open Source Code 



On Github, there are a lot of opensource projects ;


megacorpone.com on github


If we look through it, we would find a username and hash combination


There are a lot of sensitive information



A client of Brian's has set a text for MFA, and someone found a key on his website. It could be referred to as a denial of service, due to the limited number of login attempts




## The Harvester


It is a more-active approach. Mind the capitalization on the name:

theHarvester


Once we have an email address, we could deduce all of them ( such as firstname.lastname@company.com)


We set the target to nscc :


>theHarvester -d nscc



Some of the sources ,you need an API key 


Look at the sources, and find out which sources need an API key.


We can add API keys at /etc/theHarvester/api-keys.yaml

sign up for **intelx.com**, grab the API key, and add the api key to the api-keys.yaml





## Recon-NG


It is module based!

It is a framework for recon

> reconng

go to 

> marketplace


the one we want is google_site_web (google hostname enumerator)


It does the site: google hacking operator


> module load recon/domains-hosts/google_site_web


we type 

>info 


It tells us the options and what it needs from us


> back (takes us back to the previous page)



The thing about subdomains is the CNAME record. vpn.nscc.ca points to the vpn

If we want to find a mail server, or an open-facing RDP port


We cannot look up CNAMEs, we have to bruteforce them


>[!info]
>
>What is a **CNAME**? 
>
>	A "canonical name" (CNAME) record points from an alias domain to a "canonical" domain. A CNAME record is used in lieu of an [A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/), when a [domain](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/) or subdomain is an alias of another domain. All CNAME records must point to a domain, never to an [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/). Imagine a scavenger hunt where each clue points to another clue, and the final clue points to the treasure. A domain with a CNAME record is like a clue that can point you to another clue (another domain with a CNAME record) or to the treasure (a domain with an A record).


We can use **gobuster** to find the directory structure. 



The difference between gobuster and this , is gobuster does domain requests, while **ReconNG** goes through Google. 

gobuster is more bruteforcing it, and it is taxing



## Maltego


Maltego is useful for having an eagle-eye view of the targets.


We would need an account for it. We would sign in , make an account, and we would have a visual graph. 


Go to Search > Domain 


Right-click on the Domain > type nscc.ca


Rightclick on nscc.ca , and then click "run"



It goes and pulls all kinds of linked entities to NSCC.ca , and presents it graphically!



It can make a connection to a person from an email address. 



## Gobuster


>gobuster dir -u http://www.nscc.ca (or dvwa) -w directories.txt (wordlist)


You can find wordlists on SecLists , DirBuster ,...


It will look through, and find all the available folders it 



BurpIntruder can be used to stay under the radar



>[!hint]
>
>
>Go through the web page's source code. There could be useful comments and other useful information. 

>use gobuster and reconng for a target website that we have!



>[!todo]
>
>Go through all these tools. Our first assignment will involve as much reconnaisance as possible on a website
