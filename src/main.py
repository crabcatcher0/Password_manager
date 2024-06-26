from module1 import func
from module2 import process
import getpass
from colorama import Fore, Style
import pyfiglet

ascii_art = pyfiglet.figlet_format("CrabCatcher0")
print(Fore.YELLOW + ascii_art + Style.RESET_ALL)

print("********* Welcome to Password Manager *********")
password = ''
logged_in = False
username = ''
session_token = ''  # Initialize session token variable

while True:

    if not logged_in:
        user_input = input(
            f"{Fore.BLUE}{Style.BRIGHT}Options: \n"
            "Web-Based (Requires Database):\n"
            "'A' Register\n"
            "'L' to login\n"
            "\n"
            "Offline:\n"
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
            first_name = input("Enter your first name: ").strip()
            last_name = input("Enter your last name: ").strip()
            username = input("Create username: ").strip()
            password = getpass.getpass("Create password: ").strip()
            register = process.user_register(first_name, last_name, username, password)
            print(register)


        elif user_input == 'l': #login
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            session_token = process.login(username, password)  #getting session token

            if session_token:
                logged_in = True
                print(f"{Fore.GREEN}✔ Login successful!{Style.RESET_ALL}")

            else:
                print(f"{Fore.RED}Login failed. Please try again.{Style.RESET_ALL}")

        elif user_input == 'q':
            break

        else:
            print(f"{Fore.RED}{Style.BRIGHT}Invalid input please choose from the options.{Style.RESET_ALL}")


    else:  # if user is logged in

        print(f"{Fore.GREEN}{Style.BRIGHT}✔ Status 200 Ok! Active: {username}{Style.RESET_ALL}")

        user_input = input(
            f"{Fore.CYAN}{Style.BRIGHT}Available Options:\n"
            "'V' to view profile information\n"
            "'S' Add data to Vault\n"
            "'W' open Vault\n"
            "'X' to logout\n"
            f"Choose from options:{Style.RESET_ALL} "
        ).strip().lower()


        if user_input == 'v': #view info
            process.profile_info(session_token)
        

        elif user_input == 's': #add data
            site_name = input("Enter site name or URL: ").strip()
            password = input("Enter the password you want to store: ").strip()
            comment = input("Reminders (required): ").strip()
            success = process.add_data(session_token, site_name, password, comment)

            if success:
                print(f"{Fore.GREEN}{Style.BRIGHT}✔ Data added Successfully!{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}{Style.BRIGHT}Failed to add data. Please try again.{Style.RESET_ALL}")


        elif user_input == 'w': #open vault
            process.open_vault(session_token)


        elif user_input == 'x': #logout
            process.logout(session_token)  
            logged_in = False
            username = ''
            session_token = ''  
            print(f"{Fore.GREEN}✔ Logged out successfully.{Style.RESET_ALL}")

        else:
            print(f"{Fore.RED}{Style.BRIGHT}Invalid input. Please choose from the options.{Style.RESET_ALL}")

print("Exiting Password Manager. Goodbye!")
