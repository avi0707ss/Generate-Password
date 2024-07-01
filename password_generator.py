import string
import random

def generate_password(length, include_uppercase, include_digits, include_special):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if len(characters) == 0:
        print("Error: No character types selected.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    length = int(input("Enter the desired length of the password: "))
    
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    include_special = input("Include special characters? (yes/no): ").lower() == 'yes'
    
    password = generate_password(length, include_uppercase, include_digits, include_special)
    
    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
