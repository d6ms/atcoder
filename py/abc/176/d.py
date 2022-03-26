import sys
sys.setrecursionlimit(300000)
from collections import deque

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI0(): return map(lambda s: int(s) - 1, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
def LMI0(): return list(map(lambda s: int(s) - 1, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


H, W = MI()
ch, cw = MI0()
dh, dw = MI0()
S = [input() for _ in range(H)]

# dp[i][j] := d
dp = [[INF] * W for _ in range(H)]
dp[ch][cw] = 0


seen = set()
seen.add(ch * W + cw)
while True:
    found = list()

    q = deque()
    q.append((ch, cw, 0))
    while len(q) > 0:
        x, y, d = q.popleft()

        q2 = deque()
        q2.append((x, y))
        while len(q2) > 0:
            i, j = q2.popleft()
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if not (0 <= i < H and 0 <= j < W) or S[ni][nj] == '#':
                    continue




    for nx, ny in [(x + 1, y)]