from heapq import heapify, heappush, heappop

N, M = map(int, input().split())
A = list(map(lambda x: -int(x), input().split()))
heapify(A)

for _ in range(M):
    v = heappop(A)
    v /= 2
    heappush(A, v)

print(sum([int(-a) for a in A]))