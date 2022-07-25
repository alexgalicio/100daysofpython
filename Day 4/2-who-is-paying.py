import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# from Google
random_idx = random.randrange(len(names))
random_names = names[random_idx]

# my code with help
ind = len(names)
rand = random.randint(0, ind - 1)
ran = names[rand]

print(f'{ran} is going to buy the meal today.')
