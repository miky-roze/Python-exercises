# Create a database with a table 'Product' that is filled with data from Products.csv file.
# Columns constraints are stored in a productConstraints variable.
# For generating SQL query use a function 'generate_sql' from previous exercise.
# Calculate the amount of records in table 'Product'.

import csv
import sqlite3
from exercise_28 import generate_sql

productConstraints = [
    'INTEGER PRIMARY KEY',
    'TEXT NOT NULL',
    'INTEGER NOT NULL',
    'INTEGER NOT NULL',
    'TEXT NOT NULL',
    'REAL NOT NULL',
    'INTEGER NOT NULL',
    'INTEGER NOT NULL',
    'INTEGER NOT NULL',
    'INTEGER NOT NULL'
]

# Opening csv file. Reading first line (columns names) and creating SQL query using generate_sql function.
# Creating a database and table.

with open('CSV_files/Products.csv', 'r', encoding='UTF-8', newline='') as csvFile:
    csvFileReader = csv.reader(csvFile)
    columnsNames = next(csvFileReader)
    SQL_query = generate_sql('Product', columnsNames, productConstraints)

    connectionToDB = sqlite3.connect('DB_files/store.db')
    cursorToDB = connectionToDB.cursor()

    cursorToDB.execute(SQL_query)

# Reading every other csv file line and inserting it into the table in the database.

    for record in csvFileReader:
        cursorToDB.execute(f"""INSERT INTO Product VALUES {tuple(record)};""")

    connectionToDB.commit()

# Calculating the amount of all records in the table and finally closing a connection.

    amountOfRecords = len(cursorToDB.execute("""SELECT * FROM Product;""").fetchall())

    connectionToDB.close()
