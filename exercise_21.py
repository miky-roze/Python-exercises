# Function reads binary numbers from binary.txt file and returns them as a decimal numbers in a list

def binary_to_int():
    with open('TXT_files/binary.txt', 'r', encoding='UTF-8') as file:
        return [int(binNumber, 2) for binNumber in file.readlines()]


print(binary_to_int())
