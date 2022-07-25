# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
length = 0
for i in student_heights:
    length += 1

summ = 0
for student_height in student_heights:
    summ += student_height
answer = round(summ / length)

print(answer)
