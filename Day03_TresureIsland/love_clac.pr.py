print( "The Love calculator is calculating your score.")
name_1 = input (" What is your name?") 
name2 = input(" What is their name?")

added_names = name_1 + name2
lower_names=added_names.lower()

t= lower_names.count("t")
r= lower_names.count("r")
u= lower_names.count("u")
e= lower_names.count("e")

TRUE=t+r+u+e

l=lower_names.count("l")
o= lower_names.count("o")
v= lower_names.count("v")
e= lower_names.count("e")

LOVE=l+o+v+e

score=int(str(TRUE)+str(LOVE))

if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>=40 and score<=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is{score}")
       