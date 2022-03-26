import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 998244353
INF = float('inf')


N, S = MI()
s = [0, *list(map(int, input().split()))]

# dp[i][j] := i番目までの数字を使って総和をjとする場合の数
# dp[i][j] = dp[i - 1][j - a[i]] + dp[i - 1][j]
dp = [[0] * (S + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(1, N + 1):
    for j in range(S + 1):
        if j - s[i] < 0:  # j - a[i] が負の数になってしまう時はa[i]を使用することはできない
            dp[i][j] = dp[i - 1][j] % MOD
            continue
        dp[i][j] = (dp[i - 1][j - s[i]] + dp[i - 1][j]) % MOD
print(dp[N][S])