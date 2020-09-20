
from itertools import combinations_with_replacement
# ls = input().split()
ls = ['HACK', '2']
# out = []
inp, times = ls[0], int(ls[1])
total_out = []
# for i in range(1, times + 1):
a = combinations_with_replacement(inp, times)
a = list(a)
a = sorted(a)
out = []
for x in a:
    x = sorted(list(x))
    out.append("".join(x))
# total_out.append(sorted(out))

a = sorted(out)
for i in a:
    print(i)
print('test')
# ls = []
# for i in range(0, len(total_out)):
#     ls.extend(total_out[i])
# for i in ls:
#     print(i)