import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N = I()
R = []
B = []
for _ in range(N):
    X, C = input().split()
    if C == 'R':
        R.append(int(X))
    else:
        B.append(int(X))
R.sort()
B.sort()
for r in R:
    print(r)
for b in B:
    print(b)