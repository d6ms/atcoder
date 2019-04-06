import math


def solve(N, limits):
    min_limit = min(limits)
    return 4 + math.ceil(N / min_limit)


N = int(input())
limits = []
for _ in range(5):
    limits.append(int(input()))
print(solve(N, limits))
