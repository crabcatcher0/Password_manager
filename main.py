import func
from colorama import Fore, Back, Style


print("********* Welcome to Password Manager *********")
password = ''

while True:

    user_input = input(
    f"{Fore.BLUE}{Style.BRIGHT}Options: \n"
    "'G' to generate random password\n"
    "'M' to manage your account and password (Password must be generate first)\n"
    "'S' to view your account.\n"
    "'C' to check your password strength\n"
    "'Q' to quit\n"
    f"Choose from options:{Style.RESET_ALL} "
    ).strip().lower()


    if user_input == 'g':
        length = int(input("Length of password: "))
        password = func.create_pass(length)
        print(f"{Fore.GREEN}{Style.BRIGHT}✔ Success! Your Password: {password}{Style.RESET_ALL}")

    
    elif user_input == 'm':
        if password == '':
            print(f"{Fore.RED}✖ Please generate the password first.{Style.RESET_ALL}")
        
        else:
            name = input("Enter Your name: ")
            site_name = input("Enter the site name or URL: ")
            username = input("Enter username or email: ")
            creds = func.manage_pass(name, site_name, username, password)

            print(f"{Fore.GREEN}{Style.BRIGHT}✔ Success! Check the 'credential.txt' file.{Style.RESET_ALL}")
    
    elif user_input == 'c':
        input_pass = input("Enter your Password: ")
        print(func.password_check(input_pass))

    elif user_input == 's':
        func.show_my_password()

    elif user_input == 'q':
        break
    
    else:
        print(f"{Fore.RED}{Style.BRIGHT}✖ Invalid input please choose from the options.{Style.RESET_ALL}")
