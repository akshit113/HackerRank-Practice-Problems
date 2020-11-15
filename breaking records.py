def breakingRecords(scores):

    min_cache = 0
    max_cache = 0
    max_comp, min_comp = scores[0], scores[0]
    for val in scores[1:]:
        if val > max_comp:
            max_cache += 1
            max_comp = val
        if val < min_comp:
            min_comp = val
            min_cache += 1

    return [max_cache, min_cache]


if __name__ == '__main__':
    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    print('done')
