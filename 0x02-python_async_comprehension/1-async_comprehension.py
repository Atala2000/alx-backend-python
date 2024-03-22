#!/usr/bin/env python3
"""
Import async_generator from the previous task
"""
import asyncio
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    coroutine called async_comprehension that takes no arguments.
    The coroutine will collect 10 random
    """
    numbers = [number async for number in async_generator()]
    return numbers
