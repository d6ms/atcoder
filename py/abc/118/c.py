import fractions


N = int(input())
A = list(map(int, input().split()))

gcd = A[0]
for i in range(1, N):
    gcd = fractions.gcd(A[i], gcd)
print(gcd)