S = input()

# dp[i][j] := i桁目までで13で割ったあまりがjになるものの個数
# dp[i + 1][j] := S[i + 1] +
#           3        8

dp = [[0 for _ in range(13)] for _ in range(len(S))]
if S[-1] == '5':
    dp[1][5] = 1
elif S[-1] == '?':
    dp[1] = [1 for _ in range(10)]

for i in range(2, len(S)):
