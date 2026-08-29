#!/usr/bin/env python3
"""This module measures the average runtime of concurrent coroutines."""

import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Return the average execution time for wait_n."""
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time: float = time.time() - start_time
    return total_time / n
