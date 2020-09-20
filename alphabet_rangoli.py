def print_rangoli(size):
    import string
    alpha_list = list(string.ascii_lowercase)[0:size][::-1]
    chars = (size * 2) - 1
    dashes = chars - 1
    lpadded = chars + dashes

    str_list = []
    one_string = ''
    if len(alpha_list) == 1:
        one_string = alpha_list[0].center(lpadded, '-')
        print(one_string)
        return
    for index, item in enumerate(alpha_list):
        # print(item, index)
        prev = alpha_list[0:index]
        if len(prev) == 0:
            one_string = alpha_list[index].center(lpadded, '-')
            print(one_string)
        else:
            rev = prev[::-1]
            new_ls = prev + list(item) + rev
            temp_str = "-".join(new_ls)
            new_string = temp_str.center(lpadded, '-')
            print(new_string)
            str_list.append(new_string)
    if len(alpha_list) > 0:
        str_list.reverse()
        for i in str_list[1:]:
            print(i)
        print(one_string)


if __name__ == '__main__':
    # n = int(input())
    n = 1
    print_rangoli(n)
