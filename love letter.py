#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    orig = s
    if s == s[::-1]:
        return 0
    s = list(s)
    left = ord(s[0])
    right = ord(s[-1])
    count = 0

    cnt = 1
    while right > left:
        cnt += 1
        right = right - 1
        s[-1] = (chr(right))
        print(s)
        if s[::-1] == s:
            break



    while left > right:
        cnt += 1
        left = left - 1
        s[-1] = (chr(left))
        print(s)
        if s[::-1] == s:
            break

    return cnt



if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        print(str(result) + '\n')
