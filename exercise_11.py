# Function compresses the number according to this formula: (number, how_many_in_a_row)
# Example: 111155003 ----> [(1, 4), (5, 2), (0, 2), (3, 1)]

from itertools import groupby


def compress(number):

    compressedNumber = list()

    for k, g in groupby(str(number)):
        compressedNumber.append((k, list(g).count(k)))

    return compressedNumber


print(compress(111155003))
