#!/usr/bin/env python3
import aiosqlite
import asyncio
from sqlite3 import Error

class DataBaseConnection:

    @staticmethod
    async def connect_database():
        try:
            db = await aiosqlite.connect('user_alx.db')
            async with db.cursor() as cursor:
                await cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS users (
                        username TEXT,
                        age INTEGER,
                        email TEXT
                    )
                    """
                )
                await db.commit()
            return db
        except Error as e:
            print(f"Connection error: {e}")

async def async_fetch_users(db):
    async with db.execute("SELECT * FROM users") as cursor:
        results = await cursor.fetchall()
        return results


async def async_fetch_older_users(db):
    async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
        results = await cursor.fetchall()
        return results

async def fetch_concurrently():
    db = await DataBaseConnection.connect_database()
    
    # Run both queries at once
    results = await asyncio.gather(
        DataBaseConnection.async_fetch_users(db),
        DataBaseConnection.async_fetch_older_users(db)
    )

    print("All users:", results[0])
    print("Older users:", results[1])

    await db.close()

# Entry point
if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
