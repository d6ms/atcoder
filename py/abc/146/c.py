A, B, X = map(int, input().split())

# 二分探索で達成可能な最小値を見つける
l = 0
r = 10 ** 9 + 1
while l + 1 < r:
    N = (l + r) // 2
    if A * N + B * len(str(N)) <= X:
        l = N
    else:
        r = N
print(l)