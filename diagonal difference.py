# from numpy import xrange

if __name__ == '__main__':
    n = int(input())
    # n = 3
    ls = []
    for i in range(0, n):
        row = list(map(int, input().split()))
        ls.append(row)
    arr = ls

    import numpy as np

    # print(ls)
    # ls = [[1, 2, 3], [4, 5, 6], [7, 8, 20]]

    # arr = [[11, 2, 4], [4, 5, 6], [10, 8, 12]]

    d = [arr[i][i] for i in iter(range(0, len(arr)))]  # diagonal
    cd = [arr[i][~i] for i in iter(range(0, len(arr)))]  # counter-diagonal
    print(abs(sum(d) - sum(cd)))
    print(cd)
