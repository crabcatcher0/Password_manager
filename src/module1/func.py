##password generator
from colorama import Fore, Style
import random
import re
import os

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
special_characters = "!@#$%^&*,"

all_char = uppercase_letters + lowercase_letters + digits + special_characters
    


def create_pass(length):
    if length < 8:
        print(f"{Fore.RED}Length should be more then 8..")
        return f"{Fore.RED}✖ Error: Password generation failed.{Style.RESET_ALL}"
    
    else:
        password = (
            random.choice(lowercase_letters) +
            random.choice(uppercase_letters) +
            random.choice(digits) +
            random.choice(special_characters) +
            "".join(random.choice(all_char) for _ in range(length - 4)) 
            )
        
        password_list = list(password)
        random.shuffle(password_list)
        password = ''.join(password_list)

        return f"{password}"


def manage_pass(name, site_name, username, password):
    with open("credential.txt", 'w') as file:
        file.write(f"Welcome! {name}. Your informations:\n\n")
        file.write(f"Site Name: '{site_name}'\n")
        file.write(f"Username or Email: '{username}'\n")
        file.write(f"Password: '{password}'\n")         


def password_check(input_pass):

    if len(input_pass) < 8:
        return f"{Fore.RED}{Style.BRIGHT}✖ Password Strerngth: Too Weak.{Style.RESET_ALL}"
    
    has_lowercase = re.search(r'[a-z]', input_pass)
    has_uppercase = re.search(r'[A-Z]', input_pass)
    has_character = re.search(r'[\W_]', input_pass)
    has_digit = re.search(r'\d', input_pass)

    if has_lowercase and has_uppercase and has_character and has_digit:
        return f"{Fore.GREEN}{Style.BRIGHT}✔ Password Strength: Strong.u'\u2713'{Style.RESET_ALL}"
    elif has_lowercase and has_digit:
        return "Password Strength: Medium."
    elif has_lowercase:
        return "Password Strength: Weak (Missing uppercase letters, digits, or special characters)."
    else:
        return "Password Strength: Weak (Missing lowercase letters, digits, or special characters)."


def show_my_password():

    if not os.path.exists("credential.txt"):
        print(f"{Fore.RED}{Style.BRIGHT}✖ Please generate and store your detail.{Style.RESET_ALL}")
    else:
        with open("credential.txt", 'r') as file:
            file = file.read()
            print(f"{Fore.GREEN}{Style.BRIGHT}{file}{Style.RESET_ALL}")
        
    