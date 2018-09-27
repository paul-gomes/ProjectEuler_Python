

# This is problem 7 of Project Euler
#
# 10001st prime
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import math
import time


def isPrime(number):
    rangeTo = int(math.sqrt(number)) + 1
    for i in range(2, rangeTo):
        if(number % i) == 0:
            return False
    return True


def primeNumbers():
    prime10001st = 2
    primeCount = 1
    number = 3

    while(primeCount < 10001):
        if isPrime(number):
            prime10001st = number
            primeCount += 1
        number += 2
    return prime10001st


startTime = time.time()
print("The 10001st time: {0}".format(primeNumbers()))
endTime = time.time()
print("The project runtime: %d ms." %((endTime- startTime) * 1000))



