MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

print("Welcome to kanans kappi kadai ( KKK )")

# report


def coins():
    quarter = input("How many quarters $: ")
    dime = input("How many dimes $: ")
    nickle = input("How many nickles $: ")
    penny = input("How many pennies $: ")

    q = float(quarter) * (0.25)
    d = float(dime) * (0.10)
    n = float(nickle) * (0.05)
    p = float(penny) * (0.01)
    global total
    total=round(q + d + n + p, 2)
    print(f"you gave me {total}")

    
def rep(choice):

    for i,j in MENU[choice]["ingredients"].items():
        final=resources[i]-j
        if j >= resources[i]:

            print(f"sorry there is not enough {i}")
            is_on=False


        resources[i]=final

is_on=True
while is_on:
    choice = input("What would you like ?(espresso/latte/cappuccino): ").lower()

    if choice== "espresso":

        coins()
        espresso=1.5
        if total > espresso:
            print(f"come on get your change $ {round(total - espresso,2)} ")
            rep(choice)
            print("here your lovely espresso . enjoy!!!")


        elif total < espresso:
            print(f"you have not enough to get this with $ { total}")

        elif total == espresso:
            rep(choice)
            print("yes get your espresso and enjoy")

            print("here express your espresso . enjoy!!!")
        else :
            print("correct your input")

    elif choice== "latte":

        coins()
        latte= 2.5
        if total > latte:
            print(f"come on get your change $ {round(total - latte,2)} ")
            rep(choice)
            print("here your lovely lotte . enjoy!!!")
        elif total < latte:
            print(f"you have not enough to get this with $ { total}")
        elif total == latte:
            print("yes get your espresso and enjoy")
            print("here your lovely latte . enjoy!!!")
            rep(choice)
        else :
            print("correct your input")

    elif choice == "cappuccino":

        coins()
        capp=3.0
        if total > capp:
            print(f"come on get your change $ {round(total - capp,2)} ")
            rep(choice)
            print("here your lovely cappuccino . enjoy!!!")
        elif total < capp:
            print(f"you have not enough to get this with $ { total}")

        elif total == capp:
            print("yes get your espresso and enjoy")
            rep(choice)
            print("here your lovely cappuccino . enjoy!!!")
        else :
            print("correct your input")



    elif choice == "report":

        print(f"WATER:{resources['water']}ml\nMIlk:{resources['milk']}ml\nCOFFEE:{resources['coffee']}ml")



    elif choice=="off":

        print("The machine closed ")
        is_on=False
    else:

        print("Enter valid input")

# process coins

# transaction check

# make coffee
