# Function reads users form users.json file, creates objects of type User using namedtuple from collections module
# Returns objects in a list

import json
from collections import namedtuple


def json_to_object():
    with open('JSON_files/users.json', 'r', encoding='UTF-8') as jsonFile:
        ListOfUsers = json.loads(jsonFile.read())
        User = namedtuple('User', field_names=ListOfUsers[0].keys())

        users = [User(*user.values()) for user in ListOfUsers]

        return users


print(json_to_object())
