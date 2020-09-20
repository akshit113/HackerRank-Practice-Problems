if __name__ == '__main__':
    m = int(input())
    input_m = input()
    temp = input_m.split(" ")
    inp = [int(item) for item in temp]
    m_set = set(inp)
    # m_set = {1, 2, 4}
    n = int(input())
    input_n = input()
    temp = input_n.split(" ")
    inp = [int(item) for item in temp]
    n_set = set(inp)
    # n_set = {1, 2, 3, 4, 5, 6}

    ls = sorted(m_set.symmetric_difference(n_set))
    [print(val) for val in ls]

    print(ls)
