#!/usr/bin/env python3
"""This module measures concurrent async comprehension runtime."""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Run four async comprehensions and return the elapsed time."""
    start_time: float = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    return time.perf_counter() - start_time
