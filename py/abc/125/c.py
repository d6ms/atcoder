from fractions import gcd


N = int(input())
A = list(map(int, input().split()))

# l[i] := [0, i]の数のGCDメモ
l = [None for _ in range(N)]
l[0] = A[0]
for i in range(1, N):
    l[i] = gcd(l[i - 1], A[i])

# r[i] := [i, N - 1]の数のGCDメモ
r = [None for _ in range(N)]
r[N - 1] = A[N - 1]
for i in reversed(range(N - 1)):
    r[i] = gcd(r[i + 1], A[i])

ans = 0
for i in range(N):
    if i == 0:
        ans = max(ans, r[1])
    elif i == N - 1:
        ans = max(ans, l[N - 2])
    else:
        ans = max(ans, gcd(l[i - 1], r[i + 1]))
print(ans)
