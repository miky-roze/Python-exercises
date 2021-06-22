# Function calculates GCD (Greatest Common Divisor) of 2 numbers

def greatest_common_divisor(number, otherNumber):
    numberDivisors = set()
    otherNumberDivisors = set()

    for num in range(1, number + 1):
        if number % num == 0:
            numberDivisors.add(num)

    for num in range(1, otherNumber + 1):
        if otherNumber % num == 0:
            otherNumberDivisors.add(num)

    return max(numberDivisors.intersection(otherNumberDivisors))


print(greatest_common_divisor(64, 128))
