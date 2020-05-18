import sys
sys.setrecursionlimit(300000)
from fractions import gcd
from collections import defaultdict

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N = I()
d = defaultdict(int)
zero = 0
for i in range(N):
    a, b = MI()
    if a == 0 and b == 0:
        zero += 1
        continue
    g = gcd(a, b)
    a, b = a // g, b // g
    minus = (-1) ** ((a < 0) + (b < 0))
    d[(minus * abs(a), abs(b))] += 1

ans = 1
seen = set()
for a, b in d:
    if (a, b) not in seen:
        if (a, b) in [(1, 0), (0, 1)]:
            ainv, binv = b, a
        else:
            ainv, binv = b * (1 if a < 0 else -1), abs(a)
        lans = (2 ** d[(a, b)] - 1)
        lans += (2 ** d[(ainv, binv)] - 1) if d.get((ainv, binv)) is not None else 0
        lans += 1
        ans = ans * lans % MOD
        seen.add((a, b))
        seen.add((ainv, binv))
ans = (ans + zero) % MOD
print((ans + MOD - 1) % MOD)
