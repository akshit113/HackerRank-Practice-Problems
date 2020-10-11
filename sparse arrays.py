#!/bin/python3

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    # print(strings)
    # print(queries)
    from collections import Counter
    res = []
    occurs = Counter(strings)

    for item in queries:
        if item in occurs.keys():
            res.append(occurs[item])
        else:
            res.append(0)
    return res


if __name__ == '__main__':
    #
    # strings_count = int(input())
    # # strings_count = 13
    #
    # strings = []
    #
    # for _ in range(strings_count):
    #     strings_item = input()
    #     strings.append(strings_item)
    #
    # queries_count = int(input())
    #
    # queries = []
    #
    # for _ in range(queries_count):
    #     queries_item = input()
    #     queries.append(queries_item)

    strings = ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn', 'sdaklfj', 'asdjf', 'na', 'asdjf', 'na', 'basdn', 'sdaklfj',
               'asdjf']
    queries = ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn']
    res = matchingStrings(strings, queries)

    print('')
