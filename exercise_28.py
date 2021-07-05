# Create a function that receives a table name, a list/tuple with table columns and a list with columns constraints.
# The function generates SQL query that would create such a table in a database. The query should have indentation for
# better readability.

def generate_sql(tableName: str, columns: (list, tuple), constraints: list):
    columnNamesWithConstraints = ['\n\t' + ' '.join(item).rstrip() for item in zip(columns, constraints)]
    return f"CREATE TABLE IF NOT EXISTS {tableName} ({', '.join(columnNamesWithConstraints)}\n);"


# print(generate_sql('Product', ('Id', 'ProductName', 'SupplierId', 'CategoryId', 'Quantity', 'UnitPrice'), \
# ['INTEGER PRIMARY KEY', '', 'NOT NULL', '']))
# print(generate_sql('Customer', ('Id', 'FirstName'), ['INTEGER PRIMARY KEY', 'TEXT NOT NULL']))
