# File: 3-concurrent.py
import asyncio
import aiosqlite


async def async_fetch_users():
    """Fetch all users asynchronously"""
    async with aiosqlite.connect("users.db") as db:
        async with db.execute("SELECT * FROM users") as cursor:
            results = await cursor.fetchall()
            return results


async def async_fetch_older_users():
    """Fetch users older than 40 asynchronously"""
    async with aiosqlite.connect("users.db") as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            results = await cursor.fetchall()
            return results


async def fetch_concurrently():
    """Run both queries concurrently"""
    all_users, older_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

    print("All Users:", all_users)
    print("Users older than 40:", older_users)


if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
