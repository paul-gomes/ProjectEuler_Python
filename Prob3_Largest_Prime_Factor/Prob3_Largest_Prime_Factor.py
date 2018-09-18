#Problem 3
#The largest prime factor
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?

def primeFactors(num):
    factor = []
    count= 2
    while count * count <= num:
        while num % count == 0:
            factor.append(count)
            num = num/count
        count +=1

    if num > count:
        factor.append(num)
    return factor

number = input("Enter an integer to find the largest prime number: ")

primeFactorList = primeFactors(number)
print "Largest prime factor: ", primeFactorList[-1]


