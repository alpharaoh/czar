import os
from config_and_modules.config import *
import config_and_modules.module_timer
import config_and_modules.module_validation
import config_and_modules.module_slack

#httpx -> nuclei subdomain takeover template

def httpx(folder):
    try:
        start_time = config_and_modules.module_timer.start_timer()
        os.system(f"cat {folder}/final_Subdomains.txt | httpx -silent | tee {folder}/subdomain_enum/{PROJECT_NAME}_httpx.txt")
        config_and_modules.module_timer.end_timer("Httpx",folder,start_time)
    except Exception as error:
        print(f"{error}\nSomethings went wrong.")
        config_and_modules.module_slack.error(error,"nucleiSubdomainTakeover [httpx()]")

def subdomain_Takeover(folder, nuclei_folder):
    try:
        start_time = config_and_modules.module_timer.start_timer()
        os.system(f"cat {folder}/subdomain_enum/{PROJECT_NAME}_httpx.txt | nuclei -t {nuclei_folder}/subdomain-takeover/detect-all-takeovers.yaml | tee {folder}/{PROJECT_NAME}_subdomainTakeover.txt")
        
        #Check to see if there is no subdomains
        if os.stat(f"{folder}/{PROJECT_NAME}_subdomainTakeover.txt").st_size != 0:
            config_and_modules.module_slack.nucleiFiles()

        config_and_modules.module_timer.end_timer("Nuclei [Subdomain takeover]",folder,start_time)
    except Exception as error:
        print(f"{error}\nSomethings went wrong.")
        config_and_modules.module_slack.error(error,"nucleiSubdomainTakeover [subdomain_Takeover()]")

if __name__ == "__main__":
    a = config_and_modules.module_validation.output_folder()
    b = config_and_modules.module_validation.nuclei_directory()

    httpx(a)
    subdomain_Takeover(a,b)