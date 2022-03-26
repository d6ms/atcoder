import sys
from collections import defaultdict

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N = I()
A, B = MI()
P = LMI()

d = defaultdict(int)
for p in P:
    if p <= A:
        d[0] += 1
    elif A < p <= B:
        d[1] += 1
    else:
        d[2] += 1
print(min(d[0], d[1], d[2]))
