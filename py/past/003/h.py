import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N, L = MI()
X = set(MI())
T1, T2, T3 = MI()


dp = [INF] * (L + 1)
dp[0] = 0
for i in range(1, L + 1):
    dp[i] = dp[i - 1] + T1
    if i >= 2:
        dp[i] = min(dp[i], dp[i - 2] + T1 + T2)
    if i >= 4:
        dp[i] = min(dp[i], dp[i - 4] + T1 + T2 * 3)
    if i in X:
        dp[i] += T3
ans = min(
    dp[L],
    dp[L - 1] + T1 // 2 + T2 // 2,
    dp[L - 2] + T1 // 2 + T2 + T2 // 2,
    dp[L - 3] + T1 // 2 + T2 * 2 + T2 // 2
)
print(ans)