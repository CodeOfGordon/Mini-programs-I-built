#Initialize variables
import math
end = False

#Process - Function calculates the quadratic formula
def roots(a,b,c):
    #Quadratic formula, inside square root part: b^2 - 4ac
    firstPart = b**2 - 4*a*c
    
    #Quadratic formula, the rest part, positive: [-b + sqrt(b^2 - 4ac)] / 2a
    positiveSqrt = (-b + math.sqrt(firstPart)) / (2*a)
    #Quadratic formula, the rest part, negative: [-b - sqrt(b^2 - 4ac)] / 2a
    negativeSqrt = (-b - math.sqrt(firstPart)) / (2*a)
    return positiveSqrt, negativeSqrt

#Input & Output - Main program outputs the roots
while end == False:
    try:
        #Receives variables and prints the roots.
        a = float(input("Enter the 'a' variable: "))
        b = float(input("Enter the 'b' variable: "))
        c = float(input("Enter the 'c' variable: "))
        posSqrt, negSqrt = roots(a,b,c)
        print(f"The roots are {posSqrt:.2f} and {negSqrt:.2f}")
        end = True
          
    except:
        print("*"*40)
        print("The roots don't exist for this combination!\n\
Either that or you typed in the wrong thing...")
        end = False
'''
DOES NOT CURRENTLY WORK
'''
