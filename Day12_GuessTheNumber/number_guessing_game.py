import random

random_num=random.choice(range(1,101))

print("******************Welcome to play a guessing number game ******************\n")
print("I'm thinking of a number between 1 to 100.")
level=input("what level you want to play ?easy or hard ?: ").lower()

def life_lvl():
    if level=="easy":
        life=10
    elif level=="hard":
        life=5
    else:
        print("Enter a correct input")
    
    return life
        
    
#print(random_num)  #showing number

def find_number():
    if guess == random_num:
        print(f"\nyou are win , the guessed number is {random_num} ")
        global lifes
        lifes=0
        
    elif guess < random_num:
        print("too low")
        
    elif guess > random_num:
        print("too high ")
        
    else:
        print("enter valid input")


lifes=life_lvl()
while  lifes>0:

    print(f"\nyou have remaining {lifes} attempts to play")
    guess=int(input("Guess the number: "))
    find_number()
    
    
    lifes-=1
    
if lifes <=1:
    print("\nyou lose , bnetter luck next time ")





    
 
                                                    
