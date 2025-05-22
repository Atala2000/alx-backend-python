#!/usr/bin/env python3
import sqlite3
import functools

def log_queries():
    """Decorator that logs the SQL query before execution."""
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            # Get the SQL query from either args or kwargs
            query = kwargs.get('query') if 'query' in kwargs else args[0] if args else None
            if query:
                print(f"Executing SQL Query: {query}")
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

users = fetch_all_users(query="SELECT * FROM users")
print(users)
