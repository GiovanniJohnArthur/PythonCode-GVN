import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Password Generator!")
Letters = int(input("How many letters to you want in your password?\n"))
Numbers = int(input("How many numbers to you want in your password?\n"))
Symbols = int(input("How many symbols to you want in your password?\n"))

# hard password
password = []
for i in range(1, Letters + 1):
    char = random.choice(letters)
    password += char

for i in range(1, Numbers + 1):
    char = random.choice(numbers)
    password += char

for i in range(1, Symbols + 1):
    char = random.choice(symbols)
    password += char
print(password)
random.shuffle(password) # shuffles the password so that it can be unpredictable
print(password)

new_password = ""
for char in password:
    new_password += char
print(new_password)