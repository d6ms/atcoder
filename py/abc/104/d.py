MOD = 10 ** 9 + 7
S = input()

# dp[i][φ or 'A' or 'AB' or 'ABC'] := 先頭からi桁までに含まれる φ数、A数、AB数、ABC数 の数
# 便宜上 φ: 0, 'A': 1, 'AB': 2, 'ABC': 3と表現する
dp = [[0 for _ in range(4)] for _ in range(len(S) + 1)]
dp[0][0] = 1

for i in range(len(S)):
    if S[i] == '?':
        for j in range(4):
            dp[i + 1][j] = dp[i][j] * 3 % MOD
    else:
        for j in range(4):
            dp[i + 1][j] = dp[i][j]
    if S[i] in ['A', '?']:
        dp[i + 1][1] += dp[i][0]
    if S[i] in ['B', '?']:
        dp[i + 1][2] += dp[i][1]
    if S[i] in ['C', '?']:
        dp[i + 1][3] += dp[i][2]

print(dp[len(S)][3] % MOD)
