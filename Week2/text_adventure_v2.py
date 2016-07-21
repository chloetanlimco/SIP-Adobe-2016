done = False
dead = False
start = '''
You wake up one morning and find that you aren’t in your bed; you aren’t even in your room.
You’re in the middle of a giant maze.
A sign is hanging from the ivy: “You have one hour. Don’t touch the walls.”
There is a hallway to your right and to your left.
'''

user_input = 0
while (user_input != "left" and user_input != "right"):
    print("Type 'left' to go left or 'right' to go right.")
    user_input = input()
    if user_input == "left":
        print("You decide to go left and you meet a troll. Type 'fight' to fight the troll or 'back' to go backwards.")
        while (user_input != "fight" and user_input != "back"):
            user_input = input()
            if user_input == "fight":
                print("You decide to fight the troll. You receive a blow to the head. Type 'continue' to fight the troll or 'run' to go backwards.") 		
                while (user_input != "continue" and user_input != "run"):
                    user_input = input()
                    if user_input == "continue":
                        print("The troll finishes you off and begins plans to have you for dinner.")
                        dead = True
                    elif user_input == "run":
                        print("You turn back and reach a fork in the maze. Type 'left' to go left or 'right' to go right.")
                        while (user_input != "left" and user_input != "right"):
                            user_input = input()
                            if user_input == "left":
                                print("You meet a sphinx who asks if you want to answer a riddle. Type 'attempt' to engage or 'back' to go backwards.")
                                while (user_input != "attempt" and user_input != "back"):
                                    user_input = input()
                                    if user_input == "attempt":
                                        print("What is something that everyone does, but not together?")
                                        if user_input == "dream":
                                            print("The sphinx congratulates you! You have now exited the maze.")
                                        else:
                                            print("Unfortunately, you have answered incorrectly. The sphinx plans for your immediate demise.")
                                    elif user_input == "back":
                                        print("Type 'left' to go left or 'right' to go right")
                                        while (user_input != "left" and user_input != "right"):
                                            user_input = input()
                                            if user_input == "left":
                                                print ("You come across a river. Type 'swim' to swim across or 'stay' to sit at the banks of the river.")
                                                while (user_input != "swim" and user_input != "stay"):
                                                    user_input = input()
                                                    if user_input == swim:
                                                        print ("You fail to swim across the river, and the fast current pulls you downstream.")
                                                    elif user_input == stay:
                                                        print ("You have a picnic and dream of getting out.")
                            elif user_input == "right":
                                print("You exit the maze")
                                done = True
            elif user_input == "back":
                print ("You continue backwards until you arrive at where you started. Type 'left' to go back to the troll or 'right' to turn right.")
                while (user_input != "left" and user_input != "right"):
                    user_input = input()
                    if user_input == "left":
                        print("The troll recognizes you and finishes you off immediately.")
                        dead = True
                    elif user_input == "right":
                        print("You choose to go right and eventually reach a fork in the maze. Type 'left' to go left or 'right' to go right.")
                        user_input = 0
                        while (user_input != "left" and user_input != "right"):
                            user_input = input()
                            if user_input == "left":
                                print("You meet a sphinx who asks you if you want to answer a riddle. Type 'attempt' to engage or 'back' to go backwards.")
                                while (user_input != "attempt" and user_input != "back"):
                                    user_input = input()
                                    if user_input == "attempt":
                                        print("What loses its head in the morning and gets it back at night?")
                                        user_input = input()
                                        if user_input == "pillow" or "a pillow":
                                            print("The sphinx congratulates you! You have now exited the maze.")
                                        else:
                                            print("Unfortunately, you have answered incorrectly. The sphinx plans for your immediate demise.")
                                    elif user_input == "back":
                                        print("You reach another fork in the road. Type 'left' to go left or 'right' to go right.")
                                        while (user_input != "left" and user_input != "right"):
                                            user_input = input()
                                            if user_input == "left":
                                                print("You turn left and fall into a bottomless pit.")
                                                dead = True
                                            elif user_input == "right":
                                                print("You happen upon a giant's cave. Do you go in? Type 'go in' to enter or 'return' to go backwards.")
                                                while (user_input != "go in" and user_input != "return"):
                                                    user_input = input()
                                                    if user_input == "go in":
                                                        print ("You encounter a sleeping giant, who, upon recognizing your presence, kills you on sight.")
                                                        dead = True 
                                                    elif user_input == "return":
                                                        print ("You return to the fork and turn left. Unfortunately, you fall into a bottomless pit.")
                                                        dead = True
                            elif user_input == "right":
                                print("You find the exit!")
    elif user_input == "right":
        print("You decide to go right and see a lion. Do you turn around? Type 'lion' to keep going forward or 'back' to return to your starting position.")
        while (user_input != "back" and user_input != "lion")
            user_input = input()
            if user_input == "back":
                print("You meet a troll, who challenges you to a fight. Caught between a lion and a troll, you accept the challenge and inevitably fail.")
                dead = True
            elif user_input == "lion":
                print("You narrowly escape the lion's paws. You hit a dead end. Do you scale the walls or turn back? Type 'scale' to climb or 'back' to go backwards.")
                user_input = 0
                while user_input != ("scale" and user_input != "back"):
                    user_input = input()
                    if user_input == "scale":
                        print("You successfully get to the top, but you lose your balance and fall to your death.")
                        dead = True
                    elif user_input == "back":
                        print("The lion, sensing your hestitation, captures you. Status: as good as dead.")
                        dead = True

if dead == True:
    print("End.")
