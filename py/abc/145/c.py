from itertools import permutations
from math import sqrt

N = int(input())
X = [0] * N
Y = [0] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

d = []
for route in permutations(range(N), N):
    dist = 0
    for i, j in zip(range(N - 1), range(1, N)):
        dist += sqrt((X[route[j]] - X[route[i]]) ** 2 + (Y[route[j]] - Y[route[i]]) ** 2)
    d.append(dist)
print(sum(d) / len(d))
