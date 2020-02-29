

# 普通のナップサックDP
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_B&lang=jp
def knapsack():
    N, W = map(int, input().split())
    v = [None] * (N + 1)
    w = [None] * (N + 1)
    for i in range(1, N + 1):
        v[i], w[i] = map(int, input().split())

    # dp[i][j] := i番目の品物までで重さjとなるように選んだときの価値の最大値
    # dp[i][j] := max(dp[i - 1][j - w] + v, dp[i - 1][j])
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(W + 1):
            if w[i] > j:  # 今選ぼうとしている品物の重さが制限jを超える場合には当然選べない
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j - w[i]] + v[i], dp[i - 1][j])
    print(dp[N][W])


# 個数制限なしナップサックDP
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_C&lang=jp
def knapsack_duplicate_items():
    N, W = map(int, input().split())
    v = [None] * (N + 1)
    w = [None] * (N + 1)
    for i in range(1, N + 1):
        v[i], w[i] = map(int, input().split())

    # dp[i][j] := i番目の品物までで重さjとなるように選んだときの価値の最大値
    # dp[i][j] := max(dp[i][j - w] + v, dp[i - 1][j])
    #                   ~~~ 遷移前にすでにi番目の品物が入っている可能性を考慮
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(W + 1):
            if w[i] > j:  # 今選ぼうとしている品物の重さが制限jを超える場合には当然選べない
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i][j - w[i]] + v[i], dp[i - 1][j])
    print(dp[N][W])


# 部分和問題
# 「配列a内の整数をいくつか用いて、その和をAとすることができるか」
def partial_sum():
    N = int(input())
    a = [0, *list(map(int, input().split()))]
    A = int(input())

    # dp[i][j] := i番目までの数字を使って総和をjとすることができるか (bool)
    # dp[i][j] = dp[i - 1][j - a[i]] or dp[i - 1][j]
    dp = [[False] * (A + 1) for _ in range(N + 1)]
    dp[0][0] = True

    for i in range(1, N + 1):
        for j in range(A + 1):
            if j - a[i] < 0:  # j - a[i] が負の数になってしまう時はa[i]を使用することはできない
                dp[i][j] = dp[i - 1][j]
                continue
            dp[i][j] = dp[i - 1][j - a[i]] or dp[i - 1][j]
    print(dp[N][A])


# 部分和数え上げ問題
# 「配列a内の整数をいくつか用いて、その和がAとなる組み合わせの数」
def partial_sum_count():
    MOD = 10 ** 9 + 7
    N = int(input())
    a = [0, *list(map(int, input().split()))]
    A = int(input())

    # dp[i][j] := i番目までの数字を使って総和をjとする場合の数
    # dp[i][j] = dp[i - 1][j - a[i]] + dp[i - 1][j]
    dp = [[0] * (A + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(1, N + 1):
        for j in range(A + 1):
            if j - a[i] < 0:  # j - a[i] が負の数になってしまう時はa[i]を使用することはできない
                dp[i][j] = dp[i - 1][j]
                continue
            dp[i][j] = (dp[i - 1][j - a[i]] + dp[i - 1][j]) % MOD
    print(dp[N][A])


# 桁DP
# N以下でいずれかの桁に3が現れる数字の数を数える
# https://qiita.com/pinokions009/items/1e98252718eeeeb5c9ab
def digit_dp(N):
    l = len(N)

    # dp[i][smaller][three] := i桁目までで3が現れた(three)数字の数
    dp = [[[0] * 2 for _ in range(2)] for _ in range(l + 1)]
    dp[0][False][False] = 1

    for i in range(1, l + 1):
        N_i = int(N[i - 1])
        for smaller in [True, False]:
            for three in [True, False]:
                for d in range((9 if smaller else N_i) + 1):
                    # 各フラグに寄与する条件を左辺に書く
                    # e.g. smaller は既にN未満である場合か、現在桁でN未満であることが確定した場合
                    dp[i][smaller or d < N_i][three or d == 3] += dp[i - 1][smaller][three]

    print(dp[l][True][True] + dp[l][False][True])


# 区間DP
# http://kutimoti.hatenablog.com/entry/2018/03/10/220819
# def segment_dp():
#     N = int(input())
#     W = list(map(int, input().split()))
#
#     # dp[l][r] := 区間[l, r)で取り除くことのできるブロックの数
#     #
#     for l in range(N):
#         for r in range(l + 2, N + 1):
#             pass


# LIS (最長増加部分列)の長さ
# https://qiita.com/python_walker/items/d1e2be789f6e7a0851e5
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_D&lang=jp
def lis(N, A):
    from bisect import bisect_left

    # dp[i] := 長さがi以下の部分列で作られる最長部分増加列の最後の要素の最小値
    dp = [-1]  # A[i] >= 0 なのでそれ以下の値を設定し、数列の単調性を保つ
    for a in A:
        if dp[-1] < a:
            dp.append(a)
        else:
            # LISテーブルが単調増加であるため、aに更新される場所は1箇所しかあり得ず、二分探索で決定できる
            idx = bisect_left(dp, a)
            dp[idx] = a
    print(len(dp) - 1)
