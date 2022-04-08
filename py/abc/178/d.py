MOD = 10 ** 9 + 7

S = int(input())
dp = [0] * (S + 1)
dp[0] = 1
for i in range(1, S + 1):
    dp[i] = sum(dp[:max(0, i - 2)]) % MOD
print(dp[S])