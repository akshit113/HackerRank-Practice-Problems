T = int(input())


def check_subset(set_a, set_b):
    is_subset = True
    for item in set_a:
        if item not in set_b:
            is_subset = False
            return is_subset
    return is_subset


for i in range(T):
    a = int(input())
    set_a = set(map(int, input().split()))
    b = int(input())
    set_b = set(map(int, input().split()))
    print(check_subset(set_a, set_b))
