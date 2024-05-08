'''# sample list comprehension

s_list = [1, 2, 3, 4, 5]
final_list = [new*2 for new in s_list]
print(f'power values of sample  list{final_list}')

name = ['Elango', 'Praveen', 'Nitheesh', 'Dharshan', 'muthu', 'sri', 'kana']
new_name = [n.upper() for n in name if len(n) >5]
print(new_name)'''

list_of_strings = input().split(',')
# 🚨 Do  not change the code above

# TODO: Use list comprehension to convert the strings to integers 👇:
numbers = [int(new) for new in list_of_strings]
result = [num for num in numbers if num%2 == 0]
# TODO: Use list comprehension to filter out the odd numbers
# and store the even numbers in a list called "result"

# Write your code 👆 above:
print(result)

