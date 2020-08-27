import os
from config_and_modules.config import *
import config_and_modules.module_timer
import config_and_modules.module_validation
import config_and_modules.module_slack

def aquatone_targetUrls(folder):
    try:
        os.system(f"sudo cat {folder}/final_targetUrls.txt | aquatone -threads {THREADS/2} -out {folder}/aquatone/urls/")
    except Exception as error:
        print(f"{error}\nSomething went wrong.")
        config_and_modules.module_slack.error(error,"aquatone_targetUrls")

if __name__ == "__main__":
    start_time = config_and_modules.module_timer.start_timer()
    a = config_and_modules.module_validation.output_folder()
    os.system(f"sudo mkdir {a}/aquatone/urls/")
    aquatone_targetUrls(a)
    config_and_modules.module_timer.end_timer("Aquatone [Target Urls]",a,start_time)
