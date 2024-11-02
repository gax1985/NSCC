


>[!important]
>
>The Quiz is due on Friday!
>
>Sept. 13th 


Today , we will go through the **Juice Shop** Installation!


When we go through Kali/Linux Installation, we get the option for putting in various partitions. Often, there is an option for letting the Kali Linux Installer of auto-partitioning the virtual hard drive.


When we start partitioning out the hard drive, we can do a root partition, and we create different directories. 


There is an important folder called **/var/log** that could seriously impede our Kali Linux installation. It is advisable to create a separate partition for the **/var/log** folder.


## Installation Steps ( in VMWARE)



1. Create the virtual machine 
2. We boot up the virtual machine
3. We get to the Kali Linux installer
4. We select the language
5. We enter the hostname (**kali** for example)
6. We leave **Domain Name** as *blank*
7. We enter the password
8. We select the time zone (Atlantic)
9. We get to the **Partitioning** section : 
   
>[!critical]
>
>Manual - We would do the manual partitioning
>Encrypted - Everything would be encrypted
>We choose the second option Guided ---
>
>We should choose **Separate /home /var and /tmp partitions** !
>
>###### Why should we do so ?
>
>Because the system will *fail to boot* if the **/var/log** folder decided to use the entire available disk space on the drive!
> 


>[!info]
>
>###### EXT4
>
>It is the de-facto partitioning method for Linux-based systems. One of the problems that Microsoft had with FAT32 and NTFS is when you install an application, the files for it would be placed in different areas of the the drive (hence, defragmenting drives). EXT4 uses a certain algorithm to keep files in the same area, and it has other features like *journaling*
>


>[!info]
>
>Virtual Paging is not that much slower than actual RAM



#### JuiceShop Installation 


1. We should have Kali updated and upgraded!
   
   >[!command]
   >
   >``sudo apt update && sudo apt upgrade -y``
   >


2. OWASP has created the package with different methods of installation. We will install it from source!

	[juice-shop/juice-shop: OWASP Juice Shop: Probably the most modern and sophisticated insecure web application (github.com)](https://github.com/juice-shop/juice-shop)

	1. install NodeJS (OWAP has a chart for NodeJS compatibility. sudo apt install nodejs will yield version 20 )
	2. Run `git clone https://github.com/juice-shop/juice-shop.git --depth 1` (or clone [your own fork](https://github.com/juice-shop/juice-shop/fork) of the repository)

	3. Go into the cloned folder with `cd juice-shop`
	4. Run `npm install` (only has to be done before first start or when you change the source code) 
	5. Run `npm start`
	   
>[!info]
>
>#### Result 
>
>![[Pasted image 20240911111324.png]]
>
>

	
	6. Browse to [http://localhost:3000](http://localhost:3000/)
	   
	   
	   


#### Explanation for the *--depth* portion of the *git clone* command (from the **JuiceShop** installation)


Here’s a breakdown of how it works:

- **Basic Syntax**: `git clone --depth <depth> <repository-url>`
    
- **Purpose**: By specifying a depth, you are telling Git to only retrieve the most recent `<depth>` number of commits from the repository. This can significantly reduce the amount of data that needs to be downloaded and can make the cloning process faster, especially for large repositories with long histories.
    
- **Example**: If you run `git clone --depth 1 <repository-url>`, Git will only fetch the most recent commit and its corresponding snapshot of the files, leaving out all the older history.
    
- **Use Cases**: Shallow clones are useful when you only need the latest state of the repository for tasks like testing or building, but don’t need to explore the full history or perform operations that require the complete commit history.
    
- **Limitations**: Some operations, like creating branches based on older commits or accessing detailed commit history, might not be possible with a shallow clone. You can, however, convert a shallow clone into a full clone later using the `git fetch --unshallow` command if needed.
    

Here’s a practical example:

sh

Copy code

`git clone --depth 1 https://github.com/example/repo.git`

This command will create a shallow clone of the repository from `https://github.com/example/repo.git`, including only the most recent commit and not the full history.





## Instructions from the **Juice Shop** GitHub page :


[juice-shop/juice-shop: OWASP Juice Shop: Probably the most modern and sophisticated insecure web application (github.com)](https://github.com/juice-shop/juice-shop?tab=readme-ov-file)


# [![Juice Shop Logo](https://raw.githubusercontent.com/juice-shop/juice-shop/master/frontend/src/assets/public/images/JuiceShop_Logo_100px.png)](https://raw.githubusercontent.com/juice-shop/juice-shop/master/frontend/src/assets/public/images/JuiceShop_Logo_100px.png) OWASP Juice Shop

[](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#-owasp-juice-shop)

[![OWASP Flagship](https://camo.githubusercontent.com/6b56de9c3065007eb293a8fd931ba5cccd491d03415fc69ea374b6e35872a8ce/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6f776173702d666c61677368697025323070726f6a6563742d3438413634362e737667)](https://owasp.org/projects/#sec-flagships) [![GitHub release](https://camo.githubusercontent.com/641d6e729df81d9ab3a83cb96fce41ab9cd63242ff5d0ca85260b9dfcfc11d20/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f72656c656173652f6a756963652d73686f702f6a756963652d73686f702e737667)](https://github.com/juice-shop/juice-shop/releases/latest) [![Twitter Follow](https://camo.githubusercontent.com/f7484b303c824227a6ba761274f316a45203a29596eafd27fb4a16981641eeef/68747470733a2f2f696d672e736869656c64732e696f2f747769747465722f666f6c6c6f772f6f776173705f6a7569636573686f702e7376673f7374796c653d736f6369616c266c6162656c3d466f6c6c6f77)](https://twitter.com/owasp_juiceshop) [![Subreddit subscribers](https://camo.githubusercontent.com/433dab78908827eca394aef79c4462d64d38ae212751e071646021f09de9cc6b/68747470733a2f2f696d672e736869656c64732e696f2f7265646469742f7375627265646469742d73756273637269626572732f6f776173705f6a7569636573686f703f7374796c653d736f6369616c)](https://reddit.com/r/owasp_juiceshop)

[![CI/CD Pipeline](https://github.com/juice-shop/juice-shop/workflows/CI/CD%20Pipeline/badge.svg?branch=master)](https://github.com/juice-shop/juice-shop/workflows/CI/CD%20Pipeline/badge.svg?branch=master) [![Test Coverage](https://camo.githubusercontent.com/5995d4708bed574fd45e6ba68b6a2f4a74c00053c7ca46c05ba8abba83d21071/68747470733a2f2f6170692e636f6465636c696d6174652e636f6d2f76312f6261646765732f36323036633866333937326263633937613033332f746573745f636f766572616765)](https://codeclimate.com/github/juice-shop/juice-shop/test_coverage) [![Maintainability](https://camo.githubusercontent.com/52ec45635239b80b9027104edd648619cd2dff1cac9cfbd18e4657edbe7751b8/68747470733a2f2f6170692e636f6465636c696d6174652e636f6d2f76312f6261646765732f36323036633866333937326263633937613033332f6d61696e7461696e6162696c697479)](https://codeclimate.com/github/juice-shop/juice-shop/maintainability) [![Code Climate technical debt](https://camo.githubusercontent.com/c6884c689bdb483e48d274f4cc474b866a298aea28852961f2bee2404e956956/68747470733a2f2f696d672e736869656c64732e696f2f636f6465636c696d6174652f746563682d646562742f6a756963652d73686f702f6a756963652d73686f70)](https://codeclimate.com/github/juice-shop/juice-shop/trends/technical_debt) [![Cypress tests](https://camo.githubusercontent.com/e1d50a798fdd27b6a31192d568ebb8ab0a19f241d2dd20fb897a4a1ea12fe4a4/68747470733a2f2f696d672e736869656c64732e696f2f656e64706f696e743f75726c3d68747470733a2f2f64617368626f6172642e637970726573732e696f2f62616467652f73696d706c652f3368726b68752f6d6173746572267374796c653d666c6174266c6f676f3d63797072657373)](https://dashboard.cypress.io/projects/3hrkhu/runs) [![OpenSSF Best Practices](https://camo.githubusercontent.com/df8e73ff82504c70c99d58781a45592fda150b46fdbb76e2756fb7d4e7e6f481/68747470733a2f2f7777772e626573747072616374696365732e6465762f70726f6a656374732f3232332f6261646765)](https://www.bestpractices.dev/projects/223) [![GitHub stars](https://camo.githubusercontent.com/c7929dceae5c406a19d00b260d86d6f6602f7f1c5ede7d08303205acec7d8d9e/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f6a756963652d73686f702f6a756963652d73686f702e7376673f6c6162656c3d476974487562253230254532253938253835267374796c653d666c6174)](https://camo.githubusercontent.com/c7929dceae5c406a19d00b260d86d6f6602f7f1c5ede7d08303205acec7d8d9e/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f6a756963652d73686f702f6a756963652d73686f702e7376673f6c6162656c3d476974487562253230254532253938253835267374796c653d666c6174) [![Contributor Covenant](https://camo.githubusercontent.com/b939bc6b6e2370a6266a694cc4f0a583fbb99d28a82d0e5088f21739c369d3c7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f6e7472696275746f72253230436f76656e616e742d76322e3025323061646f707465642d6666363962342e737667)](https://github.com/juice-shop/juice-shop/blob/master/CODE_OF_CONDUCT.md)

> [The most trustworthy online shop out there.](https://twitter.com/dschadow/status/706781693504589824) ([@dschadow](https://github.com/dschadow)) — [The best juice shop on the whole internet!](https://twitter.com/shehackspurple/status/907335357775085568) ([@shehackspurple](https://twitter.com/shehackspurple)) — [Actually the most bug-free vulnerable application in existence!](https://youtu.be/TXAztSpYpvE?t=26m35s) ([@vanderaj](https://twitter.com/vanderaj)) — [First you 😂😂then you 😢](https://twitter.com/kramse/status/1073168529405472768) ([@kramse](https://twitter.com/kramse)) — [But this doesn't have anything to do with juice.](https://twitter.com/coderPatros/status/1199268774626488320) ([@coderPatros' wife](https://twitter.com/coderPatros))

OWASP Juice Shop is probably the most modern and sophisticated insecure web application! It can be used in security trainings, awareness demos, CTFs and as a guinea pig for security tools! Juice Shop encompasses vulnerabilities from the entire [OWASP Top Ten](https://owasp.org/www-project-top-ten) along with many other security flaws found in real-world applications!

[![Juice Shop Screenshot Slideshow](https://github.com/juice-shop/juice-shop/raw/master/screenshots/slideshow.gif)](https://github.com/juice-shop/juice-shop/blob/master/screenshots/slideshow.gif)

For a detailed introduction, full list of features and architecture overview please visit the official project page: [https://owasp-juice.shop](https://owasp-juice.shop/)

## Table of contents

[](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#table-of-contents)

- [Setup](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#setup)
    - [From Sources](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#from-sources)
    - [Packaged Distributions](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#packaged-distributions)
    - [Docker Container](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#docker-container)
    - [Vagrant](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#vagrant)
- [Demo](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#demo)
- [Documentation](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#documentation)
    - [Node.js version compatibility](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#nodejs-version-compatibility)
    - [Troubleshooting](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#troubleshooting)
    - [Official companion guide](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#official-companion-guide)
- [Contributing](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#contributing)
- [References](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#references)
- [Merchandise](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#merchandise)
- [Donations](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#donations)
- [Contributors](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#contributors)
- [Licensing](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#licensing)

## Setup

[](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#setup)

> You can find some less common installation variations as well as instructions to run Juice Shop on a variety of cloud computing providers in [the _Running OWASP Juice Shop_ documentation](https://pwning.owasp-juice.shop/companion-guide/latest/part1/running.html).

### From Sources

[](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#from-sources)

[![GitHub repo size](https://camo.githubusercontent.com/6aa61200debc069ddc9badc1a9a40bb28df4692d65a6d0e66ececbba124c776e/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f7265706f2d73697a652f6a756963652d73686f702f6a756963652d73686f702e737667)](https://camo.githubusercontent.com/6aa61200debc069ddc9badc1a9a40bb28df4692d65a6d0e66ececbba124c776e/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f7265706f2d73697a652f6a756963652d73686f702f6a756963652d73686f702e737667)

1. Install [node.js](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#nodejs-version-compatibility)
2. Run `git clone https://github.com/juice-shop/juice-shop.git --depth 1` (or clone [your own fork](https://github.com/juice-shop/juice-shop/fork) of the repository)
3. Go into the cloned folder with `cd juice-shop`
4. Run `npm install` (only has to be done before first start or when you change the source code)
5. Run `npm start`
6. Browse to [http://localhost:3000](http://localhost:3000/)

### Packaged Distributions

[](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#packaged-distributions)

[![GitHub release](https://camo.githubusercontent.com/01a63a730f0b8590cd8f50e6fefa0054bc9841ef29ea21d8f7e76f807d2c6310/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f646f776e6c6f6164732f6a756963652d73686f702f6a756963652d73686f702f746f74616c2e737667)](https://github.com/juice-shop/juice-shop/releases/latest) [![SourceForge](https://camo.githubusercontent.com/d983dd8ca19308d61e08d493731aabcd8abb0b2c1dd3ff37702fcc5328024fdd/68747470733a2f2f696d672e736869656c64732e696f2f736f75726365666f7267652f646d2f6a756963652d73686f703f6c6162656c3d736f75726365666f726765253230646f776e6c6f616473)](https://sourceforge.net/projects/juice-shop/) [![SourceForge](https://camo.githubusercontent.com/6666836fbae2a98d2124f63fa97ac91dd30617ed6478e764288ac52cbf58a40f/68747470733a2f2f696d672e736869656c64732e696f2f736f75726365666f7267652f64742f6a756963652d73686f703f6c6162656c3d736f75726365666f726765253230646f776e6c6f616473)](https://sourceforge.net/projects/juice-shop/)

1. Install a 64bit [node.js](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#nodejs-version-compatibility) on your Windows, MacOS or Linux machine
2. Download `juice-shop-<version>_<node-version>_<os>_x64.zip` (or `.tgz`) attached to [latest release](https://github.com/juice-shop/juice-shop/releases/latest)
3. Unpack and `cd` into the unpacked folder
4. Run `npm start`
5. Browse to [http://localhost:3000](http://localhost:3000/)

> Each packaged distribution includes some binaries for `sqlite3` and `libxmljs` bound to the OS and node.js version which `npm install` was executed on.

### Docker Container

[](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#docker-container)

[![Docker Pulls](https://camo.githubusercontent.com/1f2409b6c791d77573606bde1fcbd7bda03856b2a0cdc5d21389b3993f50ffe1/68747470733a2f2f696d672e736869656c64732e696f2f646f636b65722f70756c6c732f626b696d6d696e6963682f6a756963652d73686f702e737667)](https://hub.docker.com/r/bkimminich/juice-shop) [![Docker Stars](https://camo.githubusercontent.com/1497a4d29feddbc08eaad53fcd82a76efcedbec0a198f5d6123f6a70c602959f/68747470733a2f2f696d672e736869656c64732e696f2f646f636b65722f73746172732f626b696d6d696e6963682f6a756963652d73686f702e737667)](https://camo.githubusercontent.com/1497a4d29feddbc08eaad53fcd82a76efcedbec0a198f5d6123f6a70c602959f/68747470733a2f2f696d672e736869656c64732e696f2f646f636b65722f73746172732f626b696d6d696e6963682f6a756963652d73686f702e737667) [![](https://camo.githubusercontent.com/077df6eeb46bce8e3653835a6de6b8e6b25532f0341efa5b0238c172ccf03aa5/68747470733a2f2f696d616765732e6d6963726f6261646765722e636f6d2f6261646765732f696d6167652f626b696d6d696e6963682f6a756963652d73686f702e737667)](https://microbadger.com/images/bkimminich/juice-shop "Get your own image badge on microbadger.com") [![](https://camo.githubusercontent.com/587a44c3ae47117651cd235609b2b3d552bae8994c7a43e5c834565f5f1fe6fe/68747470733a2f2f696d616765732e6d6963726f6261646765722e636f6d2f6261646765732f76657273696f6e2f626b696d6d696e6963682f6a756963652d73686f702e737667)](https://microbadger.com/images/bkimminich/juice-shop "Get your own version badge on microbadger.com")

1. Install [Docker](https://www.docker.com/)
2. Run `docker pull bkimminich/juice-shop`
3. Run `docker run --rm -p 127.0.0.1:3000:3000 bkimminich/juice-shop`
4. Browse to [http://localhost:3000](http://localhost:3000/) (on macOS and Windows browse to [http://192.168.99.100:3000](http://192.168.99.100:3000/) if you are using docker-machine instead of the native docker installation)

### Vagrant

[](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#vagrant)

1. Install [Vagrant](https://www.vagrantup.com/downloads.html) and [Virtualbox](https://www.virtualbox.org/wiki/Downloads)
2. Run `git clone https://github.com/juice-shop/juice-shop.git` (or clone [your own fork](https://github.com/juice-shop/juice-shop/fork) of the repository)
3. Run `cd vagrant && vagrant up`
4. Browse to [192.168.56.110](http://192.168.56.110/)

## Demo

[](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#demo)

Feel free to have a look at the latest version of OWASP Juice Shop: [http://demo.owasp-juice.shop](http://demo.owasp-juice.shop/)

> This is a deployment-test and sneak-peek instance only! You are **not supposed** to use this instance for your own hacking endeavours! No guaranteed uptime! Guaranteed stern looks if you break it!

## Documentation

[](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#documentation)

### Node.js version compatibility

[](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#nodejs-version-compatibility)

[![GitHub package.json dynamic](https://camo.githubusercontent.com/ee1c5a30763150c19074733041b5f83991d017a298443711719e32d41c300d60/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f7061636b6167652d6a736f6e2f6370752f626b696d6d696e6963682f6a756963652d73686f70)](https://camo.githubusercontent.com/ee1c5a30763150c19074733041b5f83991d017a298443711719e32d41c300d60/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f7061636b6167652d6a736f6e2f6370752f626b696d6d696e6963682f6a756963652d73686f70) [![GitHub package.json dynamic](https://camo.githubusercontent.com/b98e0c96bbf6dca5a4b57864ae7eb78e9d63500d0d964e6b51348e78509ac5f1/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f7061636b6167652d6a736f6e2f6f732f626b696d6d696e6963682f6a756963652d73686f70)](https://camo.githubusercontent.com/b98e0c96bbf6dca5a4b57864ae7eb78e9d63500d0d964e6b51348e78509ac5f1/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f7061636b6167652d6a736f6e2f6f732f626b696d6d696e6963682f6a756963652d73686f70)

OWASP Juice Shop officially supports the following versions of [node.js](http://nodejs.org/) in line with the official [node.js LTS schedule](https://github.com/nodejs/LTS) as close as possible. Docker images and packaged distributions are offered accordingly.

|node.js|Supported|Tested|[Packaged Distributions](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#packaged-distributions)|[Docker images](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#docker-container) from `master`|[Docker images](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#docker-container) from `develop`|
|:--|:--|:--|:--|:--|:--|
|23.x|❌|❌||||
|22.x|✔️|✔️|Windows (`x64`), MacOS (`x64`), Linux (`x64`)|||
|21.x|( ✔️ )|✔️|Windows (`x64`), MacOS (`x64`), Linux (`x64`)|||
|20.x|✔️|✔️|Windows (`x64`), MacOS (`x64`), Linux (`x64`)|`latest` (`linux/amd64`, `linux/arm64`)|`snapshot` (`linux/amd64`, `linux/arm64`)|
|19.x|( ✔️ )|❌||||
|18.x|✔️|✔️|Windows (`x64`), MacOS (`x64`), Linux (`x64`)|||
|<18.x|❌|❌||||

Juice Shop is automatically tested _only on the latest `.x` minor version_ of each node.js version mentioned above! There is no guarantee that older minor node.js releases will always work with Juice Shop! Please make sure you stay up to date with your chosen version.

### Troubleshooting

[](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#troubleshooting)

[![Gitter](https://camo.githubusercontent.com/34817554c9bb5c8d51f7c60120b6f6812f7a1efccf834557c6199a97b7e7aca0/687474703a2f2f696d672e736869656c64732e696f2f62616467652f6769747465722d6a6f696e253230636861742d3164636537332e737667)](https://gitter.im/bkimminich/juice-shop)

If you need help with the application setup please check our [our existing _Troubleshooting_](https://pwning.owasp-juice.shop/appendix/troubleshooting.html) guide. If this does not solve your issue please post your specific problem or question in the [Gitter Chat](https://gitter.im/bkimminich/juice-shop) where community members can best try to help you.

🛑 **Please avoid opening GitHub issues for support requests or questions!**

### Official companion guide

[](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#official-companion-guide)

[![Write Goodreads Review](https://camo.githubusercontent.com/f609e85169127bcb542c5dab69b09ff1b06b0e30ddf8cb4ce09a17d37f7ded68/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f676f6f6472656164732d77726974652532307265766965772d34393535373234302e737667)](https://www.goodreads.com/review/edit/49557240)

OWASP Juice Shop comes with an official companion guide eBook. It will give you a complete overview of all vulnerabilities found in the application including hints how to spot and exploit them. In the appendix you will even find complete step-by-step solutions to every challenge. Extensive documentation of [custom re-branding](https://pwning.owasp-juice.shop/companion-guide/latest/part4/customization.html), [CTF-support](https://pwning.owasp-juice.shop/companion-guide/latest/part4/ctf.html), [trainer's guide](https://pwning.owasp-juice.shop/companion-guide/latest/part4/trainers.html) and much more is also included.

[Pwning OWASP Juice Shop](https://leanpub.com/juice-shop) is published under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) and is available **for free** in PDF, Kindle and ePub format on LeanPub. You can also [browse the full content online](https://pwning.owasp-juice.shop/)!

[![Pwning OWASP Juice Shop cover](https://raw.githubusercontent.com/juice-shop/pwning-juice-shop/master/docs/modules/ROOT/assets/images/cover.jpg)](https://leanpub.com/juice-shop) [![Pwning OWASP Juice Shop back cover](https://raw.githubusercontent.com/juice-shop/pwning-juice-shop/master/docs/modules/ROOT/assets/images/introduction/back.jpg)](https://leanpub.com/juice-shop)

## Contributing

[](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#contributing)

[![GitHub contributors](https://camo.githubusercontent.com/cfbced8361c71783622ea49fcea8298f179205df62022bd5f24871590190bb09/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f636f6e7472696275746f72732f626b696d6d696e6963682f6a756963652d73686f702e737667)](https://github.com/juice-shop/juice-shop/graphs/contributors) [![JavaScript Style Guide](https://camo.githubusercontent.com/69491412f56d5c52f0e9f0abddb17033b28539d38e5d05378521222236a83bb1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64652532307374796c652d7374616e646172642d627269676874677265656e2e737667)](http://standardjs.com/) [![Crowdin](https://camo.githubusercontent.com/a154bea341e48b2488effe7205c1c2364dd2326357c01848e0d3375ac74d9352/68747470733a2f2f64333232637174353834626f346f2e636c6f756466726f6e742e6e65742f6f776173702d6a756963652d73686f702f6c6f63616c697a65642e737667)](https://crowdin.com/project/owasp-juice-shop) [![GitHub issues by-label](https://camo.githubusercontent.com/c6b86f1818434625a68c2ff378be50b922aa38b275374860554b7e33ded8ea87/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732f626b696d6d696e6963682f6a756963652d73686f702f68656c7025323077616e7465642e737667)](https://camo.githubusercontent.com/c6b86f1818434625a68c2ff378be50b922aa38b275374860554b7e33ded8ea87/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732f626b696d6d696e6963682f6a756963652d73686f702f68656c7025323077616e7465642e737667) [![GitHub issues by-label](https://camo.githubusercontent.com/0189e3cb8fea1d2515504d3637adc92c6ec6a8b3f65d053f8220404eb8803d7b/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732f626b696d6d696e6963682f6a756963652d73686f702f676f6f64253230666972737425323069737375652e737667)](https://camo.githubusercontent.com/0189e3cb8fea1d2515504d3637adc92c6ec6a8b3f65d053f8220404eb8803d7b/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732f626b696d6d696e6963682f6a756963652d73686f702f676f6f64253230666972737425323069737375652e737667)

We are always happy to get new contributors on board! Please check [CONTRIBUTING.md](https://github.com/juice-shop/juice-shop/blob/master/CONTRIBUTING.md) to learn how to [contribute to our codebase](https://github.com/juice-shop/juice-shop/blob/master/CONTRIBUTING.md#code-contributions) or the [translation into different languages](https://github.com/juice-shop/juice-shop/blob/master/CONTRIBUTING.md#i18n-contributions)!

## References

[](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#references)

Did you write a blog post, magazine article or do a podcast about or mentioning OWASP Juice Shop? Or maybe you held or joined a conference talk or meetup session, a hacking workshop or public training where this project was mentioned?

Add it to our ever-growing list of [REFERENCES.md](https://github.com/juice-shop/juice-shop/blob/master/REFERENCES.md) by forking and opening a Pull Request!

## Merchandise

[](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#merchandise)

- On [Spreadshirt.com](http://shop.spreadshirt.com/juiceshop) and [Spreadshirt.de](http://shop.spreadshirt.de/juiceshop) you can get some swag (Shirts, Hoodies, Mugs) with the official OWASP Juice Shop logo
- On [StickerYou.com](https://www.stickeryou.com/products/owasp-juice-shop/794) you can get variants of the OWASP Juice Shop logo as single stickers to decorate your laptop with. They can also print magnets, iron-ons, sticker sheets and temporary tattoos.

## Donations

[](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#donations)

[![](https://camo.githubusercontent.com/9ff8b9a96c06f96f59f9e238cb75163ed1ca52eff643c831bf208c01353492df/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f737570706f72742d6f776173702532306a7569636525323073686f702d626c7565)](https://owasp.org/donate/?reponame=www-project-juice-shop&title=OWASP+Juice+Shop)

The OWASP Foundation gratefully accepts donations via Stripe. Projects such as Juice Shop can then request reimbursement for expenses from the Foundation. If you'd like to express your support of the Juice Shop project, please make sure to tick the "Publicly list me as a supporter of OWASP Juice Shop" checkbox on the donation form. You can find our more about donations and how they are used here:

[https://pwning.owasp-juice.shop/part3/donations.html](https://pwning.owasp-juice.shop/part3/donations.html)

## Contributors

[](https://github.com/juice-shop/juice-shop?tab=readme-ov-file#contributors)

The OWASP Juice Shop core project team are:

- [Björn Kimminich](https://github.com/bkimminich) aka `bkimminich` ([Project Leader](https://www.owasp.org/index.php/Projects/Project_Leader_Responsibilities)) [![Keybase PGP](https://camo.githubusercontent.com/cbb5252b16029d619bfce651184d1e7aa5d83a2a59d4209961e3be6c819ec454/68747470733a2f2f696d672e736869656c64732e696f2f6b6579626173652f7067702f626b696d6d696e696368)](https://keybase.io/bkimminich)
- [Jannik Hollenbach](https://github.com/J12934) aka `J12934`
- [Timo Pagel](https://github.com/wurstbrot) aka `wurstbrot`
- [Shubham Palriwala](https://github.com/ShubhamPalriwala) aka `ShubhamPalriwala`

For a list of all contributors to the OWASP Juice Shop please visit our [HALL_OF_FAME.md](https://github.com/juice-shop/juice-shop/blob/master/HALL_OF_FAME.md).