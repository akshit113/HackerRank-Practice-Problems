#!/bin/python3


#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    # print(d)
    # print(arr)
    # arr = list(range(100000))
    # d = 100000
    res = []
    # for value in (arr[d:] + arr[0:d]):
    #     res.append(value)
    res = arr[d:]+arr[:d]



    return res


if __name__ == '__main__':
    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])
    n = 5

    # d = int(first_multiple_input[1])
    d = 4

    # arr = list(map(int, input().rstrip().split()))
    arr = [1, 2, 3, 4, 5]

    result = rotateLeft(d, arr)

    print('test')
