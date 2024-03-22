#!/usr/bin/env python3
"""
importing asyncio for asynchorous programming and random module
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    coroutine called async_generator that takes no arguments.
    The coroutine will loop 10 times, each time asynchronously
    """
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
