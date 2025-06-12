import random
import string


def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    
    password += random.choices(characters, k=length - 4)

    
    random.shuffle(password)

    
    return ''.join(password)


try:
    user_length = int(input("Enter the desired password length: "))
    password = generate_password(user_length)
    print(f"Generated Password: {password}")
except ValueError:
    print("Please enter a valid number.")
