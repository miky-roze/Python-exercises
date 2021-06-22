# Function compresses the number according to this formula: 'number_how-many-in-a-row)'
# Example: 111155003 ----> '14_52_02_31'

from itertools import groupby


def compress(number):

    compressedNumber = list()

    for k, g in groupby(str(number)):
        compressedNumber.append(str(k) + str(len(list(g))))

    return '_'.join(compressedNumber)


# print(compress(111155003))
