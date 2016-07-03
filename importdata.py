import urllib2
import json
import csv
import sys
import time

myTime = time.strftime("%y-%m-%d")


# retrieve JSON data from URL

url = "http://104.197.190.158/elen7046/cases/perday/prediction/1998-01-01/"+myTime
data = urllib2.urlopen(url).read()
data = json.loads(data)

print ('retrieved JSON data')
#print data

fieldnames = ['DayTotal','Date']

# open file to write csv data
file = open('importedDataCasesPerDay.csv', 'wb+')
f = csv.writer(file)

# Extract JSON Keys
#ISSUE: Key order seems reversed sometimes.
#Using hardcoded key fieldnames
myjson = data
keys = {}
for i in myjson:
    for k in i.keys():
        keys[k] = 1

#write JSON file to CSV
mycsv = csv.DictWriter(file, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
mycsv.writeheader()

#write nupic fieldFormatting entries
f.writerow(['int',' datetime'])
f.writerow(['T',''])

for row in myjson:
    mycsv.writerow(row)

print 'Completes writing csv file'
