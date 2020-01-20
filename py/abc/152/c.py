N = int(input())
P = list(map(int, input().split()))

ans = 0
m = P[0]
for i, p in enumerate(P):
    if p <= m:
        ans += 1
    m = min(m, p)
print(ans)