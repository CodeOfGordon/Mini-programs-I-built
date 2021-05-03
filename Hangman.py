'''
Recreates the game of hangman with the no. of guesses allowed being 10.

Some General Outlines:

-Chooses a word to be guessed from a random list

-Only allows allows letters to be entered

-Outputs the appropriate number of dashes & spaces to represent the word, and
fills it in when guessed.
When all letters have been filled in, it'll be mentioned, before ending the
program.

-If guess has already been guessed, then it'll be mentioned.

-If guess isn't correct or hasn't already been mentioned, then it'll be
be mentioned, and the number of guesses will count down from 10.
When the no. of guesses reach 0, it'll be mentioned, before saying the hangman
word and ending the program.
'''

#Function displays hangman.
def hangman():
    print("This program works as a hangman game, with 10 guessses allowed")

    #Sets the random word.
    import random
    randWords = ["DOG","ORANGUTAN","GIRAFFE","LEOPARD"]
    randWord = random.choice(randWords)
    #Sets the count of guesses.
    count = 10
    #Creates a list for letters already guessed.
    guessedLetters = []
    #Creates a variable for use in determining already guessed letters.
    notGuessed = False

    #Makes the dashes into a list, according to the no. of letters in randWord.
    dashes = list(len(randWord) * "_")
    #join funct. removes spaces in list, while adding whatever is inside the quotations.
    print(" ".join(dashes))

    '''Main Function's program'''
    randGuess = ""
    while True:
        try:
            
            #Receives input & capitalizes it.
            randGuess = input("Guess a letter: ").upper()
            #Makes randGuess an error/exception if its length is more than 1. Since letters have 1 letter.
            if len(randGuess) > 1:
                raise randGuess

            #If guess has not already been guessed.
            if randGuess not in guessedLetters:
                notGuessed = True
            #If guess has already been guessed.
            else:
                print("This letter has already been guessed!")

            #If guess hasn't already been repeated:
            if notGuessed == True:
                #Enumerate funct. assigns index to string, but doesn't convert it to a list.
                #Also here, index & value are being made as variables in for loop.
                #Code essentially searches randWord as if it was a list.
                for index,value in enumerate(randWord):

                    #If guess is correct:
                    #If value(letter in randWord) at time is equal to the guessed letter.
                    if value == randGuess:
                        print("Congrats, you guessed the correct letter!")
                        #dashes[index] = randGuess replaces the dashes with the guessed letter.
                        dashes[index] = randGuess
                        #Adds randGuess to a list of already guessed letters.
                        guessedLetters.append(randGuess)
                        ##Resets the notGuessed variable.
                        notGuessed = False
                #Reprints the dashes.
                print(" ".join(dashes))
                        
                #If guess is incorrect.
                if randGuess not in randWord:
                    #Adds randGuess to a list of already guessed letters.
                    guessedLetters.append(randGuess)
                    ##Resets the notGuessed variable.
                    notGuessed = False
                    #Counts down when a guess is wrong.
                    count -= 1
                    print(f"WRONG, you now have {count} guesses!")

            #If user has completed the word. Space between quotations are removed here since " ".join(dashes) included spaces inbetween letters.
            #In this scenario, it needs to match randWord, which doesn't have spaces.
            if "".join(dashes) == randWord:
                print("Congrats, you guessed the word!\nEnding program...")
                break
            #If no. of guesses reach 0.
            elif count <= 0:
                print(f"You have run out of guesses! The word was {randWord}")
                print("Ending program...")
                break
                
        except:
            print("Please print an actual guess!")
            


'''MAIN PROGRAM'''

hangman()





