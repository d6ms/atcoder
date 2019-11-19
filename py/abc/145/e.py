N, T = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]


def solve(N, W, wv):
    # dp[i][j] = 品物iまでから重さの総和がj以下になるように選んだ時の価値の最大値
    # dp[i][j] = max(dp[i - 1][j - w] + v, dp[i - 1][j])

    # 初期化
    dp = [[0 for _ in range(3001)] for _ in range(3001)]
    for j in range(W + 1):
        w, v = wv[0]
        dp[1][j] = v if w <= j else 0

    for i in range(2, N + 1):
        w, v = wv[i - 1]
        for j in range(W + 1):
            picked = dp[i - 1][j - w] + v
            ignored = dp[i - 1][j]
            dp[i][j] = max(picked, ignored)

    return dp[N][W]


print(solve(N, T, AB))