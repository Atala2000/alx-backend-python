#!/usr/bin/env python3
"""
Import wait_random
"""
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    function (do not create an async function, use the regular
    function syntax to do this)
    """
    return asyncio.create_task(wait_random(max_delay))
