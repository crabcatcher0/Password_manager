from . import conn
import pymysql
import bcrypt
import pymysql.cursors
import secrets
from colorama import Fore, Style


sessions = {}

def hassed_password(password):
    salt = bcrypt.gensalt()
    hassed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hassed



def user_register(first_name: str, last_name: str, username, password): #registration
    connection = None
    try:
        if not (first_name and last_name and username and password):
            raise ValueError(f"{Fore.RED}All field must be filled.{Style.RESET_ALL}")
        
        connection = conn.connect_me()
        with connection.cursor() as cursor:
            hassed = hassed_password(password)
            sql = "INSERT INTO user(first_name, last_name, username, password) VALUES (%s, %s, %s, %s)"
            value = (first_name, last_name, username, hassed)
            cursor.execute(sql, value)
            connection.commit()
            return f"{Fore.GREEN}{Style.BRIGHT}Registration success!{Style.RESET_ALL}"

    except pymysql.Error as e:
        return f"{Fore.RED}Error: {e}{Style.RESET_ALL}"

    except ValueError as ve:
        return f"{Fore.RED}Error: {ve}{Style.RESET_ALL}"

    finally:
        if connection:
            connection.close()
        
    

def login(username, password):
    try:
        connection = conn.connect_me()
        with connection.cursor() as cursor:
            sql = "SELECT id, password FROM user WHERE username = %s"
            cursor.execute(sql, (username,))
            result = cursor.fetchone()

            if result:
                user_id = result['id']
                hashed_password = result['password'].encode('utf-8')

                if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                    session_token = secrets.token_hex(16)
                    sessions[session_token] = user_id
                    print("Login success.")
                    return session_token
                else:
                    print("Invalid username or password.")
                    return False
            else:
                print("Username not found. Please check typo.")
                return False
            
    except pymysql.Error as e:
        print(f"Error: {e}")
    
    finally:
        if connection:
            connection.close()



def logout(session_token):
    if session_token in sessions:
        del sessions[session_token]
        print(f"Logged out session: {session_token}")
    else:
        print("Session token not found. Already logged out or invalid.")


def profile_info(session_token):
    connection = None
    try:
        if session_token in sessions:
            user_id = sessions[session_token]

            connection = conn.connect_me()
            with connection.cursor() as cursor:
                sql = "SELECT first_name, last_name, username FROM user WHERE id = %s"
                cursor.execute(sql, (user_id,))
                result = cursor.fetchone()

                if result:
                    first_name, last_name, username = result
                    print("*" * 40)  
                    print("*" + " " * 38 + "*")  
                    print(f"*{'Profile Information:':^38}*") 
                    print("*" + " " * 38 + "*")  
                    print(f"* Username: {result[username]:<30} *")  
                    print(f"* Name: {result[first_name]} {result[last_name]:<25} *") 
                    print("*" + " " * 38 + "*")  
                    print("*" * 40)  
                else:
                    print(f"No user found with ID: {user_id}") 
        else:
            print("Session Expired. Please login again.")

    except pymysql.Error as e:
        print(f"Database Error: {e}")

    finally:
        if connection:
            connection.close()


def add_data(session_token, site_name, password, comment):
    connection = None

    try:
        if session_token in sessions:
            user_id = sessions[session_token]

            if not (user_id and site_name and password and comment):
                raise ValueError("All fields are required.")

            connection = conn.connect_me()
            with connection.cursor() as cursor:
                sql = "INSERT INTO data(user_id, site_name, password, comment) VALUES (%s, %s, %s, %s)"
                values = (user_id, site_name, password, comment)
                cursor.execute(sql, values)
                connection.commit()

            return f"{Fore.GREEN}{Style.BRIGHT}Successfully Added!{Style.RESET_ALL}"

        else:
            return "Session not found or expired. Please login again."

    except pymysql.Error as e:
        return f"Database Error: {e}"

    except ValueError as ve:
        return f"Error: {ve}"

    finally:
        if connection:
            connection.close()

            

                          