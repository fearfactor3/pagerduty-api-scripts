import os
import json
import requests

rulesetId = "insert-id-here"

URL = "https://api.pagerduty.com/rulesets/" + rulesetId + "/rules"
HEADERS = {
    'Authorization': 'Token token=XXXXXXX', #TODO replace XXXXXX with provided token
    'Content-Type': 'application/json'
}

FILE_NAME = "serviceList.json"

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

def pdEventRules():
    """
    Send POST requests of event rules to PagerDuty.
    """
    accFile = FILE_NAME
    logOutput = ""

    accData = openJson(accFile)
    # going through accFile to generate tagging API requests

    for acc in accData["services"]:
        body = {
            "rule": {
            "id": rulesetId,
            "position": 0,
            "disabled": False,
            "catch_all": False,
            "conditions": {
            "operator": "and",
                "subconditions": [
                {
                    "operator": "contains",
                    "parameters": {
                        "value": acc["description"],
                        "path": "payload.custom_details.activation_code[0]" 
                    }
                }
            ]
        },
        "actions": {
            "route": {"value": acc["id"]}
            }
        }
    }

        #TODO uncomment this when ready to send requests
        # https://api.pagerduty.com/services"
        #
        #response = requests.post(url=URL, data=body, headers=HEADERS)
        print(json.dumps(body, indent=4, sort_keys=True))
        #print(response.text)
        print(logOutput)

pdEventRules()