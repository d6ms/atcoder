from heapq import heappush, heappop

N = int(input())
A = list(map(int, input().split()))

q = list()
for i, num in enumerate(A):
    heappush(q, (num, i + 1))

ans = list()
while len(q) > 0:
    _, num = heappop(q)
    ans.append(num)

print(' '.join([str(x) for x in ans]))
