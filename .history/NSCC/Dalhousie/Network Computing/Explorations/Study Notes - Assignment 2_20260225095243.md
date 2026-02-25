# CSCI-3171 Network Computing

## Assignment 2 – Winter 2026

### Submission Instructions:

Submit one PDF file for your assignment on Brightspace under the Assignment 2 portal. Please ensure the
following components are included:

1. Provide comprehensive steps for any computations, along with explanations of your methodology. If
   you made assumptions, clearly explain, and justify them. Just writing the final answer will result in
   points being deducted.
2. Ensure that your full name and banner ID are clearly mentioned in the report.
   Late submission: Refer to the syllabus on Brightspace for a complete description of the late submission
   polic
   -----

### Problem 1

1. Suppose an HTTP client makes a request to the www.example.com web server.  The client has never requested a given base object, nor has it communicated recently with the www.example.com server. You can assume, however, that the client host knows the IP address of www.example.com.

   Q1. How many round-trip mes (RTTs) are needed from when the client first makes the request to when the base page is completely downloaded, assuming the me needed by the server to transmit the base page into the server's link is equal to 1/2 RTT and that the me needed to transmit the HTTP GET into the client's link is zero?  (You should consider any TCP setup me
2. required before the HTTP GET is sent by the client, the me needed for the server to transmit the
   requested object, and any propaga on delays not accounted for in these amounts of me.)

   ---

   Suppose now that after downloading the base file, the browser encounters a jpeg object in the base html
   file that is stored on www.example.com, and therefore makes another GET request to www.example.com
   for that referenced jpeg object.
   Q2. How many round-trip mes (RTTs) are needed from when the client first makes the request to
   when the base page and the jpeg file are completely downloaded, assuming the me needed by
   the server to transmit the base file, or the jpeg file into the server's link is (each) equal to 1/2 RTT
   and that the me needed to transmit the HTTP GET into the client's link is zero? You should
   assume that persistent HTTP 1.1 is being used.  (You should consider any TCP setup me required
   before an HTTP GET is sent by the client, the me needed for the server to transmit the requested
   object, and any propaga on delays not accounted for in these amounts of me.) (1 point
   calcula on, 1 point answer)
   Problem 2
   Consider the following scenario, in which a Web browser (lower) connects to a web server (above).  There
   is no web cache in this question (so make sure you understand the difference between a browser cache
   and a web cache).  Assume that the total Round Trip Time (RTT) propagation and queueing delay between
   the browser and web server is 200 msec.
   Suppose that the browser makes an HTTP request to the server for an HTTP object, that the browser has
   a copy of that object in its cache, but that copy may or may not be up to date in its cache (and so the
   browser requests the object using the HTTP If-Modified-Since header field).  Assume that the time taken
   to transmit an HTTP reply (by the sender into the TCP connection) that contains a requested object in the
   body of an HTTP reply is 50 msec, but that the time taken to transmit a HTTP reply with a "304 Not
   Modified" reply code without an included object is negligible (e.g., zero). You can assume that a TCP
   connection has already been set up, so do not include that delay in your answer below.
   Q3. What is the me from when the browser issues the ini al HTTP GET request un l it can display
   the requested object in the case that the browser does not have the requested object in its
   browser cache? (1 point calcula on, 1 point answer)
   Q4. What is the me from when the browser issues the ini al HTTP GET request un l it can display
   the requested object in the case that the browser does have the requested object in its browser
   cache? (1 point calcula on, 1 point answer)
   Suppose now that 90% of the HTTP requests are for objects that are up to date in the browser's cache,
   and so 10% are cache "misses" and will require the up-to-date object to be downloaded and browser
   cached.
   Q5. What is the average me (over all requests that the browser makes to this site) from when the
   browser issues the ini al HTTP GET request un l it can display the requested object? (1 point
   calcula on, 1 point answer)
   Problem 3
   Consider the following scenario, in which a Web browser (lower) connects to a web server (above).  There
   is also a local web cache in the bowser's access network.  In this question, we will ignore browser caching
   (so make sure you understand the difference between a browser cache and a web cache). Assume that
   the total Round Trip Time propagation, queueing and object transmission delay between the browser and
   2
   sml@dal.caweb server (and including TCP setup time) is 250 msec; if the object is retrieved from the local web cache,
   this delay is only 10 msec.
   Suppose that 80 percent of the time when the browser makes a request, the requested object is found in
   the local web cache.Q6. What is the average me (over all requests that the browser makes to this site) from when the
   browser issues the ini al HTTP GET request un l it can display the requested object? (1 point
   calcula on, 1 point answer)
   In the following question, we want to focus on the utilization of the 100 Mbps access link between the
   two networks. Suppose that each requested object is 10Mbits, and that 9 HTTP requests per second are
   being made to origin servers from the clients in the access network. Note that 80% of the requested
   objects by the client are found in the local web cache.
   Q7. What is the u liza on (ra o of throughput to transmission rate) of the access link? (1 point
   calcula on, 1 point answer)
   Problem 4
   Suppose that the local DNS server caches all information coming in from all root, TLD, and authoritative
   DNS servers for 20 time units. (Thus, for example, when a root server returns the name and address of a
   TLD server for .ca, the cache remembers that this is the TLD server to use to resolve a .ca name).  Assume
   also that the local cache is initially empty, that iterative DNS queries are always used, that DNS requests
   are just for name-to-IP-address translation, that 1 time unit is needed for each server-to-server or host
   to-server (one way) request or response, and that there is only one authoritative name server (each) for
   any .ca domain.
   3
   sml@dal.caWe consider a PC named local host on a university network in France. The DNS server configured for this
   network is named local DNS server. Consider the following DNS requests, made by the local host in France
   at the given times:
3. t=0, the local host requests that the name dal.ca be resolved to an IP address.
4. t=1, the local host requests that the name icann.org be resolved to an IP address.
5. t=5, the local host requests that the name concordia.ca be resolved to an IP address. (Hint: be
   careful!)
6. t=10, the local host again requests that the name dal.ca be resolved to an IP address.
7. t=12, the local host requests that the name utoronto.ca be resolved to an IP address.
8. t=30, the local host again requests that the name dal.ca be resolved to an IP address. (Hint: be
   careful!)
   Q8. Calculate the dura on (in me units) required for each of the six requests to be resolved. Provide
   explana ons for your results. (6 points calcula on, 6 points answer)
   4
   sml@dal.ca

Let's get this done efficiently while ensuring the concepts really stick.

To maximize memory retention, I recommend we use a method called  **Active Recall** . Instead of me explaining the steps immediately, I'll ask you to retrieve the relevant concepts from your memory (or the slides) first. This effort of "pulling" information out is what strengthens long-term memory.

We can tackle the assignment question by question.

Let's start with  **Question 1** , which asks about the total delay for a packet to travel from a source to a destination.

Based on your lecture notes on performance, what are the **four types of delay** that contribute to the total nodal delay?
