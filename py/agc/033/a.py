import sys
sys.setrecursionlimit(300000)
from collections import deque

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


H, W = MI()
grid = [list(input()) for _ in range(H)]

seen = set()
q = deque()
for i in range(H):
    for j in range(W):
        if grid[i][j] == '#':
            q.append((i, j, 0))
            seen.add(i * W + j)
while len(q) > 0:
    h, w, d = q.popleft()
    for dh, dw in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        if 0 <= h + dh < H and 0 <= w + dw < W and (h + dh) * W + w + dw not in seen:
            q.append((h + dh, w + dw, d + 1))
            seen.add((h + dh) * W + w + dw)
print(d)