import os
from config_and_modules.config import *
import config_and_modules.module_timer
import config_and_modules.module_validation
import config_and_modules.module_slack

def gau(folder):
    os.system(f"sudo mkdir {folder}/gau")
    subdomains = open(f"{folder}/final_Subdomains.txt","r").read().split("\n")
    try:
        for i in subdomains:
            os.system(f"gau {i} -o | tee {folder}/gau/{i}_gau.txt")

            if os.stat(f"{folder}/gau/{i}_gau.txt").st_size == 0:
                os.system(f"sudo rm {folder}/gau/{i}_gau.txt")

    except Exception as error:
        print(f"{error}\nThere was an error")
        config_and_modules.module_slack.error(error,"gau")


if __name__ == "__main__":
    a = config_and_modules.module_validation.output_folder()
    gau(a)

