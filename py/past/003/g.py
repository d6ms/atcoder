import sys
sys.setrecursionlimit(300000)
from collections import deque

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N, X, Y = MI()
block = set()
for _ in range(N):
    x, y = MI()
    block.add((x, y))

q = deque([(0, 0, 0)])
seen = set()
seen.add((0, 0))
while len(q) > 0:
    x, y, d = q.popleft()
    if x == X and y == Y:
        print(d)
        exit(0)
    for (nx, ny) in [(x+1, y+1), (x, y+1), (x-1, y+1), (x+1, y), (x-1, y), (x, y-1)]:
        if -205 <= nx <= 205 and -205 <= ny <= 205:
            if (nx, ny) not in block and (nx, ny) not in seen:
               q.append((nx, ny, d + 1))
               seen.add((nx, ny))
print(-1)