import csv
import json
import os

jsonFileName = 'importedDataCasesPerDay_out.json'

csvfile = open('importedDataCasesPerDay_out.csv', 'r')
jsonfile = open(jsonFileName, 'w')

fieldnames = ('DayTotal','Prediction',"TimeStamp")
reader = csv.DictReader( csvfile, fieldnames)

#skip header
reader.next()
#initialise start json file write
jsonfile.write('[')
for row in reader:
    json.dump(row, jsonfile, sort_keys=True)
    jsonfile.write(',\n')


#remove unwanted characters and write the close tag for the json file
jsonfile.seek(-1, os.SEEK_END)
jsonfile.truncate()

jsonfile.seek(-1, os.SEEK_END)
jsonfile.truncate()

jsonfile.seek(-1, os.SEEK_END)
jsonfile.truncate()

jsonfile.write(']')
jsonfile.close()

newText = ''

with open(jsonFileName) as f:
    newText = f.read().replace('"DayTotal": "', '"DayTotal":').replace('"Prediction": "', '"Prediction":').replace('",',',')
    print newText

with open(jsonFileName, "w") as f:
    f.write(newText)

print "File exported to JSON format"