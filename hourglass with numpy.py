# !/bin/python3

# Complete the hourglassSum function below.
def hourglassSum(arr):
    # this solution uses numpy arrays
    import numpy as np
    maxsum = float('-inf')
    for i in range(0, 4):
        sub = arr[i:i + 3]
        # print(sub)
        nparr = np.array(sub)
        # print(nparr)
        for j in range(0, 4):
            sub = nparr[:, j:j + 3]
            isum = (np.sum(sub) - sub[1][0] - sub[1][2])
            if isum > maxsum:
                maxsum = isum

    return maxsum


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0],
    #        [0, 0, 1, 2, 4, 0]]

    result = hourglassSum(arr)

    print('test')
