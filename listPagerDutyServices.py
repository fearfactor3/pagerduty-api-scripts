import json
import requests
from math import ceil

URL = 'https://api.pagerduty.com/services'
PARAMS = {
    'sort_by': 'name',
    'include[]': 'teams',
    'team_ids[]': 'insert-team-ID-here',
    'offset': '0',
    'limit': '100' #number of services retrieved per request. Maximum: 100.
}
PAYLOAD={}
HEADERS={
    'Authorization': 'Token token=xxxxxxxxxxxx', #TODO replace XXXXXX with provided token
    'Content-Type': 'application/json'
}

FILE_NAME = 'serviceList.json' #Output json file name

def findValue() -> int:
    """
    Performs calculation of the number of requests to be made, starting from zero, 
    for all services based on params['limit'] value.
    
    Returns:
        int: Total Number of requests starting from zero
    """
    PARAMS_ = PARAMS.copy()
    PARAMS_['limit'] = '1'
    PARAMS_['total'] = 'true'
    #Requests one service to know info about total number of services
    response = requests.get(url=URL, headers=HEADERS, data=PAYLOAD, params=PARAMS_)
    responseJson = response.json()
    return ( ceil(responseJson["total"]/int(PARAMS['limit'])) -1 )

def getServices():
    """
    Generates FILE_NAME json file with all services from the requests.
    """
    # Offset variable to design pagination search results
    offset = 0
    bool_ = True
    value = findValue()

    # Generate the json file pulled from all the requests
    while offset <= value:
        PARAMS['offset'] = str(offset*int(PARAMS['limit']))
        response = requests.get(url=URL, headers=HEADERS, data=PAYLOAD, params=PARAMS)
        jsonResponse = response.json()
        if bool_:
            # outputJson created to remove unneccesary end-part of jsonResponse
            outputJson = {}
            outputJson['services'] = jsonResponse['services']
            bool_ = False
        else: 
            # add the following services from the following requests
            for service in jsonResponse['services']:
                outputJson['services'].append(service)
            offset += 1

    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(outputJson, f, ensure_ascii=False, indent=4)

# Creates output file to use for createPagerDutyEventRules.py file to add event rules to PagerDuty.
getServices()