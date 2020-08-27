import os
from config_and_modules.config import *
import config_and_modules.module_validation
import config_and_modules.module_timer
from multiprocessing.pool import ThreadPool
import config_and_modules.module_slack

def Vulnerabilities(data):
    folder = data[0]
    nuclei_folder = data[1]
    vuln = data[2]
    
    output = f"{folder}/nuclei_vulnerabilities/{vuln.replace('.yaml','')}"

    try:
        os.system(f"cat {folder}/final_targetUrls.txt | nuclei -t {nuclei_folder}/vulnerabilities/{vuln} > {output}.txt")

        if os.stat(f"{output}.txt").st_size == 0:
            os.system(f"sudo rm {output}.txt")
        else:
            config_and_modules.module_slack.nucleiVulnerabilities(vuln.replace('.yaml',''))

    except Exception as error:
        print(f"{error}\nSomething went wrong.")
        config_and_modules.module_slack.error(error,"nucleiVulnerabilities")

if __name__ == "__main__":
    start_time = config_and_modules.module_timer.start_timer()
    a = config_and_modules.module_validation.output_folder()
    b = config_and_modules.module_validation.nuclei_directory()
    os.system(f"sudo mkdir {a}/nuclei_vulnerabilities/")

    pool = ThreadPool() #Start threading pool
    vulns = []

    for i in os.listdir(f"{b}/vulnerabilities"):
        temp = []
        temp.extend((a,b,i))
        vulns.append(temp)

    pool.map(Vulnerabilities,[vulns[0], vulns[1], vulns[2], vulns[3], vulns[4], vulns[5], 
                vulns[6], vulns[7], vulns[8], vulns[9], vulns[10], vulns[11], 
                vulns[12], vulns[13], vulns[14], vulns[15], vulns[16], vulns[17], 
                vulns[18], vulns[19], vulns[20], vulns[21], vulns[22]])

    config_and_modules.module_timer.end_timer(f"Nuclei [Vulnerabilities]",a,start_time)