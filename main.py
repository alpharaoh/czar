import os
import sys
import time
import datetime
from threading import Thread
from config_and_modules.config import *
import config_and_modules.module_ports
import config_and_modules.module_subdomains
import config_and_modules.module_liveTargetFinder
import config_and_modules.module_nucleiSubdomainTakeover
import config_and_modules.module_nucleiVulnerabilities
import config_and_modules.module_initial
import config_and_modules.module_validation
import config_and_modules.module_timer
import config_and_modules.module_ffuf_vhost
import config_and_modules.module_aquatone_targetUrls
import config_and_modules.module_aquatone_Ips
import config_and_modules.module_slack

if sys.version_info < (3, 0):
    sys.stdout.write("Sorry, this tool only works with Python 3.X\n")
    exit()

class ProjectA():
    def ASN_module(self):
        if ASN_SCAN:
            exec(open('./config_and_modules/module_initial.py').read())
        else:
            pass

    def subdomain_Enum(self):
        exec(open('./config_and_modules/module_subdomains.py').read())

    #Start to parallel process modules

    def nuclei_SubdomainTakeover(self):
        exec(open('./config_and_modules/module_nucleiSubdomainTakeover.py').read())
    
    def liveTargetFinder(self):
        exec(open('./config_and_modules/module_liveTargetFinder.py').read())

    def ports(self):
        exec(open('./config_and_modules/module_ports.py').read())

    def ffuf_vhost(self):
        exec(open('./config_and_modules/module_ffuf_vhost.py').read())

    def ffuf_dir(self):
        if FFUF_DIR:
            exec(open('./config_and_modules/module_ffuf_dir.py').read())

    def nucleiVulnerabilities(self):
        exec(open('./config_and_modules/module_nucleiVulnerabilities.py').read())

    def nucleiCVE(self):
        exec(open('./config_and_modules/module_nucleiCVE.py').read())

    def nucleiFiles(self):
        exec(open('./config_and_modules/module_nucleiFiles.py').read())

    def gau(self):
        exec(open('./config_and_modules/module_gau.py').read())

    def aquatone_targetUrls(self):
        exec(open('./config_and_modules/module_aquatone_targetUrls.py').read())

    def aquatone_Ips(self):
        exec(open('./config_and_modules/module_aquatone_Ips.py').read())

    def threading(self,folder):
        thread0 = Thread(target = self.liveTargetFinder)
        thread1 = Thread(target = self.nuclei_SubdomainTakeover)

        thread0.start()
        thread1.start()

        thread0.join()
        thread1.join()

        os.system(f"cat {folder}/subdomain_enum/{PROJECT_NAME}_httpx.txt {folder}/livetargetsfinder_output/final_Subdomains_targetUrls.txt | sort -u | tee {folder}/final_targetUrls.txt") 

    def threading2(self):
        os.system(f"sudo mkdir {a}/ffuf/")
        os.system(f"sudo mkdir {a}/aquatone/")

        thread0 = Thread(target = self.ports)
        thread1 = Thread(target = self.ffuf_vhost)
        thread3 = Thread(target = self.nucleiCVE)
        thread4 = Thread(target = self.gau)
        thread5 = Thread(target = self.ffuf_dir)
        thread6 = Thread(target = self.aquatone_targetUrls)
        thread7 = Thread(target = self.nucleiVulnerabilities)
        thread8 = Thread(target = self.nucleiFiles)
        thread9 = Thread(target = self.aquatone_Ips)

        thread0.start()
        thread1.start()
        thread3.start()
        thread4.start()
        thread5.start()
        thread6.start()
        thread7.start()
        thread8.start()
        thread9.start()

        thread0.join()
        thread1.join()
        thread3.join()
        thread4.join()
        thread5.join()
        thread6.join()
        thread7.join()
        thread8.join()
        thread9.join()


#Start timer
start_time = config_and_modules.module_timer.start_timer()

a = config_and_modules.module_validation.output_folder()

main = ProjectA()
main.ASN_module() #optional
main.subdomain_Enum()
main.threading(a) #nuclei subdomain takeover + livetargetsfinder
main.threading2() #portscan + ffuf + waybackurls + nuclei CVE's
main.aquatone_Ips() #using ips and ports found from 'ports' module

config_and_modules.module_timer.end_timer("Total",a,start_time)
config_and_modules.module_slack.finished(a)
