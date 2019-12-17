N, A, B = map(int, input().split())
X = list(map(int, input().split()))

arr = list()
for i, x in enumerate(X):
    if i == 0:
        continue
    arr.append(min((X[i] - X[i - 1]) * A, B))
print(sum(arr))
