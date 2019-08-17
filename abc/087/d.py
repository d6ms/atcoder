import sys
sys.setrecursionlimit(300000)

N, M = map(int, input().split())
nl = [[] for _ in range(N + 1)]
for _ in range(M):
    L, R, D = map(int, input().split())
    nl[L].append((R, D))
    nl[R].append((L, -D))

seen = [None for _ in range(N + 1)]


def dfs(v, d):
    seen[v] = d
    for next_v, D in nl[v]:
        next_d = d + D
        if seen[next_v] is None:
            dfs(next_v, next_d)
        else:
            if seen[next_v] != next_d:
                print('No')
                exit(0)


for v in range(1, N + 1):  # すべての連結成分に対してDFS
    if seen[v] is None:
        dfs(v, 0)

print('Yes')
