#!/usr/bin/env python3
import mysql.connector

class DatabaseConnection():
    def __init__(self, password, port, username):
        self.password = password
        self.port = port
        self.username = username
        self.connection = None

    def __enter__(self):
        try:
            self.connection = mysql.connector.connect(
            host="127.0.0.1",
            port=self.port,
            user=self.username,
            password=self.password,
            database="airbnb"
            )
        except mysql.connector.Error as e:
            print("There was an error", e)

        return self.connection
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()
        


if __name__ == "__main__":
    with DatabaseConnection('Password@123!', 3306, 'kiddie') as db:
        cursor = db.cursor()
        try:
            cursor.execute(
                """
                SELECT * FROM users
                """
            )
            results = cursor.fetchall()
            print(results)
        except mysql.connector.Error as e:
            print(e)