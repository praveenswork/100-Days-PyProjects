
def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2


oprtr_dictionary={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide

}


def calculator():
    num1=int(input("Eter 1st number: "))
    num2=int(input("Eter 1st number: "))
    for symbols in oprtr_dictionary:
        print(symbols)

    operator=input("Enter operator symbol: ")

    calc_function=oprtr_dictionary[operator](num1,num2)

    print(f"{num1} {operator} {num2} = {calc_function}")

    should_continue=True

    while should_continue:
        
        
        num3=int(input("Enter next number: "))
        operator=input("Enter operator symbol: ")
        new_output=oprtr_dictionary[operator]( calc_function,num3)
        print(new_output)
        again =input("You want to calculate again? Enter Y for 'Yes' and N for 'No': ").lower()
        if again =="y":
            should_continue=True
        elif again=="n":
            should_continue=False
            calculator()

calculator()
        

    

        








