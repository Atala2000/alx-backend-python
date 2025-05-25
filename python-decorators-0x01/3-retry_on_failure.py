#!/usr/bin/env python3
import time
import sqlite3
import functools

# Decorator for database connection
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            result = func(conn, *args, **kwargs)
            return result
        finally:
            conn.close()
    return wrapper

# Decorator factory for retry logic
def retry_on_failure(retries=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt+1} failed: {e}")
                    if attempt < retries - 1:
                        time.sleep(delay)
                    else:
                        raise
        return wrapper
    return decorator

# Use the decorators
@retry_on_failure(retries=3, delay=2)
@with_db_connection
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

# Fetch users
try:
    users = fetch_users_with_retry()
    print("Fetched users:", users)
except Exception as e:
    print("Failed after retries:", e)
