# Name: Gordon
# Date: March 24, 2021
# File Name: d2q2_quotientRemainder.py
# Description: Receives and prints the user's full name
# Test cases: Input             Expected Output                     Pass/Fail
#               7,2                 3 and 1                         Pass
#               18,5                3 and 3                         Pass
#               72,12               6 and 0                         Pass
#                0,12               0 and 0                         Pass
#                3,8                0 and 3                         Pass
#                3,0                error                           Pass

#Process - Function calculates and returns the quotient and remainder
def quot_rem(num1, num2):
    quotient = num1 // num2
    remainder = num1 % num2
    return quotient, remainder

#Input & Output - Main program
print("This program will calculate the quotient and its remainders.")
num1 = int(input("Enter the dividend: "))
num2 = int(input("Enter the divisor: "))

trueQuotient, trueRemainder = quot_rem(num1, num2)
print("The answer is " + str(trueQuotient) + ",remainder " + str(trueRemainder))
