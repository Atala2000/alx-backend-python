#!/usr/bin/env python3
"""
Antonation for a function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiply(value: float) -> float:
        return value * multiplier

    return multiply