import string
import random 

print("Welcome to the PyPassword Generator!")
length = int(input("How many letters would you like your password to be? "))
symbols = int(input("How many symbols would you like? "))
numbers = int(input("How many numbers would you like? "))

letters = string.ascii_letters
symbols_set = string.punctuation
numbers_set = string.digits

password = ""
for i in range(1,length+1):
    password += random.choice(letters)
for i in range(1,symbols+1):
    password += random.choice(symbols_set)
for i in range(1,numbers+1):
    password += random.choice(numbers_set)
print(f"Your password is: {password}")

password_list =[]
for i in range(1,length+1):
    password_list.append(random.choice(letters))
for i in range(1,symbols+1):
    password_list.append(random.choice(symbols_set))
for i in range(1,numbers+1):
    password_list.append(random.choice(numbers_set))
random.shuffle(password_list)
print("Password list after shuffling(list): ", password_list)
password_string = ""
for char in password_list:
    password_string += char
print(f"Your shuffled password is(string): {password_string}")