import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N, K = MI()

ans = 0
for i in range(K, N + 1):
    M = ((N + 1) * i) - (i * (i + 1) // 2)
    m = (i * (i - 1) // 2)
    a = M - m + 1
    ans = (ans + a) % MOD
ans = (ans + 1) % MOD
print(ans)