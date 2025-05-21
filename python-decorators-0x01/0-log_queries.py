import sqlite3
import functools


def log_queries(function):
    def wrapper(*args, **kwargs):
        for k, v in kwargs.items():
            print(v)
        function(*args,**kwargs)
    return wrapper


@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
