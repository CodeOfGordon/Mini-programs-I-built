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
