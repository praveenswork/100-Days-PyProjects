print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")

rout=input('You are at a crossroad. Where do you want to go? Type "left" or "right"\n')

if rout=="left":
    lake=input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
    if lake=="wait":
        island=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        if island=="red":
            print("It's a room full of fire. Game Over.")
        elif island=="yellow":
            print("You found the treasure! You Win!")
        elif island=="blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
        
        
    else:
        print("You get attacked by an angry trout. Game Over.")
        
else:
    print("You fell into a hole. Game Over.")
    
