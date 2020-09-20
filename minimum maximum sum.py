if __name__ == '__main__':
    # stuff = map(int, ['1', '2', '3', '4', '5'])
    stuff = map(int, input().split())
    # stuff = [1, 2, 3, 4, 5]
    import itertools

    sum_arr = []
    for subset in itertools.combinations(stuff, 4):
        s = (sum(list(subset)))
        sum_arr.append(s)
    print(f'{min(sum_arr)} {max(sum_arr)}')
