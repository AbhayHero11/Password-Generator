import random
import string

def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars):
    characters = ""

    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

        if len(characters) == 0:
            print("Error: Please select at least one character type.")
            return
        
        password = ''.join(random.choice(characters) for _ in range (length))
        print(f"Generated Passweord: {password}")

print("---Password Generator---")
length = int(input("Enter the lenght of the password: "))
include_uppercase = input("Include uppercase letters? (Y/N): ").lower() == "y"
include_lowercase = input("Include lowercase letters? (Y/N): ").lower() == "y" 
include_numbers = input("Include numbers? (Y/N): ").lower() == "y"
include_special_chars = input("Include special characters? (Y/N): ").lower() == "y"

generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars)