# Function calculates the sum of all even elements of Fibonacci sequence that are less than 1 million

def calculate(threshold=1000000):
    fibonacciNumbers = [0, 1]

    while True:

        nextFiboNumber = fibonacciNumbers[-1] + fibonacciNumbers[-2]

        if nextFiboNumber < threshold:
            fibonacciNumbers.append(nextFiboNumber)
        else:
            break

    evenFiboNumbers = [numb for numb in fibonacciNumbers if numb % 2 == 0]

    return sum(evenFiboNumbers)


print(calculate())
