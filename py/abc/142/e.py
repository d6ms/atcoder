from heapq import heappop, heappush

N, M = map(int, input().split())

q = [list() for _ in range(N)]
boxes = dict()
for k in range(M):
    a, b = map(int, input().split())
    C = list(map(int, input().split()))
    boxes[k] = C
    for c in C:
        heappush(q[c - 1], (a, k))

q.sort(key=lambda x: len(x))

cost = [float('inf') for _ in range(N)]
seen = set()
for i, queue in enumerate(q):
    if len(queue) == 0:
        print(-1)
        exit(0)
    if len(queue) == 1:
        a, k = heappop(queue)
        if k in seen:
            continue
        else:
            cost[i - 1] = a
            for c in boxes[i]:
                cost[c - 1] = a
            seen.add(k)
print(cost)