# 想定解法だが、重いケースでTLEなのでC++で書き直す
from heapq import heappush, heappop

N, Q = map(int, input().split())

event = list()
for _ in range(N):
    S, T, X = map(int, input().split())
    heappush(event, (S - X, 1, X))
    heappush(event, (T - X, -1, X))

D = [int(input()) for _ in range(Q)]
stop = set()
for d in D:
    while len(event) > 0:
        t, op, X = heappop(event)
        if t > d:
            heappush(event, (t, op, X))
            break
        if op == 1:
            stop.add(X)
        elif op == -1:
            stop.remove(X)
    ans = min(stop) if len(stop) > 0 else -1
    print(ans)
