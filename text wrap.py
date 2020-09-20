import textwrap


def wrap(string, max_width):
    out = ''
    for i in range(0, len(string)):
        if i % max_width == 0:
            print(string[i:i + max_width])
    return out


if __name__ == '__main__':
    # string, max_width = input(), int(input())
    string, max_width = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4
    result = wrap(string, max_width)
    print(result)
