from collections import defaultdict

N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]

d = defaultdict(int)
for a in A:
    d[a] += 1

for i in range(1, N + 1):
    if d[i] > Q - K:
        print('Yes')
    else:
        print('No')
