import random

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_characters = ["!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]

letter_count = int(input("How many letters? "))
digit_count = int(input("How many digits? "))
sp_count = int(input("How many special characters? "))

password = []

for i in range(0, letter_count):
    password.append(random.choice(letters))

for i in range(0, digit_count):
    password.append(random.choice(digits))

for i in range(0, sp_count):
    password.append(random.choice(special_characters))

random.shuffle(password)

password_str = ""

for i in password:
    password_str += i

print(password_str)