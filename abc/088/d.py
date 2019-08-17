from collections import deque


H, W = map(int, input().split())
S = [input() for _ in range(H)]

min_dist = -1
seen = set()
q = deque()
q.append((0, 0, 0))  # (i, j, dist)
while len(q) > 0:
    i, j, dist = q.popleft()
    if i == H - 1 and j == W - 1:
        min_dist = dist
        break
    if i > 0 and S[i - 1][j] == '.' and (i - 1, j) not in seen:
        seen.add((i - 1, j))
        q.append((i - 1, j, dist + 1))
    if j > 0 and S[i][j - 1] == '.' and (i, j - 1) not in seen:
        seen.add((i, j - 1))
        q.append((i, j - 1, dist + 1))
    if i < H - 1 and S[i + 1][j] == '.' and (i + 1, j) not in seen:
        seen.add((i + 1, j))
        q.append((i + 1, j, dist + 1))
    if j < W - 1 and S[i][j + 1] == '.' and (i, j + 1) not in seen:
        seen.add((i, j + 1))
        q.append((i, j + 1, dist + 1))

if min_dist == -1:
    print(-1)
else:
    b = 0
    for r in S:
        for c in r:
            if c == '#':
                b += 1
    print(H * W - min_dist - b - 1)