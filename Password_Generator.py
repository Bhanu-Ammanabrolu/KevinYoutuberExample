#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""

for l in range(nr_letters):
    random_letter = random.choice(letters)
    password += random_letter

for s in range(nr_symbols):
    password += random.choice(symbols)

for n in range(nr_numbers):
    random_number = random.choice(numbers)
    password += random_number

print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random_password = []

for l1 in range(nr_letters):
    random_password.append(random.choice(letters))

for s1 in range(nr_symbols):
    random_password.append(random.choice(symbols))

for n1 in range(nr_numbers):
    random_password.append(random.choice(numbers))

print(random_password)
random.shuffle(random_password)
print(random_password)

password_in_string = ""
for e in random_password:
    password_in_string += e
print(password_in_string)
