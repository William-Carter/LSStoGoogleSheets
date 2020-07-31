import json


def buildRequest(jsonName):
    with open(jsonName, "r") as f:
        runs = json.load(f)
    requestValues = []
    pbValues = []
    goldValues = []
    for key in runs["PB"]:
        pbValues.append(runs["PB"][key])
    for key in runs["Gold"]:
        goldValues.append(runs["Gold"][key])

    requestValues = [goldValues, pbValues]
    requestValuesFormat = list(zip(*requestValues))
    return requestValuesFormat
