from math import ceil
from fractions import Fraction

N = int(input())

t, a = 1, 1
for T, A in [tuple(map(int, input().split())) for _ in range(N)]:
    n = max(ceil(Fraction(t, T)), ceil(Fraction(a, A)))
    t, a = n * T, n * A
print(t + a)
