import os
import time
import datetime
from config_and_modules.config import *

def start_timer():
    #Start timer
    start_time = datetime.datetime.now().time().strftime('%H:%M:%S')
    return start_time

def end_timer(name,folder,start_time):
    #Work out elapsed time
    end_time = datetime.datetime.now().time().strftime('%H:%M:%S')
    total_time=(datetime.datetime.strptime(end_time,'%H:%M:%S') - datetime.datetime.strptime(start_time,'%H:%M:%S'))

    print(f"{name} complete - [Finished in: {total_time}]")

    #Adding elapsed time to file
    timings_file = open(f"{folder}/{PROJECT_NAME}_timings.txt", "a")
    timings_file.write(f"{name}: {total_time}\r\n")
    timings_file.close()