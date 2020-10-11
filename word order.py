if __name__ == '__main__':
    n = int(input())
    ls = []
    for i in range(n):
        ls.append(input())

    print(len(set(ls)))
    from collections import Counter
    c = Counter(ls)
    print(" ".join(map(str, c.values())))

