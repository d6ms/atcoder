from collections import defaultdict

N, Q = map(int, input().split())

nl = [[] for _ in range(N + 1)]
for a, b in [tuple(map(int, input().split())) for _ in range(N - 1)]:
    nl[a].append(b)
    nl[b].append(a)
nl[0].append(1)

val = defaultdict(int)
for p, x in [tuple(map(int, input().split())) for _ in range(Q)]:
    val[p] += x

ans = [0 for _ in range(N + 1)]

stack = list()
stack.append((0, -1, 0))
while len(stack) > 0:
    v, p, cnt = stack.pop()
    cnt += val[v]
    ans[v] = cnt
    for next_v in nl[v]:
        if next_v != p:
            stack.append((next_v, v, cnt))

print(' '.join([str(a) for a in ans[1:]]))
