import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N, M, Q = MI()
adj = [list() for _ in range(N)]
for _ in range(M):
    u, v = MI()
    adj[u - 1].append(v - 1)
    adj[v - 1].append(u - 1)
C = LMI()
for q in [input() for _ in range(Q)]:
    if q.startswith('1'):
        _, x = map(int, q.split())
        x -= 1
        print(C[x])
        for v in adj[x]:
            C[v] = C[x]
    else:
        _, x, y = map(int, q.split())
        x -= 1
        print(C[x])
        C[x] = y