N = int(input())
A = list(map(lambda a: abs(int(a) % 4 - 2), input().split()))

odd = len(list(filter(lambda x: x == 1, A)))
even2 = len(list(filter(lambda x: x == 0, A)))
even4 = len(list(filter(lambda x: x == 2, A)))

even2 %= 2

if odd + (even2 % 2) <= even4 + 1:
    print('Yes')
else:
    print('No')
