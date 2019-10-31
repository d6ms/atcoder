from collections import defaultdict

N, M = map(int, input().split())
d = defaultdict(int)
for a, b in [tuple(map(int, input().split())) for _ in range(M)]:
    d[a] += 1
    d[b] += 1

if all([i % 2 == 0 for i in d.values()]):
    print('YES')
else:
    print('NO')
