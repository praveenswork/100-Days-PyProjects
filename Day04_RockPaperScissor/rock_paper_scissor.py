import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer=random.randint(0,2)
game_image=[rock,paper,scissors]

print(f"user chose {user}")
print(f"computer chose {computer}")

print(game_image[user])
print(game_image[computer])

if user>=3 or user <0:
    print("you typed invalid number")
elif user==0 and computer==2:
    print("you wins")
elif user==2 and computer==0:
    print("you lose")
elif computer > user:
    print("you lose")
elif user> computer:
    print("you win")
elif computer ==user :
    print("Its a Draw")

else:
    print("You typed an invalid number")


