from typing import List
import logging

log = logging.basicConfig()


def diagonal_difference(arr: List[List[int]]) -> int:
    primary = 0
    secondary = 0
    len_rows = len(arr)
    len_cols = len(arr[0])
    for i in range(len_rows):
        for j in range(len_cols):
            if i == j:
                primary += arr[i][j]
            if (len_rows - 1 - i) == j:
                secondary += arr[i][j]
    return abs(primary - secondary)
