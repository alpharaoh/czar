#This is the configs file, where you will modify the variables accordingly
#This is set up for full customization (and it's easier to config!)
#This project has been designed with modularity and scalability in mind, if you wish to add-
#another tool, please contact me!

#Project name is important
#Provide unique name for every run
#A folder will be created in output named your project_name
PROJECT_NAME="project1"

#This is for some subdomain enumeration tools. 
#e.g. target.com
MAINSCOPE="target.com"

#Are you iterating subdomains enumeration
ITERATING=True

#If so, how often to run subdomain enumeration. New subdomains will be notified on slack. 86400s is 1 day
RECURSION=86400

#List of the seed/root domains
#If ASN scanning is activated, this is not need. (recommended to do some manual recon (i.e Google Fu, Crunchbase, etc.) and put all domains-
#inside this file)
TARGET_LIST="/root/roots.txt"

#Defualt output folder is ~/output
#e.g. /root/output/
#If you supply a directory and it's not found, it will create one there.
OUTPUT_FOLDER="/home/username/Documents/ProjectA/output"

#Interesting VHOSTS to add (default wordlist of vhosts will be checked)
#e.g. VHOST=["example1","example2"]
VHOST=[]

#Do you want to FFUF all target URLS? 
#Change to true if you have alot of time on your hands ;)
FFUF_DIR=False

#This wordlist will be added to, so make sure you supply a copy
DIR_WORDLIST="/root/wordlist/wl.txt"

#This wordlist is for VHOSTS. A defualt vhosts file is supplied already.
VHOST_WORDLIST="/root/ProjectA/Tools/vhosts.txt"

#Amount of threads to use. Higher = Faster.
#I recommend 200 threads, but for less capable hardware, put this number lower.
THREADS=20

#File to reolvers. 
#e.g. /dir/dir/resolvers.txt
#Leave blank to choose default options (50 resolvers are supplied by default)
RESOLVERS=""

#Range of ports to scan for masscan. Defualt is 0-65535, (yes port 0 aswell ;P)
PORT_SCAN="0-65535"

#Directory to "nuclei-templates"
#e.g. /dir/dir/nuclei-templates
#Leave blank to choose default location (./Tools/nuclei-templates)
NUCLEI_DIR="/root/ProjectA/Tools/nuclei-templates"

#Slack webhook used to notify you when:
#   - any nuclei templates have been successful
#   - when process is complete
#   - and more cool things!
SLACK_WEBHOOK_ERROR=""
SLACK_WEBHOOK_FINDINGS=""
SLACK_WEBHOOK_SUBDOMAINS=""

################## MORE CONFIGS ###################

#Helps confirm massdns and masscan processes/eliminate false positives in livetargetsfinder stage (only port 80,443)
#Setting this to true will make the process slower
#Recommended to keep "True"
NMAP_SCAN_IN_LIVETARGETSFIDER=True

#Do you want to scan your ASN's?
#Setting this to true will make the process very slow
ASN_SCAN=False

#If true:
#Leave blank if you don't want to scan ASN's
#Provide ASN without starting "AS" (AS12345 = 12345)
#e.g. ASN=["11111","22222"]
ASN=[""]

#Since scanning such ranges can result in lots of different domains (possible out of scope)
#Please supply a string to grep for the output
#e.g. example or example.com
ASN_GREP="acronis.com"

#################### API KEYS: #################### 

GITHUB_TOKEN=""
#SHODAN_KEY=""
