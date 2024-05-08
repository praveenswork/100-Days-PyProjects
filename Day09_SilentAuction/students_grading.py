                                    #student grades
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

for key ,value in student_scores.items():
    if value > 90 and value < 100:
        student_scores[key]="Outstanding"
    elif value > 80 and value < 90:
        student_scores[key]="Exceeds Expectations"
    elif value > 70  and value < 80:
        student_scores[key]="Acceptable"
    elif value <= 70:
        student_scores[key]="Fail"


student_grades=student_scores
print(student_grades)



