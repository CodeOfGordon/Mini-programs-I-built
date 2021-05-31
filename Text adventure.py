'''
Treasure cave - text adventure

#PHASE 1
start outside cave
-go inside cave, or don't

PHASE 2
travel inside cave, navigate through
meet 3 tunnels
-one leads directly to troll
-other you fight a goblin, then reach troll
-last you get hit by a trap, then reach troll

PHASE 3
end up at treasure guarded by troll
'''

#Function brings up goblin encounter, found in middle tunnel.
def goblinEncounter():
    #--Character stats--
    global hp_char
    global dmg_char
    global heavy_dmg_char

    #Goblin stats
    global hp_goblin
    global dmg_goblin

    global end
    import random
    
    print("You encounter a goblin!")
    while True:
        print("What will you do?")
        #Stats
        print(f"Goblin - HP {hp_goblin}")
        print("")
        print(f"You - HP {hp_char}")

        #Attack
        print("\n\
    a - Normal attack \n\
        -Does 2 DMG \n\
        -Low fail chance \n\
    b - Heavy attack \n\
        -Does 5 DMG \n\
        -High fail chance \n\
    c - Run")

        choice = input("")
        
        #Normal Damage
        if choice == 'a':
            dice = random.randint(1,7)
            if dice != 6:
              print("Direct hit!")
              hp_goblin -= dmg_char
            else:
                print("You slip on an ant and miss!")
        #Heavy Damage
        elif choice == 'b':
            dice = random.randint(1,7)
            if dice != 1 or 3 or 5:
              print("Direct hit!")
              hp_goblin -= heavy_dmg_char
            else:
                print("You slip on an ant and miss!")
        #Run
        elif choice == 'c':
            print("You try to run but you run into a wall!")

        #Fight ends check
        if hp_goblin <= 0:
            print("You slaughtered a goblin in its home, congrats!")
            break
        elif hp_char <= 0:
            print("You succumb to the goblin...")
            end = True
            break

        print("")
#GOBLIN'S TURN
        print("The goblin strikes!")
        hp_char -= dmg_goblin

        #Fight ends check
        if hp_goblin <= 0:
            print("You slaughtered a goblin in its home, congrats!")
            break
        elif hp_char <= 0:
            print("You succumb to the goblin...")
            end = True
            break

#Function brings up a trap encounter, found in last tunnel
def trapEncounter():
    global hp_char
    print("A giant log suddenly swings at you! You lost half of your HP!")
    hp_char -= 5
    
#Function brings up a troll encounter, found in last phase
def trollEncounter():
    #--Character stats--
    global hp_char
    global dmg_char
    global heavy_dmg_char

    #Troll stats
    global hp_troll
    global dmg_troll

    global end
    import random


    print("You encounter the final boss, the troll!")
    while True:
        print("What will you do?")
        #Stats
        print(f"Troll - HP {hp_troll}")
        print("")
        print(f"You - HP {hp_char}")

        #Attack
        print("\n\
    a - Normal attack \n\
        -Does 2 DMG \n\
        -Low fail chance \n\
    b - Heavy attack \n\
        -Does 5 DMG \n\
        -High fail chance \n\
    c - Run")

        choice = input("")
            
        #Normal Damage
        if choice == 'a':
            dice = random.randint(1,7)
            if dice != 6:
              print("Direct hit!")
              hp_troll -= dmg_char
            else:
                print("You slip on an ant and miss!")
        #Heavy Damage
        elif choice == 'b':
            dice = random.randint(1,7)
            if dice != 1 or 3 or 5:
              print("Direct hit!")
              hp_troll -= heavy_dmg_char
            else:
                print("You slip on an ant and miss!")
        #Run
        elif choice == 'c':
            print("You try to run but you run into a wall!")

        #Fight ends check
        if hp_troll <= 0:
            print("You slaughtered a troll in its home, congrats!")
            break
        elif hp_char <= 0:
            print("You succumb to the troll...")
            end = True
            break

        print("")
#TROLL'S TURN
        print("The troll strikes!")
        hp_char -= dmg_troll

        #Fight ends check
        if hp_troll <= 0:
            print("You slaughtered a troll in its home, congrats!")
            break
        elif hp_char <= 0:
            print("You succumb to the troll...")
            end = True
            break
    
    





'''MAIN PROGRAM'''
#Variables
tunnel_1 = False
tunnel_2 = False
tunnel_3 = False
end = False
import time

#--Character stats--
hp_char = 10
dmg_char = 2
heavy_dmg_char = 5

#Goblin stats
hp_goblin = 5
dmg_goblin = 1

#Troll stats
hp_troll = 10
dmg_troll = 3



while True:
#PHASE 1
    print("You travel through the forest and come across a cave! What do you do?\n\
    a - You go inside\n\
    b - Your tummy hurts so you leave\n")

    findCave_choice = input("")
    #Error check.
    if len(findCave_choice) == 1 and findCave_choice.isalpha() == True:
        if findCave_choice == 'a':
            print("You man up and go into the cave...")
        elif findCave_choice == 'b':
            print("You tuck your tail between your legs and go home...")
            break
    #Error check.
    else:
        print("Choose an actual choice!")


#PHASE 2
    print("You travel deep into the cave, and come across a tunnel that splits into 3!\n\
a - You go for the first tunnel\n\
b - You go for the middle tunnel\n\
c - You go for the last tunnel\n\
d - You chicken out and head for the exit\n")

    tunnel_choice = input("")

    if len(tunnel_choice) == 1 and tunnel_choice.isalpha() == True:
        if tunnel_choice == 'a':
            print("You head for the first tunnel...")
            tunnel_1 = True
        elif tunnel_choice == 'b':
            print("You head for the middle tunnel...")
            tunnel_2 = True
        elif tunnel_choice == 'c':
            print("You head for the last tunnel...")
            tunnel_3 = True
        elif tunnel_choice == 'd':
            print("You dash for the exit and head home...")
    else:
        print("Choose an actual choice!")


    #PHASE 2 - FIRST TUNNEL
    if tunnel_1 == True:
        print("You walked for hours and hours...")
        time.sleep(3)
    #PHASE 2 - MIDDLE TUNNEL
    elif tunnel_2 == True:
        print("You travel for a little while, until suddenly...")
        goblinEncounter()
        time.sleep(3)
    #PHASE 2 - LAST TUNNEL
    elif tunnel_3 == True:
        print("You travel for a little while, until suddenly...")
        trapEncounter()
        time.sleep(3)
        

    #If you succumbed to a fight
    if end == True:
        break


#PHASE 3
    print("\nYou continuously walk until you see light in the distance.\n\
You keep walking until...\n")
    time.sleep(3)
    trollEncounter()

    #If you succumbed to a fight
    if end == True:
        break
    #If you win.
    else:
        print("Congrats! You found a large box of treasure! The End")
        break






