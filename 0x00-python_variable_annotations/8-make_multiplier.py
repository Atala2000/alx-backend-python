#!/usr/bin/env python3
"""
Antonation for a function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that returns a function
    Args:
        multiplier (int): digit to multiply
    Returns:
        function
    """

    def multiply(value: float) -> float:
        """
        Returns a multiplied value
        Args:
            value (int): Digit to mulitply
        Returns: float
        """
        return value * multiplier

    return multiply
