import doctest


def solve(N, h):
    """
    >>> solve(4, [10, 30, 40, 20])
    30
    """
    # dp[i] = 足場iにたどり着くまでの最小コスト
    dp = [None] * (N + 1)
    dp[1] = 0
    dp[2] = abs(h[1] - h[0])
    for i in range(3, N + 1):
        dp[i] = min(dp[i - 2] + abs(h[i - 1] - h[i - 3]), dp[i - 1] + abs(h[i - 1] - h[i - 2]))
    return dp[N]


# doctest.testmod()
N = int(input())
h = list(map(int, input().split()))
print(solve(N, h))