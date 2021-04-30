'''
A working version of the guessing game with the guess number being between 1-10.
'''

#Initialize variables & picks a random number.
import random
guess = 0
guessCount = 0
guessNum = random.randint(1,10)

#Input & Process - User enters their guess and the guess is matched with the guessNum, if it's incorrect it will reprompt the user.
while guess != guessNum:
    try:
        guess = int(input("Guess a number between 1 and 10(inclusive). If you want to stop, type '-1': "))
        #Ends the program.
        if guess == -1:
            break
        #The user guesses incorrectly.
        elif guess != guessNum:
            print("It looks like your guess was off.")
        #Counts the amount of times it takes to guess correctly.
        guessCount += 1
    except:
        print("Invalid! Please guess a number between 1 and 10(inclusive)")

#Output - Prints if the guess was correct
if guess == guessNum:
    print(f"Congratulations! You guessed the right number! It only took you {guessCount} tries!")
