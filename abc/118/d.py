from math import isinf

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

m = [None, 2, 5, 5, 4, 5, 6, 3, 7, 6]

# 最大何桁作れるか

# dp[i] := ちょうど i 本のマッチ棒を使って、条件を満たす整数を作るときの最大桁数
# dp[i + 1] = max(dp[i - m[j]] + 1) for all j in A

dp = [float('-inf') for _ in range(N + 1)]
dp[0] = 0

for i in range(1, N + 1):
    for num in A:
        if i - m[num] >= 0:
            dp[i] = max(dp[i], dp[i - m[num]] + 1)

matches = N
ans = ''
for _ in range(dp[N]):
    for a in A:
        if matches - m[a] < 0:
            continue
        if dp[matches - m[a]] == dp[matches] - 1:
            matches -= m[a]
            ans += str(a)
            break

print(ans)
