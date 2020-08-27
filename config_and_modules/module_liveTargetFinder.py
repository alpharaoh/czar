import os
from config_and_modules.config import *
import config_and_modules.module_validation
import config_and_modules.module_timer
import config_and_modules.module_slack

def liveTargetFinder(folder):
    os.chdir("./Tools/livetargetsfinder/")
    try:
        if NMAP_SCAN_IN_LIVETARGETSFIDER:
            os.system(f"sudo python3 liveTargetsFinder.py --target-list {folder}/final_Subdomains.txt --nmap")
        else:
            os.system(f"sudo python3 liveTargetsFinder.py --target-list {folder}/final_Subdomains.txt")
    except Exception as error:
        print(f'{error}\n Something went wrong. Check "NMAP_SCAN_IN_LIVETARGETSFIDER" in config.py')
        config_and_modules.module_slack.error(error,"liveTargetFinder")
        
    os.system(f"sudo cp -R ./output/ {folder}/livetargetsfinder_output/")
    os.system(f"sudo rm ./output/*")
    os.chdir("./../../")
    os.system(f"sudo cat {folder}/subdomain_enum/{PROJECT_NAME}_tls_ips.txt {folder}/livetargetsfinder_output/final_Subdomains_ips_alive.txt | sort -u > {folder}/final_IPs.txt")

if __name__ == "__main__":
    start_time = config_and_modules.module_timer.start_timer()
    a = config_and_modules.module_validation.output_folder()
    liveTargetFinder(a)
    config_and_modules.module_timer.end_timer("LiveTargetsFinder",a,start_time)