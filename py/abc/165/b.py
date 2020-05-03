import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


X = I()
d = 100
for i in range(1, 3761):
    d = int(d * 1.01)
    if d >= X:
        print(i)
        exit(0)
