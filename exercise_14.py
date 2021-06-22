# Function decompresses compressed numbers from exercise 12
# Example: '14_52_02_31' ----> 111155003

from exercise_12 import compress


def decompress(compNumber):
    compNumber = compNumber.split(sep='_')
    decompNumber = list()

    for element in compNumber:
        decompNumber.append(element[0] * int(element[1]))

    return int(''.join(decompNumber))


compressedNumber = compress(111155003)
print(compressedNumber)
decompressedNumber = decompress(compressedNumber)
print(decompressedNumber, type(decompressedNumber))
