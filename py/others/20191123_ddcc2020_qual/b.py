import sys
from itertools import accumulate

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N = I()
A = LMI()

ans = INF
accum = list(accumulate(A))
for s in accum:
    t = accum[-1] - s
    ans = min(ans, abs(s - t))
print(ans)
