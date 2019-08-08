H, W = map(int, input().split())
canvas = list()
canvas.append(['.' for _ in range(W + 2)])
for _ in range(H):
    r = ['.']
    for c in input():
        r.append(c)
    r.append('.')
    canvas.append(r)
canvas.append(['.' for _ in range(W + 2)])

for i in range(len(canvas)):
    row = canvas[i]
    for j in range(len(row)):
        cell = row[j]
        if cell == '#':
            if '#' in [canvas[i - 1][j], canvas[i + 1][j], canvas[i][j - 1], canvas[i][j + 1]]:
                continue
            else:
                print('No')
                exit(0)
print('Yes')