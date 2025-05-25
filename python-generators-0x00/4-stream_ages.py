#!/usr/bin/env python3
seed = __import__('seed')

def stream_user_ages():
    """Yield user ages one at a time."""
    conn = seed.connect_to_prodev()
    cursor = conn.cursor()
    cursor.execute("SELECT age FROM user_data")
    for row in cursor.fetchall():
        yield row[0]
    conn.close()


def average_user_age():
    """Compute average age using the generator."""
    total = 0
    count = 0

    for age in stream_user_ages():
        total += age
        count += 1

    if count > 0:
        print(f"Average age of users: {total / count:.2f}")
    else:
        print("No users found.")
