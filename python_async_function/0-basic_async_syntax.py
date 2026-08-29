#!/usr/bin/env python3
"""This module provides an asynchronous coroutine with a random delay."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay and return the delay duration."""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
