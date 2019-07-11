import numpy as np


H, W = map(int, input().split())
grid = np.array([list(input()) for _ in range(H)]) == "."

up = np.zeros((H, W), dtype = int)
down = np.zeros((H, W), dtype = int)
left = np.zeros((H, W), dtype = int)
right = np.zeros((H, W), dtype = int)

for i in range(H):
    down[i] = (down[i - 1] + 1) * grid[i]
    up[-i - 1] = (up[-i] + 1) * grid[-i - 1]

for i in range(W):
    right[:, i] = (right[:, i - 1] + 1) * grid[:, i]
    left[:, -i - 1] = (left[:, -i] + 1) * grid[:, -i - 1]

print(np.max(up + down + left + right) - 3)