#Initialize variables
import math

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
<<<<<<< Updated upstream
while end == False:
=======
print("This program will calculate the roots, please type 'done' when done")
while True:
    A = input("Enter the 'a' variable: ")
    B = input("Enter the 'b' variable: ")
    C = input("Enter the 'c' variable: ")
    #If the keyword 'done' is detected, then the program stops.
    if A == "done" or B == "done" or C == "done":
        print("Keyword detected\nEnding program...")
        break
    
    #Converts variables to floating value and prints the roots.
>>>>>>> Stashed changes
    try:
        a = float(A)
        b = float(B)
        c = float(C)
        posSqrt, negSqrt = roots(a,b,c)
        print(f"The roots are {posSqrt:.2f} and {negSqrt:.2f}")
        break
    
    except:
        print("*"*40)
        print("The roots don't exist for this combination!\n\
Either that or you typed in the wrong thing...")
<<<<<<< Updated upstream
        end = False
'''
DOES NOT CURRENTLY WORK
'''
=======
        continue
>>>>>>> Stashed changes
