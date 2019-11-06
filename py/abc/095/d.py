# 色々と高速化を頑張ったけどTLE

import numpy as np

N, C = map(int, input().split())
X = [0 for _ in range(N + 1)]
V = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    X[i], V[i] = map(int, input().split())
X = np.array(X)
V = np.array(V)

X_inv = np.hstack((np.zeros(1, dtype=int), (C - X[1:])[::-1]))
V_sum = V.cumsum()
V_inv_sum = np.hstack((np.zeros(1, dtype=int), V[1:][::-1])).cumsum()


def solve(i, j):
    v = V_sum[i] + V_inv_sum[j]
    x1 = X[i] + 2 * X_inv[j]
    x2 = 2 * X[i] + X_inv[j]
    return v - min(x1, x2)


ans = [solve(i, j) for i in range(N + 1) for j in range(N - i + 1)]
print(max(ans))
