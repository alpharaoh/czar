import requests
from config_and_modules.config import *
import config_and_modules.module_validation
import json

def sendErrorMessage(data):
    requests.post(SLACK_WEBHOOK_ERROR, json.dumps(data))

def sendMessage(data):
    requests.post(SLACK_WEBHOOK_FINDINGS, json.dumps(data))

def sendSubdomainsMessage(data):
    requests.post(SLACK_WEBHOOK_SUBDOMAINS, json.dumps(data))

def error(error,module_name):
    data = {
        'text':f'*PROJECT: {PROJECT_NAME.upper()}*\n\n*OOPS! :confused: an error was found in the module: "{module_name}"*\n\n{error}'
    }
    sendErrorMessage(data)

def smuggler(domain):
    data = {
        "text":f"*CRITICAL :grinning:* \n HTTP REQUEST SMUGGLING ON {domain}"
    }
    sendMessage(data)

def newSubdomains(subdomain_file):
    data = {
        "text":f"*NEW SUBDOMAINS :grinning:* \n {subdomain_file}"
    }
    sendSubdomainsMessage(data)

def nucleiCVE(cve):
    data = {
        "text":f"*CRITICAL :grinning:, [{cve}] WAS FOUND ON {PROJECT_NAME.upper()}!!*"
    }
    sendMessage(data)

def nucleiDNS(dns):
    data = {
        "text":f"*QUICK :grinning:, DNS ISSUE WAS FOUND ON {PROJECT_NAME.upper()}!!* {dns}"
    }
    sendMessage(data)

def nucleiGeneric(dns):
    data = {
        "text":f"*QUICK :grinning:, GENERIC ISSUE WAS FOUND ON {PROJECT_NAME.upper()}!!* {dns}"
    }
    sendMessage(data)

def nucleiSecurityMisconfig(dns):
    data = {
        "text":f"*QUICK :grinning:, SECURITY MISCONFIG ISSUE WAS FOUND ON {PROJECT_NAME.upper()}!!* {dns}"
    }
    sendMessage(data)

def nucleiTechnologies(dns):
    data = {
        "text":f"*QUICK :grinning:, TECHNOLOGY ISSUE WAS FOUND ON {PROJECT_NAME.upper()}!!* {dns}"
    }
    sendMessage(data)

def nucleiFiles(fileName):
    data = {
        "text":f"*QUICK :grinning:, [{fileName}] WAS FOUND ON {PROJECT_NAME.upper()}!!* (FILE)"
    }
    sendMessage(data)

def nucleiVulnerabilities(vuln):
    data = {
        "text":f"*QUICK :grinning:, [{vuln}] WAS FOUND ON {PROJECT_NAME.upper()}!!* (VULNERABILITY)"
    }
    sendMessage(data)

def nucleiSubdomainTakeover():
    data = {
        "text":f"*CRITICAL :grinning:, A SUBDOMAIN ON {PROJECT_NAME.upper()} CAN BE TAKEN OVER!!*"
    }
    sendMessage(data)

def finished(folder):
    
    timings = open(f"{folder}/{PROJECT_NAME}_timings.txt","r").read()
    data = {
        "text":f"*FINISHED :sweat_smile: - [{PROJECT_NAME.upper()}] -*\n\n{timings}"
    }
    sendMessage(data)
