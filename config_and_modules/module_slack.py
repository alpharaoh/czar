import requests
from config_and_modules.config import *
import config_and_modules.module_validation
import json

def sendErrorMessage(data):
    requests.post(SLACK_WEBHOOK_ERROR, json.dumps(data))

def sendMessage(data):
    requests.post(SLACK_WEBHOOK_FINDINGS, json.dumps(data))

def error(error,module_name):
    data = {
        'text':f'*PROJECT: {PROJECT_NAME.upper()}*\n\n*OOPS! :confused: an error was found in the module: "{module_name}"*\n\n{error}'
    }
    sendErrorMessage(data)

def nucleiCVE(cve):
    data = {
<<<<<<< HEAD
        "text":f"*CRITICAL :grinning:, [{cve}] WAS FOUND ON {PROJECT_NAME.upper()}!!*"
=======
        "text":f"*QUICK :grinning:, [{cve}] WAS FOUND ON {PROJECT_NAME.upper()}!!*"
>>>>>>> 6e7f86c9e9fde4fabfb6d5ebff0840e32bfa2ba9
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
<<<<<<< HEAD
        "text":f"*CRITICAL :grinning:, A SUBDOMAIN ON {PROJECT_NAME.upper()} CAN BE TAKEN OVER!!*"
=======
        "text":f"*QUICK :grinning:, A SUBDOMAIN ON {PROJECT_NAME.upper()} CAN BE TAKEN OVER!!*"
>>>>>>> 6e7f86c9e9fde4fabfb6d5ebff0840e32bfa2ba9
    }
    sendMessage(data)

def finished(folder):
    
    timings = open(f"{folder}/{PROJECT_NAME}_timings.txt","r").read()
    data = {
        "text":f"*FINISHED :sweat_smile: - [{PROJECT_NAME.upper()}] -*\n\n{timings}"
    }
    sendMessage(data)
