import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


K, N = MI()
A = LMI()

m = 0
for i in range(N - 1):
    m = max(m, A[i + 1] - A[i])
m = max(m, K - A[-1] + A[0])
print(K - m)