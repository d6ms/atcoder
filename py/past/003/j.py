import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N, M = MI()
A = LMI()

children = [0] * N

def bi(children, x):
    l = -1
    r = len(children)
    while l + 1 < r:
        p = (l + r) // 2
        if x > children[p]:
            r = p
        else:
            l = p
    return r

for a in A:
    eater = bi(children, a)
    if eater == N:
        print(-1)
    else:
        print(eater + 1)
        children[eater] = a