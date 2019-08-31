# TLEなのでC++で書き直した
from itertools import combinations

N, K = map(int, input().split())
XY = []
X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    XY.append((x, y))
    X.append(x)
    Y.append(y)

X.sort()
Y.sort()
ans = float('inf')
for x1, x2 in combinations(X, 2):
    for y1, y2 in combinations(Y, 2):
        cnt = 0
        for x, y in XY:
            if x1 <= x <= x2 and y1 <= y <= y2:
                cnt += 1
        if K <= cnt:
            ans = min(ans, (x2 - x1) * (y2 - y1))
print(ans)