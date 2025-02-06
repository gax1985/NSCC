This page is going to guide you through the process of setting up your environment and running your first investigation.

## Installing the default modules

By default, sn0int doesn’t have any modules installed. If you start up sn0int it’s going to download some files that it needs and then suggests to install a number of recommended modules:

```
<span></span>$ sn0int

                   ___/           .
     ____ , __   .'  /\ ` , __   _/_
    (     |'  `. |  / | | |'  `.  |
    `--.  |    | |,'  | | |    |  |
   \___.' /    | /`---' / /    |  \__/

        osint | recon | security
      irc.hackint.org:6697/#sn0int

[+] Connecting to database
[+] Downloading public suffix list
[+] Downloading "GeoLite2-City.mmdb"
[+] Downloading "GeoLite2-ASN.mmdb"
[+] Loaded 0 modules
[*] No modules found, run pkg quickstart to install default modules
[sn0int][default] &gt;
```

Typing `pkg quickstart` is going to get you a fair number of featured modules:

```
<span></span><span>[</span><span>sn0int</span><span>][</span><span>default</span><span>]</span> <span>&gt;</span> <span>pkg</span> <span>quickstart</span>
<span>[</span><span>+</span><span>]</span> <span>Installing</span> <span>kpcyrd</span><span>/</span><span>asn</span>
<span>[</span><span>+</span><span>]</span> <span>Installing</span> <span>kpcyrd</span><span>/</span><span>ctlogs</span>
<span>[</span><span>+</span><span>]</span> <span>Installing</span> <span>kpcyrd</span><span>/</span><span>dns</span><span>-</span><span>resolve</span>
<span>[</span><span>+</span><span>]</span> <span>Installing</span> <span>kpcyrd</span><span>/</span><span>geoip</span>
<span>[</span><span>+</span><span>]</span> <span>Installing</span> <span>kpcyrd</span><span>/</span><span>hackertarget</span><span>-</span><span>subdomains</span>
<span>[</span><span>+</span><span>]</span> <span>Installing</span> <span>kpcyrd</span><span>/</span><span>otx</span><span>-</span><span>subdomains</span>
<span>[</span><span>+</span><span>]</span> <span>Installing</span> <span>kpcyrd</span><span>/</span><span>passive</span><span>-</span><span>spider</span>
<span>[</span><span>+</span><span>]</span> <span>Installing</span> <span>kpcyrd</span><span>/</span><span>pgp</span><span>-</span><span>keyserver</span>
<span>[</span><span>+</span><span>]</span> <span>Installing</span> <span>kpcyrd</span><span>/</span><span>threatminer</span><span>-</span><span>ipaddr</span>
<span>[</span><span>+</span><span>]</span> <span>Installing</span> <span>kpcyrd</span><span>/</span><span>threatminer</span><span>-</span><span>subdomains</span>
<span>[</span><span>+</span><span>]</span> <span>Installing</span> <span>kpcyrd</span><span>/</span><span>url</span><span>-</span><span>scan</span>
<span>[</span><span>+</span><span>]</span> <span>Installing</span> <span>kpcyrd</span><span>/</span><span>waybackurls</span>
<span>[</span><span>+</span><span>]</span> <span>Loaded</span> <span>12</span> <span>modules</span>
<span>[</span><span>sn0int</span><span>][</span><span>default</span><span>]</span> <span>&gt;</span>
```

## Adding something to scope

You probably want to separate your investigations so you should select a workspace where your results should go:

```
<span></span><span>[</span><span>sn0int</span><span>][</span><span>default</span><span>]</span> <span>&gt;</span> <span>workspace</span> <span>demo</span>
<span>[</span><span>+</span><span>]</span> <span>Connecting</span> <span>to</span> <span>database</span>
<span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>]</span> <span>&gt;</span>
```

Next, we have to start somewhere and add the first entity to our scope:

```
<span></span><span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>]</span> <span>&gt;</span> <span>add</span> <span>domain</span>
<span>Domain</span><span>:</span> <span>example</span><span>.</span><span>com</span>
<span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>]</span> <span>&gt;</span>
```

Note

There is a concept of a domain vs a subdomain. We are referring to a domain as everything that is a subdomain of a [public suffix][1]. For example, .com is a public suffix, which makes example.com a domain in sn0int terms. Every subdomain of that, like www.example.com, is referred to as a subdomain.

Note that example.com can be added as a subdomain as well since it can hold records. In that case, example.com is both the name of the dns zone, while also being an entity in that zone.

You can confirm this by running a select on the domains we now have:

```
<span></span><span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>]</span> <span>&gt;</span> <span>select</span> <span>domains</span>
<span>#1, "example.com"</span>
<span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>]</span> <span>&gt;</span>
```

Something we don’t need right now, but is going to be useful later on is the ability to filter your entities:

```
<span></span><span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>]</span> <span>&gt;</span> <span>select</span> <span>domains</span> <span>where</span> <span>id</span><span>=</span><span>1</span>
<span>#1, "example.com"</span>
<span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>]</span> <span>&gt;</span>
<span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>]</span> <span>&gt;</span> <span>select</span> <span>domains</span> <span>where</span> <span>value</span> <span>like</span> <span>%.</span><span>com</span>
<span>#1, "example.com"</span>
<span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>]</span> <span>&gt;</span>
<span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>]</span> <span>&gt;</span> <span>select</span> <span>domains</span> <span>where</span> <span>(</span> <span>value</span> <span>like</span> <span>e</span><span>%</span> <span>and</span> <span>value</span> <span>like</span> <span>%</span><span>m</span> <span>)</span> <span>or</span> <span>false</span>
<span>#1, "example.com"</span>
<span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>]</span> <span>&gt;</span>
```

Note

Almost all entities have a `value` column that holds the primary value of the entity.

## Running a module

Now that we have something to get started with, we can run our first module. First lets list all modules we have:

```
<span></span><span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>]</span> <span>&gt;</span> <span>pkg</span> <span>list</span>
<span>kpcyrd</span><span>/</span><span>asn</span> <span>(</span><span>0.1.0</span><span>)</span>
    <span>Run</span> <span>a</span> <span>asn</span> <span>lookup</span> <span>for</span> <span>an</span> <span>ip</span> <span>address</span>
<span>kpcyrd</span><span>/</span><span>ctlogs</span> <span>(</span><span>0.1.0</span><span>)</span>
    <span>Query</span> <span>certificate</span> <span>transparency</span> <span>logs</span> <span>to</span> <span>discover</span> <span>subdomains</span>
<span>kpcyrd</span><span>/</span><span>dns</span><span>-</span><span>resolve</span> <span>(</span><span>0.1.0</span><span>)</span>
    <span>Query</span> <span>subdomains</span> <span>to</span> <span>discovery</span> <span>ip</span> <span>addresses</span> <span>and</span> <span>verify</span> <span>the</span> <span>record</span> <span>is</span> <span>visible</span>
<span>kpcyrd</span><span>/</span><span>geoip</span> <span>(</span><span>0.1.0</span><span>)</span>
    <span>Run</span> <span>a</span> <span>geoip</span> <span>lookup</span> <span>for</span> <span>an</span> <span>ip</span> <span>address</span>
<span>kpcyrd</span><span>/</span><span>hackertarget</span><span>-</span><span>subdomains</span> <span>(</span><span>0.1.0</span><span>)</span>
    <span>Query</span> <span>hackertarget</span> <span>for</span> <span>subdomains</span> <span>of</span> <span>a</span> <span>domain</span>
<span>kpcyrd</span><span>/</span><span>otx</span><span>-</span><span>subdomains</span> <span>(</span><span>0.1.0</span><span>)</span>
    <span>Query</span> <span>alienvault</span> <span>otx</span> <span>passive</span> <span>dns</span> <span>for</span> <span>subdomains</span> <span>of</span> <span>a</span> <span>domain</span>
<span>kpcyrd</span><span>/</span><span>passive</span><span>-</span><span>spider</span> <span>(</span><span>0.1.0</span><span>)</span>
    <span>Scrape</span> <span>known</span> <span>http</span> <span>responses</span> <span>for</span> <span>urls</span>
<span>kpcyrd</span><span>/</span><span>pgp</span><span>-</span><span>keyserver</span> <span>(</span><span>0.1.0</span><span>)</span>
    <span>Query</span> <span>pgp</span> <span>keyserver</span> <span>for</span> <span>email</span> <span>addresses</span>
<span>kpcyrd</span><span>/</span><span>threatminer</span><span>-</span><span>ipaddr</span> <span>(</span><span>0.1.0</span><span>)</span>
    <span>Query</span> <span>ThreatMiner</span> <span>passive</span> <span>dns</span> <span>for</span> <span>subdomains</span> <span>of</span> <span>an</span> <span>ip</span> <span>address</span>
<span>kpcyrd</span><span>/</span><span>threatminer</span><span>-</span><span>subdomains</span> <span>(</span><span>0.1.0</span><span>)</span>
    <span>Query</span> <span>ThreatMiner</span> <span>passive</span> <span>dns</span> <span>for</span> <span>subdomains</span> <span>of</span> <span>a</span> <span>domain</span>
<span>kpcyrd</span><span>/</span><span>url</span><span>-</span><span>scan</span> <span>(</span><span>0.1.0</span><span>)</span>
    <span>Scan</span> <span>subdomains</span> <span>for</span> <span>websites</span>
<span>kpcyrd</span><span>/</span><span>waybackurls</span> <span>(</span><span>0.1.0</span><span>)</span>
    <span>Discover</span> <span>subdomains</span> <span>from</span> <span>wayback</span> <span>machine</span>
<span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>]</span> <span>&gt;</span>
```

Let’s start by querying certificate transparency logs:

```
<span></span><span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>]</span> <span>&gt;</span> <span>use</span> <span>ctlogs</span>
<span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>][</span><span>kpcyrd</span><span>/</span><span>ctlogs</span><span>]</span> <span>&gt;</span> <span>run</span>
<span>[</span><span>*</span><span>]</span> <span>"example.com"</span>                                     <span>:</span> <span>Subdomain</span><span>:</span> <span>"www.example.com"</span>
<span>[</span><span>*</span><span>]</span> <span>"example.com"</span>                                     <span>:</span> <span>Subdomain</span><span>:</span> <span>"m.example.com"</span>
<span>[</span><span>*</span><span>]</span> <span>"example.com"</span>                                     <span>:</span> <span>Subdomain</span><span>:</span> <span>"dev.example.com"</span>
<span>[</span><span>*</span><span>]</span> <span>"example.com"</span>                                     <span>:</span> <span>Subdomain</span><span>:</span> <span>"products.example.com"</span>
<span>[</span><span>*</span><span>]</span> <span>"example.com"</span>                                     <span>:</span> <span>Subdomain</span><span>:</span> <span>"support.example.com"</span>
<span>[</span><span>+</span><span>]</span> <span>Finished</span> <span>kpcyrd</span><span>/</span><span>ctlogs</span>
<span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>][</span><span>kpcyrd</span><span>/</span><span>ctlogs</span><span>]</span> <span>&gt;</span>
```

Looks like we’ve discovered some subdomains here. It might be tempting to throw some of them in a browser but hold on, there’s a more efficient way to approach this.

Hint

You can run the modules concurrently with `run -j3`.

## Running followup modules on the results

A lot of time has been spent on the database part. While it sort of feels like a no-sql database we are actually enforcing a schema for a reason instead of just using generic dictionaries and calling it a day.

It’s crucial that entities created by one module can be picked up by another module, like LEGOs. Let’s continue with a module to query the dns records:

```
<span></span><span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>][</span><span>kpcyrd</span><span>/</span><span>ctlogs</span><span>]</span> <span>&gt;</span> <span>use</span> <span>dns</span><span>-</span><span>resolve</span>
<span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>][</span><span>kpcyrd</span><span>/</span><span>dns</span><span>-</span><span>resolve</span><span>]</span> <span>&gt;</span> <span>run</span>
<span>[</span><span>*</span><span>]</span> <span>"www.example.com"</span>                                 <span>:</span> <span>Updating</span> <span>"www.example.com"</span> <span>(</span><span>resolvable</span> <span>=&gt;</span> <span>true</span><span>)</span>
<span>[</span><span>*</span><span>]</span> <span>"www.example.com"</span>                                 <span>:</span> <span>IpAddr</span><span>:</span> <span>93.184.216.34</span>
<span>[</span><span>*</span><span>]</span> <span>"www.example.com"</span>                                 <span>:</span> <span>"www.example.com"</span> <span>-&gt;</span> <span>93.184.216.34</span>
<span>[</span><span>*</span><span>]</span> <span>"m.example.com"</span>                                   <span>:</span> <span>Updating</span> <span>"m.example.com"</span> <span>(</span><span>resolvable</span> <span>=&gt;</span> <span>false</span><span>)</span>
<span>[</span><span>*</span><span>]</span> <span>"dev.example.com"</span>                                 <span>:</span> <span>Updating</span> <span>"dev.example.com"</span> <span>(</span><span>resolvable</span> <span>=&gt;</span> <span>false</span><span>)</span>
<span>[</span><span>*</span><span>]</span> <span>"products.example.com"</span>                            <span>:</span> <span>Updating</span> <span>"products.example.com"</span> <span>(</span><span>resolvable</span> <span>=&gt;</span> <span>false</span><span>)</span>
<span>[</span><span>*</span><span>]</span> <span>"support.example.com"</span>                             <span>:</span> <span>Updating</span> <span>"support.example.com"</span> <span>(</span><span>resolvable</span> <span>=&gt;</span> <span>false</span><span>)</span>
<span>[</span><span>+</span><span>]</span> <span>Finished</span> <span>kpcyrd</span><span>/</span><span>dns</span><span>-</span><span>resolve</span>
<span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>][</span><span>kpcyrd</span><span>/</span><span>dns</span><span>-</span><span>resolve</span><span>]</span> <span>&gt;</span>
```

Two things happened here: We’ve discovered some IP addresses and added them to scope, and we also updated our subdomain entities with new information, since we now know which of them are resolvable and which aren’t.

Let’s run the next module, which is actually going to check for websites on them, but let’s only target subdomains that we know are resolvable:

```
<span></span><span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>][</span><span>kpcyrd</span><span>/</span><span>dns</span><span>-</span><span>resolve</span><span>]</span> <span>&gt;</span> <span>use</span> <span>url</span><span>-</span><span>scan</span>
<span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>][</span><span>kpcyrd</span><span>/</span><span>url</span><span>-</span><span>scan</span><span>]</span> <span>&gt;</span> <span>target</span>
<span>#1, "www.example.com"</span>
    <span>93.184.216.34</span>
<span>#2, "m.example.com"</span>
<span>#3, "dev.example.com"</span>
<span>#4, "products.example.com"</span>
<span>#5, "support.example.com"</span>
<span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>][</span><span>kpcyrd</span><span>/</span><span>url</span><span>-</span><span>scan</span><span>]</span> <span>&gt;</span> <span>target</span> <span>where</span> <span>resolvable</span>
<span>[</span><span>+</span><span>]</span> <span>1</span> <span>entities</span> <span>selected</span>
<span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>][</span><span>kpcyrd</span><span>/</span><span>url</span><span>-</span><span>scan</span><span>]</span> <span>&gt;</span> <span>target</span>
<span>#1, "www.example.com"</span>
    <span>93.184.216.34</span>
<span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>][</span><span>kpcyrd</span><span>/</span><span>url</span><span>-</span><span>scan</span><span>]</span> <span>&gt;</span>
```

We can both preview and limit the targets that are going to be passed to the module with the target command. Once we are satisfied with our selection we can run this module:

```
<span></span><span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>][</span><span>kpcyrd</span><span>/</span><span>url</span><span>-</span><span>scan</span><span>]</span> <span>&gt;</span> <span>run</span>
<span>[</span><span>*</span><span>]</span> <span>"www.example.com"</span>                                 <span>:</span> <span>Url</span><span>:</span> <span>"http://www.example.com/"</span> <span>(</span><span>200</span><span>)</span>
<span>[</span><span>*</span><span>]</span> <span>"www.example.com"</span>                                 <span>:</span> <span>Url</span><span>:</span> <span>"https://www.example.com/"</span> <span>(</span><span>200</span><span>)</span>
<span>[</span><span>+</span><span>]</span> <span>Finished</span> <span>kpcyrd</span><span>/</span><span>url</span><span>-</span><span>scan</span>
<span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>][</span><span>kpcyrd</span><span>/</span><span>url</span><span>-</span><span>scan</span><span>]</span> <span>&gt;</span>
```

We’ve now probed both port 80 and port 443 for each subdomain and found two http responses this way. If you want a list of urls you may want to visit in your browser can now query them:

```
<span></span><span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>][</span><span>kpcyrd</span><span>/</span><span>url</span><span>-</span><span>scan</span><span>]</span> <span>&gt;</span> <span>select</span> <span>urls</span>
<span>#1, "http://www.example.com/" (200)</span>
<span>#2, "https://www.example.com/" (200)</span>
<span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>][</span><span>kpcyrd</span><span>/</span><span>url</span><span>-</span><span>scan</span><span>]</span> <span>&gt;</span>
```

## Unscoping entities

Something you are going to run into is that modules are too greedy and add things to the scope we are not interested in. You can delete them using the delete command, but those are likely picked up by a module again.

What you can do instead is setting a flag on an entity that removes it from our scope. This is done using the noscope command:

```
<span></span><span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>]</span> <span>&gt;</span> <span>use</span> <span>ctlogs</span>
<span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>][</span><span>kpcyrd</span><span>/</span><span>ctlogs</span><span>]</span> <span>&gt;</span> <span>target</span>
<span>#1, "example.com"</span>
<span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>][</span><span>kpcyrd</span><span>/</span><span>ctlogs</span><span>]</span> <span>&gt;</span> <span>add</span> <span>domain</span>
<span>Domain</span><span>:</span> <span>google</span><span>.</span><span>com</span>
<span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>][</span><span>kpcyrd</span><span>/</span><span>ctlogs</span><span>]</span> <span>&gt;</span> <span>target</span>
<span>#1, "example.com"</span>
<span>#2, "google.com"</span>
<span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>][</span><span>kpcyrd</span><span>/</span><span>ctlogs</span><span>]</span> <span>&gt;</span> <span>noscope</span> <span>domains</span> <span>where</span> <span>value</span><span>=</span><span>google</span><span>.</span><span>com</span>
<span>[</span><span>+</span><span>]</span> <span>Updated</span> <span>1</span> <span>rows</span>
<span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>][</span><span>kpcyrd</span><span>/</span><span>ctlogs</span><span>]</span> <span>&gt;</span> <span>target</span>
<span>#1, "example.com"</span>
<span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>][</span><span>kpcyrd</span><span>/</span><span>ctlogs</span><span>]</span> <span>&gt;</span>
```

Entities that are unscoped are automatically ignored by all modules.

You can reverse this using the scope command:

```
<span></span><span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>][</span><span>kpcyrd</span><span>/</span><span>ctlogs</span><span>]</span> <span>&gt;</span> <span>target</span>
<span>#1, "example.com"</span>
<span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>][</span><span>kpcyrd</span><span>/</span><span>ctlogs</span><span>]</span> <span>&gt;</span> <span>scope</span> <span>domains</span> <span>where</span> <span>true</span>
<span>[</span><span>+</span><span>]</span> <span>Updated</span> <span>2</span> <span>rows</span>
<span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>][</span><span>kpcyrd</span><span>/</span><span>ctlogs</span><span>]</span> <span>&gt;</span> <span>target</span>
<span>#1, "example.com"</span>
<span>#2, "google.com"</span>
<span>[</span><span>sn0int</span><span>][</span><span>demo</span><span>][</span><span>kpcyrd</span><span>/</span><span>ctlogs</span><span>]</span> <span>&gt;</span>
```

Hint

All entities have this field, you can refer to it in queries using `unscoped=1`.

[1]: https://publicsuffix.org/