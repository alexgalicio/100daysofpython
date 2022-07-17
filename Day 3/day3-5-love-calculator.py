# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
new_name = name1.lower() + name2.lower()
true = new_name.count('t') + new_name.count('r') + new_name.count('u') + new_name.count('e')

love = new_name.count('l') + new_name.count('o') + new_name.count('v') + new_name.count('e')

score = int(str(true) + str(love))

if score < 10 or score > 90:
    print(f'You score is {score}, you go together like coke and mentos.')
elif 40 <= score <= 50:
    print(f'You score is {score}, you are alright together.')
else:
    print(f'You score is {score}.')
