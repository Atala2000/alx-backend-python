#!/usr/bin/env python3
"""
asyncio module to implement asynchronous programming
"""
import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    a new function task_wait_n. The code is nearly identical
    to wait_n
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
