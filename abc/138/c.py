from heapq import heappush, heappop, heapify

N = int(input())
V = list(map(int, input().split()))

heapify(V)
while len(V) > 1:
    v1 = heappop(V)
    v2 = heappop(V)
    heappush(V, (v1 + v2) / 2)
ans = heappop(V)
print(ans)