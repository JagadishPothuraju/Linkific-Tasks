import asyncio
import logging
import time

from . import config

log = logging.getLogger("api")


def send_confirmation_sync(email: str) -> None:
    time.sleep(config.EMAIL_LATENCY)  # v1: runs inline, client waits
    log.info("Confirmation sent to %s", email)


async def send_confirmation(email: str) -> None:
    await asyncio.sleep(config.EMAIL_LATENCY)  # v2: runs after the response is sent
    log.info("Confirmation sent to %s", email)
