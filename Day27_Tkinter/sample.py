def sum(*args):
    for i in args:
        i +=i
    print(i)

sum(112,121)

def func(**hi):
    print(hi["greet"])

func(greet = "hello", greet2 = "bye")