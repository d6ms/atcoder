# ARC 029 C
# プリム法の実装 この実装だと遅くてTLEになってしまうが。。。
from heapq import heappush, heappop


N, M = map(int, input().split())
c = [int(input()) for _ in range(N)]
ABR = [tuple(map(int, input().split())) for _ in range(M)]

# 交易所が設置されている頂点0を追加し、交易所の設置コストをその頂点と結ぶ辺のコストと考えれば、単純なMST問題にできる
# 0を最初の頂点としてPrim法を実装する
added = [False for _ in range(N + 1)]
added[0] = True

q = list()
for i in range(N):
    heappush(q, (c[i], 0, i + 1))

mst = list()
while len(q) != 0:
    cost, src, dst = heappop(q)

    if added[src] and added[dst]:
        continue

    mst.append((src, dst, cost))
    if added[src] == 1:
        added[dst] = 1
        for s, d, c in ABR:
            if s == dst or d == dst:
                heappush(q, (c, s, d))
    elif added[dst] == 1:
        added[src] = 1
        for s, d, c in ABR:
            if s == src or d == src:
                heappush(q, (c, s, d))

total_cost = 0
for src, dst, cost in mst:
    total_cost += cost
print(total_cost)
