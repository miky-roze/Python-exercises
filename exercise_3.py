# Function calculates the prime factorization of given number

def calculate(number):
    if not isinstance(number, (int, float)):
        raise TypeError(f"The argument must be of type int or float. NOT  {type(number)}")

    def primeNumbersGenerator():
        for potentialPrimeNumber in range(2, 1000000):
            factors = []
            for divisor in range(2, 1000000):
                if potentialPrimeNumber % divisor == 0:
                    factors.append(divisor)
                elif len(factors) > 2 or divisor > potentialPrimeNumber:
                    break

            if len(factors) == 1:
                yield potentialPrimeNumber

    primeFactors = list()
    primeNumbers = primeNumbersGenerator()
    tmpNumber = number

    while tmpNumber != 1:
        divisor = next(primeNumbers)
        while tmpNumber % divisor == 0:
            tmpNumber = tmpNumber / divisor
            primeFactors.append(divisor)

    return primeFactors


print(calculate(10469))
