import numpy as np

N = int(input())
A = list(map(int, input().split()))

colors = np.array([0 for _ in range(9)])
for a in A:
    if 1 <= a <= 399: colors[0] += 1
    elif 400 <= a <= 799: colors[1] += 1
    elif 800 <= a <= 1199: colors[2] += 1
    elif 1200 <= a <= 1599: colors[3] += 1
    elif 1600 <= a <= 1999: colors[4] += 1
    elif 2000 <= a <= 2399: colors[5] += 1
    elif 2400 <= a <= 2799: colors[6] += 1
    elif 2800 <= a <= 3199: colors[7] += 1
    else: colors[8] += 1

if colors[8] == 0:
    ans = len(colors[colors > 0])
    print(ans, ans)
else:
    legend = colors[8]
    colors = colors[:8]
    v = len(colors[colors > 0])
    print(max(1, v), v + legend)
