# import doctest

# TLEだがO(NK)ではあるので一旦ここまで


def solve(N, K, h):
    """
    >>> solve(5, 3, [10, 30, 40, 50, 20])
    30
    """
    # dp[i] = 足場iにたどり着くまでの最小コスト
    # dp[i] = min in dp[i - j] + |h[i] - h[i - j]|  for all j in [1, K]
    dp = [None] * (N + 1)
    dp[1] = 0
    dp[2] = abs(h[1] - h[0])
    for i in range(3, N + 1):
        arr = []
        for j in range(1, K + 1):
            if i - j < 1:
                continue
            arr.append(dp[i - j] + abs(h[i - 1] - h[i - 1 - j]))
        dp[i] = min(arr)
    return dp[N]


# doctest.testmod()
N, K = map(int, input().split())
h = list(map(int, input().split()))
print(solve(N, K, h))
