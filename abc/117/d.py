from operator import xor


N, K = map(int, input().split())
A = list(map(int, input().split()))


def f(X):
    s = 0
    for a in A:
        s += xor(X, a)
    return s


for i in range(K):
    print(f(i))