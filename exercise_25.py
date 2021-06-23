# Script reads data from users.json file, than dumps them to a pickle file (users.pickle)
# Than it reads that pickle file to a list and returns the user of id=4

import json
from collections import namedtuple
import pickle


with open('JSON_files/users.json', 'r', encoding='UTF-8') as jsonFile:
    listOfUsers = json.load(jsonFile)
    User = namedtuple('User', field_names=listOfUsers[0].keys())

    users = [User(*user.values()) for user in listOfUsers]

with open('PICKLE_files/users.pickle', 'wb') as pickleFile:
    pickle.dump(users, pickleFile)

with open('PICKLE_files/users.pickle', 'rb') as pickleFile:
    usersV2 = pickle.load(pickleFile)

print(usersV2[3])
