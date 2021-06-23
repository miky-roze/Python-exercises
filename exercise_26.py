# Script creates SQL database (app.db) with table 'customers' with columns: customer_id, first_name, last_name, email.
# Than adds two records, commits changes, reads the database and closes the connection

import sqlite3

connectionAppDB = sqlite3.connect('DB_files/app.db')
commandsAppDB = connectionAppDB.cursor()

commandsAppDB.execute("""CREATE TABLE IF NOT EXISTS customer (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT)""")

commandsAppDB.execute("""INSERT INTO customer (first_name, last_name, email) VALUES (
    'John', 'Smith', 'john.smith@esmartdata.org')""")
commandsAppDB.execute("""INSERT INTO customer (first_name, last_name, email) VALUES (
    'Mike', 'Doe', 'mike.doe@esmartdata.org')""")

connectionAppDB.commit()

customers = [customer for customer in commandsAppDB.execute("""SELECT * FROM customer""")]

print(customers)

connectionAppDB.close()
