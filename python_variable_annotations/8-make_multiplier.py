#!/usr/bin/env python3
"""This module creates a function that multiplies floating-point values."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by the multiplier."""
    def multiply(value: float) -> float:
        """Multiply a floating-point value by the stored multiplier."""
        return value * multiplier

    return multiply
