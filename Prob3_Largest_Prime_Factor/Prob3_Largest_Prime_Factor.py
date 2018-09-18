#Problem 3
#The largest prime factor
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?


# Prime number is any number that is only divisible by 1 and itself
# To find the prime factorization, we need to break the number to its prime factors
# "Factors" are the numbers you multiply together to get another number
# Can we divide 147 exactly by 2?
# 147 ÷ 2 = 73½
# No it can't. The answer should be a whole number, and 73½ is not.
# Let's try the next prime number, 3:
# 147 ÷ 3 = 49
# That worked, now we try factoring 49, and find that 7 is the smallest prime number that works:
# 49 ÷ 7 = 7
# And that is as far as we need to go, because all the factors are prime numbers.
# 147 = 3 × 7 × 7


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


