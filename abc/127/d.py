# 問題の順序通りの書き換えをそのまま実装すると O(MN^2)
# heapで高速化しつつ O(MNlogN) で実装したけどだめでした

from heapq import heappush, heappop, heapify

N, M = map(int, input().split())
A = list(map(int, input().split()))

heapify(A)
for j in range(M):
    B, C = map(int, input().split())
    cnt = 0
    while cnt < B:
        a = heappop(A)
        if a < C:
            heappush(A, C)
            cnt += 1
        else:
            heappush(A, a)
            break
print(sum(A))