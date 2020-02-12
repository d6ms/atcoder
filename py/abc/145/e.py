N, T = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]
AB.sort(key=lambda ab: ab[0])

# dp[i][j] := i番目の料理までから選んだときの、j分後における満足度の最大値
# dp[i][j] := max(dp[i - 1][j - A] + B, dp[i - 1][j])
dp = [[0] * (T + 1) for _ in range(N + 1)]
ans = 0
for i in range(1, N + 1):
    a, b = AB[i - 1]
    for j in range(T + 1):
        if j == T:
            a = 1
        if j - a < 0:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - a] + b, dp[i - 1][j])

print(dp[N][T])
