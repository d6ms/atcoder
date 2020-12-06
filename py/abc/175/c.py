import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI0(): return map(lambda s: int(s) - 1, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
def LMI0(): return list(map(lambda s: int(s) - 1, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


X, K, D = MI()

if abs(X) >= K * D:
    print(abs(X) - K * D)
else:
    a = abs(abs(X) - (abs(X) // D) * D)
    K -= (abs(X) // D)
    if K % 2 == 0:
        print(a)
    else:
        print(abs(a - D))