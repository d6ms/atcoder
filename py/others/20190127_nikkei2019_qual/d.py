import sys
from collections import deque

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N, M = MI()

nl = [list() for _ in range(N + 1)]
rev = [list() for _ in range(N + 1)]
for _ in range(N - 1 + M):
    A, B = MI()
    nl[A].append(B)
    rev[B].append(A)

for i, l in enumerate(rev):
    if i > 0 and len(l) == 0:
        root = i
        break


ans = [-1] * (N + 1)
q = deque([(root, 0)])
while len(q) > 0:
    v, p = q.popleft()
    if ans[v] < 0:
        for next_v in nl[v]:
            q.append((next_v, v))
    ans[v] = p

for a in ans[1:]:
    print(a)