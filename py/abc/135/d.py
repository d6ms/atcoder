MOD = 10 ** 9 + 7
S = input()
N = len(S)

# dp[i][j] := i桁目までで13で割ったあまりがjになるものの個数

dp = [[0] * 13 for _ in range(N + 1)]
if S[-1] == '?':
    for j in range(10):
        dp[1][j] = 1
else:
    dp[1][int(S[-1])] = 1

m = 1
for i in range(2, N + 1):
    m = m * 10 % 13
    for j in range(13):
        num = '?' if S[-i] == '?' else int(S[-i])
        for k in range(10):
            if num == '?' or k == num:
                d = k * m % 13
                dp[i][j] = (dp[i][j] + dp[i - 1][(13 + j - d) % 13]) % MOD

print(dp[N][5])
