import os
import json
import requests

URL = "https://api.pagerduty.com/services"
HEADERS = {
    'Authorization': 'Token token=XXXXXXX', #TODO replace XXXXXX with provided token
    'Content-Type': 'application/json'
}

def openJson(infile: str) -> dict:
    """
    Opens and loads JSON file.
    
    Args:
        infile (str): JSON file to be loaded
        
    Returns:
        dict: Python JSON object
    """
    with open(infile, 'r', encoding='utf-8-sig') as f:
        return json.load(f)

def pdCreateService():
    """
    Send POST requests of the services to PagerDuty
    """

    # exported Account Match tool to get the data
    accFile = "infrastructures.json"
    logOutput = ""

    accData = openJson(accFile)
    #going through accFile to generate tagging API requests
    for acc in accData["infrastructures"]:
        body = {
            "service": {
                "id": "null",
                "summary": "null",
                "type": "service",
                "self": "null",
                "html_url": "null",
                "name": acc["Client Name"],
                "description": acc["Activation Code"],
                "auto_resolve_timeout": 14400,
                "acknowledgement_timeout": 1800,
                "created_at": "<datetime>",
                "status": "active",
                "escalation_policy": {
                    "id": "insert-Id-Here",
                    "type": "escalation_policy_reference"
            }
        }
    }

        #TODO uncomment this when ready to send requests
        # "https://api.pagerduty.com/services"
        #
        #response = requests.request("POST", url=URL, json=body, headers=HEADERS)
        #print(response.text)
        print(logOutput)

pdCreateService()