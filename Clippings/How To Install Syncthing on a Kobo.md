---
title: "How To Install Syncthing on a Kobo"
source: "https://guissmo.com/blog/how-to-install-syncthing-on-a-kobo/"
author:
  - "[[Jared Asuncion]]"
published:
created: 2025-12-05
description: "Unlock wireless Kobo syncing! Learn how to install Syncthing on your Kobo Clara 2E for seamless 2-way file transfer. Move files from Kobo & laptop."
tags:
  - "clippings"
---
- [Blog](https://guissmo.com/blog)
	- [Tech](https://guissmo.com/blog/category/tech)
		- How To Install Syncthing on a Kobo

On this page

- [Prerequisites](https://guissmo.com/blog/how-to-install-syncthing-on-a-kobo/#prerequisites)
- [Getting SSH to work](https://guissmo.com/blog/how-to-install-syncthing-on-a-kobo/#getting-ssh-to-work)
- [Install and configure Syncthing](https://guissmo.com/blog/how-to-install-syncthing-on-a-kobo/#install-and-configure-syncthing)
- [Sanity Check: Test If It Works](https://guissmo.com/blog/how-to-install-syncthing-on-a-kobo/#sanity-check-test-if-it-works)
- [Adding NickelMenu scripts](https://guissmo.com/blog/how-to-install-syncthing-on-a-kobo/#adding-nickelmenu-scripts)

Tags

- [#kobo](https://guissmo.com/blog/tag/kobo)
- [#syncthing](https://guissmo.com/blog/tag/syncthing)
- [#dropbox](https://guissmo.com/blog/tag/dropbox)
- [#ssh](https://guissmo.com/blog/tag/ssh)
- [#elliptic curves](https://guissmo.com/blog/tag/elliptic-curves)
- [#koreader](https://guissmo.com/blog/tag/koreader)
- [#nickelmenu](https://guissmo.com/blog/tag/nickelmenu)

Pages

- [Home](https://guissmo.com/)
- [Blog](https://guissmo.com/blog)
- [Board Games](https://guissmo.com/board-games)
- [Contact](https://guissmo.com/contact)
- [CV](https://guissmo.com/cv)
- [Friends](https://guissmo.com/friends)
- [Uses](https://guissmo.com/uses)
- [Phonebook](https://guissmo.com/phonebook)

Dream, Believe, Subscribe

- [RSS Feed](https://guissmo.com/blog/rss.xml) ([What's a feed?](https://aboutfeeds.com/))

# How To Install Syncthing on a Kobo

I finally found **THE** way to sync my eBooks from my laptop to Kobo by installing Syncthing.

I used to use [a Dropbox plugin](https://guissmo.com/blog/2023-kobo-guide-dropbox-integration/) and [an Omnivore plugin](https://guissmo.com/blog/swap-pocket-omnivore-on-your-kobo-converter-github/). Both of those were fun weekend hacking projects but both only gave a one-way receive-only sync. If I wanted to move a file *from* the Kobo to another machine, say exported highlights, then I have to physically connect the Kobo to that machine. It’s 2025 and we can do better.

Quick side note: I followed the post on [Milwaukee County Blog](https://mkecountyblog.com/install-koreader-nickelmenu-and-syncthing-on-a-kobo-ereader). Some of their steps did not work for me, so I’m writing down what worked on my Kobo Clara 2E. Also, I find it curious how a county seems to have a blog dealing with technology but why not?

# Prerequisites

If you’re following this write-up you need to have KoReader and NickelMenu installed. There are [one-click packages](https://www.mobileread.com/forums/showthread.php?t=314220) to install both at the same time. Just read up on it and follow the instructions. Feel free to ask if you get stuck.

The idea of this *hack* is to *install* Syncthing on the Kobo via SSH then add scripts to NickelMenu so that the Kobo can start and stop its instance of Syncthing.

You also clearly to have another machine with Syncthing installed to sync files with. Here’s [one way to setup Syncthing](https://guissmo.com/blog/tag/syncthing/).

More of a disclaimer than a pre-requisite, this guide is not for the faint of heart.

# Getting SSH to work

First, you’ll have to add your **public SSH key** into `/mnt/onboard/KOBOeReader/.adds/koreader/settings/SSH/authorized_keys`. However, as pointed out in this [Github thread](https://github.com/koreader/koreader/issues/8370#issuecomment-1283562382) and [this section](https://github.com/koreader/koreader/wiki/SSH#troubleshooting), the key must use **ecdsa**, also known as the **elliptic curve Digital Signature Algorithm**. Hooray for [math](https://guissmo.com/blog/tag/math/)! To generate an ssh key which uses this scheme, it suffices to run `ssh-keygen -t ecdsa`.

If at any point you need to debug using `ssh`, you could add `-v` or `-vvvv` or anything in between to see debug lines. The more `v`s, the noisier it gets.

On your Kobo, open KoReader, click the cog icon. Then enable Wifi connection and the SSH server. I think it’s best to have the SSH port to be `2222` instead of `22`. You’ll also have to check the **Login without password (DANGEROUS)** option. Just make sure to turn off the SSH server once we’re done installing. Once you’ve set it up, enable the SSH server by checking the checkbox and **take note of the IP address** that appears.

# Install and configure Syncthing

Next step is to download the latest version of Syncthing. Download the [latest Syncthing version](https://syncthing.net/downloads/) for ARM (32‑bit), Linux. Take the `syncthing` binary, and copy it onto the machine using SSH. I copied it to `/mnt/onboard/.adds`. Something like

```
scp -P 2222 syncthing root@192.168.1.87:/mnt/onboard/.adds/
```

should do the trick. According to the blog post I followed, we should also copy SSL certs onto the Kobo like so:

```
scp -P /etc/ssl/certs/ca-certificates.crt root@192.168.1.87:/etc/ssl/certs/
```

# Sanity Check: Test If It Works

Run that `syncthing` binary on the Kobo machine via SSH.

Apart from the text that appears, you can also check that the installation works by going to `http://<KOBO IP ADDRESS>:8384`, where `<KOBO IP ADDRESS>` was the IP address that looked something like `192.168.1.X` that you should have taken note of when you enabled the Kobo SSH server.

At this point, you could start adding folders to sync. It is highly recommended to secure the GUI with a password, so do that at some point too.

Stop the process by using Ctrl+C and you have now installed Syncthing! But to start and stop the process, you shouldn’t need to enable your SSH server every time. After all, it’s dangerous.

# Adding NickelMenu scripts

On `/mnt/onboard/.adds/scripts`, a directory you should create if you haven’t yet, make two files, `syncthing-start` and `syncthing-stop`.

The file `syncthing-start` should contain:

```
#!/bin/sh

/mnt/onboard/.adds/syncthing serve &
```

and `syncthing-stop` should contain:

```
#!/bin/sh

/usr/bin/pkill syncthing
```

Note that `syncthing-start` references the `syncthing` binary so if you placed it elsewhere, you have to modify the file as well.

Finally, go to the NickelMenu folder, which is in `/mnt/onboard/.adds/nm` in my machine. Write a new `txt` file and name it `syncthing` and paste the following:

```
menu_item :main    :Start Syncthing    :cmd_spawn         :quiet :exec /mnt/onboard/.adds/scripts/syncthing-start
  chain_always                         :nickel_setting    :enable :force_wifi
  chain_always                         :nickel_wifi       :enable
  chain_always                         :nickel_wifi       :autoconnect_silent
  chain_success                        :cmd_spawn         :quiet :exec /mnt/onboard/.adds/scripts/syncthing-start
menu_item :main    :Stop Syncthing     :cmd_spawn         :quiet :exec /mnt/onboard/.adds/scripts/syncthing-stop
  chain_always                         :nickel_setting    :disable :force_wifi
  chain_always                         :nickel_wifi       :disable
```

This is a lightly edited version of [this Github gist](https://gist.github.com/alechemy/c0851386077db797499253d8538b6e4e) and it seems to work even without the rescan books line. Maybe that will bite me in the ass one day but whatever.

And that’s it. Don’t forget to turn off the SSH server on your Kobo machine and enjoy never having to connect your Kobo via USB like a caveman ever again.

Posts on Tech[RSS](https://guissmo.com/blog/category/tech/rss.xml "RSS feed for Tech")

[«How To Connect FreshRSS To NetNewsWire](https://guissmo.com/blog/how-to-connect-freshrss-to-netnewswire)[My current AI Code Review Workflow»](https://guissmo.com/blog/my-current-ai-code-review-workflow)

Posts on this blog [RSS](https://guissmo.com/blog/rss.xml "RSS feed for all blog posts")

[«How To Connect FreshRSS To NetNewsWire](https://guissmo.com/blog/how-to-connect-freshrss-to-netnewswire)[My current AI Code Review Workflow»](https://guissmo.com/blog/my-current-ai-code-review-workflow)