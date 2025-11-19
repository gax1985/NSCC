[Syslog Explained | Cisco CCNA 200-301](https://www.youtube.com/watch?v=BMVHHX02T4Q)



Hey what's up guys welcome to CertBros. In  this video we're going to be looking at Syslog.

Meet Bill. Bill is a network admin, and it's  his job to manage and troubleshoot the network.  

Part of that job means searching  through log files when things go wrong.  

This network is pretty small so it's easy to  keep on top of all of the log information.  

The problem is, as the business grew so did the  network. It got bigger and bigger and bigger.  

Now it's nearly impossible to keep on top of all  of the network log information. So Bill decided to  

find a solution and he discovered syslog servers.  A syslog server allows all of his network devices  

to send their log information to one centralized  place. The log messages will be sent on UDP port  

514 to the syslog server. From here he can manage,  search and archive all of the log information. Ok  

so i hope you liked my little story there.  Using a syslog server allows us to centrally  

manage our log information. Why would you want  to do that? Well there are a few reasons why.  

First log information is very important  when troubleshooting problems.  

Let's say a user reports a network outage, you  can go through all of the log information to  

see if there were any problems. Another benefit  of storing log information in a central place  

is data retention. Cisco devices by default store  log information in RAM. This means when a device  

reboots the logs are erased. Other vendors may  write log information to disk but network devices  

tend to have a small amount of storage available.  Keeping all of your log information in one place  

allows for easy archiving. Ok, so now we know  what a syslog server is and why we use them  

let's look at some log messages. This is a  syslog message, it will probably look familiar  

to you by now. It's the messages you see when  configuring routers and switches. It may not  

seem like it straight away but these messages  follow an industry-standard, this makes it easy  

to correlate logs from different vendors. The  first part is the timestamp or sequence number,  

on cisco devices, you can choose which one you  want to use. The next part is called the facility  

this shows the source of the message. Next, we  have severity this shows you how urgent the log  

message is. Then we have something called the  mnemonic this is a code to identify the message.  

And finally, we have the description which  contains the log message. There are two key  

bits of information here that we need to look  at further. These are facility and severity.  

First, let's look at the facility. Here is a table  of all available facilities. Remember the facility  

represents the process that generated the message.  Because syslog was adopted early by unix systems  

these facility codes are mostly unix-based. For  example if a unix kernel generated a message  

the facility would be kern, if an authentication  message was locked the facility may show auth.  

You'll notice there aren't many network related  facilities. At the bottom we have 16 to 23  

local use, these are undefined custom values  that are generally used for network devices.  

So the next and probably the most  important bit of information here  

is the severity. Syslog has eight severity levels  ranging from 0-7, the top is the most urgent  

so severity is 0 and the bottom is the  least urgent which is 7 for debug messages.  

This is important because you likely don't want  to send all log messages to your server. You  

can choose which messages are sent based on  their severity, this way your server doesn't  

get clogged up with messages you'd rather not  see. Now, unfortunately, this is one of those  

tables you're going to have to memorize for your  CCNA exam. You need to know not only the severity  

levels but which order they're in. As with most  of these things mnemonics come to the rescue.  

A popular one is Every Awesome Cisco Engineer  Will Need Ice Cream Daily. Another one i found  

was Ernie Always Cries Even When No One Is Dying,  which made me laugh probably more than it should.  

Ok, so now we've been over the theory let's  see it in action. Here is my computer,  

I'm running a program called kiwi syslog server.  There are lots of different syslog servers out  

there, some are free, some are paid. I'm using  this one because it's free for up to five  

devices. As you can see nothing is going on here.  That's because we haven't configured anything.  

The first thing i'm going  to do is go to file > setup

scroll down to inputs and if you're doing this at  home you will need to input the ip address of the  

device you want to receive syslog messages from.  I've already entered the ip address of my cisco  

router. After you've done that just click ok. Our  server is now ready to receive syslog messages  

but still nothing is happening. We need to  configure the router to send syslog messages  

to the server. So i'll open the router and you'll  already see some familiar-looking messages,  

these are syslog messages showing when  the router boots up. You'll notice the  

timestamps are completely wrong so we'll  need to fix that. It's recommended to use an  

NTP server to sync our time correctly but in  this example i'll just set the time manually.  

I'm already in privilege exec mode so I don't have  to type enable. Now i'll type clock question mark,  

we only have one option here and  that is to set the clock manually.  

If i type clock set question mark, we can see that  it asks for the hours minutes and seconds. It's  

8:22 so I'll just type 08 22 00. It then wants  the day and the month I'll type 0 7 September,  

and if I press the question mark one more time it  asks us for the year, so I'll type good old 2020.  

When we hit enter we're greeted with an  information message telling us the clock  

has been changed. Now the time is set we need to  make sure it's included in the syslog messages.  

To do this we need to enter global  configuration by typing configure terminal,  

now i'll type service question mark

lots of information here. The two main ones are  sequence numbers and timestamps. Remember earlier  

when i said syslog messages can either  have a sequence number or a timestamp,  

this is where we choose. I'll choose timestamps  

and if I type question mark we have the option  for debugging and log messages. We want to  

change the log messages so we'll type log, again  question mark, and now we get the choice between  

date time or system uptime, of course we  want the date time so we type date time.  

The last few options here, if we choose msec then  it will include the milliseconds in the timestamp,  

this can be very handy when troubleshooting.  Hit enter and now the timestamps are set.  

We're now ready to tell the router to  send log messages to our syslog server.  

First, we tell the router where to send the  logs. We do this with the command logging,  

and then the ip address of our  server, in my case it's 192.168.0.1.  

Now we need to choose which logs to send. If i  type logging again, but this time with a question  

mark, we'll see lots of options. The one I want  is trap. The description says "set syslog server  

logging level" so we type logging trap and to see  the levels we type a question mark, here we choose  

the severity of logs we want to send. In this  example, we're going to choose informational.  

An important note here is that whichever  level you choose, it will send those logs  

as well as the logs with a higher severity. So  we've chosen informational which is level six,  

the router will send all log messages  with a severity of zero to six.  

The last thing I need to do is configure  the ip address. So i'll type interface  

fastethernet 0/0 then ip address 192.168.0.254  and a subnet mask of 255.255.255.0

and i'll bring the interface up by typing no  shutdown. Now our router is configured and  

waiting to send some log messages, we just  need to generate some logs. To do this I'll  

just exit here, go into another interface  and this time it will be fastethernet 0/1

and type no shutdown. Our router will generate  some logs saying the interface is now up.  

I'll now shut it down again  to generate a few more.

If we now go back to our syslog server, we can now  see our router's logs. From here we could search,  

filter and correlate all of our log messages.  This video is part of the full CCNA course  

which can be found in the description so  please feel free to go and check that out.  

If you like this video, don't forget to give it  a thumbs up, leave a comment and subscribe. The  

support from you guys really helps this channel  grow. Other than that, thank you for watching