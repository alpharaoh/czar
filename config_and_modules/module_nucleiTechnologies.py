import os
from config_and_modules.config import *
import config_and_modules.module_validation
import config_and_modules.module_timer
from multiprocessing.pool import ThreadPool
import config_and_modules.module_slack

def getTargetDomains(folder: str) -> list:
    targets_file = open(f"{folder}/final_targetUrls.txt","r")
    targets = targets_file.read().split("\n")
    targets_file.close()
    targets.pop()

    return targets

def genericDetections(target):
    os.system(f"echo '{target}' | nuclei -t {NUCLEI_DIR}/technologies/ >> nuclei_Technologies.txt") #idgaf

    if os.stat(f"nuclei_Technologies.txt").st_size == 0:
        os.system(f"rm nuclei_Technologies.txt")
    else:
        config_and_modules.module_slack.nucleiGeneric(target)

def main():
    start_time = config_and_modules.module_timer.start_timer()
    a = config_and_modules.module_validation.output_folder()
    targets = getTargetDomains(a)

    pool = ThreadPool() #Start threading pool
    pool.map(genericDetections,[i for i in targets])

    config_and_modules.module_timer.end_timer(f"Nuclei [Technologies]",a,start_time)