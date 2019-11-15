from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

d = defaultdict(int)
for a in A:
    d[a] += 1

ans = 0
for i, c in d.items():
    if c >= i:
        ans += c - i
    else:
        ans += c
print(ans)
