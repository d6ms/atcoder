from fractions import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


N = int(input())
A = list(map(int, input().split()))

cumlcm = A[0]
for a in A[1:]:
    cumlcm = lcm(cumlcm, a)
m = cumlcm - 1
f = sum(map(lambda a: m % a, A))
print(f)
