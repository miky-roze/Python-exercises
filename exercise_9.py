# Function checks if given number is palindromic in both binary and decimal systems

def is_palindrome(number):
    binNumber = bin(number)

    if str(number) == str(number)[::-1] and binNumber[2:] == binNumber[-1: 1: -1]:
        return True
    else:
        return False


# is_palindrome(7)
