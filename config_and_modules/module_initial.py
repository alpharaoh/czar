import os
from config_and_modules.config import *
import config_and_modules.module_validation
import config_and_modules.module_timer
import config_and_modules.module_slack

def ASN_Amass(ASN_Numbers, folder):
    try:
        if len(ASN_Numbers) > 1:
            ASN_Numbers = ','.join(ASN_Numbers)
        else:
            ASN_Numbers = ASN_Numbers[0]

        os.system(f"amass intel -asn {ASN_Numbers} | tee {folder}/subdomain_enum/{PROJECT_NAME}_ASNintel_temporary.txt")
        os.system(f"cat {folder}/subdomain_enum/{PROJECT_NAME}_ASNintel.txt | grep {ASN_GREP} | tee {folder}/subdomain_enum/{PROJECT_NAME}_ASNintel.txt")
        os.system(f"rm {folder}/subdomain_enum/{PROJECT_NAME}_ASNintel_temporary.txt")
        TARGET_LIST=f"{folder}/subdomain_enum/{PROJECT_NAME}_ASNintel_temporary.txt"
        print("*" * 6 + " ASN SCAN COMPLETE "+"*" * 6)
        
    except Exception as error:
        print(f"Error: {error}\nSomething went wrong with the ASN scan. Please see config.py")
        config_and_modules.module_slack.error(error,"initial")

if __name__ == "__main__":
    start_time = config_and_modules.module_timer.start_timer()
    a = ASN
    b = config_and_modules.module_validation.output_folder()
    ASN_Amass(a,b)
    config_and_modules.module_timer.end_timer("Amass ASN",b,start_time)
