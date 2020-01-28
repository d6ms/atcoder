H, N = map(int, input().split())

# dp[i][j] = 魔法iまでからダメージの総和がj以上になるように選んだ時の魔力の最小値
# dp[i][j] = min(dp[i][j - a] + b, dp[i - 1][j])

# この形式の初期化はTLEする
# dp = [[float('inf') for _ in range(H + 1)] for _ in range(N + 1)]
dp = [[float('inf')] * (H + 1)] * (N + 1)
for i in range(N + 1):
    dp[i][0] = 0
for i in range(1, N + 1):
    a, b = map(int, input().split())
    for j in range(H + 1):
        dp[i][j] = min(dp[i][max(0, j - a)] + b, dp[i - 1][j])
print(dp[N][H])