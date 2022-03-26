import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


H, W = MI()
A = [LMI() for _ in range(H)]
B = [LMI() for _ in range(H)]

max_k = 13000

# dp[i][j] = bitset(k) := マス(i, j)までの経路で偏りがkになることがあるか
dp = [[0] * W for _ in range(H)]
dp[0][0][abs(A[0][0] - B[0][0])] = True

for i in range(H):
    for j in range(W):
        p = abs(A[i][j] - B[i][j])
        for k in range(max_k):
            if i > 0:
                if abs(k - p) < max_k:
                    dp[i][j][k] |= dp[i - 1][j][abs(k - p)]
                if k + p < max_k:
                    dp[i][j][k] |= dp[i - 1][j][k + p]
            if j > 0:
                if abs(k - p) < max_k:
                    dp[i][j][k] |= dp[i][j - 1][abs(k - p)]
                if k + p < max_k:
                    dp[i][j][k] |= dp[i][j - 1][k + p]
print(dp[H - 1][W - 1].index(True))
