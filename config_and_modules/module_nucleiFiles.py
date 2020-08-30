import os
from config_and_modules.config import *
import config_and_modules.module_validation
import config_and_modules.module_timer
from multiprocessing.pool import ThreadPool
import config_and_modules.module_slack

def Files(data):
    folder = data[0]
    nuclei_folder = data[1]
    vuln = data[2]
    
    output = f"{folder}/nuclei_files/{vuln.replace('.yaml','')}"

    try:
        os.system(f"cat {folder}/final_targetUrls.txt | nuclei -t {nuclei_folder}/files/{vuln} > {output}.txt")

        if os.stat(f"{output}.txt").st_size == 0:
            os.system(f"sudo rm {output}.txt")
        else:
            config_and_modules.module_slack.nucleiFiles(vuln.replace('.yaml',''))

    except Exception as error:
        print(f"{error}\nSomething went wrong.")
        config_and_modules.module_slack.error(error,"nucleiFiles")

if __name__ == "__main__":
    start_time = config_and_modules.module_timer.start_timer()
    a = config_and_modules.module_validation.output_folder()
    b = config_and_modules.module_validation.nuclei_directory()
    os.system(f"sudo mkdir {a}/nuclei_files/")

    pool = ThreadPool() #Start threading pool
    files = []

    for i in os.listdir(f"{b}/files"):
        temp = []
        temp.extend((a,b,i))
        files.append(temp)

    pool.map(Files,[files[0], files[1], files[2], files[3], files[4], files[5], 
                files[6], files[7], files[8], files[9], files[10], files[11], 
                files[12], files[13], files[14], files[15], files[16], files[17], 
                files[18], files[19], files[20], files[21], files[22],files[23],
                files[24],files[25],files[26],files[27],files[28]])

    config_and_modules.module_timer.end_timer(f"Nuclei [Files]",a,start_time)
