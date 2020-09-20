if __name__ == '__main__':
    n = int(input())
    inp = input().split()
    set_p = set([int(item) for item in inp])
    m = int(input())
    inp = input().split()
    set_q = set([int(item) for item in inp])

    un = set_q.intersection(set_p)
    print(len(un))
