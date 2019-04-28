def solve(N, A):
    if len(list(filter(lambda x: x < 0, A))) % 2 == 0:
        return sum(map(abs, A))
    else:
        min_abs = min(map(abs, A))
        return sum(map(abs, A)) - 2 * min_abs


def solve_dp(N, A):
    """
    >>> N = 3
    >>> A = [-10, 5, -4]
    >>> solve_dp(N, A)
    19
    >>> N = 5
    >>> A = [10, -4, -8, -11, 3]
    >>> solve_dp(N, A)
    30
    """
    # 複数回同じインデックスを反転する意味はないので、各iについて反転回数は0, 1のいずれか
    # 考えられる結果の集合はN^2なので空間的には余裕
    # すべてのパターンをメモしながら動的計画法で解く

    # dp(i, j) = A_i-1までを確定とし、jによってA_iを反転させた場合のSUM(A_0 ~ A_i)の最大値
    dp = [[None, None] for _ in range(N)]
    for i in range(N - 1):
        if i == 0:
            dp[0][0] = A[0]
            dp[0][1] = -A[0]
            continue
        dp[i][0] = max(dp[i - 1][0] + A[i], dp[i - 1][1] - A[i])
        dp[i][1] = max(dp[i - 1][0] - A[i], dp[i - 1][1] + A[i])
    # i = N - 1の場合は反転操作は許されないので、可能なパターン2つを手作業で計算
    return max(dp[N - 2][0] + A[N - 1], dp[N - 2][1] - A[N - 1])


import doctest
doctest.testmod()

N = int(input())
A = list(map(int, input().split()))
print(solve_dp(N, A))
