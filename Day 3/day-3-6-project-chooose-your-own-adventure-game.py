print('Welcome to Treasure Island.\nYour mission is to find the treasure.')
direction = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right' ")
if direction == 'right':
    next = input("You've come to the lake. There is an island in the middle of the lake. "
                 "Type 'wait' to wait for a boat. Type 'swim' to swim across'")
    if next == 'wait':
        stage3 = input("You arrive at the island unharmed. There is a house with 3 doors. "
                       "One red, one yellow and one blue. Which colour do you choose?")
        if stage3 == 'yellow':
            print("You found the treasure! You Win!")
        elif stage3 == 'red':
            print("It's a room full of fire. Game Over.")
        elif stage3 == 'blue':
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print('You fell into a hole. Game Over.')
