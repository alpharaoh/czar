import os
from config_and_modules.config import *
import config_and_modules.module_validation
import config_and_modules.module_timer
import config_and_modules.module_slack
from multiprocessing.pool import ThreadPool

def getTargetUrls(folder: str) -> list:
    targets_file = open(f"{folder}/final_targetUrls.txt","r")
    targets = targets_file.read().split("\n")
    targets_file.close()
    targets.pop()

    return targets

def smuggler(domain: str):
    file_name = domain.replace('http://','').replace('https://','')

    os.system(f"python3 ./Tools/smuggler/smuggler.py -m POST -t 200 -u {domain} -q | grep CRITICAL > ./output/{PROJECT_NAME}/{file_name}_smuggler.txt")
    os.system(f"python3 ./Tools/smuggler/smuggler.py -m DELETE -t 200 -u {domain} -q | grep CRITICAL >> ./output/{PROJECT_NAME}/{file_name}_smuggler.txt")

    if os.stat(f"./output/{PROJECT_NAME}/{file_name}_smuggler.txt").st_size == 0:
        os.system(f"rm ./output/{PROJECT_NAME}/{file_name}_smuggler.txt")
    else:
        config_and_modules.module_slack.smuggler(file_name)
    
def main():
    print("Starting HTTP Request Smuggler")
    start_time = config_and_modules.module_timer.start_timer()
    a = config_and_modules.module_validation.output_folder()
    targets = getTargetUrls(a)

    pool = ThreadPool() #Start threading pool
    pool.map(smuggler,[i for i in targets])

    config_and_modules.module_timer.end_timer(f"HTTP Request Smuggler",a,start_time)