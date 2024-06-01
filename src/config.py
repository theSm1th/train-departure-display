import os
import re

# validate platform number
def parsePlatformData(platform):
    if platform is None:
        return ""
    elif bool(re.match(r'^(?:\d{1,2}[A-D]|[A-D]|\d{1,2})$', platform)):
        return platform
    else:
        return ""

def loadConfig():
    data = {
        "journey": {},
        "api": {}
    }

    with open("config.json", "r") as file:
        file_json = json.load(file)
    
    general_json = file_json["general"]
    journey_json = file_json["journey"]
    api_json = file_json["api"]

    for item in general_json:
        if item == "hoursPattern":
            data[item] = re.compile(general_json[item])
        else:
            data[item] = general_json[item]
    
    for item in journey_json:
        if item in ["screenOnePlatform", "screenTwoPlatform"]:
            data["journey"][item] = parsePlatformData(journey_json[item]) 
        else:
            data["journey"][item] = journey_json[item]
    
    for item in api_json:
        data["api"][item] = api_json[item]

    return data
