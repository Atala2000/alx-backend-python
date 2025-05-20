#!/usr/bin/env python3
from itertools import islice


seed = __import__('seed')

def stream_users():
    connection = seed.connect_to_prodev()
    query = 'SELECT * FROM user_data'
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    for result in results:
        yield result    

if __name__ == '__main__':
    for user in islice(stream_users(), 6):
        print(user)
