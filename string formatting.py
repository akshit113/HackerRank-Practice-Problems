def print_formatted(number):
    width = len(str(bin(number))) - 2
    for i in range(1, number + 1):
        print("%s %s %s %s" % (
        str(i).rjust(width, " "), str(oct(i))[2:].rjust(width, " "), hex(i)[2:].rjust(width, " ").upper(),
        bin(i)[2:].rjust(width, " ")))


if __name__ == '__main__':
    n = 17
    print_formatted(n)
