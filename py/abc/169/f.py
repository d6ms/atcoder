import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 998244353
INF = float('inf')


N, A = MI()
a = [0, *list(map(int, input().split()))]

# dp[i][j] := i番目までの数字を使って総和をjとする場合の数
# dp[i][j] = dp[i - 1][j - a[i]] + dp[i - 1][j]
dp = [[0] * (A + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(1, N + 1):
    for j in range(A + 1):
        if j - a[i] < 0:  # j - a[i] が負の数になってしまう時はa[i]を使用することはできない
            dp[i][j] = dp[i - 1][j]
            continue

        if a[i] == j:
            dp[i][j] = (pow(2, i, MOD) - 2 ) % MOD
        else:
            dp[i][j] = (dp[i - 1][j - a[i]] + dp[i - 1][j]) % MOD
print(dp[N][A])