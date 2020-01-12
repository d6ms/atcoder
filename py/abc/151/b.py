from math import ceil
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

f = ((M * N) - sum(A))
if f > K:
    print(-1)
else:
    print(max(0, f))