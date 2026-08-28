#!/usr/bin/env python3
"""This module calculates the length of each sequence in an iterable."""

from typing import Iterable, List, Sequence, Tuple


def element_length(
        lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return each sequence paired with its length."""
    return [(i, len(i)) for i in lst]
