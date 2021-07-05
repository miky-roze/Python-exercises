# Transform data from Customers.csv file into Customers.json file

import csv
import json

data_dict = dict()

with open('CSV_files/Customers.csv', 'r', encoding='UTF-8', newline='') as csvFile:
    csvFileReader = csv.DictReader(csvFile)
    rows = tuple(csvFileReader)

    for row in rows:
        rowId = row['Id']
        del row['Id']
        data_dict[rowId] = row

with open('JSON_files/Customers.json', 'w', encoding='UTF-8') as jsonFile:
    json.dump(data_dict, jsonFile, indent=4)
