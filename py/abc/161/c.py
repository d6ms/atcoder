import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N, K = MI()

if N == K:
    print(0)
elif N > K:
    N = N - (N // K) * K
    if K < 2 * N:
        print(abs(N - K))
    else:
        print(N)
elif K < 2 * N:
    print(abs(N - K))
else:
    print(N)