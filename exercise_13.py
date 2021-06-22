# Function compresses the number according to this formula: 'number..'. Dots indicate the amount of occurrences in a row
# Example: 111155003 ----> '1....5..0..3.'

from itertools import groupby


def compress(number):

    compressedNumber = list()

    for k, g in groupby(str(number)):
        compressedNumber.append(str(k) + "." * len(list(g)))

    return ''.join(compressedNumber)


print(compress(111155003))
