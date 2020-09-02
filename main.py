import os
import sys
import time
import datetime
from threading import Thread
from config_and_modules.config import *
import config_and_modules.module_validation
import config_and_modules.module_iterating
from config_and_modules import module_nucleiDNS
from config_and_modules import module_nucleiGeneric
from config_and_modules import module_nucleiTechnologies
from config_and_modules import module_nucleiSecurityMisconfig
from config_and_modules import module_smuggler

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

    def nuclei_SubdomainTakeover(self):
        os.system("pwd")
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
    
    def nucleiDNS(self): #AH, why did I not call the scripts like this before 
        module_nucleiDNS.main()

    def smuggler(self):
        module_smuggler.main()

    def nucleiTechnology(self):
        module_nucleiTechnologies.main()

    def nucleiGeneric(self):
        module_nucleiGeneric.main()

    def nucleiSecurityMisconfig(self):
        module_nucleiSecurityMisconfig.main()

    def threading2(self):
        os.system(f"sudo mkdir {a}/ffuf/")
        os.system(f"sudo mkdir {a}/aquatone/")

        #your CPU will hate you

        thread0 = Thread(target = self.ports)
        thread1 = Thread(target = self.ffuf_vhost)
        thread3 = Thread(target = self.nucleiCVE)
        thread4 = Thread(target = self.gau)
        thread5 = Thread(target = self.ffuf_dir)
        thread6 = Thread(target = self.aquatone_targetUrls)
        thread7 = Thread(target = self.nucleiVulnerabilities)
        thread8 = Thread(target = self.nucleiFiles)
        thread9 = Thread(target = self.aquatone_Ips)
        thread10 = Thread(target = self.nucleiDNS)
        thread11 = Thread(target = self.smuggler)
        thread12 = Thread(target = self.nucleiGeneric)
        thread13 = Thread(target = self.nucleiSecurityMisconfig)
        thread14 = Thread(target = self.nucleiTechnology)

        thread0.start()
        thread1.start()
        thread3.start()
        thread4.start()
        thread5.start()
        thread6.start()
        thread7.start()
        thread8.start()
        thread9.start()
        thread10.start()
        thread11.start()
        thread12.start()
        thread13.start()
        thread14.start()

        thread0.join()
        thread1.join()
        thread3.join()
        thread4.join()
        thread5.join()
        thread6.join()
        thread7.join()
        thread8.join()
        thread9.join()
        thread10.join()
        thread11.join()
        thread12.join()
        thread13.join()
        thread14.join()


#Start timer
start_time = config_and_modules.module_timer.start_timer()
a = config_and_modules.module_validation.output_folder()

if ITERATING:
    os.system(f"mkdir {a}/iterating/")
    iteration_file = open(f"{a}/iterating/number_of_runs.txt","w")
    iteration_file.write("0\n")
    iteration_file.close()

main = ProjectA()
main.ASN_module() #optional
main.subdomain_Enum()
main.liveTargetFinder()
main.nuclei_SubdomainTakeover()
os.system(f"cat {a}/subdomain_enum/{PROJECT_NAME}_httpx.txt {a}/livetargetsfinder_output/final_Subdomains_targetUrls.txt | sort -u | tee {a}/final_targetUrls.txt")
main.threading2() #portscan + ffuf + waybackurls + nuclei CVE's
main.aquatone_Ips() #using ips and ports found from 'ports' module

config_and_modules.module_timer.end_timer("Total",a,start_time)
config_and_modules.module_slack.finished(a)

if ITERATING:
    time.sleep(RECURSION)
    iteration_file = open(f"{a}/iterating/number_of_runs.txt","a")
    iteration_file.write("1\n")
    iteration_file.close()
    while True:
        main.subdomain_Enum()

