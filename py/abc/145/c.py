from itertools import combinations
from math import sqrt

N = int(input())
X = [0] * N
Y = [0] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

d = 0
cnt = 0
for i, j in combinations(range(N), 2):
    print(i, j)
    dist = sqrt((X[j] - X[i]) ** 2 + (Y[j] - Y[i]) ** 2)
    d += dist
    cnt += 1
print((d / cnt) * 8)