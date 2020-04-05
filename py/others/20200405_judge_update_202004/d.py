import sys
sys.setrecursionlimit(300000)
from math import gcd

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')

def bi(A, x):
    l = -1
    r = len(A) + 1
    while l + 1 < r:
        p = (l + r) // 2
        if gcd(x, A[p]) == 1:
            r = p
        else:
            l = p
    return r


N, Q = MI()
A = LMI()
S = LMI()

Agcd = [A[0]]
for i in range(1, N):
    Agcd.append(gcd(Agcd[-1], A[i]))

for s in S:
    g = gcd(Agcd[-1], s)
    if g > 1:
        print(g)
        continue
    idx = bi(Agcd, s)
    print(idx + 1)