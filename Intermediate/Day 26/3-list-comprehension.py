with open("file1.txt") as f1:
    num = f1.readlines()

with open("file2.txt") as f2:
    num2 = f2.readlines()

numbers = num
result = [int(n) for n in numbers if n in num2]

# Write your code above 👆
print(result)
