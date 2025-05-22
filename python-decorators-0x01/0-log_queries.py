#!/usr/bin/env python3
import sqlite3
import functools

#### decorator to log SQL queries
def log_queries():
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            if 'query' in kwargs:
                print(f"Executing SQL Query: {kwargs['query']}")
            elif len(args) > 0:
                print(f"Executing SQL Query: {args[0]}")
            return function(*args, **kwargs)
        return wrapper
    return decorator

@log_queries()
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
print(users)
