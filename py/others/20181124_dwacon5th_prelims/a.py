from fractions import Fraction
N = int(input())
A = list(map(int, input().split()))

avg = Fraction(sum(A), N)

min_val = float('inf')
for a in A:
    val = abs(a - avg)
    min_val = min(min_val, val)

for i, a in enumerate(A):
    val = abs(a - avg)
    if val == min_val:
        print(i)
        exit(0)