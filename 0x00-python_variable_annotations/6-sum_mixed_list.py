#!/usr/bin/env python3
"""
Antonation for mixed values
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ "
    Union list for a mixed list
    Args:
        mxd_lst (list): mixed list
    Returns:
            float
    """
    return float(sum(mxd_lst))
