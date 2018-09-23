# This is problem 6 of Project euler
#
# Sum square difference
#
# The sum of the squares of the first ten natural numbers is,
#
# 1^2 + 2^2 + ... + 10^2 = 385 The square of the sum of the first ten natural numbers is,
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


# The formula for 1 + 2 + 3 + .... + n = n(n+1) / 2
# The formula for 1 ^ 2 + 2 ^ 2 + 3 ^ 2 + ...... + n ^ 2 = n(2n+1)(n+1) / 6

import time

def sumOfSquare(n):
    sum = long((n * (2*n + 1) *(n + 1)) / 6)
    return sum

def squareOfSum(n):
    sum = (n * (n+1))/ 2
    return sum*sum


#Main

startTime = time.time();
print("The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum %d" %(sumOfSquare(100) - squareOfSum(100)))
endTime = time.time();
print("The project runtime: %d ms." %((endTime- startTime) * 1000))
