def swap_case(s):
    ls = ([ch.upper() if ch.islower() else ch.lower() for ch in s])
    new = ''
    for x in ls:
        new += str(x)
    return new


if __name__ == '__main__':
    s = "HackerRank.com presents \"Pythonist 2\"."
    result = swap_case(s)
    print(result)
