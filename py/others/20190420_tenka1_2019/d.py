import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 998244353
INF = float('inf')

N = I()
A = [I() for _ in range(N)]

# max(R, G, B) < (R + G + B) / 2 となれば三角形が成立することを利用する
