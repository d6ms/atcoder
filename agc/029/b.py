from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
A.sort()
d = defaultdict(int)
for a in A:
    d[a] += 1

cnt = 0
for a in reversed(A):
    if d[a] > 0:
        d[a] -= 1
        pair = (1 << a.bit_length()) - a
        if d[pair] > 0:
            cnt += 1
            d[pair] -= 1
print(cnt)
