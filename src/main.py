from module1 import func
from module2 import process
import getpass
from colorama import Fore, Style

print("********* Welcome to Password Manager *********")
password = ''
logged_in = False
username = ''
session_token = ''  # Initialize session token variable

while True:

    if not logged_in:
        user_input = input(
            f"{Fore.BLUE}{Style.BRIGHT}Options: \n"
            "'A' Register (Web based.)\n"
            "'L' to login\n"
            "'G' to generate random password\n"
            "'M' to manage your account and password (Password must be generated first)\n"
            "'S' to view your account.\n"
            "'C' to check your password strength\n"
            "'Q' to quit\n"
            f"Choose from options:{Style.RESET_ALL} "
        ).strip().lower()

        if user_input == 'g': #optin g
            length = int(input("Length of password: "))
            password = func.create_pass(length)
            print(f"{Fore.GREEN}{Style.BRIGHT}✔ Success! Your Password: {password}{Style.RESET_ALL}")


        elif user_input == 'm': #option m

            if password == '':
                print(f"{Fore.RED}✖ Please generate the password first.{Style.RESET_ALL}")

            else:
                name = input("Enter Your name: ")
                site_name = input("Enter the site name or URL: ")
                username = input("Enter username or email: ")
                creds = func.manage_pass(name, site_name, username, password)
                print(f"{Fore.GREEN}{Style.BRIGHT}✔ Success! Check the 'credential.txt' file.{Style.RESET_ALL}")


        elif user_input == 'c': #option c
            input_pass = input("Enter your Password: ")
            print(func.password_check(input_pass))


        elif user_input == 's': #option s
            func.show_my_password()


        elif user_input == 'a': #register
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            username = input("Create username: ")
            password = getpass.getpass("Create password: ")
            register = process.user_register(first_name, last_name, username, password)
            print(register)


        elif user_input == 'l': #login
            username = input("Enter username: ")
            password = input("Enter password: ")
            session_token = process.login(username, password)  #getting session token

            if session_token:
                logged_in = True
                print(f"{Fore.GREEN}Login successful!{Style.RESET_ALL}")

            else:
                print(f"{Fore.RED}Login failed. Please try again.{Style.RESET_ALL}")

        elif user_input == 'q':
            break

        else:
            print(f"{Fore.RED}{Style.BRIGHT}✖ Invalid input please choose from the options.{Style.RESET_ALL}")


    else:  # if user is logged in

        print(f"{Fore.GREEN}{Style.BRIGHT}Status 200 Ok! Active: {username}{Style.RESET_ALL}")

        user_input = input(
            f"{Fore.CYAN}{Style.BRIGHT}Options:\n"
            "'V' to view profile information\n"
            "'S' to view status\n"
            "'X' to logout\n"
            f"Choose from options:{Style.RESET_ALL} "
        ).strip().lower()

        if user_input == 'v':
            process.profile_info(session_token)
          

        elif user_input == 'x': #logout
            process.logout(session_token)  
            logged_in = False
            username = ''
            session_token = ''  
            print(f"{Fore.GREEN}Logged out successfully.{Style.RESET_ALL}")

        else:
            print(f"{Fore.RED}{Style.BRIGHT}✖ Invalid input. Please choose from the options.{Style.RESET_ALL}")

print("Exiting Password Manager. Goodbye!")
