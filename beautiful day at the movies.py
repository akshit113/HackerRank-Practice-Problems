#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    count = 0
    for val in range(i, j + 1):
        str_i = str(val)
        rev = str_i[::-1]
        int_rev = int(rev)
        quot = abs(int_rev - val) / k
        if (quot == round(quot, 0)) | (quot == 0.0):
            count += 1

    print(count)
    return count


if __name__ == '__main__':
    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    print(rev)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
