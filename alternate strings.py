#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    dels = 0
    i = 0
    while i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            dels += 1
            s = s[0: i] + s[i + 1:]
        else:
            i += 1

    return dels


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        print(str(result) + '\n')

    # fptr.close()
