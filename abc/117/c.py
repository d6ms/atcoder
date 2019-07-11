N, M = map(int, input().split())
X = list(map(int, input().split()))
X = sorted(X)

L = [X[i + 1] - X[i] for i in range(M - 1)]
L = sorted(L, reverse=True)
result = X[-1] - X[0] - sum(L[:N - 1])
print(result)
