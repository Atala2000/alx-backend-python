#!/usr/bin/env python3
import aiosqlite
import asyncio

DB_NAME = 'users.db'

async def setup_database():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT,
                age INTEGER,
                email TEXT
            )
        """)
        await db.commit()

        # Optional: Add sample data if table is empty
        async with db.execute("SELECT COUNT(*) FROM users") as cursor:
            count = await cursor.fetchone()
            if count[0] == 0:
                users = [
                    ('Alice', 25, 'alice@example.com'),
                    ('Bob', 45, 'bob@example.com'),
                    ('Charlie', 35, 'charlie@example.com'),
                    ('Diana', 50, 'diana@example.com'),
                ]
                await db.executemany("INSERT INTO users (username, age, email) VALUES (?, ?, ?)", users)
                await db.commit()


async def async_fetch_users():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            users = await cursor.fetchall()
            return users


async def async_fetch_older_users():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            older_users = await cursor.fetchall()
            return older_users


async def fetch_concurrently():
    # Set up the database and run both fetches in parallel
    await setup_database()
    
    results = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

    all_users, older_users = results

    print("All users:")
    for user in all_users:
        print(user)

    print("\nUsers older than 40:")
    for user in older_users:
        print(user)


if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
