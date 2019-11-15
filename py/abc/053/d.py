from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

d = defaultdict(int)
for a in A:
    d[a] += 1

k = len(d)
if k % 2 == 0:
    print(k - 1)
else:
    print(k)
