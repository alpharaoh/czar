import os
from config_and_modules.config import *

def output_folder():
    #Validate output folder
    if OUTPUT_FOLDER == "":
        try:
            folder = f"./output/{PROJECT_NAME}"
            #Check if project folder already exists
            if os.path.isdir(folder):
                pass
            else:
                os.system(f"mkdir {folder}")
        except Exception as error:
            print(f"Error: {error}\nHave you deleted your output folder?")
            exit()
    else:
        try:
            #if not, it will create use user supplied output folder
            folder = f"{OUTPUT_FOLDER}/{PROJECT_NAME}"
            if os.path.isdir(folder):
                pass
            else:
                os.system(f"mkdir {folder}")
            
        except Exception as error:
            print(f"Error: {error}\nSomething went wrong.")
            exit()

    return folder

def resolvers():
    #Validate resolvers file
    if RESOLVERS == "":
        if os.path.isfile("./config_and_modules/50resolvers.txt"):
            path_to_file = "./config_and_modules/50resolvers.txt"
        else:
            print("Something went wrong. There is no 50resolvers.txt in /config_and_modules/")
            exit()
    else:
        if os.path.isfile(RESOLVERS):
            path_to_file=RESOLVERS
        else:
            print("Something went wrong. We couldn't find your resolvers file")
            exit()

    return path_to_file

def nuclei_directory():
    #Validate output nuclei_folder and output_folder
    if NUCLEI_DIR == "":
        try:
            nuclei_folder = f"./Tools/nuclei-templates/"
            #Check if nuclei_folder already exists
            if os.path.isdir(nuclei_folder):
                pass
            else:
                print('"nuclei-templates" does not exit.')
        except Exception as error:
            print(error)
            exit()
    else:
        try:
            nuclei_folder = NUCLEI_DIR
            if os.path.isdir(nuclei_folder):
                pass
            else:
                print("Didn't find nuclei-templates directory.")
                exit()
            
        except Exception as error:
            print(f"{error}\nSomething went wrong.")
            exit()

    return nuclei_folder