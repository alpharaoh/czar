import os
from config_and_modules.config import *
import config_and_modules.module_timer
import config_and_modules.module_validation
import config_and_modules.module_slack

def ffuf_dir(folder):
    file = open(f"{folder}/final_targetUrls.txt","r").read().split("\n")
    file.pop()
    import subprocess
    import json

    for i in file:
        try:
            file_name = i.replace("https://","").replace("http://","")
            os.system(f'ffuf -w {DIR_WORDLIST} -t {THREADS/2} -u {i}/FUZZ -of json -o {folder}/ffuf/{file_name}_dir.json')

            ffuf_data = open(f"{folder}/ffuf/{file_name}_dir.json","r")
            ffuf_json = ffuf_data.read()
            data = json.loads(ffuf_json)
            ffuf_data.close()
            output = open(f"{folder}/ffuf/{file_name}_dir.txt","w")
            output.write(data["commandline"]+"\n\n")
            
            const = 40

            for i in data["results"]:
                length = len(i["input"]["FUZZ"])
                seperate = const-length
                if seperate < 0:
                    seperate = const
                output.write(f'input: {i["input"]["FUZZ"]}{" " * seperate}| status: {i["status"]} | length: {i["length"]} | words: {i["words"]} | lines: {i["lines"]} |\n')
            
            os.system(f"sudo rm {folder}/ffuf/{file_name}_dir.json")
        except Exception as error:
            print(f"{error}\nSomething went wrong.")
            config_and_modules.module_slack.error(error,"ffuf_dir")

if __name__ == "__main__":
    start_time = config_and_modules.module_timer.start_timer()
    a = config_and_modules.module_validation.output_folder()
    ffuf_dir(a)
    config_and_modules.module_timer.end_timer("FFUF [dir]",a,start_time)