# なぜかいくつかREになるけど、アルゴリズムの大枠は正しい

N = int(input())

neighbors = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    neighbors[u].append((v, w))
    neighbors[v].append((u, w))

ans = [None for _ in range(N)]


def dfs(v, p, c):
    ans[v - 1] = c
    for next_v, distance in neighbors[v]:
        if next_v == p:
            continue
        next_c = c if distance % 2 == 0 else 1 - c
        dfs(next_v, v, next_c)


dfs(1, -1, 0)
for e in ans:
    print(e)
