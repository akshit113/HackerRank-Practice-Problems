if __name__ == '__main__':
    # k, m = input().split()
    # k, m = int(k), int(m)
    k, m = 3, 1000
    all_list = []
    for ls in range(1, k + 1):
        inps = input().split()
        inp = [int(x) for x in inps]
        all_list.append(inp[1:])

    # k, m = 3, 1000
    # all_list = [[2, 5, 4], [3, 7, 8, 9], [5, 5, 7, 8, 9, 10]]
    from itertools import combinations, product

    c = list(product(*all_list))
    maxm = 0
    for tup in c:
        sum_tup = 0
        for ele in tup:
            sum_tup += ele * ele
        sum_tup = sum_tup % m
        if sum_tup > maxm:
            maxm = sum_tup
    print(maxm)

    # print(c)
