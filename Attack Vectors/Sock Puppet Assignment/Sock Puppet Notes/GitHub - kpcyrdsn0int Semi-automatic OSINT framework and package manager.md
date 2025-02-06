sn0int (pronounced [`/snoɪnt/`][1]) is a semi-automatic OSINT framework and package manager. It's used by IT security professionals, bug bounty hunters, law enforcement agencies and in security awareness trainings to gather intelligence about a given target or about yourself. sn0int is enumerating attack surface by semi-automatically processing public information and mapping the results in a unified format for followup investigations.

Among other things, sn0int is currently able to:

-   Harvest subdomains from certificate transparency logs and passive dns
-   Mass resolve collected subdomains and scan for http or https services
-   Enrich ip addresses with asn and geoip info
-   Harvest emails from pgp keyservers and whois
-   Discover compromised logins in breaches
-   Find somebody's profiles across the internet
-   Enumerate local networks with unique techniques like passive arp
-   Gather information about phonenumbers
-   Harvest activity and images from social media profiles
-   Basic image processing

sn0int is heavily inspired by recon-ng and maltego, but remains more flexible and is fully opensource. None of the investigations listed above are hardcoded in the source, instead they are provided by modules that are executed in a sandbox. You can easily extend sn0int by writing your own modules and share them with other users by publishing them to the sn0int registry. This allows you to ship updates for your modules on your own instead of pull-requesting them into the sn0int codebase.

For questions and support join us on IRC: [irc.hackint.org:6697/#sn0int][2]

[![asciicast](https://camo.githubusercontent.com/eee99b1b40b25bb02cd29f84c28511e5311e767c9b83832bab2e7c1dba96a247/68747470733a2f2f61736369696e656d612e6f72672f612f73685a33545659316f306f7047466c6e334f693244414d43422e737667)][3]

## Installation

[![Packaging status](https://camo.githubusercontent.com/59e993f5abad442cdc551ee117d9cae23aebebad11fbef18df4d17ee0713c609/68747470733a2f2f7265706f6c6f67792e6f72672f62616467652f766572746963616c2d616c6c7265706f732f736e30696e742e737667)][4]

Archlinux

Mac OSX

Debian/Ubuntu/Kali

There are prebuilt packages signed by a debian maintainer:

```
sudo apt install curl sq
curl -sSf https://apt.vulns.sexy/kpcyrd.pgp | sq dearmor | sudo tee /etc/apt/trusted.gpg.d/apt-vulns-sexy.gpg &gt; /dev/null
echo deb http://apt.vulns.sexy stable main | sudo tee /etc/apt/sources.list.d/apt-vulns-sexy.list
sudo apt update
```

Docker

```
docker run --rm --init -it -v "$PWD/.cache:/cache" -v "$PWD/.data:/data" ghcr.io/kpcyrd/sn0int
```

Alpine

OpenBSD

Gentoo

```
layman -a pentoo
emerge --ask net-analyzer/sn0int
```

NixOS

For everything else please have a look at the [detailed list][5].

## Getting started

-   [Installation][6]
    -   [Archlinux][7]
    -   [Mac OSX][8]
    -   [Debian >= bullseye, Ubuntu >= 20.04, Kali][9]
    -   [Debian <= buster, Ubuntu <= 19.10][10]
    -   [Fedora/CentOS/Redhat][11]
    -   [Docker][12]
    -   [Alpine][13]
    -   [OpenBSD][14]
    -   [Gentoo][15]
    -   [NixOS][16]
    -   [Windows][17]
-   [Build from source][18]
    -   [Install dependencies][19]
        -   [Archlinux][20]
        -   [Mac OSX][21]
        -   [Debian/Ubuntu/Kali][22]
        -   [Alpine][23]
        -   [OpenBSD][24]
        -   [Gentoo][25]
        -   [Windows][26]
    -   [Building][27]
-   [Running your first investigation][28]
    -   [Installing the default modules][29]
    -   [Adding something to scope][30]
    -   [Running a module][31]
    -   [Running followup modules on the results][32]
    -   [Unscoping entities][33]
-   [Autonoscope][34]
    -   [Domains][35]
    -   [IPs][36]
    -   [URLs][37]
-   [Writing your first module][38]
    -   [Creating a repository][39]
    -   [Publish your module][40]
    -   [Publish your repo][41]
    -   [Reading data from stdin][42]
-   [Database][43]
    -   [db\_add][44]
    -   [db\_add\_ttl][45]
    -   [db\_activity][46]
    -   [db\_update][47]
    -   [db\_select][48]
-   [Structs][49]
    -   [Domains][50]
    -   [Subdomains][51]
    -   [IpAddrs][52]
    -   [URLs][53]
    -   [Emails][54]
    -   [Phonenumbers][55]
    -   [Devices][56]
    -   [Networks][57]
    -   [Accounts][58]
    -   [Breaches][59]
    -   [Images][60]
    -   [Ports][61]
    -   [Netblocks][62]
    -   [CryptoAddrs][63]
    -   [Activity][64]
    -   [Relations][65]
        -   [subdomain\_ipaddr][66]
        -   [network\_device][67]
        -   [breach\_email][68]
-   [Activity][69]
    -   [Anatomy of an event][70]
    -   [Logging events][71]
    -   [Querying events][72]
    -   [Visualization][73]
-   [Notifications][74]
    -   [Receiving notifications][75]
        -   [Telegram][76]
        -   [Pushover][77]
        -   [Discord][78]
        -   [Signal][79]
        -   [Writing your own module][80]
    -   [Setting up notification rules][81]
    -   [Testing notifications][82]
    -   [Running sn0int automatically][83]
        -   [Monitors][84]
        -   [Timers][85]
-   [Keyring][86]
    -   [Managing the keyring][87]
    -   [Using access keys in scripts][88]
    -   [Using access keys as source argument][89]
-   [Configuration][90]
    -   [\[core\]][91]
    -   [\[namespaces\]][92]
    -   [\[network\]][93]
-   [Sandbox][94]
    -   [Linux][95]
    -   [OpenBSD][96]
    -   [IPC Protocol][97]
    -   [Limitations][98]
    -   [Diagnosing a sandbox failure][99]
-   [Function reference][100]
    -   [asn\_lookup][101]
    -   [base64\_decode][102]
    -   [base64\_encode][103]
    -   [base64\_custom\_decode][104]
    -   [base64\_custom\_encode][105]
    -   [base32\_custom\_decode][106]
    -   [base32\_custom\_encode][107]
    -   [clear\_err][108]
    -   [create\_blob][109]
    -   [datetime][110]
    -   [db\_add][111]
    -   [db\_add\_ttl][112]
    -   [db\_activity][113]
    -   [db\_select][114]
    -   [db\_update][115]
    -   [dns][116]
    -   [error][117]
    -   [geoip\_lookup][118]
    -   [hex][119]
    -   [hmac\_md5][120]
    -   [hmac\_sha1][121]
    -   [hmac\_sha2\_256][122]
    -   [hmac\_sha2\_512][123]
    -   [hmac\_sha3\_256][124]
    -   [hmac\_sha3\_512][125]
    -   [html\_select][126]
    -   [html\_select\_list][127]
    -   [http\_mksession][128]
    -   [http\_request][129]
    -   [http\_send][130]
    -   [http\_fetch][131]
    -   [http\_fetch\_json][132]
    -   [img\_load][133]
    -   [img\_exif][134]
    -   [img\_ahash][135]
    -   [img\_dhash][136]
    -   [img\_phash][137]
    -   [img\_nudity][138]
    -   [info][139]
    -   [intval][140]
    -   [json\_decode][141]
    -   [json\_decode\_stream][142]
    -   [json\_encode][143]
    -   [key\_trunc\_pad][144]
    -   [keyring][145]
    -   [last\_err][146]
    -   [md5][147]
    -   [mqtt\_connect][148]
    -   [mqtt\_subscribe][149]
    -   [mqtt\_recv][150]
    -   [mqtt\_ping][151]
    -   [pgp\_pubkey][152]
    -   [pgp\_pubkey\_armored][153]
    -   [print][154]
    -   [psl\_domain\_from\_dns\_name][155]
    -   [ratelimit\_throttle][156]
    -   [regex\_find][157]
    -   [regex\_find\_all][158]
    -   [semver\_match][159]
    -   [set\_err][160]
    -   [sha1][161]
    -   [sha2\_256][162]
    -   [sha2\_512][163]
    -   [sha3\_256][164]
    -   [sha3\_512][165]
    -   [sleep][166]
    -   [sn0int\_time][167]
    -   [sn0int\_time\_from][168]
    -   [sn0int\_version][169]
    -   [sock\_connect][170]
    -   [sock\_upgrade\_tls][171]
    -   [sock\_options][172]
    -   [sock\_send][173]
    -   [sock\_recv][174]
    -   [sock\_sendline][175]
    -   [sock\_recvline][176]
    -   [sock\_recvall][177]
    -   [sock\_recvline\_contains][178]
    -   [sock\_recvline\_regex][179]
    -   [sock\_recvn][180]
    -   [sock\_recvuntil][181]
    -   [sock\_sendafter][182]
    -   [sock\_newline][183]
    -   [sodium\_secretbox\_open][184]
    -   [status][185]
    -   [stdin\_readline][186]
    -   [stdin\_read\_to\_end][187]
    -   [str\_find][188]
    -   [str\_replace][189]
    -   [strftime][190]
    -   [strptime][191]
    -   [strval][192]
    -   [time\_unix][193]
    -   [url\_decode][194]
    -   [url\_encode][195]
    -   [url\_escape][196]
    -   [url\_join][197]
    -   [url\_parse][198]
    -   [url\_unescape][199]
    -   [utf8\_decode][200]
    -   [warn][201]
    -   [warn\_once][202]
    -   [ws\_connect][203]
    -   [ws\_options][204]
    -   [ws\_recv\_text][205]
    -   [ws\_recv\_binary][206]
    -   [ws\_recv\_json][207]
    -   [ws\_send\_text][208]
    -   [ws\_send\_binary][209]
    -   [ws\_send\_json][210]
    -   [x509\_parse\_pem][211]
    -   [xml\_decode][212]
    -   [xml\_named][213]

## Rationale

This tool was written for companies to help them understand their attack surface from a blackbox point of view. It's often difficult to understand that something is easier to discover than some people assume, putting them at risk of false security.

It's also designed to be useful for red team assessments and bug bounties, which also help companies to identify weaknesses that could result in a compromise.

Some functionality was written to do the same thing for individuals to raise awareness about personal attack surface, privacy and how much data is publicly available. These issues are often out of scope in bug bounties and sometimes by design. We believe that blaming the user is the wrong approach and these issues should be addressed at the root cause by the people designing those systems.

## License

GPLv3+

[1]: http://ipa-reader.xyz/?text=sno%C9%AAnt
[2]: https://webirc.hackint.org/#irc://irc.hackint.org/#sn0int
[3]: https://asciinema.org/a/shZ3TVY1o0opGFln3Oi2DAMCB
[4]: https://repology.org/project/sn0int/versions
[5]: https://sn0int.readthedocs.io/en/latest/install.html
[6]: https://sn0int.readthedocs.io/en/latest/install.html
[7]: https://sn0int.readthedocs.io/en/latest/install.html#archlinux
[8]: https://sn0int.readthedocs.io/en/latest/install.html#mac-osx
[9]: https://sn0int.readthedocs.io/en/latest/install.html#debian-bullseye-ubuntu-20-04-kali
[10]: https://sn0int.readthedocs.io/en/latest/install.html#debian-buster-ubuntu-19-10
[11]: https://sn0int.readthedocs.io/en/latest/install.html#fedora-centos-redhat
[12]: https://sn0int.readthedocs.io/en/latest/install.html#docker
[13]: https://sn0int.readthedocs.io/en/latest/install.html#alpine
[14]: https://sn0int.readthedocs.io/en/latest/install.html#openbsd
[15]: https://sn0int.readthedocs.io/en/latest/install.html#gentoo
[16]: https://sn0int.readthedocs.io/en/latest/install.html#nixos
[17]: https://sn0int.readthedocs.io/en/latest/install.html#windows
[18]: https://sn0int.readthedocs.io/en/latest/build.html
[19]: https://sn0int.readthedocs.io/en/latest/build.html#install-dependencies
[20]: https://sn0int.readthedocs.io/en/latest/build.html#archlinux
[21]: https://sn0int.readthedocs.io/en/latest/build.html#mac-osx
[22]: https://sn0int.readthedocs.io/en/latest/build.html#debian-ubuntu-kali
[23]: https://sn0int.readthedocs.io/en/latest/build.html#alpine
[24]: https://sn0int.readthedocs.io/en/latest/build.html#openbsd
[25]: https://sn0int.readthedocs.io/en/latest/build.html#gentoo
[26]: https://sn0int.readthedocs.io/en/latest/build.html#windows
[27]: https://sn0int.readthedocs.io/en/latest/build.html#building
[28]: https://sn0int.readthedocs.io/en/latest/usage.html
[29]: https://sn0int.readthedocs.io/en/latest/usage.html#installing-the-default-modules
[30]: https://sn0int.readthedocs.io/en/latest/usage.html#adding-something-to-scope
[31]: https://sn0int.readthedocs.io/en/latest/usage.html#running-a-module
[32]: https://sn0int.readthedocs.io/en/latest/usage.html#running-followup-modules-on-the-results
[33]: https://sn0int.readthedocs.io/en/latest/usage.html#unscoping-entities
[34]: https://sn0int.readthedocs.io/en/latest/autonoscope.html
[35]: https://sn0int.readthedocs.io/en/latest/autonoscope.html#domains
[36]: https://sn0int.readthedocs.io/en/latest/autonoscope.html#ips
[37]: https://sn0int.readthedocs.io/en/latest/autonoscope.html#urls
[38]: https://sn0int.readthedocs.io/en/latest/scripting.html
[39]: https://sn0int.readthedocs.io/en/latest/scripting.html#creating-a-repository
[40]: https://sn0int.readthedocs.io/en/latest/scripting.html#publish-your-module
[41]: https://sn0int.readthedocs.io/en/latest/scripting.html#publish-your-repo
[42]: https://sn0int.readthedocs.io/en/latest/scripting.html#reading-data-from-stdin
[43]: https://sn0int.readthedocs.io/en/latest/database.html
[44]: https://sn0int.readthedocs.io/en/latest/database.html#db-add
[45]: https://sn0int.readthedocs.io/en/latest/database.html#db-add-ttl
[46]: https://sn0int.readthedocs.io/en/latest/database.html#db-activity
[47]: https://sn0int.readthedocs.io/en/latest/database.html#db-update
[48]: https://sn0int.readthedocs.io/en/latest/database.html#db-select
[49]: https://sn0int.readthedocs.io/en/latest/structs.html
[50]: https://sn0int.readthedocs.io/en/latest/structs.html#domains
[51]: https://sn0int.readthedocs.io/en/latest/structs.html#subdomains
[52]: https://sn0int.readthedocs.io/en/latest/structs.html#ipaddrs
[53]: https://sn0int.readthedocs.io/en/latest/structs.html#urls
[54]: https://sn0int.readthedocs.io/en/latest/structs.html#emails
[55]: https://sn0int.readthedocs.io/en/latest/structs.html#phonenumbers
[56]: https://sn0int.readthedocs.io/en/latest/structs.html#devices
[57]: https://sn0int.readthedocs.io/en/latest/structs.html#networks
[58]: https://sn0int.readthedocs.io/en/latest/structs.html#accounts
[59]: https://sn0int.readthedocs.io/en/latest/structs.html#breaches
[60]: https://sn0int.readthedocs.io/en/latest/structs.html#images
[61]: https://sn0int.readthedocs.io/en/latest/structs.html#ports
[62]: https://sn0int.readthedocs.io/en/latest/structs.html#netblocks
[63]: https://sn0int.readthedocs.io/en/latest/structs.html#cryptoaddrs
[64]: https://sn0int.readthedocs.io/en/latest/structs.html#activity
[65]: https://sn0int.readthedocs.io/en/latest/structs.html#relations
[66]: https://sn0int.readthedocs.io/en/latest/structs.html#subdomain-ipaddr
[67]: https://sn0int.readthedocs.io/en/latest/structs.html#network-device
[68]: https://sn0int.readthedocs.io/en/latest/structs.html#breach-email
[69]: https://sn0int.readthedocs.io/en/latest/activity.html
[70]: https://sn0int.readthedocs.io/en/latest/activity.html#anatomy-of-an-event
[71]: https://sn0int.readthedocs.io/en/latest/activity.html#logging-events
[72]: https://sn0int.readthedocs.io/en/latest/activity.html#querying-events
[73]: https://sn0int.readthedocs.io/en/latest/activity.html#visualization
[74]: https://sn0int.readthedocs.io/en/latest/notifications.html
[75]: https://sn0int.readthedocs.io/en/latest/notifications.html#receiving-notifications
[76]: https://sn0int.readthedocs.io/en/latest/notifications.html#telegram
[77]: https://sn0int.readthedocs.io/en/latest/notifications.html#pushover
[78]: https://sn0int.readthedocs.io/en/latest/notifications.html#discord
[79]: https://sn0int.readthedocs.io/en/latest/notifications.html#signal
[80]: https://sn0int.readthedocs.io/en/latest/notifications.html#writing-your-own-module
[81]: https://sn0int.readthedocs.io/en/latest/notifications.html#setting-up-notification-rules
[82]: https://sn0int.readthedocs.io/en/latest/notifications.html#testing-notifications
[83]: https://sn0int.readthedocs.io/en/latest/notifications.html#running-sn0int-automatically
[84]: https://sn0int.readthedocs.io/en/latest/notifications.html#monitors
[85]: https://sn0int.readthedocs.io/en/latest/notifications.html#timers
[86]: https://sn0int.readthedocs.io/en/latest/keyring.html
[87]: https://sn0int.readthedocs.io/en/latest/keyring.html#managing-the-keyring
[88]: https://sn0int.readthedocs.io/en/latest/keyring.html#using-access-keys-in-scripts
[89]: https://sn0int.readthedocs.io/en/latest/keyring.html#using-access-keys-as-source-argument
[90]: https://sn0int.readthedocs.io/en/latest/config.html
[91]: https://sn0int.readthedocs.io/en/latest/config.html#core
[92]: https://sn0int.readthedocs.io/en/latest/config.html#namespaces
[93]: https://sn0int.readthedocs.io/en/latest/config.html#network
[94]: https://sn0int.readthedocs.io/en/latest/sandbox.html
[95]: https://sn0int.readthedocs.io/en/latest/sandbox.html#linux
[96]: https://sn0int.readthedocs.io/en/latest/sandbox.html#openbsd
[97]: https://sn0int.readthedocs.io/en/latest/sandbox.html#ipc-protocol
[98]: https://sn0int.readthedocs.io/en/latest/sandbox.html#limitations
[99]: https://sn0int.readthedocs.io/en/latest/sandbox.html#diagnosing-a-sandbox-failure
[100]: https://sn0int.readthedocs.io/en/latest/reference.html
[101]: https://sn0int.readthedocs.io/en/latest/reference.html#asn-lookup
[102]: https://sn0int.readthedocs.io/en/latest/reference.html#base64-decode
[103]: https://sn0int.readthedocs.io/en/latest/reference.html#base64-encode
[104]: https://sn0int.readthedocs.io/en/latest/reference.html#base64-custom-decode
[105]: https://sn0int.readthedocs.io/en/latest/reference.html#base64-custom-encode
[106]: https://sn0int.readthedocs.io/en/latest/reference.html#base32-custom-decode
[107]: https://sn0int.readthedocs.io/en/latest/reference.html#base32-custom-encode
[108]: https://sn0int.readthedocs.io/en/latest/reference.html#clear-err
[109]: https://sn0int.readthedocs.io/en/latest/reference.html#create-blob
[110]: https://sn0int.readthedocs.io/en/latest/reference.html#datetime
[111]: https://sn0int.readthedocs.io/en/latest/reference.html#db-add
[112]: https://sn0int.readthedocs.io/en/latest/reference.html#db-add-ttl
[113]: https://sn0int.readthedocs.io/en/latest/reference.html#db-activity
[114]: https://sn0int.readthedocs.io/en/latest/reference.html#db-select
[115]: https://sn0int.readthedocs.io/en/latest/reference.html#db-update
[116]: https://sn0int.readthedocs.io/en/latest/reference.html#dns
[117]: https://sn0int.readthedocs.io/en/latest/reference.html#error
[118]: https://sn0int.readthedocs.io/en/latest/reference.html#geoip-lookup
[119]: https://sn0int.readthedocs.io/en/latest/reference.html#hex
[120]: https://sn0int.readthedocs.io/en/latest/reference.html#hmac-md5
[121]: https://sn0int.readthedocs.io/en/latest/reference.html#hmac-sha1
[122]: https://sn0int.readthedocs.io/en/latest/reference.html#hmac-sha2-256
[123]: https://sn0int.readthedocs.io/en/latest/reference.html#hmac-sha2-512
[124]: https://sn0int.readthedocs.io/en/latest/reference.html#hmac-sha3-256
[125]: https://sn0int.readthedocs.io/en/latest/reference.html#hmac-sha3-512
[126]: https://sn0int.readthedocs.io/en/latest/reference.html#html-select
[127]: https://sn0int.readthedocs.io/en/latest/reference.html#html-select-list
[128]: https://sn0int.readthedocs.io/en/latest/reference.html#http-mksession
[129]: https://sn0int.readthedocs.io/en/latest/reference.html#http-request
[130]: https://sn0int.readthedocs.io/en/latest/reference.html#http-send
[131]: https://sn0int.readthedocs.io/en/latest/reference.html#http-fetch
[132]: https://sn0int.readthedocs.io/en/latest/reference.html#http-fetch-json
[133]: https://sn0int.readthedocs.io/en/latest/reference.html#img-load
[134]: https://sn0int.readthedocs.io/en/latest/reference.html#img-exif
[135]: https://sn0int.readthedocs.io/en/latest/reference.html#img-ahash
[136]: https://sn0int.readthedocs.io/en/latest/reference.html#img-dhash
[137]: https://sn0int.readthedocs.io/en/latest/reference.html#img-phash
[138]: https://sn0int.readthedocs.io/en/latest/reference.html#img-nudity
[139]: https://sn0int.readthedocs.io/en/latest/reference.html#info
[140]: https://sn0int.readthedocs.io/en/latest/reference.html#intval
[141]: https://sn0int.readthedocs.io/en/latest/reference.html#json-decode
[142]: https://sn0int.readthedocs.io/en/latest/reference.html#json-decode-stream
[143]: https://sn0int.readthedocs.io/en/latest/reference.html#json-encode
[144]: https://sn0int.readthedocs.io/en/latest/reference.html#key-trunc-pad
[145]: https://sn0int.readthedocs.io/en/latest/reference.html#keyring
[146]: https://sn0int.readthedocs.io/en/latest/reference.html#last-err
[147]: https://sn0int.readthedocs.io/en/latest/reference.html#md5
[148]: https://sn0int.readthedocs.io/en/latest/reference.html#mqtt-connect
[149]: https://sn0int.readthedocs.io/en/latest/reference.html#mqtt-subscribe
[150]: https://sn0int.readthedocs.io/en/latest/reference.html#mqtt-recv
[151]: https://sn0int.readthedocs.io/en/latest/reference.html#mqtt-ping
[152]: https://sn0int.readthedocs.io/en/latest/reference.html#pgp-pubkey
[153]: https://sn0int.readthedocs.io/en/latest/reference.html#pgp-pubkey-armored
[154]: https://sn0int.readthedocs.io/en/latest/reference.html#print
[155]: https://sn0int.readthedocs.io/en/latest/reference.html#psl-domain-from-dns-name
[156]: https://sn0int.readthedocs.io/en/latest/reference.html#ratelimit-throttle
[157]: https://sn0int.readthedocs.io/en/latest/reference.html#regex-find
[158]: https://sn0int.readthedocs.io/en/latest/reference.html#regex-find-all
[159]: https://sn0int.readthedocs.io/en/latest/reference.html#semver-match
[160]: https://sn0int.readthedocs.io/en/latest/reference.html#set-err
[161]: https://sn0int.readthedocs.io/en/latest/reference.html#sha1
[162]: https://sn0int.readthedocs.io/en/latest/reference.html#sha2-256
[163]: https://sn0int.readthedocs.io/en/latest/reference.html#sha2-512
[164]: https://sn0int.readthedocs.io/en/latest/reference.html#sha3-256
[165]: https://sn0int.readthedocs.io/en/latest/reference.html#sha3-512
[166]: https://sn0int.readthedocs.io/en/latest/reference.html#sleep
[167]: https://sn0int.readthedocs.io/en/latest/reference.html#sn0int-time
[168]: https://sn0int.readthedocs.io/en/latest/reference.html#sn0int-time-from
[169]: https://sn0int.readthedocs.io/en/latest/reference.html#sn0int-version
[170]: https://sn0int.readthedocs.io/en/latest/reference.html#sock-connect
[171]: https://sn0int.readthedocs.io/en/latest/reference.html#sock-upgrade-tls
[172]: https://sn0int.readthedocs.io/en/latest/reference.html#sock-options
[173]: https://sn0int.readthedocs.io/en/latest/reference.html#sock-send
[174]: https://sn0int.readthedocs.io/en/latest/reference.html#sock-recv
[175]: https://sn0int.readthedocs.io/en/latest/reference.html#sock-sendline
[176]: https://sn0int.readthedocs.io/en/latest/reference.html#sock-recvline
[177]: https://sn0int.readthedocs.io/en/latest/reference.html#sock-recvall
[178]: https://sn0int.readthedocs.io/en/latest/reference.html#sock-recvline-contains
[179]: https://sn0int.readthedocs.io/en/latest/reference.html#sock-recvline-regex
[180]: https://sn0int.readthedocs.io/en/latest/reference.html#sock-recvn
[181]: https://sn0int.readthedocs.io/en/latest/reference.html#sock-recvuntil
[182]: https://sn0int.readthedocs.io/en/latest/reference.html#sock-sendafter
[183]: https://sn0int.readthedocs.io/en/latest/reference.html#sock-newline
[184]: https://sn0int.readthedocs.io/en/latest/reference.html#sodium-secretbox-open
[185]: https://sn0int.readthedocs.io/en/latest/reference.html#status
[186]: https://sn0int.readthedocs.io/en/latest/reference.html#stdin-readline
[187]: https://sn0int.readthedocs.io/en/latest/reference.html#stdin-read-to-end
[188]: https://sn0int.readthedocs.io/en/latest/reference.html#str-find
[189]: https://sn0int.readthedocs.io/en/latest/reference.html#str-replace
[190]: https://sn0int.readthedocs.io/en/latest/reference.html#strftime
[191]: https://sn0int.readthedocs.io/en/latest/reference.html#strptime
[192]: https://sn0int.readthedocs.io/en/latest/reference.html#strval
[193]: https://sn0int.readthedocs.io/en/latest/reference.html#time-unix
[194]: https://sn0int.readthedocs.io/en/latest/reference.html#url-decode
[195]: https://sn0int.readthedocs.io/en/latest/reference.html#url-encode
[196]: https://sn0int.readthedocs.io/en/latest/reference.html#url-escape
[197]: https://sn0int.readthedocs.io/en/latest/reference.html#url-join
[198]: https://sn0int.readthedocs.io/en/latest/reference.html#url-parse
[199]: https://sn0int.readthedocs.io/en/latest/reference.html#url-unescape
[200]: https://sn0int.readthedocs.io/en/latest/reference.html#utf8-decode
[201]: https://sn0int.readthedocs.io/en/latest/reference.html#warn
[202]: https://sn0int.readthedocs.io/en/latest/reference.html#warn-once
[203]: https://sn0int.readthedocs.io/en/latest/reference.html#ws-connect
[204]: https://sn0int.readthedocs.io/en/latest/reference.html#ws-options
[205]: https://sn0int.readthedocs.io/en/latest/reference.html#ws-recv-text
[206]: https://sn0int.readthedocs.io/en/latest/reference.html#ws-recv-binary
[207]: https://sn0int.readthedocs.io/en/latest/reference.html#ws-recv-json
[208]: https://sn0int.readthedocs.io/en/latest/reference.html#ws-send-text
[209]: https://sn0int.readthedocs.io/en/latest/reference.html#ws-send-binary
[210]: https://sn0int.readthedocs.io/en/latest/reference.html#ws-send-json
[211]: https://sn0int.readthedocs.io/en/latest/reference.html#x509-parse-pem
[212]: https://sn0int.readthedocs.io/en/latest/reference.html#xml-decode
[213]: https://sn0int.readthedocs.io/en/latest/reference.html#xml-named