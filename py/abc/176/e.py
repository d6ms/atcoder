import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI0(): return map(lambda s: int(s) - 1, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
def LMI0(): return list(map(lambda s: int(s) - 1, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


H, W, M = MI()
rows = [0] * H
cols = [0] * W
bombs = []
for _ in range(M):
    h, w = MI0()
    rows[h] += 1
    cols[w] += 1
    bombs.append((h, w))

mrows = max(rows)
rows = set(i for i, row in enumerate(rows) if row == mrows)
mcols = max(cols)
cols = set(i for i, col in enumerate(cols) if col == mcols)


cnt = 0
for h, w in bombs:
    if h in rows and w in cols:
        cnt += 1
if len(rows) * len(cols) <= cnt:
    print(mrows + mcols - 1)
else:
    print(mrows + mcols)