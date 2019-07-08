N, M = map(int, input().split())

lower = 1
upper = N
for i in range(M):
    L, R = map(int, input().split())
    lower = max(L, lower)
    upper = min(R, upper)

ans = upper - lower + 1
ans = max(0, ans)
print(ans)