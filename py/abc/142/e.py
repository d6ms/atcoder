from math import isinf

N, M = map(int, input().split())

a = [0 for _ in range(M + 1)]
k = [0 for _ in range(M + 1)]
for i in range(M):
    a_i, _ = map(int, input().split())
    a[i + 1] = a_i
    k_i = 0
    for c in map(int, input().split()):
        k_i = k_i | 2 ** (c - 1)
    k[i + 1] = k_i

# 各宝箱の開封状態をbitで管理し、その値をsとして保持するbitDP
# dp[i][s] := i番目の鍵まででsの状態を作るときの最小コスト
dp = [[float('inf') for _ in range(2 ** N)] for _ in range(M + 1)]
dp[0][0] = 0

for i in range(1, M + 1):
    for s in range(2 ** N):
        # i番目の鍵を使わない場合
        dp[i][s] = min(dp[i][s], dp[i - 1][s])
        # i番目の鍵を使う場合
        dp[i][s | k[i]] = min(dp[i][s | k[i]], dp[i - 1][s] + a[i])

ans = dp[M - 1][2 ** N - 1]
if isinf(ans):
    ans = -1
print(ans)