import mysql.connector

# Close connection
def connect_db():
    connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="kiddie",
    password="Password@123!")

    return connection

def create_database(connection):
    cursor = connection.cursor()
    try:
        cursor.execute(
            """
            CREATE DATABASE IF NOT EXISTS ALX_prodev
            """
        )
    except Exception as e:
        print(e)
    finally:
        connection.close()

def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="kiddie",        # replace with your MySQL username
            password='Password@123',    # replace with your MySQL password
            database='ALX_prodev'
        )

        if connection.is_connected():
            print("Connected to ALX_prodev database")
            return connection

    except mysql.connector.Error as e:
        print("Error while connecting to MySQL:", e)
        return None


def create_table(connection):
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS user_data (
            user_id UUID PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL

            INDEX idx_user_id (user_id)
            )
            """
        )
    except mysql.connector.Error as e:
        print("Error while connecting to MySQL:", e)

    finally:
        connection.close()


def insert(connection, data):
    cursor  = connection.cursor

    