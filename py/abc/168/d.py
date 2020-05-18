import sys
from collections import deque
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N, M = MI()
adj = [list() for _ in range(N)]
for _ in range(M):
    a, b = MI()
    a, b, = a - 1, b - 1
    adj[a].append(b)
    adj[b].append(a)

q = deque()
q.append((0, -1))
seen = set()
seen.add(0)
ans = [0] * N
while len(q) > 0:
    v, p = q.popleft()
    ans[v] = p
    for nxt in adj[v]:
        if nxt not in seen:
            q.append((nxt, v))
            seen.add(nxt)
print('Yes')
for a in ans[1:]:
    print(a + 1)