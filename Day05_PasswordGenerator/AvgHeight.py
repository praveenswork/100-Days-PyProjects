# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total=0
for height in student_heights:
    total+=height
print(total)

tot_student=0
for student in student_heights:
    tot_student+=1
print(tot_student)

avg=round(total/tot_student)

print(avg)
