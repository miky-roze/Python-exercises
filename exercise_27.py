# Create a database with table named 'category' with 2 columns: category_id and category_name.
# Insert 3 records, commit changes and then read the table into a Python list.
# For item with category_id=2 change category_name value to 'online shop'.


import sqlite3

connectionAppDB = sqlite3.connect('DB_files/app.db')
commandsAppDB = connectionAppDB.cursor()

commandsAppDB.execute("""CREATE TABLE IF NOT EXISTS category (
    category_id INTEGER PRIMARY KEY,
    category_name TEXT NOT NULL)""")

commandsAppDB.executescript("""
INSERT INTO category (category_name) VALUES ('technology');

INSERT INTO category (category_name) VALUES ('e-commerce');

INSERT INTO category (category_name) VALUES ('gaming');
""")

connectionAppDB.commit()

categories = [category for category in commandsAppDB.execute("""SELECT * FROM category""")]

commandsAppDB.execute("""UPDATE category
SET category_name = 'online shop'
WHERE category_id = 2;""")

connectionAppDB.commit()

updatedCategories = commandsAppDB.execute('''SELECT * FROM category''').fetchall()

connectionAppDB.close()
