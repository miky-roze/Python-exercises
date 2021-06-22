# Function calculates if given natural number is a prime number (True) or not (False)


def is_prime(number):
    numberDivisors = list()

    i = 2
    while i ** 2 <= number:
        if number % i == 0:
            numberDivisors.append(i)

        i += 1

    if len(numberDivisors) == 0:
        return True
    else:
        return False


# print(is_prime(7919))
# print(is_prime(15))
# print(is_prime(6389))
# print(is_prime(104923))
