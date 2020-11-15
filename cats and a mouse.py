#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the gemstones function below.
def gemstones(arr):
    chars = "".join(arr)
    unq = list(set(chars))
    l = 0
    for ch in chars:
        if ch in all(string for string in arr):
            l += 1

    return l


if __name__ == '__main__':

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)
    print(str(result) + '\n')

    fptr.close()
