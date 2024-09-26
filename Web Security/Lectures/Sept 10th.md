


CyberSci - National Finals 2024 Ottawa June 20-23 2024


## Web Security


We will be installing Kali Linux or other Debian-based distributions


We can use Ubuntu, but it is preferred that we use Kali Linux

Install Firefox and FoxyProxy

We will set up OWASP Juice Shop


We are being taught about how to infiltrate into devices, but that does not make us experts into the subject


He is certain that someone can do a Denial of Service attack on a car.


With computers, there is a finesse.


We talk about cyber attacks against web applications


## SQL Injection


We go to a website that is a shop. When programmers create code, if it is done badly, such as Form Fields, some websites does not have good measures to prevent it from crashing. Some limits the number of characters that you can enter, and it is much better, as they know how to create a proper webform. 

It limits the number of problems people can inject into the system. 


He used to get a catalogue involving cars. He did not get one one year, and he called them. They accused him of hacking into their website 


When we discuss bad programming :

You leave flaws in the code, and individuals will exploit it.  It is best to make it custom!

>[!example]
>
>You can make a GoDaddy page, or use Amazon to set up a store. For more customization, Shopify is popular and stable. Shopify is a huge target, because if they take them down, they take down thousands of pages. if you custom-build your own, such as a company building the shopping cart from scratch, it is best to do it that way. He has seen someone who placed a measure to prevent SQL Injection, and ban the offending party for six months!


## Enigma Machine


In the Imperial War Museum, Bletchly Park has a full Enigma machine, as well as a Bombe, which was created first by Polish cryptographers. 


Allan Turing used the Bombe to attack the Enigma encryption. 


The Polish were the first to create a Bombe, but it was Allan Turning who first used it. They came up with a method to crack the Enigma code. 


The Nazis had a flaw in their system, where they used "Heil Hitler!" always in the code. So, when we discuss the ciphers , this Enigma cypher is quite sophisticated!

>[!info]
>
>Check out the **Enigma Machine Emulator**!
>
>[Enigma Machine Emulator - 101 Computing](https://www.101computing.net/enigma-machine-emulator/)


They still had many encrypted messages encrypted with the Enigma machine , and they asked the public (and still do) to help crack these messages with their computers. 



>[!todo]
>
>1. Set up a Kali Virtual Machine
>2. Set up OWASP Juice Shop


#### OWASP


They are a volunteer organization specializing in **Web Applications' Cyber Security**. They try to teach Web Application Cyber Security. Their goal is to have a more-robust security for Web Applications. 

They are similar to NEST, and every year, they update the **Top Ten Web Application Vulnerabilities**. They keep this list up to date. 


Here is the **2024 OWASP Top 10 Vulnerabilities** : 


- [**A01:2021-Broken Access Control**](https://owasp.org/Top10/A01_2021-Broken_Access_Control/) moves up from the fifth position; 94% of applications were tested for some form of broken access control. The 34 Common Weakness Enumerations (CWEs) mapped to Broken Access Control had more occurrences in applications than any other category.
- [**A02:2021-Cryptographic Failures**](https://owasp.org/Top10/A02_2021-Cryptographic_Failures/) shifts up one position to #2, previously known as Sensitive Data Exposure, which was broad symptom rather than a root cause. The renewed focus here is on failures related to cryptography which often leads to sensitive data exposure or system compromise.
- [**A03:2021-Injection**](https://owasp.org/Top10/A03_2021-Injection/) slides down to the third position. 94% of the applications were tested for some form of injection, and the 33 CWEs mapped into this category have the second most occurrences in applications. Cross-site Scripting is now part of this category in this edition.
- [**A04:2021-Insecure Design**](https://owasp.org/Top10/A04_2021-Insecure_Design/) is a new category for 2021, with a focus on risks related to design flaws. If we genuinely want to “move left” as an industry, it calls for more use of threat modeling, secure design patterns and principles, and reference architectures.
- [**A05:2021-Security Misconfiguration**](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/) moves up from #6 in the previous edition; 90% of applications were tested for some form of misconfiguration. With more shifts into highly configurable software, it’s not surprising to see this category move up. The former category for XML External Entities (XXE) is now part of this category.
- [**A06:2021-Vulnerable and Outdated Components**](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/) was previously titled Using Components with Known Vulnerabilities and is #2 in the Top 10 community survey, but also had enough data to make the Top 10 via data analysis. This category moves up from #9 in 2017 and is a known issue that we struggle to test and assess risk. It is the only category not to have any Common Vulnerability and Exposures (CVEs) mapped to the included CWEs, so a default exploit and impact weights of 5.0 are factored into their scores.
- [**A07:2021-Identification and Authentication Failures**](https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/) was previously Broken Authentication and is sliding down from the second position, and now includes CWEs that are more related to identification failures. This category is still an integral part of the Top 10, but the increased availability of standardized frameworks seems to be helping.
- [**A08:2021-Software and Data Integrity Failures**](https://owasp.org/Top10/A08_2021-Software_and_Data_Integrity_Failures/) is a new category for 2021, focusing on making assumptions related to software updates, critical data, and CI/CD pipelines without verifying integrity. One of the highest weighted impacts from Common Vulnerability and Exposures/Common Vulnerability Scoring System (CVE/CVSS) data mapped to the 10 CWEs in this category. Insecure Deserialization from 2017 is now a part of this larger category.
- [**A09:2021-Security Logging and Monitoring Failures**](https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/) was previously Insufficient Logging & Monitoring and is added from the industry survey (#3), moving up from #10 previously. This category is expanded to include more types of failures, is challenging to test for, and isn’t well represented in the CVE/CVSS data. However, failures in this category can directly impact visibility, incident alerting, and forensics.
- [**A10:2021-Server-Side Request Forgery**](https://owasp.org/Top10/A10_2021-Server-Side_Request_Forgery_%28SSRF%29/) is added from the Top 10 community survey (#1). The data shows a relatively low incidence rate with above average testing coverage, along with above-average ratings for Exploit and Impact potential. This category represents the scenario where the security community members are telling us this is important, even though it’s not illustrated in the data at this time.


>[!todo]
>
>Let us Install : 
>
>1. Kali Linux
>2. Firefox
>3. FoxyProxy


