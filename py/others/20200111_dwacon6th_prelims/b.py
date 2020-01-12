N = int(input())
X = list(map(int, input().split()))
MOD = 10 ** 9 + 7


for i in range(1, N):
    v = 0
    for j in range(1, i):
        v += 1 / j
    X[j - 1] - X[i - 1]