N, M, X = map(int, input().split())
A = list(map(int, input().split()))

l = len(list(filter(lambda a: a < X, A)))
r = len(list(filter(lambda a: a > X, A)))
print(min(l, r))
