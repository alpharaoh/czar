import requests
from config_and_modules.config import *
import config_and_modules.module_validation
import json

def sendMessage(data):
    requests.post(SLACK_WEBHOOK, json.dumps(data))

def error(error,module_name):
    data = {
        'text':f'*PROJECT: {PROJECT_NAME.upper()}*\n\n*OOPS! :confused: an error was found in the module: "{module_name}"*\n\n{error}'
    }
    sendMessage(data)

def nucleiCVE(cve):
    data = {
        "text":f"*QUICK :grinning:, [{cve}] WAS FOUND ON {PROJECT_NAME.upper()}!!*"
    }
    sendMessage(data)

def nucleiFiles(fileName):
    data = {
        "text":f"*QUICK :grinning:, [{fileName}] WAS FOUND ON {PROJECT_NAME.upper()}!!*"
    }
    sendMessage(data)

def nucleiVulnerabilities(vuln):
    data = {
        "text":f"*QUICK :grinning:, [{vuln}] WAS FOUND ON {PROJECT_NAME.upper()}!!*"
    }
    sendMessage(data)

def nucleiSubdomainTakeover():
    data = {
        "text":f"*QUICK :grinning:, A SUBDOMAIN ON {PROJECT_NAME.upper()} CAN BE TAKEN OVER!!*"
    }
    sendMessage(data)

def finished(folder):
    
    timings = open(f"{folder}/{PROJECT_NAME}_timings.txt","r").read()
    data = {
        "text":f"*FINISHED :sweat_smile: - [{PROJECT_NAME.upper()}] -*\n\n{timings}"
    }
    sendMessage(data)
