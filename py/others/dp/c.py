# import doctest


def solve(N, abc):
    """
    >>> solve(3, [(10, 40, 70), (20, 50, 80), (30, 60, 90)])
    210
    """
    # dp[i][j] = i日目にjの活動を選んだ時の幸福度総和の最大値
    # 本日の活動を幸福度が高い順にx, y, zとして、
    # dp[i][j] = max(dp[i - 1][y] + x, dp[i - 1][z] + x, dp[i - 1][x] + y, dp[i - 1][z] + y)
    dp = [[None, None, None] for _ in range(N + 1)]
    a1, b1, c1 = abc[0]
    # a, b, c を 0, 1, 2と読み替える
    dp[1][0] = a1
    dp[1][1] = b1
    dp[1][2] = c1
    for i in range(2, N + 1):
        a, b, c = abc[i - 1]
        dp[i][0] = max(dp[i - 1][1] + a, dp[i - 1][2] + a)  # aを選ぶとき
        dp[i][1] = max(dp[i - 1][0] + b, dp[i - 1][2] + b)  # bを選ぶとき
        dp[i][2] = max(dp[i - 1][0] + c, dp[i - 1][1] + c)  # cを選ぶとき
    return max(dp[N][0], dp[N][1], dp[N][2])


# doctest.testmod()
N = int(input())
abc = [tuple(map(int, input().split())) for _ in range(N)]
print(solve(N, abc))
