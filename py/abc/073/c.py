from collections import defaultdict

N = int(input())
A = [int(input()) for _ in range(N)]

d = defaultdict(int)
for a in A:
    d[a] += 1

ans = 0
for k, v in d.items():
    if v % 2 == 1:
        ans += 1
print(ans)
