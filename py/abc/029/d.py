N = input()
l = len(N)

# 桁DPで数え上げ
# dp[i][smaller][j] := i桁目までで1がj回現れた数
dp = [[[0] * (l + 1) for _ in range(2)] for _ in range(l + 1)]
dp[0][False][0] = 1
for i in range(1, l + 1):
    N_i = int(N[i - 1])
    for smaller in [True, False]:
        for j in range(i + 1):
            for d in range((9 if smaller else N_i) + 1):
                if j + (1 if d == 1 else 0) <= l:
                    dp[i][smaller or d < N_i][j + (1 if d == 1 else 0)] += dp[i - 1][smaller][j]

ans = 0
for i in range(1, l + 1):
    ans += i * (dp[l][True][i] + dp[l][False][i])
print(ans)
