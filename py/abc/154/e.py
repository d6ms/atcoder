def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))


# dp[i][j] := 上からi桁目までで0でない数字がちょうどj個ある数字の数 (i+1桁目以降は0)
# dp[i][j] := dp[i - 1][j] + dp[i - 1][j - 1] * (D - 1)

N = input()
K = I()
dp = [[0] * (K + 1) for _ in range(len(N))]
dp[0][1] = int(N[0])

beki = 10 ** (len(N) - 1)
for i in range(1, len(N)):
    beki = beki // 10
    for j in range(K + 1):
        dp[i][j] += dp[i - 1][j] + dp[i - 1][j - 1] * int(N[i]) * beki
print(dp)
print(dp[len(N) - 1][K])