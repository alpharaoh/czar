import os
import re
from config_and_modules.config import *
import config_and_modules.module_timer
import config_and_modules.module_validation
from collections import defaultdict
import config_and_modules.module_slack

#Scanning all 65535 ports, including port 0 ;) (or otherwise - check configs)
#masscan -> nmap -> brutespray

def ports_andIps(lis,folder): #uses httpx to resolve the ips and ports
    try:
        ip_with_ports = open(f"{folder}/{PROJECT_NAME}_ports_andIps.txt","w")
        ip_with_ports.write("\n".join(lis))
        os.system(f"cat {folder}/{PROJECT_NAME}_ports_andIps.txt | httpx -silent | tee {folder}/../{PROJECT_NAME}_httpx_PortsIps.txt")
    except Exception as error:
        print(f"{error}\nSomething went wrong.")
        config_and_modules.module_slack.error(error,"ports [ports_andIps()]")

def masscan(folder):
    import socket
    try:
        start_time = config_and_modules.module_timer.start_timer()
        os.system(f"sudo mkdir {folder}")
        os.system(f"sudo masscan -p{PORT_SCAN},U:{PORT_SCAN} -iL {folder}/../final_IPs.txt --rate=1800 | tee {folder}/masscan_IpPort.txt")
        #Parsing results 
        config_and_modules.module_timer.end_timer("Masscan",f"{folder}/../",start_time)

        var1 = open(f"{folder}/masscan_IpPort.txt","r").read()
        var = re.split("                                     \n|                                    \n|                                  \n|                                   \n|                                  \n",var1)
        var.pop()                                                
        lis = []

        for i in var:
            a = i.split()
            print(a[5],a[3])
            lis.append(f"{a[5]}:{a[3]}".replace("/tcp","").replace("/udp",""))

        ports_andIps(lis,folder)

        ip_to_ports = defaultdict(set)

        for i in lis:
            a = i.split(":")
            ip_to_ports[a[0]].add(a[1])

        start_time = config_and_modules.module_timer.start_timer()
        for ip in sorted(ip_to_ports, key=socket.inet_aton):
            #sort the ports
            ports = sorted(ip_to_ports[ip])
            ports = ','.join(ports)
            ##NMAP
            os.system(f"sudo mkdir {folder}/{ip}")
            os.system(f"sudo nmap -T4 -A -p {ports} {ip} -oA {folder}/{ip}/{ip} --stylesheet https://raw.githubusercontent.com/honze-net/nmap-bootstrap-xsl/master/nmap-bootstrap.xsl")
        
        config_and_modules.module_timer.end_timer("Nmap",f"{folder}/../",start_time)
        return ip_to_ports
    except Exception as error:
        print(f"{error}\nSomething went wrong.")
        config_and_modules.module_slack.error(error,"ports [masscan()]")

def brutespray(folder, ip_to_ports):
    import socket
    start_time = config_and_modules.module_timer.start_timer()
    for ip in sorted(ip_to_ports, key=socket.inet_aton):
        #brutespray
        try:
            os.system(f"python ./Tools/brutespray/brutespray.py -t {round(THREADS/2)} -f {folder}/{ip}/{ip}.gnmap -T 20 -o output/{PROJECT_NAME}/ips/{ip}/brutespray")
        except Exception as error:
            print(f"{error}\nSomething went wrong.")
            config_and_modules.module_slack.error(error,"ports [brutespray()]")
    config_and_modules.module_timer.end_timer("Brutespray",f"{folder}/../",start_time)

if __name__ == "__main__":
    folder = config_and_modules.module_validation.output_folder()
    a = f"{folder}/ips"
    b = masscan(a)
    brutespray(a,b)
