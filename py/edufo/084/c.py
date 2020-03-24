import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


n, m, k = MI()
XY = [tuple(MI()) for _ in range(k)]
for i in range(k):
    x, y = XY[i]
    dstx, dsty = MI()
    XY[i] = (dstx - x, dsty - y)

d = dict()
for x, y in XY:
    if d.get(x) is None:
        d[x] = [y]
    else:
        d[x].append(y)

X = list(map(lambda xy: xy[0], XY))
X.sort()
for x in X:
    d[x].sort()

ans = [('x', X[0]), ('y', d[X[0]][0])]
curx, cury = X[0], 0
for x in X:
