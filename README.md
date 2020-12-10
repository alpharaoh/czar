<img src="https://cdn.pixabay.com/photo/2012/04/26/11/48/crown-42251_960_720.png" width=200>

# Czar V0.1

## What is Czar?

Czar is a *fully automated* active bug hunting tool for full reconnaissance on a target's domain(s). It utilizes many different tools and also custom made tools to perform a scan every 24 hours (optional). It also produces a report of findings and also sends a message on slack whenever a potential bug is found! 


This tool is currently a work in progress with no intention to further develop it. I would highly recommend to use DigitalOcean or AWS instance and get it constantly running on a VPS. Luckily, most websites that offer server hosting have a free tier/trial.

## Does it work?

I have currently stopped running Czar on my Digital Ocean droplet but I did for around a week around September 2020. For this period of time the tool discovered many security vunlrabilities such as Subdomain Takeovers, Host Injection Vulrabilities, CVE's. *(Check Slack screenshots below)*

## Usage

Type the following into your terminal on your VPS (or local machine; __*not recommended*__)

1. `git clone https://github.com/alpharaoh/czar.git`

2. Now we need to make the requirments.sh file excecutable and run it<br>
`chmod +x requirements.sh`<br>
`./requirements.sh`

4. Then configure your settings and target in config.py located<br>
 `nano ./config_and_modules/config.py`

5. Now run!<br>
`python3 main.py`

## What does it do?

Here is a chart representation of what Czar does.

<img src="https://i.imgur.com/57a5233.png">

## Slack Screenshots

<img src="https://i.imgur.com/j1paw9W.png">
<img src="https://i.imgur.com/m1Elssg.png">
<img src="https://i.imgur.com/ehKFAkD.png">
<img src="https://i.imgur.com/pKkCV9b.png">

## Bugs

Czar is still a work in progress and may have some bugs. The program will send a slack message when an error occurs and tell you some information on why it happened.
