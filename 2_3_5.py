import math


def primes():
    result = 2
    while True:
        if (math.factorial(result-1)+1) % result == 0:
            yield result
        result += 1
