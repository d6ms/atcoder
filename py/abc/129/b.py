N = int(input())
W = list(map(int, input().split()))

ans = float('inf')
for T in range(1, N):
    sum1 = sum(W[:T + 1])
    sum2 = sum(W[T + 1:])
    ans = min(ans, abs(sum2 - sum1))

print(ans)