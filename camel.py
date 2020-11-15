#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the camelcase function below.
def camelcase(s):

    from collections import Counter

    dc = Counter(s)
    new_dict = dict()
    for key, value in dc.items():
        if str(key).isupper():
            new_dict[key] = value
    s = sum(new_dict.values()) + 1
    return s


if __name__ == '__main__':
    # s = input()
    s = 'saveChangesInTheEditor'

    result = camelcase(s)

    print(result)
