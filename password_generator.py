import random

password_length = input("Enter the desired password length: ")
include_uppercase = input("Include uppercase letters? (yes/no): ")
include_lowercaswe = input("Include lowercase letters? (yes/no): ")
include_numbers = input("Include numbers? (yes/no): ")
include_special = input("Include special characters? (yes/no): ")

character = []

if include_uppercase.lower() == "yes":   #adds each character to a list
    character.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ") 

if include_lowercaswe.lower() == "yes":
    character.extend("abcdefghijklmnopqrstuvwxyz")

if include_numbers.lower() == "yes":
    character.extend("0123456789")

if include_special.lower() == "yes":
    character.extend("!@#$%^&*()-+")

if not character:
    print("No valid characters selected.")

else:
    password = ''.join(random.choice(character) for _ in range(int(password_length)))
    print("Generated Password:", password)

