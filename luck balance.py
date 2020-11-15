#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the luckBalance function below.
def luckBalance(k, contests):
    from operator import itemgetter
    luck = 0
    print(contests)
    L = []
    T = []
    wins = []
    loss = []
    for [a, b] in contests:
        L.append(a)
        T.append(b)
        if b == 1:
            wins.append(a)
        else:
            loss.append(a)

    print(L)
    print(T)
    wins.sort()
    total_wins = T.count(1)

    if k >= total_wins:
        luck = sum(L)
    else:
        rm = total_wins - k
        more = wins[rm:]
        del_sum = wins[:rm]
        luck = sum(loss) + sum(more)-sum(del_sum)


    return luck


if __name__ == '__main__':
    # nk = input().split()
    #
    # n = int(nk[0])
    #
    # k = int(nk[1])
    #
    # contests = []
    #
    # for _ in range(n):
    #     contests.append(list(map(int, input().rstrip().split())))

    contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]
    k = 3
    result = luckBalance(k, contests)

    fptr.close()
