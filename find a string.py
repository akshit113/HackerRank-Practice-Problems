def count_substring(string, sub_string):
    from itertools import combinations
    from collections import Counter

    res = [string[i: j] for i in range(len(string))
           for j in range(i + 1, len(string) + 1)]
    dc = Counter(res)
    cnt = dc[sub_string]
    return cnt


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
