with open('D:\project file\python_100day_projects/100_Projects\Day26_NATO\list_comprehension\data_overlap/file1.txt','r') as file1:
  list1 = file1.readlines()
with open('D:\project file\python_100day_projects/100_Projects\Day26_NATO\list_comprehension\data_overlap/file2.txt','r') as file2:
  list2 = file2.readlines()
  
result = [int(n) for n in list1 if n in list2]

print(result)
