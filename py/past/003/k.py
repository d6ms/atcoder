import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N, Q = MI()
par = ['T' + str(i) for i in range(N + 1)]
head = list(range(N + 1))

for s, d, x in [MI() for _ in range(Q)]:
    pparx = par[x]
    par[x] = head[d]
    head[d] = head[s]
    head[s] = pparx

memo = dict()
def table(x):
    if isinstance(x, str):
        return x[1:]
    if memo.get(x) is not None:
        return memo[x]
    ans = table(par[x])
    memo[x] = ans
    return ans

for i in range(1, N + 1):
    print(table(i))
