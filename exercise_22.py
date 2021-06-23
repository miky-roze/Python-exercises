# Function reads file users.json and writes active users (active=true) to a active_users.json file

import json


def filter_active_users():
    activeUsers = list()
    with open('JSON_files/users.json', 'r', encoding='UTF-8') as jsonFile:
        jsonString = json.loads(jsonFile.read())
        for user in jsonString:
            if user['is_active']:
                activeUsers.append(user)

    with open('JSON_files/active_users.json', 'w', encoding='UTF-8') as jsonFile:
        jsonFile.write(json.dumps(activeUsers, indent=2))


filter_active_users()
