import buildSpreadSheetRequest
import extractData
import writeToSpreadsheet

# This is the string in the google docs URL after d/
googleSheetsID = ''

# This is where to put the information (Gold splits in 1 column and PB in the next)
rangeName = "Sheet1!A1:B2"

# The name of the splits file
splitsFile = ""

# Just a file to store temporary data
runsFile = "runs.json"

extractData.populateRunsFile(splitsFile, runsFile)
valuesToWrite = buildSpreadSheetRequest.buildRequest(runsFile)
writeToSpreadsheet.main(googleSheetsID, rangeName, valuesToWrite)
