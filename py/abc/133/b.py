from math import sqrt


N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        s = 0
        for d in range(D):
            s += (X[i][d] - X[j][d]) ** 2
        s = sqrt(s)
        if s.is_integer():
            cnt += 1
print(cnt // 2)

