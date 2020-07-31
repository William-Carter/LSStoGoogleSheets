import xml.etree.ElementTree as ET
import json
import HMStoSpp


def populateRunsFile(splitsFile, jsonFile):
    runs = {}
    tree = ET.parse(splitsFile)
    root = tree.getroot()
    runsDic = {}
    for attempt in root[6]:
        runsDic[attempt.attrib["id"]] = {
            "started": attempt.attrib["started"], "ended": attempt.attrib["ended"]}
        for segment in root[7]:
            runIdsInSegment = []
            for k in segment[4]:
                runIdsInSegment.append(k.attrib["id"])
            if attempt.attrib["id"] in runIdsInSegment:
                runsDic[attempt.attrib["id"]][segment[0].text] = HMStoSpp.formatToSeconds(segment[4][runIdsInSegment.index(
                    attempt.attrib["id"])][1].text)

    runsDic["PB"] = {}
    runsDic["Gold"] = {}
    previousNum = 0
    for segment in root[7]:
        if not previousNum:
            runsDic["PB"][segment[0].text] = HMStoSpp.formatToSeconds(
                segment[2][0][1].text)
        else:
            runsDic["PB"][segment[0].text] = round(HMStoSpp.formatToSeconds(
                segment[2][0][1].text)-previousNum, 3)
        runsDic["Gold"][segment[0].text] = HMStoSpp.formatToSeconds(
            segment[3][1].text)
        previousNum = HMStoSpp.formatToSeconds(
            segment[2][0][1].text)
    with open(jsonFile, "w") as f:
        json.dump(runsDic, f)
