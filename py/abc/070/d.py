N = int(input())
nl = [list() for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    nl[a].append((b, c))
    nl[b].append((a, c))
Q, K = map(int, input().split())

ans = [-1 for _ in range(N + 1)]
stack = [(K, -1, 0)]  # v, p, c
while len(stack) > 0:
    v, p, c = stack.pop()
    ans[v] = c
    for next_v, next_c in nl[v]:
        if next_v == p:
            continue
        stack.append((next_v, v, c + next_c))
for x, y in [tuple(map(int, input().split())) for _ in range(Q)]:
    print(ans[x] + ans[y])
