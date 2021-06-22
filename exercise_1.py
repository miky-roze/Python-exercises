# Function calculates the sum of all natural numbers that are less than 100 and are divided by 5 or 7

def calculate():
    numbersDevidedBy7Or5 = [numb for numb in range(100) if numb % 5 == 0 or numb % 7 == 0]

    return sum(numbersDevidedBy7Or5)


print(calculate())
