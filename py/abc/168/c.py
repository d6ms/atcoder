import sys
from math import sqrt, cos, radians
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


A, B, H, M = MI()

d1 = (H * 60 + M) / 720
d2 = M / 60
theta = 360 * min(abs(d1 - d2), 1 - abs(d1 - d2))
ans = sqrt(A ** 2 + B ** 2 - 2 * A * B * cos(radians(theta)))
print(ans)
