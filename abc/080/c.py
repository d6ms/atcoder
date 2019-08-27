N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

ans = float('-inf')
for i in range(1, 2 ** 10):
    p = 0
    for k in range(N):
        store = F[k]
        c = 0
        for j in range(10):
            if (i >> j) & 1 and F[k][j] == 1:
                c += 1
        p += P[k][c]
    ans = max(ans, p)
print(ans)