if __name__ == '__main__':
    N = int(input())
    inp_list = []
    for i in range(N):
        inp_list.append(input())
    # inp_list = ['insert 0 5', 'insert 1 10', 'insert 0 6', 'print', 'remove 6', 'append 9', 'append 1', 'sort ',
    #             'print', 'pop', 'reverse', 'print']
    print(inp_list)
    out_list = []
    for item in inp_list:
        numbers = item.split()
        operation, operand = numbers[0], numbers[1:len(numbers)]
        operand = [int(x) for x in operand]
        if operation == 'insert':
            out_list.insert(operand[0], operand[1])
        elif operation == 'print':
            print(out_list)
        elif operation == 'remove':
            out_list.remove(operand[0])
        elif operation == 'append':
            out_list.append(operand[0])
        elif operation == 'sort':
            out_list = sorted(out_list)
        elif operation == 'pop':
            out_list.pop()
        elif operation == 'reverse':
            out_list.reverse()

    print('test')
