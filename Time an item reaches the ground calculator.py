# Name: Gordon
# Date: March 24, 2021
# File Name: d1q4_timeGround.py
# Description: Calculates the time an object takes to hit the ground from a
#certain height
# Test cases: Input             Expected Output                     Pass/Fail
#           10,1                    2.14  

#Process - Function determines the time it took to hit the ground
#Formula is -4.9t^2 + vt + h = 0
def find_time(v, h):
    import math
    a = -4.9
    b = v
    c = h
    #Calculates the first part: b^2 - 4ac, positive version. 
    firstPart = b**2 - 4*a*c
    #Calculates time using [-b + sqrt(b^2 - 4ac)] / 2a, positive version.
    time = ((-b) + math.sqrt(firstPart)) / (2*a)
    #If positive version doesn't work, try negative.
    if time < 0:
        #Calculates the first part: b^2 - 4ac, negative version.
        firstPart = b**2 - 4*a*c
        #Calculates time using [-b - sqrt(b^2 - 4ac)] / 2a, negative version.
        time = ((-b) - math.sqrt(firstPart)) / (2*a)
        return time
    else:
        return time

#Input & Output - Main program
v = float(input("Enter the velocity(m/s): "))
h = float(input("Enter the height(m): "))
objectTime = find_time(v,h)
print(f"The time the object took to reach the ground was {objectTime:.2f}")

