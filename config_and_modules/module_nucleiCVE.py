import os
from config_and_modules.config import *
import config_and_modules.module_validation
import config_and_modules.module_timer
from multiprocessing.pool import ThreadPool
import config_and_modules.module_slack

def CVE(data):
    folder = data[0]
    nuclei_folder = data[1]
    cve = data[2]
    
    output = f"{folder}/nuclei_cves/{cve.replace('.yaml','')}"

    try:
        os.system(f"cat {folder}/final_targetUrls.txt | nuclei -t {nuclei_folder}/cves/{cve} > {output}.txt")

        if os.stat(f"{output}.txt").st_size == 0:
            os.system(f"sudo rm {output}.txt")
        else:
            config_and_modules.module_slack.nucleiCVE(cve.replace('.yaml',''))

    except Exception as error:
        print(f"{error}\nSomething went wrong.")
        config_and_modules.module_slack.error(error,"nucleiCVE")

if __name__ == "__main__":
    start_time = config_and_modules.module_timer.start_timer()
    a = config_and_modules.module_validation.output_folder()
    b = config_and_modules.module_validation.nuclei_directory()
    os.system(f"sudo mkdir {a}/nuclei_cves/")

    pool = ThreadPool() #Start threading pool
    cves = []

    for i in os.listdir(f"{b}/cves"):
        temp = []
        temp.extend((a,b,i))
        cves.append(temp)

    pool.map(CVE,[cves[0], cves[1], cves[2], cves[3], cves[4], cves[5], 
                cves[6], cves[7], cves[8], cves[9], cves[10], cves[11], 
                cves[12], cves[13], cves[14], cves[15], cves[16], cves[17], 
                cves[18], cves[19], cves[20], cves[21], cves[22], cves[23], 
                cves[24], cves[25], cves[26], cves[27], cves[28], cves[29], 
                cves[30], cves[31], cves[32], cves[33], cves[34], cves[35], 
                cves[36], cves[37], cves[38], cves[39], cves[40], cves[41], 
                cves[42], cves[43], cves[44], cves[45], cves[46], cves[47], 
                cves[48], cves[49], cves[50], cves[51], cves[52], cves[53], 
                cves[54], cves[55], cves[56], cves[57], cves[58], cves[59], 
                cves[60], cves[61], cves[62], cves[63], cves[64], cves[65], 
                cves[66], cves[67], cves[68], cves[69], cves[70], cves[71], 
                cves[72], cves[73], cves[74], cves[75], cves[76]])

    config_and_modules.module_timer.end_timer(f"Nuclei [CVE's]",a,start_time)