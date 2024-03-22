#!/usr/bin/env python3
"""
asyncio module to implement asynchronous programming
"""
from time import perf_counter
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Function to measure the total execution
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elasped = perf_counter() - start

    return elasped / n
