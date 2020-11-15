#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the angryProfessor function below.
def angryProfessor(k, a):
    late = []
    early = []
    for i in a:
        if i > 0:
            late.append(i)
        else:
            early.append(i)

    if len(early) >= k:
        return 'NO'
    else:
        return 'YES'


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)
        print(result)
