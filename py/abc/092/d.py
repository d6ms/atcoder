A, B = map(int, input().split())

grid = [['#' if i < 50 else '.'] * 100 for i in range(100)]


def gen(X):
    cnt = 0
    for i in range(1, 50, 2):
        for j in range(1, 100, 2):
            if cnt < X:
                yield i, j
                cnt += 1


for i, j in gen(A - 1):
    grid[i][j] = '.'
for i, j in gen(B - 1):
    grid[i + 50][j] = '#'

print(100, 100)
for row in grid:
    print(''.join(row))
