# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

highest_score = 0
for student_score in student_scores:
    if student_score > highest_score:
        highest_score = student_score
print(f'The highest score in the class is: {highest_score}')
