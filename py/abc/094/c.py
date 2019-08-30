N = int(input())
X = list(map(int, input().split()))

Xs = sorted(X)
med_d = Xs[N // 2 - 1]
med_u = Xs[N // 2]

for i in range(N):
    if X[i] <= med_d:
        print(med_u)
    elif X[i] >= med_u:
        print(med_d)

