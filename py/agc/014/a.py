import numpy as np

A, B, C = map(int, input().split())

ans = 0
T = A + B + C
s = np.array([A, B, C])
while all(s % 2 == 0):
    if A == B == C:
        print(-1)
        exit(0)
    s = (T - s) // 2
    ans += 1

print(ans)
