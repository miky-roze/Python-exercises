# Transform data from CSV file to a Python dictionary. Keys are values from 'Id' column
# and values are dictionaries containing the rest of the data in format — ColumnName: Value.

import csv

with open('CSV_files/Customers.csv', 'r', encoding='UTF-8', newline='') as csvFile:
    csvFileReader = csv.DictReader(csvFile)
    rows = tuple(csvFileReader)
    data_dict = dict()
    for row in rows:
        rowId = row['Id']
        del row['Id']
        data_dict[rowId] = row
