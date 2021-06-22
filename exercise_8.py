# Function calculates n-th prime number using function is_prime from exercise_7

from exercise_7 import is_prime


def prime_number(n):
    primeNumbers = list()
    for potentialPrimeNumber in range(2, 10000000):
        if is_prime(potentialPrimeNumber):
            primeNumbers.append(potentialPrimeNumber)
            if len(primeNumbers) == n:
                return primeNumbers[n-1]


print(prime_number(100))
