import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N, M, Q = MI()
S = [tuple(MI())for _ in range(Q)]

ac = [0] * (M + 1)
status = [list() for _ in range(N + 1)]
for s in S:
    if s[0] == 2:
        _, n, m = s
        status[n].append(m)
        ac[m] += 1
    else:
        _, n = s
        ans = 0
        for m in status[n]:
            ans += N - ac[m]
        print(ans)