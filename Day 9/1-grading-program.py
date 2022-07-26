student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for students in student_scores:
    grades = student_scores[students]

    if grades > 90:
        grades = 'Outstanding'
    elif grades > 80:
        grades = 'Exceeds Expectations'
    elif grades > 70:
        grades = 'Acceptable'
    else:
        grades = 'Fail'
    student_grades[students] = grades

# 🚨 Don't change the code below 👇
print(student_grades)
