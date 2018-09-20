
# This is a project euler problem 4 Largest palindrome product
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


#reverses the string

import time

def reverse( number):
    num = str(number)
    return num[::-1]



#checks if it is a palindrome

def isPalindrome (number):
    if (str(number) == reverse(number)):
        return True
    else:
        return False



#Main

#strat time

stratTime = time.time()

largestPalindrome = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):

        if( isPalindrome(i*j) and (i*j) > largestPalindrome):
            largestPalindrome = i*j


print ("largest palindrome made from the product of two 3-digit numbers: " + str(largestPalindrome))


#End time

endTime = time.time()
totalTime = endTime - stratTime

print("The progrm runtime: %d ms" % (totalTime*1000))