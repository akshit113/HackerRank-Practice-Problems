#!/bin/python3

import os
import sys

from datetime import datetime, timedelta


def timeConversion(s):
    zone = s[-2:]
    ts = s[:-2].split(":")
    h, m, sec = tuple(map(int, ts))

    if zone == 'AM':
        if h == 12:
            ts = timedelta(hours=0, minutes=m, seconds=sec)
        else:
            ts = timedelta(hours=h, minutes=m, seconds=sec)

    else:
        if h == 12:
            ts = timedelta(hours=0, minutes=0, seconds=0) + timedelta(hours=h, minutes=m, seconds=int(sec))
        else:
            ts = timedelta(hours=12, minutes=0, seconds=0) + timedelta(hours=h, minutes=m, seconds=int(sec))

    dt = datetime.strptime(str(ts), "%H:%M:%S")
    dt = dt.time()
    print(str(dt))
    return str(dt)


#
# Write your code here.
#

if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()
    s = '12:00:00PM'
    result = timeConversion(s)

    # f.write(result + '\n')
    #
    # f.close()
