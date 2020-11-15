s = input()
# s = 'Sorting1234'
lowers = []
uppers = []
odd = []
even = []
from string import ascii_lowercase, ascii_uppercase

for ch in s:
    if ch in ascii_lowercase:
        lowers.append(ch)
    elif ch in ascii_uppercase:
        uppers.append(ch)
    elif int(ch) % 2 == 0:
        even.append(ch)
    elif int(ch) % 2 == 1:
        odd.append(ch)

lowers.sort()
uppers.sort()
odd.sort()
even.sort()
#
# print(lowers)
# print(odd)
l = lowers + uppers + odd + even
# print(l)
print("".join(l))
# print('')