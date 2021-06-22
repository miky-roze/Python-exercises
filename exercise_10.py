# Function returns all 3-digit numbers that are palindromic in both binary and decimal systems.
# Using is_palindrome for exercise 9

from exercise_9 import is_palindrome


def calculate():
    threeDigitPalindromes = list()
    for number in range(100, 1000):
        if is_palindrome(number):
            threeDigitPalindromes.append(number)

    return threeDigitPalindromes


print(calculate())
