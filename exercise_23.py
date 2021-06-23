# Function converts JSON data (users.json) to CSV data (users.csv)

import json
import csv


def json_to_csv():
    # jsonData = list()
    with open('JSON_files/users.json', 'r', encoding='UTF-8') as jsonFile:
        jsonData = json.loads(jsonFile.read())

    with open('CSV_files/users.csv', 'w', encoding='UTF-8') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(jsonData[0].keys())
        for user in jsonData:
            csvWriter.writerow(user.values())


json_to_csv()
