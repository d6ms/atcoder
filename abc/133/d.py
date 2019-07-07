# コンテスト中ではTLE

N = int(input())
A = list(map(int, input().split()))

X = list()
for i in range(N):
    x_i = A[i]
    keisu = -1
    for j in range(1, N):
        x_i += keisu * A[(i + j) % N]
        keisu = keisu * -1
    X.append(str(x_i))
print(' '.join(X))