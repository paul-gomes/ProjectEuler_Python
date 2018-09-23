# This is problem 5 of project Euler
#
# Smallest multiple
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


import  time;

def evenlyDivisibleBy20(num):
    for i in range(2, 60, 1):
        if(num % i != 0):
            return False

    return True


#Main
stratTime = time.time()

number = 20

while( not evenlyDivisibleBy20(number)):
    number += 2

if(evenlyDivisibleBy20(number)):
    print ("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20: %d" %number)
else:
    print ("Not found!!")


endTime = time.time()
totalTime = endTime - stratTime
print("The program runtime: %d ms" %(totalTime * 1000))
