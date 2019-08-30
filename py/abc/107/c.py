N, K = map(int, input().split())
x = list(map(int, input().split()))

ans = float('inf')
for i in range(N - K + 1):
    l = x[i]
    r = x[i + K - 1]
    ans = min(ans, abs(l) + abs(r - l))
    ans = min(ans, abs(r) + abs(r - l))
print(ans)
