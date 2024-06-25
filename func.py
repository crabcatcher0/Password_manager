##password generator
import random
import re

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
special_characters = "!@#$%^&*,"

all_char = uppercase_letters + lowercase_letters + digits + special_characters


def create_pass(length):
    if length < 8:
        print("Length should be more then 8..")
        return "Password generation failed."
    
    else:
        password = (
            random.choice(lowercase_letters) +
            random.choice(uppercase_letters) +
            random.choice(digits) +
            random.choice(special_characters) +
            "".join(random.choice(all_char) for _ in range(length - 3)) 
            )
        
        password_list = list(password)
        random.shuffle(password_list)
        password = ''.join(password_list)

        return f"This is your password: '{password}'"
    
   
# def write_pass(password):
#     with open("generated_pass.txt", 'w') as file:
#         file = file.write(password)


def manage_pass(site_name, username, password):
    with open("credential.txt", 'w') as file:
        file.write(f"Site Name: '{site_name}'\n")
        file.write(f"Username or Email: '{username}'\n")
        file.write(f"Password: '{password}'\n")         

def password_check(input_pass):

    if len(input_pass) < 8:
        return f"Password Strerngth: Too Weak."
    
    has_lowercase = re.search(r'[a-z]', input_pass)
    has_uppercase = re.search(r'[A-Z]', input_pass)
    has_character = re.search(r'[\W_]', input_pass)
    has_digit = re.search(r'\d', input_pass)

    if has_lowercase and has_uppercase and has_character and has_digit:
        return "Password Strength: Strong."
    elif has_lowercase and has_digit:
        return "Password Strength: Medium."
    elif has_lowercase:
        return "Password Strength: Weak (Missing uppercase letters, digits, or special characters)."
    else:
        return "Password Strength: Weak (Missing lowercase letters, digits, or special characters)."



    
        