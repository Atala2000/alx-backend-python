#!/usr/bin/env python3
"""
Module for python async
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine that takes in an integer argument (max_delay,
    with a default value of 10
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
