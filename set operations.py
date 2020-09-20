if __name__ == '__main__':

    n = int(input())
    s = set(map(int, input().split()))
    operations = int(input())
    for _ in range(0, operations):
        inp = input().split()
        if len(inp) >= 2:
            operation, operand = inp[0], int(inp[1])
            if operation == 'remove':
                s.remove(operand)
            elif operation == 'discard':
                s.discard(operand)

        else:
            operation = inp[0]
            if operation == 'pop':
                s.pop()

        # print(out_set)
    print(sum(s))
    #
    #
    # n = int(input())
    # ls = (input().split(" "))
    # out_set = set([int(item) for item in ls])
    # operations = int(input())
    # for _ in range(0, operations):
    #     inp = input().split()
    #     if len(inp) >= 2:
    #         operation, operand = inp[0], int(inp[1])
    #         if operation == 'remove':
    #             out_set.remove(operand)
    #         elif operation == 'discard':
    #             out_set.discard(operand)
    #
    #         # if operation == '':9
    #         #     pass
    #     else:
    #         operation = inp[0]
    #         if operation == 'pop':
    #             out_set.pop()
    #
    # # print(out_set)
    # print(sum(out_set))
