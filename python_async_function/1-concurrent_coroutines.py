#!/usr/bin/env python3
"""This module runs multiple asynchronous coroutines concurrently."""

import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Run wait_random multiple times and return delays in completion order."""
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []

    for coroutine in asyncio.as_completed(coroutines):
        delays.append(await coroutine)

    return delays
