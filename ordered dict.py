if __name__ == '__main__':

    n = int(input())
    # n = 9
    from collections import OrderedDict

    dc = OrderedDict()
    for i in range(0, n):
        inp = input().split()
        name, price = " ".join(inp[0:-1]), int(inp[-1])
        if name in dc.keys():
            dc[name] += price
        else:
            dc[name] = price

    for tup in dc.items():
        st = " ".join(list(map(str, tup)))
        print(st)
