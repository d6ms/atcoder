from fractions import gcd
from functools import reduce


N, X = map(int, input().split())
x = list(map(int, input().split()))

x = map(lambda x_i: abs(X - x_i), x)
ans = reduce(gcd, x)
print(ans)
