from itertools import combinations, permutations

N, C = map(int, input().split())
D = [[0] * (C + 1)]
for _ in range(C):
    a = [0]
    a.extend(list(map(int, input().split())))
    D.append(a)
c = [list(map(int, input().split())) for _ in range(N)]

# color[g][c] := グループgのうち、色cであるグリッドの数
color = [[0 for _ in range(C + 1)] for _ in range(3)]
for row in range(1, len(c) + 1):
    for col in range(1, len(c[row - 1]) + 1):
        g = (row + col) % 3
        color[g][c[row - 1][col - 1]] += 1


def count():
    for x, y, z in combinations(range(C), 3):
        for a, b, c in permutations([x + 1, y + 1, z + 1]):
            yield a, b, c


ans = float('inf')
for c1, c2, c3 in count():
    cost = 0
    for i in range(1, C + 1):
        cost += color[0][i] * D[i][c1]
    for i in range(1, C + 1):
        cost += color[1][i] * D[i][c2]
    for i in range(1, C + 1):
        cost += color[2][i] * D[i][c3]
    ans = min(ans, cost)

print(ans)
