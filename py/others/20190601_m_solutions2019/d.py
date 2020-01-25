from heapq import heapify, heappop
N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N - 1)]
C = list(map(int, input().split()))

M = sum(C) - max(C)

nl = [list() for i in range(N)]
for a, b in AB:
    nl[a - 1].append(b - 1)
    nl[b - 1].append(a - 1)

v0 = -1
mlen = 0
for i, n in enumerate(nl):
    if len(n) > mlen:
        mlen = len(n)
        v0 = i

q = [-c for c in C]
heapify(q)
ans = [0] * N
stack = [(v0, -1)]
while len(stack) > 0:
    v, p = stack.pop()
    c = heappop(q)
    ans[v] = -c
    for next_v in nl[v]:
        if next_v != p:
            stack.append((next_v, v))
print(M)
print(*ans)