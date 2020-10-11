# !/bin/python3

# Complete the isBalanced function below.


def isBalanced(str):
    stack = []
    dicc = {'(': ')', '[': ']', '{': '}'}
    for char in str:
        if char in dicc.keys():  # opening char
            stack.append(char)
        elif char in dicc.values():  # closing char
            if dicc[stack[-1]] == char:  # check if closing char corresponds to last opening char
                stack.pop()
            else:
                return False
    return not len(stack)  # ret


if __name__ == '__main__':

    # t = int(input())
    t = 1

    for t_itr in range(t):
        # s = input()
        s = '{[(]}'

        result = isBalanced(s)
        print('')
