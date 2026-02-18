# run this code to see the TypeError
# print("Length of character in name :"+ len(input("Enter your name")))

# Corrected code to avoid TypeError
name =input("Enter your name: ")
length_of_name = len(name)
print("Length of characters in name: " + str(length_of_name))