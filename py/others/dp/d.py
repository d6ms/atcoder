# import doctest


def solve(N, W, wv):
    """
    >>> solve(3, 8, [(5, 60), (4, 50), (3, 30)])
    90
    """
    # dp[i][j] = 品物iまでから重さの総和がj以下になるように選んだ時の価値の最大値
    # dp[i][j] = max(dp[i - 1][j - w] + v, dp[i - 1][j])

    # 初期化
    dp = [[None for _ in range(W + 1)] for _ in range(N + 1)]
    for j in range(W + 1):
        w, v = wv[0]
        dp[1][j] = v if w <= j else 0

    for i in range(2, N + 1):
        w, v = wv[i - 1]
        for j in range(W + 1):
            if w > j:
                dp[i][j] = dp[i - 1][j]
                continue
            picked = dp[i - 1][j - w] + v
            ignored = dp[i - 1][j]
            dp[i][j] = max(picked, ignored)

    return dp[N][W]


# doctest.testmod()
N, W = map(int, input().split())
wv = [tuple(map(int, input().split())) for _ in range(N)]
print(solve(N, W, wv))