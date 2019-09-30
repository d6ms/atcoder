from heapq import heappop, heappush

N, M = map(int, input().split())
cost = [float('inf') for _ in range(N)]
kC = [None for _ in range(M)]
for k in range(M):
    a, b = map(int, input().split())
    C = list(map(int, input().split()))
    kC[k] = C
    for c in C:
        cost[c - 1] = min(cost[c - 1], a)

cost = [float('inf') for _ in range(N)]
seen = set()
for i, queue in enumerate(q):
    if len(queue) == 0:
        print(-1)
        exit(0)
    a, k = heappop(queue)
    if k in seen:
        continue
    else:
        cost[i] = a
        for c in kC[k]:
            cost[c - 1] = min(cost[c - 1], a)
        seen.add(k)
print(sum(cost))