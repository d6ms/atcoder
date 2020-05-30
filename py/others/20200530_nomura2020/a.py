import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


h1, m1, h2, m2, k = MI()
t = h2 * 60 + m2
s = h1 * 60 + m1
print(max(0, t-k-s))