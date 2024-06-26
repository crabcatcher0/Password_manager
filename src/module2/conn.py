import pymysql
import pymysql


def connect_me():
    try:
        connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'password_manager',
            cursorclass = pymysql.cursors.DictCursor
        )
        return connection
    
    except pymysql.Error as e:
        print(f"Error connecting to database: {e}")
        return None


