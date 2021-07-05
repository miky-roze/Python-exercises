# Read data from Customers.csv file and create a sorted list with unique countries.

import csv

with open('CSV_files/Customers.csv', 'r', encoding='UTF-8', newline='') as csvFile:
    csvFileReader = csv.reader(csvFile)
    columnNames = next(csvFileReader)
    countryIndex = columnNames.index('Country')
    rows = tuple(csvFileReader)
    uniqueCountries = sorted(set([record[countryIndex] for record in rows]))
    # print(uniqueCountries)
