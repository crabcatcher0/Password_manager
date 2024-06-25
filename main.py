import func

print("********* Welcome to Password Manager *********")
password = ''

while True:

    user_input = input(
    "Options: \n"
    "'G' to generate random password\n"
    "'M' to manage your account and password (Password must be generate first)\n"
    "'C' to check your password strength\n"
    "'Q' to quit\n"
    "Choose from options: "
    ).strip().lower()

    if user_input == 'g':
        length = int(input("Length of password: "))
        password = func.create_pass(length)
        print(password)

    # elif first_in == 's':
    #     if password == '':
    #         print("Please generate the password first.")
    #     else:
    #         file_gen = func.write_pass(password)
    #         print("Success! Check the file name 'generated_pass.txt' in current directory!")
    
    elif user_input == 'm':
        if password == '':
            print("Please generate the password first.")
        
        else:
            site_name = input("Enter the site name or URL: ")
            username = input("Enter username or email: ")
            creds = func.manage_pass(site_name, username, password)
            print("Check the 'credential.txt' file.")
    
    elif user_input == 'c':
        input_pass = input("Enter your Password: ")
        print(func.password_check(input_pass))


    elif user_input == 'q':
        break
    
    else:
        print("Invalid input please choose from the options.")
