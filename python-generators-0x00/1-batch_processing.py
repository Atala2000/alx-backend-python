#!/usr/bin/env python3
seed = __import__('seed')

def stream_users():
    """Yield one user at a time from the database."""
    conn = seed.connect_to_prodev()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_data")
    cols = [desc[0] for desc in cursor.description]

    for row in cursor.fetchall():
        yield dict(zip(cols, row))


def stream_users_in_batches(batch_size):
    """Yield users in batches of batch_size."""
    batch = []
    for user in stream_users():
        batch.append(user)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch


def batch_processing(batch_size):
    """Print users over age 25 in each batch."""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user["age"] > 25:
                print(user)


batch_processing(20)