import os
import time
from config_and_modules.config import *
import config_and_modules.module_timer
import config_and_modules.module_validation
import config_and_modules.module_slack

def check_iteration(folder: str) -> int:
    list_of_count = open(f"{folder}/number_of_runs.txt","r")
    lis = list_of_count.read().split("\n")
    list_of_count.close()
    lis.pop()
    counter = int(lis[-1])

    return counter

def wait():
    time.sleep(RECURSION)