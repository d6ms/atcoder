H, W, D = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

d = [None for _ in range(H * W + 1)]
for i in range(H):
    for j in range(W):
        d[A[i][j]] = (i, j)

cumsum = [0 for _ in range(H * W + 1)]
for m in range(1, D + 1):
    i = m
    while i <= H * W:
        if i - D <= 0:
            i += D
            continue
        x1, y1 = d[i - D]
        x2, y2 = d[i]
        dist = abs(x2 - x1) + abs(y2 - y1)
        cumsum[i] = cumsum[i - D] + dist
        i += D

Q = int(input())
LR = [tuple(map(int, input().split())) for _ in range(Q)]
for L, R in LR:
    print(cumsum[R] - cumsum[L])
