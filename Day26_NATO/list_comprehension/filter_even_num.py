list_of_strings = range(1,101)

numbers = [int(new) for new in list_of_strings]

# list comprehension for filter even numbers from input 
result = [num for num in numbers if num%2 == 0 ]

print(result)
