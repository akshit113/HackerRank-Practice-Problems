def main():
    # n_input = int(input())
    # ls_input = list(map(int, input().split()))
    # print(n_input)
    # print(ls_input)
    # n_shoes = int(input())

    # dc = dict()
    from collections import defaultdict
    dc = defaultdict(list)

    # for i in range(0, n_shoes):
    #     shoe = list(map(int, input().split()))
    #     size, price = shoe[0], shoe[1]
    #     dc[size].append(price)

    dc = {6: [55, 45, 55], 4: [40], 18: [60], 10: [50]}
    ls_input = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
    amt = 0
    # for i in ls_input:
    #     if i in dc.keys():
    #         prices = sorted(dc[i])
    #         if len(prices) == 0:
    #             del dc[i]
    #         else:
    #             p = prices[0]
    #             amt += p
    #             prices.remove(p)
    #             dc[i] = prices
    # print(amt)
    print(len(dc))

    for key, value in dc.items():
        if key in ls_input:
            for val in value:
                if key in ls_input:
                    amt += val
                    ls_input.remove(key)
    print(amt)


if __name__ == '__main__':
    main()
