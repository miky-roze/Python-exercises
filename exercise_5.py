# Function calculates the largest palindromic number that is a product of multiplication of two 2-digit numbers

def calculate():
    palindromicNumbers = list()

    for number in range(10, 100):
        for otherNumber in range(10, 100):
            if str(number * otherNumber) == str(number * otherNumber)[::-1]:
                palindromicNumbers.append(number * otherNumber)

    return max(palindromicNumbers)


print(calculate())
