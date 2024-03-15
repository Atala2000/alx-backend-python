#!/usr/bin/env python3
"""
Returns a list
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list
    Args:
        lst (list): list

    Returns:
        a list
    """
    return [(i, len(i)) for i in lst]
