#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the gridChallenge function below.
def gridChallenge(grid):
    sorted_grid = []

    for row in grid:
        sorted_row = list(sorted(row))
        temp = ''.join(sorted_row)
        sorted_grid.append(temp)

    grid = sorted_grid
    print(grid)
    col_ans = True
    trans = list(zip(*grid))
    for row in trans:
        row = list(row)
        sorted_row = list(sorted(row))
        if list(row) != sorted_row:
            col_ans = False
            break

    if col_ans:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)
