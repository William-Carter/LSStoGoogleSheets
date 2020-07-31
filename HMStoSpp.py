def formatToSeconds(inp):
    """00:00:30.7650000"""
    splitInp = inp.split(":")
    splitSecond = splitInp[len(splitInp)-1].split(".")
    splitInp.pop(len(splitInp)-1)
    splitSecond[1] = "0."+splitSecond[1]
    for i in splitSecond:
        splitInp.append(i)

    weightKey = [3600, 60, 1, 1]
    finalSum = 0
    for i in range(len(splitInp)):
        finalSum += float(splitInp[i])*weightKey[i]
    return finalSum
