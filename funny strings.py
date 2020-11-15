#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the funnyString function below.
def funnyString(s):
    rev = s[::-1]
    n = len(s)
    i = 0
    straight = []
    reversed = []
    while i <= n - 2:
        curr, next = ord(s[i]), ord(s[i + 1])
        rev_curr, rev_next = ord(rev[i]), ord(rev[i + 1])
        straight.append(abs(curr - next))
        reversed.append(abs(rev_curr - rev_next))
        i += 1
    if straight == reversed:
        ans = 'Funny'
    else:
        ans = 'Not Funny'
    return ans


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        print(result + '\n')
