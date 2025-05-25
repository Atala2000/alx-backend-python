#!/usr/bin/env python3
import aiosqlite
import asyncio
from sqlite3 import Error


async def async_fetch_users(db):
    async with db.execute("SELECT * FROM users") as cursor:
        results = await cursor.fetchall()
        return results


async def async_fetch_older_users():
    async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
        results = await cursor.fetchall()
        return results
    
results = await asyncio.gather(
    async_fetch_users(),
    async_fetch_older_users()
)

async def fetch_concurrently():
    
    # Run both queries at once


    print("All users:", results[0])
    print("Older users:", results[1])

    await db.close()

# Entry point
if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
