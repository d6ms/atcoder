import sys
sys.setrecursionlimit(300000)
from collections import defaultdict

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')

N = I()
S = [input() for _ in range(N)]
M = I()
T = [input() for _ in range(M)]

d = defaultdict(int)
for s in S:
    d[s] += 1
for t in T:
    d[t] = max(0, d[t] - 1)

print(max(d.values()))