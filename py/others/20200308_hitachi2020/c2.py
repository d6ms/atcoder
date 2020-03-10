import sys
from collections import deque

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7


N = I()
nl = [list() for _ in range(N)]
for _ in range(N - 1):
    a, b = MI()
    nl[a - 1].append(b - 1)
    nl[b - 1].append(a - 1)

g = {
    0: list(),
    1: list(),
    2: list()
}
q = deque()
q.append((0, -1, 0))
while len(q) > 0:
    v, p, d = q.popleft()
    g[d % 3].append(v)
    for next_v in nl[v]:
        if next_v != p:
            q.append((next_v, v, d + 1))

elnum = list(map(len, g.values()))
elnum.sort()
l, m = divmod(N, 3)
if (m == 0 and [l, l, l] != elnum) or (m == 1 and [l, l, l + 1] != elnum) or (m == 2 and [l, l + 1, l + 1] != elnum):
    print(-1)
    exit(0)


ans = [0] * N
g = list(g.values())
g.sort(key=lambda e: len(e))
for i, v in enumerate(g[2]):
    ans[v] = 3 * i + 1
for i, v in enumerate(g[1]):
    ans[v] = 3 * i + 2
for i, v in enumerate(g[0]):
    ans[v] = 3 * (i + 1)
print(' '.join([str(x) for x in ans]))
