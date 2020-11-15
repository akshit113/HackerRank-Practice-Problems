#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr = sorted(arr)
    n = len(arr)

    # [-7330761, -6461594, -3916237, -3620601, -357920, -20, 30, 266854, 6246457, 7374819]
    from collections import defaultdict
    dc = defaultdict(list)

    for i in range(n - 1):
        diff = abs(arr[i] - arr[i + 1])
        dc[diff].append(arr[i:i+2])

    # print(dc)
    min_sum = min(list(dc.keys()))
    flat_list = [str(item) for sublist in dc[min_sum] for item in sublist]


    return flat_list


if __name__ == '__main__':
    # n = int(input())

    # arr = list(map(int, input().rstrip().split()))
    # arr = [-7330761, -6461594, -3916237, -3620601, -357920, -20, 30, 266854, 6246457, 7374819]
    arr = [-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854, -520, -470]
    result = closestNumbers(arr)

    print(' '.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
