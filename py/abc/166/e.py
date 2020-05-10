import sys
sys.setrecursionlimit(300000)
from collections import defaultdict

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N = I()
A = LMI()

d = defaultdict(int)
for i, a in enumerate(A):
    d[-a + i + 1] += 1

ans = 0
for i, a in enumerate(A):
    c = d[a + i + 1]
    if c > 0:
        ans += c
print(ans)
