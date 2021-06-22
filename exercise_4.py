# Function finds the amount of all 3-digit palindromic numbers

def calculate():
    palindromicNumbers = list()

    for numb in range(100, 1000):
        if str(numb) == str(numb)[::-1]:
            palindromicNumbers.append(numb)

    return len(palindromicNumbers)


print(calculate())
