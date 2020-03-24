import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


t = I()
for _ in range(t):
    n = I()
    G = [None] * n
    for i in range(n):
        _, *g = MI()
        G[i] = [x - 1 for x in g]

    k_married = set()
    d_married = set()
    for d, g in enumerate(G):
        for k in g:
            if k not in k_married:
                k_married.add(k)
                d_married.add(d)
                break

    if len(k_married) < n:
        print('IMPROVE')
        for i in range(n):
            if i not in d_married:
                print(i + 1, end=' ')
                break
        for i in range(n):
            if i not in k_married:
                print(i + 1)
                break
    else:
        print('OPTIMAL')