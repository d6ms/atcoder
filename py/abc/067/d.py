from collections import deque

N = int(input())
nl = [list() for _ in range(N + 1)]
for a, b in [tuple(map(int, input().split())) for _ in range(N - 1)]:
    nl[a].append(b)
    nl[b].append(a)

# (v, dist)
q = deque()
q.append((1, -1))
seen = set()
while len(q) > 0:
    v, dist = q.popleft()
    if v == N:
        break
    seen.add(v)
    for next_v in nl[v]:
        if next_v not in seen:
            q.append((next_v, dist + 1))
shared = dist

# v, p, cnt
q = deque()
q.append((N, 0, -1))
while len(q) > 0:
    v, p, cnt = q.popleft()
    cnt += 1
    for next_v in nl[v]:
        if next_v not in seen and next_v != p:
            q.append((next_v, v, cnt + 1))
s_back = max(0, cnt)

f_back = N - 2 - shared - s_back

if shared % 2 == 0:
    if f_back <= s_back:
        print('Snuke')
    else:
        print('Fennec')
else:
    if s_back <= f_back:
        print('Fennec')
    else:
        print('Snuke')

