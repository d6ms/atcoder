from collections import deque

N = int(input())
nl = [[] for _ in range(N + 1)]
i = 0
for a, b in [tuple(map(int, input().split())) for _ in range(N - 1)]:
    nl[a].append((b, i))
    nl[b].append((a, i))
    i += 1

print(max(map(len, nl)))

ans = [-1 for _ in range(N - 1)]
q = deque()
q.append((1, -1, -1))
while len(q) > 0:
    v, p, pc = q.popleft()
    color = 1
    for next_v, i in nl[v]:
        if next_v == p:
            continue
        if color == pc:
            color += 1
        ans[i] = color
        q.append((next_v, v, color))
        color += 1
for a in ans:
    print(a)
