from collections import defaultdict
MOD = 1000000007
N = int(input())
A = list(map(int, input().split()))

ans = 1
d = defaultdict(int)
for a in A:
    if a == 0:
        ans *= 3 - d[a]
        d[a] += 1
        continue
    ans *= d[a - 1] - d[a]
    ans %= MOD
    d[a] += 1
print(ans)
