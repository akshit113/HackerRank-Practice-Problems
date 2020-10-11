ls = list(map(int, input().split()))

m, d, y = ls[0], ls[1], ls[2]
from datetime import datetime

d = datetime(month=m, day=d, year=y)
print(d.strftime('%A').upper())
print()
