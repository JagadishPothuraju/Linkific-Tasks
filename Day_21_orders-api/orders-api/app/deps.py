"""Dependency injection: a database with blocking and non-blocking calls."""
import asyncio
import time

from . import config


class Database:
    def get_user_sync(self, uid: int) -> dict:
        time.sleep(config.DB_LATENCY)  # simulates a blocking DB call
        return {"id": uid, "name": f"user-{uid}"}

    async def get_user(self, uid: int) -> dict:
        await asyncio.sleep(config.DB_LATENCY)  # simulates a non-blocking DB call
        return {"id": uid, "name": f"user-{uid}"}


def get_db() -> Database:
    return Database()
