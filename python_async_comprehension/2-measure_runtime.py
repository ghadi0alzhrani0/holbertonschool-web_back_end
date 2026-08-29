#!/usr/bin/env python3
"""This module measures the runtime of parallel async comprehensions."""

import asyncio
import time

async_comprehension = __import__(
    "1-async_comprehension"
).async_comprehension


async def measure_runtime() -> float:
    """Run four async comprehensions concurrently and return the runtime."""
    start_time: float = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    return time.time() - start_time
