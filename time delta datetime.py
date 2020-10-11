#!/bin/python3

# Complete the time_delta function below.
def time_delta(t1, t2):
    t1 = t1.split()
    t2 = t2.split()

    m1, d1, y1, [h, m, s], tz1 = t1[1], t1[2], t1[3], list(map(int, t1[4].split())), int(t1[5])
    print(m1, d1, y1, [h, m, s])
    print()
    return 0


if __name__ == '__main__':
    print('test')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        print('test')
