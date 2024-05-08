import random
letters=['a','b','c','d','e','F','g','h','i','j','k','l','m',
         'N','O','P','Q','r','S','t','U','V','W','X','y','Z']
number=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','^','&','*','{','}','(',')','?','/' ]

print("welcome to pypassword generator")

user_let=int(input("Enter how many letters you want in password: "))
user_num=int(input("Enter how many numbers you want in password: "))
user_sym=int(input("Enter how many symbols you want in password: "))

password_list=[]

for char in range(1,user_let+1):
    password_list.append(random.choice(str(letters)))

for char in range(1,user_num+1):
    password_list.append(random.choice(number))

for char in range(1,user_sym+1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password=""

for char in password_list:
    password+=char
print(f"your password is {password}")
