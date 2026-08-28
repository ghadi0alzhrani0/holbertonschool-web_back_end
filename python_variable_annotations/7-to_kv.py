#!/usr/bin/env python3
"""This module creates a tuple containing a key and a squared value."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple containing the string and the square of the value."""
    return (k, v ** 2)
