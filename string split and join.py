def split_and_join(line):
    ls = line.split(" ")
    out_str = "-".join(ls)
    return out_str


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
