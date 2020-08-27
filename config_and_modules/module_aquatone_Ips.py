import os
from config_and_modules.config import *
import config_and_modules.module_timer
import config_and_modules.module_validation
import config_and_modules.module_slack

def aquatone_Ips(folder):
    try:
        os.system(f"sudo cat {folder}/{PROJECT_NAME}_ports_andIps.txt | aquatone -threads {THREADS} -out {folder}/aquatone/ips/")
    except Exception as error:
        print(f"{error}\nSomething went wrong.")
        config_and_modules.module_slack.error(error,"aquatone_Ips")

if __name__ == "__main__":
    start_time = config_and_modules.module_timer.start_timer()
    a = config_and_modules.module_validation.output_folder()
    os.system(f"sudo mkdir {a}/aquatone/ips/")
    aquatone_Ips(a)
    config_and_modules.module_timer.end_timer("Aquatone [Ips]",a,start_time)
