N = int(input())
A = list(map(int, input().split()))

# x1さえ求めてしまえば連立方程式の解は連鎖的にO(N)で求まる
X = list()
x_1 = sum(A)
for i in range(N):
    if i % 2 != 0:
        x_1 -= 2 * A[i]
X.append(x_1)

for i in range(1, N):
    x_i = 2 * A[i - 1] - X[i - 1]
    X.append(x_i)
print(' '.join([str(x) for x in X]))