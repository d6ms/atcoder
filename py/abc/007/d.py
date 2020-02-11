def digit_dp(N):
    l = len(N)

    # dp[i][smaller][fn] := i桁目までで4|9が現れた(fn)数字の数
    dp = [[[0] * 2 for _ in range(2)] for _ in range(l + 1)]
    dp[0][False][False] = 1

    for i in range(1, l + 1):
        N_i = int(N[i - 1])
        for smaller in [True, False]:
            for fn in [True, False]:
                for d in range((9 if smaller else N_i) + 1):
                    # 各フラグに寄与する条件を左辺に書く
                    # e.g. smaller は既にN未満である場合か、現在桁でN未満であることが確定した場合
                    dp[i][smaller or d < N_i][fn or d in [4, 9]] += dp[i - 1][smaller][fn]

    return dp[l][True][True] + dp[l][False][True]


A, B = map(int, input().split())
print(digit_dp(str(B)) - digit_dp(str(A - 1)))
