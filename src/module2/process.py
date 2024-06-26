from . import conn
import pymysql
import bcrypt
import pymysql.cursors
import secrets

sessions = {}

def hassed_password(password):
    salt = bcrypt.gensalt()
    hassed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hassed



def user_register(first_name: str, last_name: str, username, password):
    try:
        connection = conn.connect_me()
        with connection.cursor() as cursor:
            hassed = hassed_password(password)
            sql = "INSERT INTO user(first_name, last_name, username, password) VALUES (%s, %s, %s, %s)"
            value = first_name, last_name, username, hassed
            cursor.execute(sql, value)
            connection.commit()
            print("Registration success!")

    except pymysql.Error as e:
        print(f"Error: {e}")

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

                # print(f"Debug - session_token: {session_token}, user_id: {user_id}, result: {result}")

                if result:
                    first_name, last_name, username = result
                    print("Profile Information:")
                    print(f"Username: {result[username]}")
                    print(f"Name: {result[first_name]} {result[last_name]}")
                else:
                    print(f"No user found with ID: {user_id}") 
        else:
            print("Session Expired. Please login again.")

    except pymysql.Error as e:
        print(f"Database Error: {e}")

    finally:
        if connection:
            connection.close()


                          