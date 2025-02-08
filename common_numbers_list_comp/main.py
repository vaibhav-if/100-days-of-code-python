num1 = []
num2 = []

with open("file1.txt") as file:
    contents = file.readlines()
    num1 = [int(n) for n in contents]

with open("file2.txt") as file:
    contents = file.readlines()
    num2 = [int(n) for n in contents]

num = [n for n in num1 if n in num2]

print(num)