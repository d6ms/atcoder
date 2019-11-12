H, W = map(int, input().split())
pic = [list(input()) for _ in range(H)]


def outer(i, j):
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if 0 <= (i + di) < H and 0 <= (j + dj) < W:
                yield i + di, j + dj


ans = [['.'] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if pic[i][j] == '#':
            if all([pic[x][y] == '#' for x, y in outer(i, j)]):
                ans[i][j] = '#'

restored = [['.'] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if pic[i][j] == '#':
            if all([ans[x][y] == '.' for x, y in outer(i, j)]):
                print('impossible')
                exit(0)

print('possible')
for l in ans:
    print(''.join(l))
