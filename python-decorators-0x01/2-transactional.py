#!/usr/bin/env python3
import sqlite3 
import functools
# with_db_connection = __import__('1-with_db_connection').with_db_connection



"""your code goes here"""

def transactional(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = args[0]  # Get the DB connection passed in by with_db_connection
        try:
            result = func(*args, **kwargs)
            conn.commit()
            return result
        except Exception as e:
            conn.rollback()
            print(f"Transaction failed: {e}")
    return wrapper

@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
    #### Update user's email with automatic transaction handling 

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')