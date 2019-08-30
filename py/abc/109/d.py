H, W = map(int, input().split())

N = 0
ans = list()
last_col = list()
for i in range(H):
    A_i = list(map(int, input().split()))
    for j in range(W - 1):
        if A_i[j] % 2 != 0:
            N += 1
            ans.append(((i + 1, j + 1), (i + 1, j + 2)))
            A_i[j] -= 1
            A_i[j + 1] += 1
    last_col.append(A_i[-1])
for i in range(H - 1):
    if last_col[i] % 2 != 0:
        N += 1
        ans.append(((i + 1, W), (i + 2, W)))
        last_col[i] -= 1
        last_col[i + 1] += 1

print(N)
for (y1, x1), (y1_, x1_) in ans:
    print(y1, x1, y1_, x1_)
