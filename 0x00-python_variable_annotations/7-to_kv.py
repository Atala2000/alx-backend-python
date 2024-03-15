#!/usr/bin/env python3
"""
TYpe and antonations
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple of a string and float
    Args:
        k (str): String value
        v (itn | float): Value of either int or float

        Returns:
            tuple[str, float]: key value pair with squared value
    """
    return (k, v**2)
