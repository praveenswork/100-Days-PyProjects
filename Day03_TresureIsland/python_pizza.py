
print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input()

if size== "S":
    S=15
    if add_pepperoni=="Y":
        S+=2
    else:
        pass

    if extra_cheese=="Y":
        S+=1
    print(f"Your final bill is: {S}.")
elif size=="M":
    
    M=20
    if add_pepperoni=="Y":
        M+=3
    else:
        pass

    if extra_cheese=="Y":
        M+=1
    print(f"Your final bill is: {M}.")
elif size=="L":
    L=25
    if add_pepperoni=="Y":
        L+=3
    elif add_pepperoni=="N":
        pass
    else:
        pass

    if extra_cheese=="Y":
        L+=1
    print(f"Your final bill is: {L}.")
else:
    pass
