# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = round(weight / (height ** 2))

if bmi < 18.5:
    BMI = "underweight"
elif bmi < 25:
    BMI = "normal weight"
elif bmi < 30:
    BMI = "slightly overweight"
elif bmi < 35:
    BMI = "obese"
else:
    BMI = "clinically obese"

print(f'Your BMI is {bmi}, your are {BMI}.')
