# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the gameOfThrones function below.
def gameOfThrones(s):
    n = len(s)
    from collections import Counter
    dc = Counter(s)
    vals = list(dc.values())
    odd = list(set([val % 2 == 1 for val in vals]))
    if len(odd) == 1:
        return 'YES'
    else:
        return 'NO'

    for ana in anagrams:
        if ana == s[::-1]:
            return 'YES'
    return 'NO'


if __name__ == '__main__':
    s = input()

    result = gameOfThrones(s)
    print(result)
