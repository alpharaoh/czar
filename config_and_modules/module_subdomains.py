import os
import time
import json
from threading import Thread
from config_and_modules.config import *
import config_and_modules.module_timer
import config_and_modules.module_validation
import config_and_modules.module_slack
import config_and_modules.module_iterating

class Subdomain_Enumeration():
    def Subfinder(self, folder):
        start_time = config_and_modules.module_timer.start_timer()
        try:
            os.system(f"subfinder -silent -d {MAINSCOPE} -config ./Tools/subfinder_config.yaml | tee {folder}/subdomain_enum/{PROJECT_NAME}_subfinder.txt")
        except Exception as error:
            print(f"Error: {error}\nDo you have subfinder installed correctly? Make sure it's in $PATH (/usr/local/bin)")
            config_and_modules.module_slack.error(error,"subdomains [Subfinder()]")
        config_and_modules.module_timer.end_timer("Subdomain module [Subfinder]",folder,start_time)

    def Amass(self, folder, resolvers):
        start_time = config_and_modules.module_timer.start_timer()
        try:
            os.system(f"amass enum -passive -d {MAINSCOPE} -o {folder}/subdomain_enum/{PROJECT_NAME}_amass.txt -rf {resolvers} -config ./Tools/amass_config.ini")
        except Exception as error:
            print(f"Error: {error}\nDo you have amass installed correctly? Make sure it's in $PATH (/usr/local/bin)")
            config_and_modules.module_slack.error(error,"subdomains [Amass()]")
        config_and_modules.module_timer.end_timer("Subdomain module [Amass]",folder,start_time)

    def Sublister(self, folder):
        start_time = config_and_modules.module_timer.start_timer()
        try:
            os.system(f"python3 ./Tools/sublist3r.py -d {MAINSCOPE} -t {THREADS} -o {folder}/subdomain_enum/{PROJECT_NAME}_sublister.txt")
        except Exception as error:
            print(f"Error: {error}\nDo you have Sublister installed correctly? Check the Tools directory.")
            config_and_modules.module_slack.error(error,"subdomains [Sublister()]")
        config_and_modules.module_timer.end_timer("Subdomain module [Sublister]",folder,start_time)

    def GithubSubdomains(self, folder):
        start_time = config_and_modules.module_timer.start_timer()
        try:
            for i in range(4): #going to loop 5 times
                os.system(f"python3 ./Tools/github_subdomains.py -d {MAINSCOPE} -t {GITHUB_TOKEN} | tee {folder}/subdomain_enum/{PROJECT_NAME}_git_{i+1}.txt")
                time.sleep(60)

            #Last loop will have longer sleep.
            time.sleep(60)
            os.system(f"python3 ./Tools/github_subdomains.py -d {MAINSCOPE} -t {GITHUB_TOKEN} | tee {folder}/subdomain_enum/{PROJECT_NAME}_git_{5}.txt")
            
            #Cat all files, sort, and remove access.
            os.system(f"cat {folder}/subdomain_enum/{PROJECT_NAME}_git_{1}.txt {folder}/subdomain_enum/{PROJECT_NAME}_git_{2}.txt {folder}/subdomain_enum/{PROJECT_NAME}_git_{3}.txt {folder}/subdomain_enum/{PROJECT_NAME}_git_{4}.txt {folder}/subdomain_enum/{PROJECT_NAME}_git_{5}.txt | sort -u > {folder}/subdomain_enum/{PROJECT_NAME}_git_subdomains.txt")
            for i in range(5):
                os.system(f"rm {folder}/subdomain_enum/{PROJECT_NAME}_git_{i+1}.txt")

        except Exception as error:
            print(f"{error}\nSomething went wrong")
            config_and_modules.module_slack.error(error,"subdomains [GithubSubdomains()]")
        config_and_modules.module_timer.end_timer("Subdomain module [Github subdomains]",folder,start_time)

    def tls_Bufferover(self, folder):
        try:
            start_time = config_and_modules.module_timer.start_timer()
            import requests
            ips = []
            domains = []

            URL = f"http://tls.bufferover.run/dns?q={MAINSCOPE}"
            request = requests.get(URL) 
            data = request.json().get("Results")

            for i in data:
                j = i.split(",")
                ips.append(j[-1])

                #if wildcard found in subdomain, skip
                if "*" in j[1]:
                    pass
                else:
                    domains.append(j[1])

            #Sorting files
            ips = sorted(set(ips))
            domains = sorted(set(domains))

            #Appending ips and subdomains to file.
            ips_file = open(f"{folder}/subdomain_enum/{PROJECT_NAME}_tls_ips.txt", "a")
            for i in ips:
                ips_file.write(f"{i}\r\n")

            domains_file = open(f"{folder}/subdomain_enum/{PROJECT_NAME}_tls_subdomains.txt", "a")
            for i in domains:
                domains_file.write(f"{i}\r\n")

            #Closing files
            ips_file.close()
            domains_file.close()
            config_and_modules.module_timer.end_timer("Subdomain module [tls.bufferover.run]",folder,start_time)

        except Exception as error:
            print(f"{error}\nSomething went wrong")
            config_and_modules.module_slack.error(error,"subdomains [tls_Bufferover()] no data found or too much data (timeout)")

    def newCheck(self,folder,iteration_number):
        new = f"{folder}/final_Subdomains_number_{iteration_number}.txt"
        old = f"{folder}/final_Subdomains_number_{iteration_number-1}.txt"

        os.system(f"diff {old} {new} | grep '>' > {folder}/diff.txt")

        if os.stat(f"{folder}/diff.txt").st_size != 0:
            fil = open(f"{folder}/diff.txt","r")
            subdomains = fil.read()
            fil.close()

            config_and_modules.module_slack.newSubdomains(subdomains)
            os.system(f"rm {folder}/diff.txt")
        else:
            os.system(f"rm {folder}/diff.txt")

    def sort_Final(self,folder,iteration_number=None):
        try:
            if iteration_number != None and iteration_number != 0:
                os.system(f"cat {folder}/subdomain_enum/{PROJECT_NAME}_subfinder.txt {folder}/subdomain_enum/{PROJECT_NAME}_amass.txt {folder}/subdomain_enum/{PROJECT_NAME}_sublister.txt {folder}/subdomain_enum/{PROJECT_NAME}_git_subdomains.txt {folder}/subdomain_enum/{PROJECT_NAME}_tls_subdomains.txt | sort -u > {folder}/final_Subdomains_number_{iteration_number}.txt")
                os.system(f"rm -r {folder}/subdomain_enum/")

                if iteration_number != 0:
                    ##Check if there is new subdomains.
                    self.newCheck(folder, iteration_number)

                iteration_file = open(f"{folder}/number_of_runs.txt","a")
                iteration_file.write(f"{iteration_number+1}\n")
                iteration_file.close()

                iteration_number = config_and_modules.module_iterating.wait()
            else: 
                os.system(f"cat {folder}/subdomain_enum/{PROJECT_NAME}_subfinder.txt {folder}/subdomain_enum/{PROJECT_NAME}_amass.txt {folder}/subdomain_enum/{PROJECT_NAME}_sublister.txt {folder}/subdomain_enum/{PROJECT_NAME}_git_subdomains.txt {folder}/subdomain_enum/{PROJECT_NAME}_tls_subdomains.txt | sort -u > {folder}/final_Subdomains.txt")

        except Exception as error:
            print(f"{error}\nSomething went wrong")
            config_and_modules.module_slack.error(error,"subdomains [tls_Bufferover()]")

    def start(self,a,iteration_number=None):
        os.system(f"sudo mkdir {a}/subdomain_enum/")

        b = config_and_modules.module_validation.resolvers()

        #thread0 = Thread(target = self.Subfinder, args=(a,))
        #thread1 = Thread(target = self.Amass, args=(a,b,))
        #thread2 = Thread(target = self.Sublister, args=(a,))
        #thread3 = Thread(target = self.GithubSubdomains, args=(a,))
        thread4 = Thread(target = self.tls_Bufferover, args=(a,))

        #thread0.start()
        #thread1.start()
        #thread2.start()
        #thread3.start()
        thread4.start()

        #thread0.join()
        #thread1.join()
        #thread2.join()
        #thread3.join()
        thread4.join()

        #Cat's all subdomains and sorts into a final file.
        self.sort_Final(a,iteration_number)

if __name__ == "__main__":
    enum = Subdomain_Enumeration()
    start_time = config_and_modules.module_timer.start_timer()
    a = config_and_modules.module_validation.output_folder() #returns path to project folder as string
    b = a + "/iterating/"

    if ITERATING:
        #Check iteration
        iteration_number = config_and_modules.module_iterating.check_iteration(b)

        if iteration_number == 0:
            enum.start(a)

        else:   
            enum.start(b,iteration_number)
    else:
        enum.start(a)

    config_and_modules.module_timer.end_timer("Total time gathering subdomains",a,start_time)
