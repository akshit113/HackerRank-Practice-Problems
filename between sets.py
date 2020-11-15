#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    b.sort()
    i = 0
    factors = [1]
    while i <= len(b) - 1:
        y = b[i]
        x = b[0:i] + b[i + 1:]
        res = [i % y for i in x]
        s = sum(res)
        if s == 0:
            factors.append(y)
        i += 1
    fact = max(factors)
    print(fact)


if __name__ == '__main__':
    # first_multiple_input = input().rstrip().split()
    # n = int(first_multiple_input[0])
    # m = int(first_multiple_input[1])
    # arr = list(map(int, input().rstrip().split()))
    # brr = list(map(int, input().rstrip().split()))
    arr = [2, 4]
    brr = [16, 32, 96]
    print(arr)
    print(brr)
    total = getTotalX(arr, brr)
