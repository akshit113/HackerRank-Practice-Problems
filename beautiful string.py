#!/bin/python3

# Complete the beautifulBinaryString function below.
def beautifulBinaryString(b):
    ct = 0
    b = list(b)
    n = len(b)
    for i in range(0, n - 2):
        temp = b[i:i + 3]
        st = "".join(temp)
        if st == '010':
            b[i + 2] = '1'
            temp = b[i:i + 3]
            st = "".join(temp)
            print(st)
            ct += 1
    return ct


if __name__ == '__main__':
    # b = input()
    b = '0101010'
    result = beautifulBinaryString(b)

    print(result)
