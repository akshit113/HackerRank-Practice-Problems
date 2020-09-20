def merge_the_tools(string, k):
    if k == 1:
        for char in list(string):
            print(char)
    else:
        import textwrap
        words = textwrap.wrap(string, k)
        print(len(words))
        for word in words:
            chars = list(word)
            temp = []
            for ch in chars:
                if ch not in temp:
                    temp.append(ch)
            print("".join(temp))


if __name__ == '__main__':
    string, k = 'AAAAAAAAAAAAAAA', 1
    # string, k = input(), int(input())

    merge_the_tools(string, k)
