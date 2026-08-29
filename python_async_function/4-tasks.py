#!/usr/bin/env python3
"""This module runs multiple asyncio Tasks concurrently."""

import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Run multiple random-delay Tasks and return their results."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []

    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays
