#!/usr/bin/env python3
import mysql.connector
DatabaseConnection = __import__('0-databaseconnection').DatabaseConnection

class ExecuteQuery():
        def __init__(self, param, password, port, username):
                self.database_conn = DatabaseConnection(password, port, username)
                self.param= param
        
        def __enter__(self):
                if self.database_conn:
                        print(self.database_conn.__dict__)
                        with self.database_conn as con:
                            cursor = con.cursor()
                            try:
                                cursor.execute("SELECT * FROM users WHERE age > %s", (self.param,))
                                results = cursor.fetchall()
                                print(results)
                                return results
                            except mysql.connector.Error as e:
                                print(e)

        
        def __exit__(self, exc_type, exc_value, traceback):
                self.database_conn.__exit__(exc_type, exc_value, traceback)


if __name__ == "__main__":
       with ExecuteQuery(25, 'Password@123!', 3306, 'kiddie') as db:
              print(db)