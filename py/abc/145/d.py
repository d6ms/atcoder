X, Y = map(int, input().split())

# dp[i][j] := マス(i, j) に移動させる方法の数
dp = [[0 for _ in range(Y + 1)] for _ in range(X + 1)]
dp[0][0] = 1

for i in range(1, X + 1):
    for j in range(1, Y + 1):
        if j - 2 >= 0:
            dp[i][j] += dp[i - 1][j - 2]
        if i - 2 >= 0:
            dp[i][j] += dp[i - 2][j - 1]

print(dp[X][Y])
